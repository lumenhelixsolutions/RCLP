# RCLP

<p align="center">
  <a href="https://lumenhelix.com">
    <img src="docs/assets/lumenhelix-logo.svg" alt="LumenHelix Solutions" width="180">
  </a>
</p>

<h3 align="center">Post-quantum cryptography from the Golay code, Leech lattice, and two-sided surfaces</h3>

<p align="center">
  <a href="https://lumenhelixsolutions.github.io/RCLP/">
    <img src="https://img.shields.io/badge/Launch_Page-RCLP-00D4FF?style=flat-square&logo=githubpages&logoColor=white" alt="Launch Page">
  </a>
  <a href="https://lumenhelix.com">
    <img src="https://img.shields.io/badge/Built_by-LumenHelix-7C3AED?style=flat-square" alt="Built by LumenHelix">
  </a>
  <img src="https://img.shields.io/badge/license-MIT-8A95A8?style=flat-square" alt="License">
</p>

---

**RCLP** is part of the [LumenHelix Solutions](https://lumenhelix.com) portfolio — applied symbolic dynamics & reversible computation for deterministic, traceable AI systems.

RCLP (Reversibility-Constrained Lattice Problem) is a post-quantum cryptographic framework built by LumenHelix. It defines a new hardness assumption using two-sided surface flips constrained by the Golay code and embedded in the Leech lattice. RCLP-KEM achieves 100 percent decryption correctness in verification and produces ciphertexts and secret keys roughly 5-6 times smaller than ML-KEM-768.

## Why this exists

- **Compact keys.** 192-byte ciphertexts and 388-byte secret keys at the 128-bit security level.
- **Self-inverse decryption.** The flip operation is an involution: applying it twice returns the original state.
- **Mathematically transparent.** Every foundational claim is backed by exact-computation verification scripts.

## Quick start

Install and run RCLP in under two minutes.

### macOS / Linux

```bash
# Clone
git clone https://github.com/lumenhelixsolutions/RCLP.git
cd RCLP

# Install & run
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/pip install -e .
.venv/bin/python -m pytest tests/
```

### Windows (PowerShell)

```powershell
# Clone
git clone https://github.com/lumenhelixsolutions/RCLP.git
Set-Location RCLP

# Install & run
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
.venv\Scripts\pip install -e .
.venv\Scripts\python -m pytest tests/
```

### Windows (Git Bash / WSL)

```bash
git clone https://github.com/lumenhelixsolutions/RCLP.git
cd RCLP
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/pip install -e .
.venv/bin/python -m pytest tests/
```

> **Device note:** RCLP is tested on Windows 11, macOS Sonoma, Ubuntu 22.04/24.04, and modern mobile browsers.

## Full documentation

Visit the launch page for architecture, API reference, and deployment guides:  
**https://lumenhelixsolutions.github.io/RCLP/**

## Features

| Feature | What it gives you |
|---------|-------------------|
| Golay constraint structure | The [24,12,8] extended binary Golay code enforces valid flip patterns and corrects up to 3 errors. |
| Leech lattice substrate | The unique 24-dimensional even unimodular lattice with 196,560 minimal vectors provides the geometric hardness. |
| Conway automorphisms | Sign-change automorphisms indexed by Golay codewords embed the monomial subgroup 2^12.M24 in Co0. |
| Verified by computation | All mathematical foundations — Golay weight distribution, Leech minimal vectors, KEM correctness — are computationally verified. |

## Architecture at a glance

```
RCLP/
├── golay.py          [24,12,8] Golay code construction
├── leech.py          Leech lattice Lambda_24 construction
├── surface.py        Two-sided surface model
├── kem.py            RCLP-KEM implementation
├── decoder.py        Babai + Golay nearest-codeword decoder
├── hypercomplex.py   Quaternion, octonion, sedenion arithmetic
└── tests/            Unit tests for Golay, Leech, KEM, and decoder
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

## Support & consulting

Need deterministic AI systems with full traceability? LumenHelix builds reversible computation kernels, governance layers, and end-to-end AI integrations.

- **Website:** https://lumenhelix.com
- **Services:** AI diagnostics, B.Y.O. support packages, governance audits
- **Research:** TEN² kernel, R.U.B.I.C. boundary discipline, C.O.R.E. constraint lens

## License

Released under the MIT License.

---

<p align="center">
  <sub>Engineered by <a href="https://lumenhelix.com">LumenHelix Solutions</a> — Applied Symbolic Dynamics & Reversible Computation.</sub>
</p>
