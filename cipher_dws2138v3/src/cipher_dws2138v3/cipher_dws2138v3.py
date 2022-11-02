def cipher(text, shift, encrypt=True):
    
    '''
    Cesar shift cipher.  Tool to decrypt/encrypt text that uses the substitution of a letter by another one further in the alphabet.

    Parameters
    ----------
    text : str plain text: The message to encrypt.
    shift : integer input: The number of letters the cipher will shift the text. Can be a positive for negative integer. 
    encrypt : boolean True, False: If True, the message is encrypted.  If False, the message is decrypted.

    Returns
    -------
    New str plain text message that is encrypted, or decrypted, by a shift in letters down or up the cipher alphabet. 

    Examples
    --------
    >>> Cipher (text, shift, encrypt=True)
        >>> text = str([‘Two Bites of the Apple’])
        >>> shift = int([3])
        >>> encrypt = True
    [‘Wzr Elwhv ri wkh Dssoh’]

    >>> Cipher (text, shift, encrypt=False)
        >>> text = str([‘Wzr Elwhv ri wkh Dssoh’])
        >>> shift = int([3])
        >>> encrypt = False
    [‘Two Bites of the Apple’]
    '''
    
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text