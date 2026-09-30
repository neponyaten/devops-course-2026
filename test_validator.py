from validator import validate_email, validate_phone, validate_snils


def test_validate_email():
    assert validate_email('user@example.com') is True
    assert validate_email('bad-email') is False


def test_validate_phone():
    assert validate_phone('+79991234567') is True
    assert validate_phone('89991234567') is False
    assert validate_phone('+7999123') is False


def test_validate_snils():
    assert validate_snils('11223344595') is True
    assert validate_snils('123') is False
