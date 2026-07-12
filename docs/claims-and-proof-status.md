# RCLP — Claims and Proof Status

Award-quality work is honest about epistemic status. Every claim below is tagged:

- 🟢 **Proven** — algebraic proof and/or exhaustive computation.
- 🟢 **Measured** — established empirically by a reproducible measurement.
- 🟡 **Experimental** — supported by benchmarks/trials under stated assumptions.
- 🔴 **Open** — conjecture or embodiment; needs proof or careful limitation.
- ⛔ **Withdrawn** — previously asserted, now retracted as indefensible.

| # | Claim | Status | Evidence |
|---|---|---|---|
| 1 | Golay `[24,12,8]` has 4096 codewords; weight enum `{0:1,8:759,12:2576,16:759,24:1}` | 🟢 Proven | exhaustive enumeration (`test_rclp.py`) |
| 2 | `σ_c² = id` for all `c ∈ {0,1}²⁴` (involution) | 🟢 Proven | algebra: `(-1)^{2c_i}=1`; 5000 random trials exact |
| 3 | `σ_c` preserves Euclidean norm | 🟢 Proven | `|±x_i| = |x_i|`; 5000 trials |
| 4 | Valid flip patterns form the sign-change subgroup `2¹² ⊂ Co₀` | 🟢 Proven | standard Leech/Co₀ theory (Conway–Sloane) |
| 5 | Single-coordinate tamper detected with certainty | 🟢 Proven | min-distance 8 ⇒ weight-1 ∉ code; 98304/98304 |
| 6 | Encode/decode round-trips exactly (noiseless layer) | 🟢 Proven | involution; 1000/1000 |
| 7 | Leech lattice Λ₂₄ construction is correct (kissing number 196560) | 🟢 Proven | exact count of the 3 minimal shapes 1104+97152+98304 (`test_leech.py`) |
| 8 | Leech nearest-point quantizer is exact / bounded-distance-correct | 🟢 Proven | BDD round-trip within packing radius; numpy decoder matches reference, Δcost=0 |
| 9 | Random multi-coordinate tamper detected w.p. ≈ 1 − 4096/2²⁴ | 🟡 Experimental | membership probability bound; trials |
| 10 | CER reduction inside ML-KEM | 🟡 Experimental | `benchmark_mlkem.py`: **exact** FIPS-203 baselines (768/1088/1568 B) + coding-gain model ⇒ ~2–12.5%; cited range 7.4–31.9% (Liu–Sakzad) |
| 11 | Per-block timing: Leech quantize ~1.9 ms (vectorised) + sign-change ~2.7 µs | 🟡 Experimental | measured (hardware-dependent); reference quantizer ~129 ms; O(1) decoders faster |
| 12 | Multi-key derivation via wreath products in Co₀ | 🔴 Open | embodiment; independence needs KDF / non-commuting structure |
| 13 | Tamper flag introduces no decryption / reaction oracle | 🟢 Proven | `oracle-safety-analysis.md`: no DFR amplification (Lemma 1); membership redundant on the FO accept branch (Thm 1) ⇒ IND-CCA preserved (Thm 2), under placement A. Its constant-time dependency (#14) is now implemented + measured |
| 14 | Constant-time membership check (branch-free, data-oblivious) | 🟢 Measured | `rclp.golay_ct` + `ct/`: self-dual-basis predicate, no input-dependent branch/index/early-out; dudect `|t|≈1.8 < 4.5` with null control `0.93` on the dev machine — re-run on deployment target |
| 15 | Standalone post-quantum hardness from RCLP | ⛔ **Withdrawn** | indefensible — see `security-scope.md` |

## Language discipline (carried from the filing packet)

To keep claims defensible, the paper uses:

- "the sign-change layer is **self-inverse**" (not "the encoding is its own inverse")
- "**exact reversibility of the transformation layer**" (not "exact recovery for the whole KEM")
- "**auxiliary structural tamper-evidence without additional ciphertext expansion**"
  (not "tamper detection without MAC")
- "**domain-separated derived keys** from layer-indexed automorphism transcripts;
  independence requires a KDF" (not "independent keys from nested sign changes")

## What would move 🔴 → 🟢

- **#12 (multi-key):** a proof that chosen nested masks yield (computationally)
  independent keys under a named KDF, or a concrete non-commuting construction.
- **#13 (oracle):** ✅ done — see `oracle-safety-analysis.md`. Its constant-time
  dependency (#14) is now satisfied, so the result holds on platforms where the
  `ct/` measurement passes.
- **#14 (constant-time):** ✅ done — branch-free predicate (`rclp.golay_ct`) +
  dudect measurement (`ct/`), clean on the dev machine. Residual: re-run the
  harness on the production target (constant-time is microarchitecture-specific).
