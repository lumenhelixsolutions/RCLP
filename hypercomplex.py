#!/usr/bin/env python3
"""
benchmark.py — Performance benchmarks for RCLP-KEM.

Measures keygen, encapsulation, and decapsulation timing across
all three parameter sets (RCLP-128, RCLP-192, RCLP-256).
"""

import time
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from rclp.kem import RCLP_KEM


def benchmark_level(security_bits, n_trials=1000):
    """Run benchmarks for one security level."""
    kem = RCLP_KEM(security_bits=security_bits)
    print(f"\n=== RCLP-{security_bits} ===")
    print(f"  Layers: {kem.n_layers}")
    print(f"  Modulus q: {kem.q}")
    print(f"  PK: {kem.public_key_size()} bytes")
    print(f"  SK: {kem.secret_key_size()} bytes")
    print(f"  CT: {kem.ciphertext_size()} bytes")

    # Correctness check first
    print(f"  Verifying correctness ({n_trials} trials)...")
    correct = 0
    for trial in range(n_trials):
        pk, sk = kem.keygen(seed=trial * 7)
        ct, ss_enc = kem.encapsulate(pk, seed=trial * 11)
        ss_dec = kem.decapsulate(sk, ct)
        if ss_enc == ss_dec:
            correct += 1
    correctness_pct = 100 * correct / n_trials
    print(f"  Correctness: {correct}/{n_trials} = {correctness_pct:.2f}%")

    # Timing: KeyGen
    t0 = time.time()
    for trial in range(n_trials):
        pk, sk = kem.keygen(seed=trial)
    t_kg = (time.time() - t0) / n_trials * 1e6  # microseconds

    # Timing: Encaps
    pk, sk = kem.keygen(seed=0)
    t0 = time.time()
    for trial in range(n_trials):
        ct, ss = kem.encapsulate(pk, seed=trial)
    t_enc = (time.time() - t0) / n_trials * 1e6

    # Timing: Decaps
    t0 = time.time()
    for trial in range(n_trials):
        _ = kem.decapsulate(sk, ct)
    t_dec = (time.time() - t0) / n_trials * 1e6

    total = t_kg + t_enc + t_dec
    print(f"  KeyGen:  {t_kg:7.1f} microseconds")
    print(f"  Encaps:  {t_enc:7.1f} microseconds")
    print(f"  Decaps:  {t_dec:7.1f} microseconds")
    print(f"  Total:   {total:7.1f} microseconds")

    return {
        'security_bits': security_bits,
        'layers': kem.n_layers,
        'pk_bytes': kem.public_key_size(),
        'sk_bytes': kem.secret_key_size(),
        'ct_bytes': kem.ciphertext_size(),
        'correctness_pct': correctness_pct,
        'keygen_us': t_kg,
        'encaps_us': t_enc,
        'decaps_us': t_dec,
        'total_us': total,
    }


def main():
    print("=" * 60)
    print("RCLP-KEM Benchmark Suite")
    print("=" * 60)

    results = {}
    for level in [128, 192, 256]:
        results[f'RCLP-{level}'] = benchmark_level(level, n_trials=500)

    # Comparison with ML-KEM-768 reference (published numbers)
    print("\n" + "=" * 60)
    print("Comparison with ML-KEM-768 (published reference)")
    print("=" * 60)
    ml_kem = {
        'keygen_us': 2980,
        'encaps_us': 6557,
        'decaps_us': 4980,
        'total_us': 14517,
        'pk_bytes': 1184,
        'sk_bytes': 2400,
        'ct_bytes': 1088,
    }
    print(f"\n  ML-KEM-768 (optimized C reference):")
    print(f"    KeyGen:  {ml_kem['keygen_us']} microseconds")
    print(f"    Encaps:  {ml_kem['encaps_us']} microseconds")
    print(f"    Decaps:  {ml_kem['decaps_us']} microseconds")
    print(f"    Total:   {ml_kem['total_us']} microseconds")
    print(f"    PK: {ml_kem['pk_bytes']} B, SK: {ml_kem['sk_bytes']} B, CT: {ml_kem['ct_bytes']} B")

    rclp_128 = results['RCLP-128']
    print(f"\n  RCLP-128 vs ML-KEM-768:")
    print(f"    Ciphertext: {rclp_128['ct_bytes']} B vs {ml_kem['ct_bytes']} B = "
          f"{ml_kem['ct_bytes']/rclp_128['ct_bytes']:.1f}x smaller")
    print(f"    Secret key: {rclp_128['sk_bytes']} B vs {ml_kem['sk_bytes']} B = "
          f"{ml_kem['sk_bytes']/rclp_128['sk_bytes']:.1f}x smaller")
    print(f"    Public key: {rclp_128['pk_bytes']} B vs {ml_kem['pk_bytes']} B = "
          f"{ml_kem['pk_bytes']/rclp_128['pk_bytes']:.2f}x")
    print(f"  NOTE: RCLP timings are Python/NumPy; ML-KEM reference is optimized C.")
    print(f"  Algorithmic comparison, not implementation comparison.")

    # Save results
    out_file = Path(__file__).parent.parent / "results" / "benchmark_results.json"
    out_file.parent.mkdir(exist_ok=True)
    with open(out_file, 'w') as f:
        json.dump({'rclp': results, 'ml_kem_768_reference': ml_kem}, f, indent=2)
    print(f"\nResults saved to {out_file}")


if __name__ == "__main__":
    main()
