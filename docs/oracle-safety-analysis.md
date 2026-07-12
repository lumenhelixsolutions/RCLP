# RCLP — Oracle-Safety of the Tamper-Evidence Flag

*Resolves open item #13 (decryption-failure / reaction oracle from the membership
check). Safety holds for a precisely specified usage ("placement A") and a
constant-time membership check; the latter precondition is now implemented and
measured (item #14, see `../ct/`). We state the conditions, prove the safety
result under them, and prohibit the unsafe placement.*

## 1. The question

RCLP adds a check to decoding: recover the sign pattern `ĉ` and test `ĉ ∈ 𝒞`
(the Golay code). Any input-dependent accept/reject branch in a KEM's
decapsulation is a candidate **oracle**. Lattice KEMs are specifically vulnerable
to **reaction / decryption-failure attacks** (Guo–Johansson–Stankovski;
D'Anvers et al.): an adversary who learns *whether an internal check passed* for
chosen ciphertexts can recover the secret key. ML-KEM defends against this with
the **Fujisaki–Okamoto (FO) transform** — decapsulation re-encrypts and, on
mismatch, returns a pseudorandom **implicit-rejection** key in constant time, so
"valid" and "invalid" are indistinguishable to the adversary.

The worry: does RCLP's membership flag create a *second*, observable accept/reject
predicate that the FO transform does not cover — i.e. a new oracle?

## 2. Preconditions

- **P1 (codeword-valued by construction).** RCLP only ever applies `σ_c` for
  `c ∈ 𝒞`. The encoder never emits a non-codeword sign pattern.
- **P2 (deterministic, FO-bound selection).** `c = f(m)` is a deterministic
  function of the message `m`, fixed by the FO randomness derivation (`r = G(m)`),
  and `σ_c` is applied to the lattice-encoded message block *inside* the
  deterministic encryption that the FO transform re-encrypts.
- **P3 (constant-time check).** The membership test runs in time independent of
  its input and of secret data. This is item #14, now implemented and measured
  (§8, `../ct/`); the result below assumes it.
- **P4 (implicit-rejection placement — "Placement A").** The membership result is
  folded into the *same* decision as the FO re-encryption check: if re-encryption
  fails **or** membership fails, decapsulation returns the FO implicit-rejection
  key. The flag is **not** surfaced as a distinct value, error code, or early-out.

## 3. RCLP does not amplify the decryption-failure rate

**Lemma 1.** RCLP does not change the host KEM's decryption-failure event; the
post-RCLP decode error equals the baseline decode error exactly.

*Proof.* `σ_c` is a diagonal `±1` map, hence an isometry and an involution
(Thms. 2 and 1 of the paper). Decapsulation applies `σ_c` to invert the encoding
before lattice decoding. The decoder therefore sees `σ_c(σ_c(x)+e) = x + σ_c(e)`,
and `‖σ_c(e)‖ = ‖e‖`: the noise reaching the decoder has the **same distribution
and the same norm** as without RCLP. The nearest-point decision, and thus the
failure event `{decode ≠ x}`, is unchanged. ∎

*Consequence.* RCLP adds no surface for failure-boosting attacks: it neither
creates new failures nor shifts their probability.

## 4. The membership check is redundant on the accepting branch

**Theorem 1.** Under P1–P2, for any ciphertext on which FO re-encryption
succeeds, the recovered sign pattern is a Golay codeword. Hence the membership
predicate never rejects a ciphertext that the FO check accepts.

*Proof.* Decapsulation recovers a candidate message `m'`, recomputes
`r' = G(m')` and `c' = f(m')`, and re-encrypts to `ct'`. Re-encryption success
means `ct' = ct` (the input). By P2 the RCLP-encoded components of `ct'` carry the
sign pattern `c'`, so the pattern recovered from `ct` equals `c'`; by P1,
`c' ∈ 𝒞`. Therefore membership holds. ∎

So on the **accept** branch the predicate is always true, and on the **reject**
branch (P4) decapsulation already returns implicit rejection. The predicate's
value is fixed by, and adds nothing to, the FO decision.

## 5. No new oracle

**Theorem 2 (oracle-freeness).** Let the host KEM be IND-CCA secure via the FO
transform in the ROM. Under P1–P4, the RCLP-wrapped KEM is IND-CCA secure with the
*same* advantage bound; in particular the membership check yields no decryption
oracle.

*Proof (reduction).* RCLP placement A instantiates the host's deterministic PKE
with an extra invertible isometric encoding step `σ_c`. By Lemma 1 this PKE has
the *same* correctness error, and the FO transform's IND-CCA analysis
(Hofheinz–Hövelmanns–Kiltz 2017) is agnostic to the specific deterministic
encoding provided re-encryption is exact — which it is, since `σ_c` is a
deterministic bijection recomputed during re-encryption. By Theorem 1 the
membership predicate is implied by re-encryption equality, and by P4 it shares the
implicit-rejection output. Hence the RCLP decapsulation function is **identical**,
on every input, to the standard FO decapsulation for this PKE. Two identical
oracles confer identical adversarial advantage, so the bound carries over
verbatim. ∎

## 6. The unsafe placement (prohibited)

**Placement B (variable-time or observable flag).** If an implementation surfaces
the membership result as a distinct outcome — a "tamper detected" error, a
distinguishable return value, or a variable-time early-out *before* FO
re-encryption — then it **is** a reaction oracle. An adversary can submit
malformed ciphertexts and learn whether the secret-dependent recovered pattern
landed in `𝒞`, leaking key information. Placement B violates P4 (and typically
P3) and is **forbidden** in any CCA-exposed deployment.

> Normative rule: *the tamper flag must never be an adversarially observable event
> distinct from FO implicit rejection.*

## 7. Where the flag is legitimately useful

Theorems 1–2 show the flag is *redundant* in the CCA path — which is exactly why
it is safe there. Its value lies in settings the FO transform does not cover, and
where no chosen-ciphertext oracle exists:

- **Non-adversarial corruption.** Detecting random transmission bit-flips for
  diagnostics/telemetry on the **accept** path (an early-out that only ever fires
  on already-rejected traffic is still constant-time-safe).
- **Forensic / audit.** A structural witness over **already-authenticated** data
  (post-decapsulation, behind the KEM's integrity guarantee), supporting RCLP's
  exact-reversibility/auditability claim.
- **Non-FO hosts.** If RCLP is used as a general encoding layer over a primitive
  *without* FO-style CCA protection, the flag is a genuine integrity primitive —
  but then the §6 oracle warning applies in full and a MAC is the right tool for
  adversarial integrity.

## 8. Status and residual obligation

| Result | Status |
|---|---|
| No DFR amplification (Lemma 1) | 🟢 Proven (unconditional) |
| Membership redundant on accept branch (Thm 1) | 🟢 Proven under P1–P2 |
| No new oracle / IND-CCA preserved (Thm 2) | 🟢 Proven under P1–P4 (ROM, FO host) |
| Constant-time membership (P3) | 🟢 Implemented + measured — branch-free `rclp.golay_ct`; dudect clean in `../ct/` (re-run on target) |

**Net:** open item #13 is **resolved**. The tamper-evidence flag introduces no
decryption oracle when implemented as placement A, and its one load-bearing
precondition — a constant-time membership check (P3) — is now satisfied: a
branch-free, data-oblivious predicate (`rclp.golay_ct`) verified functionally
equivalent to the reference, and certified by a dudect measurement (`../ct/`,
`|t| ≈ 1.8 < 4.5` with a clean null control) on the development machine. The only
residual is operational: re-run the `ct/` harness on the production target, since
constant-time behaviour is microarchitecture-specific.

## References
- Hofheinz, Hövelmanns, Kiltz. *A Modular Analysis of the Fujisaki–Okamoto
  Transformation.* TCC 2017.
- D'Anvers, Vercauteren, Verbauwhede. *On the Impact of Decryption Failures on the
  Security of LWE/LWR-Based Schemes.* PKC 2019.
- Guo, Johansson, Stankovski. *A Key-Recovery Reaction Attack on QC-MDPC.* (reaction-attack methodology.)
- NIST FIPS 203 (ML-KEM); the FO variant and implicit rejection.
