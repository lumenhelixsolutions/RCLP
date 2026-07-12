# RCLP — Prior Art and Novelty

## The line of work RCLP builds on

| Work | Venue | Contribution | Relation to RCLP |
|---|---|---|---|
| Conway & Sloane, *Sphere Packings, Lattices and Groups* | Springer 1988 | Leech lattice Λ₂₄, Co₀, Golay construction | foundational objects RCLP uses |
| NIST FIPS 203 (ML-KEM) | NIST 2024 | standardized Module-LWE KEM | the host scheme |
| Liu & Sakzad, *CRYSTALS-Kyber with Lattice Quantizer* | IEEE ISIT 2024 | first Leech-lattice Kyber encoder | the encoder RCLP wraps |
| Liu & Sakzad, *Lattice Codes for CRYSTALS-Kyber* | Des. Codes Cryptogr. **93** (2025) 3181–3205 | 32.6% CER reduction; DFR ↓ ×2⁸⁵ | efficiency baseline |
| Liu & Sakzad, *Compact Lattice-Coded (Multi-Recipient) Kyber…* | ASIACRYPT 2025 | 90% CER via ℓ=24 packing; IND-CCA under M-LWE | multi-recipient context |
| van Poppelen, *Cryptographic decoding of the Leech lattice* | ePrint 2016/1050 | Leech CVP aids LWE decoding | why Leech ≠ hardness (scope evidence) |

## What is genuinely novel in RCLP

The Liu–Sakzad encoders treat the lattice encoding as an **opaque sphere
packing**. RCLP's novelty is to add an algebraic layer on top of that encoding:

1. **A code-indexed automorphism as a post-encoding transform.** Using a Golay
   codeword `c` to select an element `σ_c` of the Leech sign-change subgroup
   `2¹² ⊂ Co₀`, applied *after* lattice encoding, is — to our knowledge — not
   present in prior KEM encoders. It yields exact, schedule-free reversibility.
2. **Tamper-evidence as a structural by-product.** Deriving an integrity check
   from membership of the recovered sign pattern in an error-correcting code,
   with **no additional ciphertext bandwidth**, is novel for a lattice KEM
   encoder (prior practice uses a separate MAC/AEAD).
3. **A wreath-product nesting for multi-key derivation** addressing the
   multi-key need Liu–Sakzad (ASIACRYPT 2025) explicitly call out (PQ3, TLS 1.3).
   *(Embodiment — see proof-status.)*

## Novelty boundaries (what is NOT claimed as novel)

- The Golay code, the Leech lattice, Co₀ — classical objects.
- Using dense lattice codes to shrink Kyber ciphertexts — that is Liu–Sakzad.
- Any new hardness assumption — explicitly **not** claimed (see security-scope).

## Suggested prior-art search terms (for the filing's IDS)

`lattice code KEM encoder`, `Leech lattice Kyber`, `Golay code cryptography`,
`reversible encoding lattice`, `sign-change automorphism Conway group`,
`MAC-free integrity lattice ciphertext`, `multi-key KEM derivation`.
