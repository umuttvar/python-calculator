from calculator import topla, cikar, carp, bol

def test_topla():
    assert topla(2, 3) == 5
    assert topla(-1, 1) == 0

def test_cikar():
    assert cikar(5, 3) == 2
    assert cikar(0, 5) == -5

def test_carp():
    assert carp(3, 4) == 12
    assert carp(0, 5) == 0

def test_bol():
    assert bol(10, 2) == 5
    assert bol(9, 3) == 3