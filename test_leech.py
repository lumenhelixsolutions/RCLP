"""Unit tests for RCLP-KEM."""

import pytest
from rclp.kem import RCLP_KEM


@pytest.fixture
def kem128():
    return RCLP_KEM(security_bits=128)


def test_parameter_validation():
    with pytest.raises(ValueError):
        RCLP_KEM(security_bits=100)


def test_keygen_structure(kem128):
    pk, sk = kem128.keygen(seed=42)
    assert len(pk) == kem128.n_layers
    assert len(sk) == kem128.n_layers
    for layer in pk:
        assert 't' in layer
    for layer in sk:
        assert 'c' in layer
        assert 'p' in layer


def test_kem_roundtrip(kem128):
    """Single keygen/encaps/decaps roundtrip."""
    pk, sk = kem128.keygen(seed=42)
    ct, ss_enc = kem128.encapsulate(pk, seed=43)
    ss_dec = kem128.decapsulate(sk, ct)
    assert ss_enc == ss_dec


def test_kem_correctness_100_trials(kem128):
    """Run 100 KEM roundtrips — should all succeed."""
    successes = 0
    for trial in range(100):
        pk, sk = kem128.keygen(seed=trial * 101)
        ct, ss_enc = kem128.encapsulate(pk, seed=trial * 103)
        ss_dec = kem128.decapsulate(sk, ct)
        if ss_enc == ss_dec:
            successes += 1
    assert successes == 100


def test_rclp_128_sizes():
    kem = RCLP_KEM(security_bits=128)
    assert kem.public_key_size() == 1152
    assert kem.secret_key_size() == 388
    assert kem.ciphertext_size() == 192


def test_rclp_192_sizes():
    kem = RCLP_KEM(security_bits=192)
    assert kem.public_key_size() == 1728
    assert kem.secret_key_size() == 582
    assert kem.ciphertext_size() == 288


def test_rclp_256_sizes():
    kem = RCLP_KEM(security_bits=256)
    assert kem.public_key_size() == 2304
    assert kem.secret_key_size() == 776
    assert kem.ciphertext_size() == 384


def test_different_encaps_yield_different_secrets():
    """Different encapsulation randomness yields different shared secrets."""
    kem = RCLP_KEM(security_bits=128)
    pk, sk = kem.keygen(seed=1)
    ct1, ss1 = kem.encapsulate(pk, seed=100)
    ct2, ss2 = kem.encapsulate(pk, seed=200)
    assert ss1 != ss2
    # And both should decrypt correctly
    assert kem.decapsulate(sk, ct1) == ss1
    assert kem.decapsulate(sk, ct2) == ss2
