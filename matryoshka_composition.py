# RCLP Security Model

## Disclaimer

**RCLP is a research prototype. Do NOT use in production systems.** The hardness assumption has not been independently peer-reviewed. For production post-quantum key exchange, use ML-KEM (FIPS 203).

## Five Hardness Sources

RCLP derives security from the composition of five independent sources:

| Source | Description | Estimated Bits |
|---|---|---|
| H1 (Lattice CVP) | Closest Vector Problem in Λ₂₄ | ~40 per instance |
| H2 (Golay Constraint) | Solution must be valid codeword (4,096/16.7M) | 12 |
| H3 (Involution Quantization) | σ² = id, no partial flips, min weight 8 | structural |
| H4 (Cross-Channel) | 4 coupled channels must all be consistent | ~20 |
| H5 (Matryoshka) | Nested wreath products, sequential depth | multiplicative |

## The Central Question: Does Golay Help or Hinder?

**When p is known (conservative model):** The Golay constraint is security-neutral. Brute-force succeeds in O(4,096) = O(2¹²) per layer. The constraint reduces search from 2²⁴ to 2¹², but this is offset by eliminating independent per-position testing.

**When p is unknown (enriched model):** The Golay constraint becomes security-positive. The attacker cannot decompose the problem into 24 independent binary decisions because the Golay structure forces commitment to weight-8+ codewords. The enriched encoding (192 bits/position across 4 channels) protects the base point p.

## Security Estimates

| Model | Per Layer | 2 Layers | 3 Layers | 4 Layers |
|---|---|---|---|---|
| Conservative (p known) | 12 bits | 24 | 36 | 48 |
| Moderate (p unknown) | 40 bits | 80 | 120 | 160 |
| Optimistic (enriched) | 72 bits | 144 | 216 | 288 |

**Critical assumption:** The secrecy of the base point p, protected by the enriched state encoding.

## Known Attack Vectors

1. **Brute-force Golay search (with known p):** O(4,096) per layer. Mitigated by keeping p secret via enriched encoding.
2. **BKZ lattice reduction:** Standard lattice attack. Dimension 24 provides ~40 bits alone; enrichment and Golay constraint add structure.
3. **Quantum Fourier sampling:** Co₀ is non-abelian, which should resist quantum Fourier sampling. No formal proof exists.

## What Is NOT Proven

- Formal reduction from RCLP to a standard lattice problem
- Quantum security under Grover/Shor/Regev
- Information-theoretic contribution of cross-channel coupling
- Side-channel resistance
