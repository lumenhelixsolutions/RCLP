#!/usr/bin/env python3
"""
verify_all.py — Run the complete RCLP mathematical verification suite.

This script exercises every verification method in the RCLP library and
produces a JSON report of all results.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from rclp.verification import verify_all


def main():
    results = verify_all(verbose=True)

    # Save to JSON
    out_file = Path(__file__).parent.parent / "results" / "verification_report.json"
    out_file.parent.mkdir(exist_ok=True)
    with open(out_file, 'w') as f:
        json.dump({
            'tests': results,
            'total': len(results),
            'passed': sum(1 for v in results.values() if v),
            'failed': sum(1 for v in results.values() if not v),
        }, f, indent=2)

    print(f"\nReport saved to {out_file}")

    # Exit with nonzero code if any tests failed
    if not all(results.values()):
        sys.exit(1)


if __name__ == "__main__":
    main()
