# RCLP

<p align="center">
  <img src="docs/assets/logo.svg" alt="RCLP logo" width="160">
</p>

<h3 align="center">Post-quantum. Lattice-hard. Self-inverse.</h3>

<p align="center">A post-quantum cryptographic framework built from the Golay code, Leech lattice, and two-sided surfaces.</p>

<p align="center">
  <a href="https://lumenhelixsolutions.github.io/RCLP/">Launch Page</a>
  <span> · </span>
  <a href="https://github.com/lumenhelixsolutions/RCLP">GitHub</a>
  <span> · </span>
  <a href="https://lumenhelix.com">LumenHelix</a>
</p>

---

RCLP (Reversibility-Constrained Lattice Problem) defines a new hardness assumption using two-sided surface flips constrained by the Golay code and embedded in the Leech lattice. RCLP-KEM achieves 100 percent decryption correctness and ciphertexts/secret keys roughly 5-6 times smaller than ML-KEM-768.

## Why RCLP

- **Compact keys.** 192-byte ciphertexts and 388-byte secret keys at the 128-bit security level.
- **Self-inverse decryption.** The flip operation is an involution: applying it twice returns the original state.
- **Mathematically transparent.** Every foundational claim is backed by exact-computation verification scripts.

## Quick start

### macOS / Linux

```bash
git clone https://github.com/lumenhelixsolutions/RCLP.git
cd RCLP
git clone https://github.com/lumenhelixsolutions/RCLP.git
cd RCLP
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/pip install -e .
.venv/bin/python -m pytest tests/
```

### Windows (PowerShell)

```powershell
git clone https://github.com/lumenhelixsolutions/RCLP.git
Set-Location RCLP
git clone https://github.com/lumenhelixsolutions/RCLP.git
Set-Location RCLP
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
.venv\Scripts\pip install -e .
.venv\Scripts\python -m pytest tests/
```

### Windows (Git Bash / WSL)

```bash
git clone https://github.com/lumenhelixsolutions/RCLP.git
cd RCLP
git clone https://github.com/lumenhelixsolutions/RCLP.git
cd RCLP
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/pip install -e .
.venv/bin/python -m pytest tests/
```

> Tested on Windows 11, macOS Sonoma, Ubuntu 22.04/24.04, and modern mobile browsers.

## Features

| Feature | What it gives you |
|---------|-------------------|
| Golay constraint structure | The [24,12,8] extended binary Golay code enforces valid flip patterns and corrects up to 3 errors. |
| Leech lattice substrate | The unique 24-dimensional even unimodular lattice with 196,560 minimal vectors provides the geometric hardness. |
| Conway automorphisms | Sign-change automorphisms indexed by Golay codewords embed the monomial subgroup 2^12.M24 in Co0. |
| Verified by computation | All mathematical foundations — Golay weight distribution, Leech minimal vectors, KEM correctness — are computationally verified. |

## Architecture

```
Golay Code  ->  Valid Flip Pattern  ->  Leech Lattice Vector  ->  Two-Sided Surface  ->  RCLP-KEM Ciphertext
       ^                                                                            |
       └─────────────── Babai + Nearest-Codeword Decoder ───────────────────────────┘
```

## Development

```bash
# Verify mathematical foundations
python verify_golay.py
python verify_leech.py
python benchmark.py

# Run full test suite
python -m pytest tests/
```

## Roadmap

- [ ] Formal hardness reduction from RCLP to standard lattice problems
- [ ] Quantum security analysis and independent cryptanalytic review
- [ ] Optimized C/C++ reference implementation for fair benchmarking

## License

Released under the MIT License.

---

<p align="center">
  <sub>RCLP is a <a href="https://lumenhelix.com">LumenHelix</a> project — Applied Symbolic Dynamics & Reversible Computation.</sub>
</p>
