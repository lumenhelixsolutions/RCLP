{
  "decoder_version": "v3 (Babai + Golay nearest-codeword + min-coord rejection)",
  "correctness": "100.00% (5000/5000 trials)",
  "best_config": {
    "q": 31,
    "min_coord": 4,
    "noise_weight": 1
  },
  "techniques": [
    "Babai nearest-plane rounding: compare |diff_i| vs |diff_i + 2p_i|",
    "Golay nearest-codeword: O(4096 x 24), corrects up to 3 errors",
    "Min coordinate rejection: |p_i| >= 4 ensures signal dominates noise"
  ]
}