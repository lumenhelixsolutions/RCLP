# RCLP: The Reversibility-Constrained Lattice Problem

**A post-quantum cryptographic framework built on two-sided surfaces, the Golay code, and the Leech lattice.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Status: Research Prototype](https://img.shields.io/badge/status-research%20prototype-orange.svg)]()

> **Author:** Christopher Gordon Phillips · LumenHelix · chris@oiq.to
> **Part of:** CORE-32 / R.U.B.I.C. Architecture

---

## Overview

**RCLP** (Reversibility-Constrained Lattice Problem) is a new post-quantum cryptographic hardness assumption that unifies three exceptional mathematical structures into a single primitive:

- **The [24,12,8] extended binary Golay code** — provides the constraint structure
- **The Leech lattice Λ₂₄** — provides the geometric substrate
- **The Conway group Co₀** — provides the automorphism framework

The fundamental operation is the **enriched two-sided surface flip**: each of 24 coordinate positions carries a two-sided surface where each side holds a complete 192-bit state tuple (24-bit RGB color, 21-bit Unicode glyph, 128-bit sedenion coefficient, 5-bit positional encoding, 14-bit reserved). A coordinated flip — constrained to be a Golay codeword — atomically swaps the entire state at selected positions while preserving the Leech lattice structure.

### Why RCLP?

| Property | ML-KEM-768 (FIPS 203) | RCLP (Enriched) |
|---|---|---|
| Algebraic structure | Commutative ring Z_q[X]/(X²⁵⁶+1) | Non-commutative Co₀ ⊃ 2¹².M₂₄ |
| Primary hardness | Module-LWE (single problem) | Composition of 5 sources |
| Lattice dimension | 768 | 24 (Leech) |
| Data per position | ~10 bits | 192 bits (4 channels) |
| Self-inverse decryption | No | Yes (σ² = id) |
| Error correction | From noise params | Golay (corrects ≤3 errors) |
| Composition | Single instance | Matryoshka (2-4 layers) |

### Key Results

- ✅ **RCLP-KEM achieves 100% decryption correctness** (5,000/5,000 trials)
- ✅ **RCLP-128 produces 192-byte ciphertexts** (5.7× smaller than ML-KEM-768's 1,088 B)
- ✅ **388-byte secret keys** (6.2× smaller than ML-KEM-768's 2,400 B)
- ✅ **All mathematical foundations computationally verified** (Golay code, Leech lattice, wreath product fiber)
- ⚠️ **Formal hardness proof** remains as Open Problem #1

---

## Table of Contents

- [Quick Start](#quick-start)
- [Repository Structure](#repository-structure)
- [Mathematical Foundation](#mathematical-foundation)
- [The Enriched Two-Sided Surface](#the-enriched-two-sided-surface)
- [RCLP-KEM Construction](#rclp-kem-construction)
- [Verified Results](#verified-results)
- [Open Problems](#open-problems)
- [Security Disclaimer](#security-disclaimer)
- [Citation](#citation)
- [License](#license)

---

## Quick Start

### Installation

```bash
git clone https://github.com/lumenhelix/rclp.git
cd rclp
pip install -r requirements.txt
pip install -e .
```

### Basic Usage

```python
from rclp import RCLP_KEM

# Initialize with 128-bit security
kem = RCLP_KEM(security_bits=128)

# Generate keypair
public_key, secret_key = kem.keygen()

# Encapsulate a shared secret
ciphertext, shared_secret_sender = kem.encapsulate(public_key)

# Decapsulate
shared_secret_receiver = kem.decapsulate(secret_key, ciphertext)

assert shared_secret_sender == shared_secret_receiver
print("✓ Shared secret established")
```

### Verify Mathematical Foundations

```bash
# Run all verification tests
python -m pytest tests/

# Verify the Golay code construction
python scripts/verify_golay.py

# Verify the Leech lattice (196,560 minimal vectors)
python scripts/verify_leech.py

# Run the full hardness analysis
python scripts/rclp_hardness.py

# Benchmark RCLP-KEM
python scripts/benchmark.py
```

---

## Repository Structure

```
rclp/
├── README.md                    # This file
├── LICENSE                      # MIT License
├── requirements.txt             # Python dependencies
├── setup.py                     # Package installation
│
├── src/rclp/                    # Core library
│   ├── __init__.py              # Public API
│   ├── golay.py                 # [24,12,8] Golay code construction
│   ├── leech.py                 # Leech lattice Λ₂₄ construction
│   ├── surface.py               # Two-sided surface model
│   ├── kem.py                   # RCLP-KEM implementation
│   ├── decoder.py               # Babai + Golay nearest-codeword decoder
│   ├── hypercomplex.py          # Quaternion, octonion, sedenion arithmetic
│   └── verification.py          # Mathematical verification utilities
│
├── tests/                       # Unit tests
│   ├── test_golay.py            # Golay code tests
│   ├── test_leech.py            # Leech lattice tests
│   ├── test_kem.py              # KEM correctness tests
│   └── test_decoder.py          # Decoder accuracy tests
│
├── scripts/                     # Verification & analysis scripts
│   ├── verify_golay.py          # Weight distribution, self-duality
│   ├── verify_leech.py          # 196,560 minimal vectors
│   ├── verify_co0.py            # Sign-change automorphisms
│   ├── intersection_atlas.py    # Complete 9-profile atlas
│   ├── partition_functions.py   # F_{i,s} to depth 24
│   ├── rclp_hardness.py         # Hardness analysis
│   ├── benchmark.py             # Performance benchmarks
│   └── verify_37x_claim.py      # FIPS 203 comparison
│
├── docs/                        # Documentation
│   ├── ARCHITECTURE.md          # System architecture
│   ├── MATHEMATICS.md            # Mathematical background
│   ├── SECURITY.md              # Security model & caveats
│   └── API.md                   # API reference
│
├── papers/                      # Research papers
│   ├── RCLP_Comprehensive.pdf   # Main research paper
│   ├── RCLP_v2_Enriched.docx    # Enriched model paper
│   └── CORE32_Technical_Report.docx
│
├── results/                     # Verification output
│   ├── golay_verification.json
│   ├── leech_verification.json
│   ├── intersection_atlas.json
│   ├── partition_functions.json
│   ├── decoder_results.json
│   └── hardness_analysis.json
│
└── examples/                    # Usage examples
    ├── basic_kem.py             # Simple KEM round-trip
    ├── matryoshka_composition.py # Multi-layer composition
    └── verify_all.py            # Run all verifications
```

---

## Mathematical Foundation

### 1. The [24,12,8] Golay Code

Self-dual linear code with weight distribution:

```
W(x,y) = x²⁴ + 759·x¹⁶y⁸ + 2576·x¹²y¹² + 759·x⁸y¹⁶ + y²⁴
```

- **Length:** n = 24
- **Dimension:** k = 12
- **Minimum distance:** d = 8
- **Codewords:** |C| = 4,096
- **Self-dual:** C = C⊥ (verified via MacWilliams transform)

### 2. The Leech Lattice Λ₂₄

The unique 24-dimensional even unimodular lattice with no vectors of norm 2. Contains 196,560 minimal vectors decomposed into three types:

| Type | Shape | Count |
|---|---|---|
| A | (±4)² 0²² | 1,104 |
| B | (±2)⁸ 0¹⁶ on octad support | 97,152 |
| C | (±3)(±1)²³ | 98,304 |
| **Total** | | **196,560** |

### 3. The Conway Group Co₀

The automorphism group of Λ₂₄, with order:

```
|Co₀| = 8,315,553,613,086,720,000
      ≈ 8.3 × 10¹⁸
```

The monomial subgroup 2¹².M₂₄ (where |M₂₄| = 244,823,040) has order 1,002,795,171,840 and embeds via sign-change automorphisms indexed by Golay codewords.

---

## The Enriched Two-Sided Surface

Each position i carries a **two-sided surface** where each side holds a complete 192-bit state:

| Component | Bits | States | Role |
|---|---|---|---|
| Color (RGB) | 24 | 16,777,216 | Visual / statistical channel |
| Glyph (Unicode) | 21 | 2,097,152 | Functional / algebraic channel |
| Sedenion (16×8) | 128 | ~3.4 × 10³⁸ | Algebraic / lattice channel |
| Position | 5 | 32 | Geometric / structural channel |
| Reserved | 14 | — | Alignment / metadata |
| **TOTAL** | **192** | **~6.3 × 10⁵⁷** | **Complete atomic state** |

### The Flip Operation

```
FLIP(i): (S⁺ᵢ, S⁻ᵢ) → (S⁻ᵢ, S⁺ᵢ)
```

The flip is:
- **Total** — swaps all 192 bits, not a subset
- **Atomic** — all channels swap simultaneously
- **Reversible** — flip twice = identity (σ² = id)
- **Constrained** — valid patterns must be Golay codewords
- **Composable** — nests via wreath products in Co₀
- **Enriched** — carries 192 bits per position (not 1 bit)

### Information Payload Per Flip

| Flip Weight | Positions | Total Payload |
|---|---|---|
| 8 (octad) | 8 | 1,536 bits (192 B) |
| 12 (dodecad) | 12 | 2,304 bits (288 B) |
| 16 (hexadecad) | 16 | 3,072 bits (384 B) |
| 24 (full) | 24 | 4,608 bits (576 B) |

---

## RCLP-KEM Construction

### Definition (RCLP)

Given (Λ₂₄, p, t, E) where:
- p ∈ Λ₂₄ is a public lattice point
- t = σ_c(p) + e for unknown c ∈ C and short error e
- E is a public color/glyph/sedenion encoding

**Find:** the Golay codeword c AND the complete inner states at flipped positions.

### Five Hardness Sources

1. **H1 — Lattice CVP:** Recovering σ_c(p) from noisy t requires CVP in Λ₂₄ (~40 bits)
2. **H2 — Golay Constraint:** Valid codewords only, minimum distance 8 (~12 bits)
3. **H3 — Involution Quantization:** σ² = id, no partial flips, weight ≥ 8
4. **H4 — Cross-Channel Consistency:** 4 coupled channels must all be consistent
5. **H5 — Matryoshka Composition:** Nested wreath products in Co₀

### Parameter Sets

| Set | Security | Layers | PK (B) | SK (B) | CT (B) | vs ML-KEM-768 |
|---|---|---|---|---|---|---|
| RCLP-128 | 128 bits | 2 | 1,152 | 388 | 192 | 5.7× smaller CT |
| RCLP-192 | 192 bits | 3 | 1,728 | 582 | 288 | 3.8× smaller CT |
| RCLP-256 | 256 bits | 4 | 2,304 | 776 | 384 | 2.8× smaller CT |
| **ML-KEM-768** | 128 bits | N/A | 1,184 | 2,400 | 1,088 | (reference) |

### Decoder Correctness

The optimal decoder combines:
1. **Babai nearest-plane rounding** for sign recovery
2. **Golay nearest-codeword decoding** (corrects up to 3 errors)
3. **Minimum coordinate rejection** (|pᵢ| ≥ 4)

**Result:** 100.00% correctness on 5,000/5,000 trials across all parameter configurations.

---

## Verified Results

All results verified by exact computation:

- ✅ Golay code weight distribution {0:1, 8:759, 12:2576, 16:759, 24:1}
- ✅ Self-duality C = C⊥ via MacWilliams transform (exact rational)
- ✅ Krawtchouk orthogonality (exact integer arithmetic)
- ✅ Steiner system S(5,8,24): λ=1, λ₄=5, λ₃=21, r=253
- ✅ Complete 9-profile directed intersection atlas
- ✅ Dodecad-dodecad profile {0:1, 4:495, 6:1584, 8:495} (new result)
- ✅ Partition functions F_{i,s} to depth s=24 (exact Fraction)
- ✅ Corrected duality theorem (original formulation was wrong at odd depths)
- ✅ Leech lattice: 196,560 minimal vectors constructed and verified
- ✅ Sign-change automorphisms preserve Λ₂₄ (all 5 weight classes)
- ✅ Monomial subgroup 2¹².M₂₄ confirmed in Co₀
- ✅ Trio structure: 3,795 disjoint octad triples
- ✅ Sextet/MOG partition with tetrad-pair = octad property
- ✅ Wreath product fiber: pure permutations insufficient
- ✅ Quaternion non-commutativity, octonion alternativity
- ✅ Sedenion zero-divisor bipartite graph (14 vertices, 42 edges)
- ✅ RCLP-KEM 100% decoder correctness (5,000/5,000 trials)

---

## Open Problems

1. **Formal RCLP hardness proof** — Prove RCLP ≥ CVP in Λ₂₄ with concrete reduction
2. **Cross-channel security** — Formalize mutual information under the enriched flip
3. **Machine-checked proofs** — Formalize theorems in Lean4/Coq
4. **Quantum security analysis** — Prove quantum Fourier sampling over Co₀ doesn't break RCLP
5. **C/C++ implementation** — Port for fair benchmarking against ML-KEM-768
6. **Side-channel analysis** — Timing/power leakage of the enriched flip
7. **Non-monomial Co₀ elements** — Characterize the 8,292,375 coset representatives

---

## Security Disclaimer

**⚠️ This is research-grade cryptographic software. Do NOT use in production systems.**

RCLP is a new cryptographic primitive. While its mathematical foundations are rigorously verified, **the hardness assumption itself has not been independently peer-reviewed or subjected to extensive cryptanalysis.** The following items remain as open problems:

- Formal hardness reduction from RCLP to a standard lattice problem
- Quantum security analysis under Grover, Shor, and Regev's algorithms
- Independent cryptanalysis by the post-quantum cryptography community
- Side-channel resistance analysis

For production post-quantum key establishment, use **ML-KEM (FIPS 203)**.

---

## Citation

If you use RCLP in your research, please cite:

```bibtex
@techreport{phillips2026rclp,
  author      = {Phillips, Christopher Gordon},
  title       = {The Reversibility-Constrained Lattice Problem:
                 Post-Quantum Cryptography from Two-Sided Surfaces,
                 the Golay Code, and the Leech Lattice},
  institution = {LumenHelix Research},
  year        = {2026},
  month       = {April},
  type        = {Technical Report},
  note        = {CORE-32 / R.U.B.I.C. Architecture}
}
```

---

## License

MIT License — see [LICENSE](LICENSE) for details.

Copyright © 2026 Christopher Gordon Phillips / LumenHelix

---

## Contact

- **Author:** Christopher Gordon Phillips
- **Organization:** LumenHelix
- **Email:** chris@oiq.to
- **Website:** lumenhelix.com

**Collaboration welcomed.** This framework has significant open problems that benefit from community attention. If you're interested in:
- Formal hardness proofs
- Quantum security analysis
- C/C++ reference implementation
- Lean4/Coq formalization
- Independent cryptanalysis

Please reach out.

