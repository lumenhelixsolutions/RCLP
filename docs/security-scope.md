# RCLP — Security Scope and Threat Model

> **The single most important sentence in this project:**
> **RCLP is a reversible *encoding layer*, not a standalone hardness assumption.**
> All computational security derives from the underlying M-LWE assumption of the
> host KEM (ML-KEM / Kyber). The Golay code and Leech lattice contribute
> *encoding efficiency and structural integrity* — reversibility and
> tamper-evidence — **not** computational hardness.

This document states precisely what RCLP does and does not claim, so the work is
evaluated on defensible ground.

## What RCLP claims

1. **Reversibility (proven).** The encoding-layer transform `σ_c` is a strict
   involution (`σ_c² = id`) and norm-preserving for every `c ∈ {0,1}²⁴`. The
   layer is exactly invertible with no separate inverse schedule.
2. **Structural tamper-evidence (proven for the stated model).** A recovered
   sign pattern that is not a Golay codeword reveals corruption. Single-coordinate
   corruption is detected with certainty (minimum distance 8).
3. **Efficiency parity with dense lattice codes (experimental).** Used as the
   encoder inside ML-KEM, RCLP inherits the ciphertext-expansion benefits of the
   Liu–Sakzad Leech-lattice line of work.
4. **Multi-key derivation (embodiment / conjectural).** The sign-change subgroup
   `2¹² ⊂ Co₀` and its wreath-product structure suggest a route to deriving
   several keys from one exchange. Independence requires a KDF or non-commuting
   structure and is **not** claimed as proven.

## What RCLP explicitly does NOT claim

- ❌ **RCLP is not a new hardness assumption.** An earlier internal draft
  (`RCLP_Paper_v2_Enriched`, Mar 2026) proposed RCLP as a standalone KEM deriving
  ~128-bit security from "five compositional hardness sources." **That framing is
  withdrawn.** It does not survive scrutiny:
  - **Leech CVP is easy.** The Leech lattice has polynomial-time closest-vector
    decoders (Conway–Sloane 1982; Vardy–Be'ery 1993). At dimension 24 it provides
    no asymptotic hardness — indeed van Poppelen (ePrint 2016/1050) studied Leech
    for LWE and found its structure *aids* decoding.
  - **Golay ML-decoding is polynomial-time.** Membership/decoding is a structural
    restriction, not a computational barrier.
  - **No compositional proof.** There is no proof that the proposed hardness
    sources compose to a quantified security level.
  Honest standalone enumeration-resistance could be as low as ~30–50 bits — far
  below the 128-bit floor. We therefore do not make standalone-hardness claims.
- ❌ **RCLP does not modify the M-LWE security argument** of the host KEM. Used
  correctly it is transparent to that argument (cf. Liu–Sakzad).
- ❌ **RCLP does not replace authenticated encryption.** Its tamper-evidence is a
  structural by-product, useful as defense-in-depth, not a substitute for a MAC
  where one is required by the protocol.

## Resolved

- **Decryption / reaction oracle from the tamper flag, and FO-transform
  interaction.** Resolved in [`oracle-safety-analysis.md`]: RCLP does not amplify
  the decryption-failure rate, and under placement A the membership check is
  redundant on the FO accept branch, so IND-CCA is preserved.
- **Constant-time membership check** (the load-bearing dependency of the above).
  Resolved: a branch-free, data-oblivious predicate (`rclp.golay_ct`, from
  self-duality of the code) measured leak-free by dudect (`ct/`). Residual is
  operational — re-run the harness on the production target.

## Open security questions (see `claims-and-proof-status.md`)

- Whether multi-key derivations are independent when sign-change masks commute.
- Broader side-channel review of the full encode/decode path (beyond the
  membership check) on the deployment target.

## Threat model (encoding layer)

- **In scope:** detection of post-encoding ciphertext bit-corruption via Golay
  membership; exact rollback of the encoding transform for audit.
- **Out of scope:** confidentiality (provided by the host KEM), active attackers
  with a decryption oracle (must be analyzed under the host KEM's IND-CCA proof),
  implementation side channels (future work).
