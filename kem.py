{
  "name": "Reversibility-Constrained Lattice Problem",
  "lattice": "Leech Lambda_24 (24-dimensional, min norm 4)",
  "code": "[24,12,8] extended binary Golay code",
  "flip_group": "2^12 sign changes (Golay codewords)",
  "valid_patterns": 4096,
  "total_patterns": 16777216,
  "constraint_ratio": "4096:1",
  "hardness_sources": [
    "H1: Lattice CVP (~40 bits)",
    "H2: Golay constraint (12 bits)",
    "H3: Involution quantization (sigma^2 = id, min weight 8)",
    "H4: Cross-channel consistency (4 coupled channels)",
    "H5: Matryoshka composition (wreath products in Co_0)"
  ],
  "fundamental_operation": "FLIP: swap complete 192-bit state tuples at Golay-constrained positions"
}