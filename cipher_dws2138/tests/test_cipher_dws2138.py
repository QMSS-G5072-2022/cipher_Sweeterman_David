from cipher_dws2138 import cipher_dws2138

def test_negative_cipher():
    example = 'Apple', -2
    expected = 'ynnjc'
    actual = cipher_dws2138.cipher('Apple', -2)
    assert actual == expected