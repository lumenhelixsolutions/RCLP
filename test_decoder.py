"""Unit tests for the Leech lattice Lambda_24."""

import pytest
import numpy as np
from rclp.leech import LeechLattice


@pytest.fixture(scope="module")
def leech():
    return LeechLattice()


def test_type_a_count(leech):
    vecs = leech.build_type_a()
    assert len(vecs) == 1104


def test_type_a_norms(leech):
    vecs = leech.build_type_a()
    norms = (vecs ** 2).sum(axis=1)
    assert bool(np.all(norms == 32))


def test_sign_change_preserves_type_a(leech):
    """Sign-change automorphisms preserve the Type A minimal vector set."""
    assert leech.verify_sign_change_preservation(sample_size=30)


def test_co0_order():
    assert LeechLattice.CO0_ORDER == 8_315_553_613_086_720_000


def test_m24_order():
    assert LeechLattice.M24_ORDER == 244_823_040


def test_monomial_order():
    assert LeechLattice.MONOMIAL_ORDER == 1_002_795_171_840


def test_co0_index():
    assert LeechLattice.co0_index() == 8_292_375


@pytest.mark.slow
def test_full_kissing_number(leech):
    """Verify all 196,560 minimal vectors. Slow: builds Type B + Type C."""
    assert leech.verify_kissing_number()
