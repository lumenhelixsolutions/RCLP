#!/usr/bin/env python3
"""
verify_leech.py — Verify the Leech lattice Lambda_24 construction.

Builds all 196,560 minimal vectors (Type A + Type B + Type C) and verifies
norms, antipodal symmetry, and sign-change automorphism preservation.

NOTE: Full verification builds Type C (98,304 vectors) which is slow in Python.
"""

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from rclp.leech import LeechLattice


def main():
    print("=" * 60)
    print("Leech Lattice Lambda_24 Verification")
    print("=" * 60)

    L = LeechLattice()

    print("\n[1] Building Type A vectors (+/-4)^2 0^22...")
    t0 = time.time()
    a = L.build_type_a()
    print(f"    Count: {len(a)} (expected 1,104)")
    print(f"    Time: {time.time()-t0:.1f} s")
    assert len(a) == 1104

    print("\n[2] Building Type B vectors (+/-2)^8 on octad supports...")
    t0 = time.time()
    b = L.build_type_b()
    print(f"    Count: {len(b)} (expected 97,152)")
    print(f"    Time: {time.time()-t0:.1f} s")
    assert len(b) == 97152

    print("\n[3] Building Type C vectors (+/-3)(+/-1)^23 (slow)...")
    t0 = time.time()
    c = L.build_type_c()
    print(f"    Count: {len(c)} (expected 98,304)")
    print(f"    Time: {time.time()-t0:.1f} s")
    assert len(c) == 98304

    total = len(a) + len(b) + len(c)
    print(f"\n[4] Total minimal vectors: {total} (expected 196,560)")
    assert total == 196560
    print(f"    ✓ Kissing number verified")

    print("\n[5] Verifying all have squared norm 32...")
    ok_norm = L.verify_norms()
    print(f"    {'✓' if ok_norm else '✗'} All 196,560 vectors have ||v||^2 = 32")

    print("\n[6] Verifying antipodal symmetry (v in set iff -v in set)...")
    ok_anti = L.verify_antipodal()
    print(f"    {'✓' if ok_anti else '✗'} Antipodal symmetry confirmed")

    print("\n[7] Verifying sign-change automorphisms preserve the minimal vector set...")
    ok_sigma = L.verify_sign_change_preservation(sample_size=50)
    print(f"    {'✓' if ok_sigma else '✗'} All 5 weight classes preserve Type A")

    print("\n[8] Co_0 group order constants")
    print(f"    |M_24|        = {LeechLattice.M24_ORDER:,}")
    print(f"    |2^12 . M_24| = {LeechLattice.MONOMIAL_ORDER:,}")
    print(f"    |Co_0|        = {LeechLattice.CO0_ORDER:,}")
    print(f"    [Co_0 : N]    = {LeechLattice.co0_index():,}")

    # Save report
    report = {
        'type_a_count': len(a),
        'type_b_count': len(b),
        'type_c_count': len(c),
        'total_kissing': total,
        'norms_ok': ok_norm,
        'antipodal_ok': ok_anti,
        'sign_change_ok': ok_sigma,
        'co0_order': LeechLattice.CO0_ORDER,
        'm24_order': LeechLattice.M24_ORDER,
        'monomial_order': LeechLattice.MONOMIAL_ORDER,
        'co0_index': LeechLattice.co0_index(),
    }
    out_file = Path(__file__).parent.parent / "results" / "leech_verification.json"
    out_file.parent.mkdir(exist_ok=True)
    with open(out_file, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"\nReport saved to {out_file}")


if __name__ == "__main__":
    main()
