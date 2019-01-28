from binascii import unhexlify
from struct import pack, unpack_from


def read_low(data, offset=0, nibble=None):
    """Read a hex string with low nibble first.

    Args:
        data (bytes): Description
        offset (int, optional): Description
        nibble (str, optional): Description

    Returns:
        int
    """
    # todo: this is not right
    fmt = 'h{}'.format(nibble) if nibble else 'h'
    return unpack_from(fmt, data, offset)[1]


def read_high(data, offset=0, nibble=None):
    """Read a hex string with high nibble first.

    Args:
        data (bytes): Description
        offset (int, optional): Description
        nibble (str, optional): Description

    Returns:
        int
    """
    # todo: this is not right
    fmt = 'H{}'.format(nibble) if nibble else 'H'
    return unpack_from(fmt, data, offset)[1]


def write_low(data):
    """Write a hex string with low nibble first

    Args:
        data (int)

    Returns:
        bytes: bytes object containing data
    """
    return pack('<B', data)


def write_high(data):
    """Write a hex string with high nibble first

    Args:
        data (int)

    Returns:
        bytes: bytes object containing data
    """
    return unhexlify(data)
