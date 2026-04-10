# RCLP Mathematical Background

## The [24,12,8] Extended Binary Golay Code

The Golay code C is the unique self-dual [24,12,8] binary linear code. Weight distribution: A₀ = A₂₄ = 1, A₈ = A₁₆ = 759, A₁₂ = 2,576.

The 759 octads (weight-8 codewords) form a Steiner system S(5,8,24): every 5-element subset of {0,...,23} lies in exactly one octad.

**Corrections identified in this work:** The duality relation F(w,s) = (-1)^s F(n-w,s) holds only at even depths. The odd-depth formulation in prior work is incorrect.

## The Leech Lattice Λ₂₄

The unique 24-dimensional even unimodular lattice with no vectors of norm 2. Kissing number: 196,560 = 1,104 (Type A) + 97,152 (Type B) + 98,304 (Type C).

## The Conway Group Co₀

|Co₀| = 8,315,553,613,086,720,000. Contains the monomial subgroup 2¹².M₂₄ (|M₂₄| = 244,823,040) at index 8,292,375.

**Key theorem:** For each Golay codeword c, the sign-change σ_c(v)_i = (-1)^{c_i}·v_i is an automorphism of Λ₂₄. This is the mathematical foundation of the two-sided surface flip.

## Intersection Atlas

All 9 directed pairwise intersection profiles between octads, dodecads, and hexadecads were computed. Notable new result: the dodecad-dodecad profile {0:1, 4:495, 6:1584, 8:495} is palindromic, reflecting complement symmetry.

## Hypercomplex Algebras

The post-quantum crypto suite uses three Cayley-Dickson algebras:
- Quaternions (4D): non-commutative, associative → QTRU
- Octonions (8D): non-commutative, non-associative, alternative → OTRU
- Sedenions (16D): has 1,344 zero-divisor pairs in bipartite graph → CSTRU

The Lie algebra chain G₂ ⊂ F₄ ⊂ E₈ → Λ₂₄ → Co₀ connects all three to the Leech lattice.
