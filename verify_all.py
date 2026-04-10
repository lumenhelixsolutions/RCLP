{
  "rclp": {
    "RCLP-128": {
      "security_bits": 128,
      "layers": 2,
      "pk_bytes": 1152,
      "sk_bytes": 388,
      "ct_bytes": 192,
      "correctness_pct": 100.0,
      "keygen_us": 180.93204498291016,
      "encaps_us": 52.58798599243164,
      "decaps_us": 398.79322052001953,
      "total_us": 632.3132514953613
    },
    "RCLP-192": {
      "security_bits": 192,
      "layers": 3,
      "pk_bytes": 1728,
      "sk_bytes": 582,
      "ct_bytes": 288,
      "correctness_pct": 100.0,
      "keygen_us": 283.43725204467773,
      "encaps_us": 88.33742141723633,
      "decaps_us": 617.0468330383301,
      "total_us": 988.8215065002441
    },
    "RCLP-256": {
      "security_bits": 256,
      "layers": 4,
      "pk_bytes": 2304,
      "sk_bytes": 776,
      "ct_bytes": 384,
      "correctness_pct": 100.0,
      "keygen_us": 388.03815841674805,
      "encaps_us": 90.8365249633789,
      "decaps_us": 804.9163818359375,
      "total_us": 1283.7910652160645
    }
  },
  "ml_kem_768_reference": {
    "keygen_us": 2980,
    "encaps_us": 6557,
    "decaps_us": 4980,
    "total_us": 14517,
    "pk_bytes": 1184,
    "sk_bytes": 2400,
    "ct_bytes": 1088
  }
}