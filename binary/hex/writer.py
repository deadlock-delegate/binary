from struct import pack


def write_low(data, nibble=None):
    """Write a hex string with low nibble first

    Args:
        data (int)
        nibble (str, optional): format string

    Returns:
        bytes: bytes object containing data
    """
    fmt = 'h{}'.format(nibble) if nibble else 'h'
    return pack(fmt, data)


def write_high(data, nibble=None):
    """Write a hex string with high nibble first

    Args:
        data (int)
        nibble (str, optional): format string

    Returns:
        bytes: bytes object containing data
    """
    fmt = 'H{}'.format(nibble) if nibble else 'H'
    return pack(fmt, data)
