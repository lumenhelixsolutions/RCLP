"""Unit tests for the [24,12,8] Golay code."""

import pytest
import numpy as np
from rclp.golay import GolayCode


@pytest.fixture(scope="module")
def golay():
    return GolayCode()


def test_codeword_count(golay):
    assert len(golay.codewords) == 4096


def test_weight_distribution(golay):
    assert golay.verify_weight_distribution()


def test_self_duality(golay):
    assert golay.verify_self_duality()


def test_minimum_distance(golay):
    """Every pair of distinct codewords differs in at least 8 positions."""
    np.random.seed(42)
    for _ in range(1000):
        i, j = np.random.randint(0, 4096, 2)
        if i == j:
            continue
        dist = int(np.sum(golay.codewords[i] != golay.codewords[j]))
        assert dist >= 8


def test_octad_count(golay):
    assert len(golay.octads()) == 759


def test_dodecad_count(golay):
    assert len(golay.dodecads()) == 2576


def test_hexadecad_count(golay):
    assert len(golay.hexadecads()) == 759


def test_steiner_system(golay):
    assert golay.verify_steiner_system(n_samples=200)


def test_nearest_codeword_corrects_3_errors(golay):
    """Nearest-codeword decoder should correct up to 3 errors perfectly."""
    np.random.seed(42)
    correct = 0
    trials = 1000
    for _ in range(trials):
        idx = np.random.randint(0, 4096)
        cw = golay.codewords[idx].copy()
        n_err = np.random.randint(0, 4)
        if n_err > 0:
            positions = np.random.choice(24, n_err, replace=False)
            received = cw.copy()
            for p in positions:
                received[p] ^= 1
        else:
            received = cw.copy()
        decoded, _ = golay.decode_nearest_codeword(received)
        if np.array_equal(decoded, cw):
            correct += 1
    assert correct == trials  # 100% for 0-3 errors


def test_sign_change_involution(golay):
    """Sigma_c^2 = identity."""
    np.random.seed(42)
    cw = golay.codewords[np.random.randint(0, 4096)]
    v = np.random.randint(-10, 11, size=24)
    once = GolayCode.apply_sign_change(cw, v)
    twice = GolayCode.apply_sign_change(cw, once)
    assert np.array_equal(twice, v)


def test_dodecad_dodecad_intersection(golay):
    """Verify the new dodecad-dodecad intersection profile {0:1, 4:495, 6:1584, 8:495}."""
    profile = golay.directed_intersection_profile(12, 12)
    assert profile == {0: 1, 4: 495, 6: 1584, 8: 495}


def test_krawtchouk_dodecad_parity_vanishing(golay):
    """K_s(12; 24) = 0 for all odd s."""
    for s in range(1, 24, 2):
        assert GolayCode.krawtchouk(s, 12, 24) == 0
