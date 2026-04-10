#!/usr/bin/env python3
"""
verify_golay.py — Verify all properties of the [24,12,8] Golay code.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from rclp.golay import GolayCode
from fractions import Fraction


def main():
    print("=" * 60)
    print("[24,12,8] Extended Binary Golay Code Verification")
    print("=" * 60)

    g = GolayCode()

    # Weight distribution
    print("\n[1] Weight distribution")
    import numpy as np
    weight_dist = {int(w): int((g.weights == w).sum()) for w in np.unique(g.weights)}
    for w, count in sorted(weight_dist.items()):
        print(f"    A_{w} = {count}")
    ok_wd = g.verify_weight_distribution()
    print(f"    {'✓' if ok_wd else '✗'} Matches expected {{0:1, 8:759, 12:2576, 16:759, 24:1}}")

    # Self-duality
    print("\n[2] Self-duality C = C^perp")
    ok_sd = g.verify_self_duality()
    print(f"    {'✓' if ok_sd else '✗'} MacWilliams transform confirms self-duality")

    # Steiner system
    print("\n[3] Steiner system S(5,8,24)")
    ok_ss = g.verify_steiner_system(n_samples=500)
    print(f"    {'✓' if ok_ss else '✗'} Every 5-subset in exactly one octad (500 samples)")
    print(f"    Octads: {len(g.octads())} (expected 759)")
    print(f"    Dodecads: {len(g.dodecads())} (expected 2576)")
    print(f"    Hexadecads: {len(g.hexadecads())} (expected 759)")

    # Intersection atlas
    print("\n[4] Directed intersection atlas")
    profiles = {}
    for ref in [8, 12, 16]:
        for pool in [8, 12, 16]:
            profile = g.directed_intersection_profile(ref, pool)
            name = f"{'Oct' if ref==8 else 'Dod' if ref==12 else 'Hex'} -> " \
                   f"{'Oct' if pool==8 else 'Dod' if pool==12 else 'Hex'}"
            print(f"    {name}: {profile}")
            profiles[f"{ref}->{pool}"] = profile

    # Partition functions
    print("\n[5] Partition functions F_{i,s} (sample values)")
    for weight in [8, 12, 16]:
        for s in [1, 2, 4]:
            F = g.partition_function(weight, s)
            print(f"    F({weight},{s}) = {F}")

    # Krawtchouk parity vanishing
    print("\n[6] Krawtchouk parity vanishing: K_s(12; 24) = 0 for odd s")
    all_zero = all(GolayCode.krawtchouk(s, 12, 24) == 0 for s in range(1, 24, 2))
    print(f"    {'✓' if all_zero else '✗'} Verified for all odd s in 1..23")

    # Save report
    report = {
        'weight_distribution': weight_dist,
        'self_dual': ok_sd,
        'steiner_system': ok_ss,
        'directed_atlas': profiles,
        'krawtchouk_parity_vanishing': all_zero,
    }
    out_file = Path(__file__).parent.parent / "results" / "golay_verification.json"
    out_file.parent.mkdir(exist_ok=True)
    with open(out_file, 'w') as f:
        json.dump(report, f, indent=2, default=str)
    print(f"\nReport saved to {out_file}")


if __name__ == "__main__":
    main()
