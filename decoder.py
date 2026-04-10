{
  "bits_per_side": 192,
  "bytes_per_side": 24,
  "components": {
    "color": 24,
    "glyph": 21,
    "sedenion": 128,
    "position": 5,
    "reserved": 14
  },
  "total_bits_24_positions": 9216,
  "min_flip_payload_bits": 1536,
  "per_layer_secret_bits": 1548,
  "amplification_factor": 129,
  "parameter_sets": {
    "RCLP-128": {
      "layers": 2,
      "pk_bytes": 1152,
      "sk_bytes": 388,
      "ct_bytes": 192
    },
    "RCLP-192": {
      "layers": 3,
      "pk_bytes": 1728,
      "sk_bytes": 582,
      "ct_bytes": 288
    },
    "RCLP-256": {
      "layers": 4,
      "pk_bytes": 2304,
      "sk_bytes": 776,
      "ct_bytes": 384
    }
  }
}