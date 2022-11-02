from cipher_dws2138v2 import cipher_dws2138v2

def test_negative_cipher():
    example = 'Apple', -2
    expected = 'ynnjc'
    actual = cipher_dws2138v2.cipher('Apple', -2)
    assert actual == expected