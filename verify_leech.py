{
  "golay_helps": "reduces search from 2^24 to 2^12 given p",
  "golay_hinders": [
    "quantization (no weight 1-7)",
    "min_distance_8 prevents hill-climbing",
    "algebraic_rigidity (k known bits -> 2^(12-k) compatible)"
  ],
  "net_effect": "security-neutral if p known, security-positive if p unknown",
  "critical_assumption": "secrecy of base point p (protected by enriched encoding)",
  "security_estimates": {
    "conservative_per_layer_bits": 12,
    "moderate_per_layer_bits": 40,
    "optimistic_per_layer_bits": 72
  },
  "brute_force_with_known_p": "100% success in O(4096)",
  "verdict": "Enrichment is where real security lives, not bare Golay constraint"
}