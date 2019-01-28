from struct import pack, unpack_from


def read_bit8(data, offset=0):
    """Write a signed 8 bit integer

    Args:
        data (bytes)

    Returns:
        int
    """
    return unpack_from('b', data, offset)[0]


def read_bit16(data, offset=0):
    """Write a signed 16 bit integer

    Args:
        data (bytes)

    Returns:
        int
    """
    return unpack_from('h', data, offset)[0]


def read_bit32(data, offset=0):
    """Write a signed 32 bit integer

    Args:
        data (bytes)

    Returns:
        int
    """
    return unpack_from('l', data, offset)[0]


def read_bit64(data, offset=0):
    """Write a signed 64 bit integer

    Args:
        data (bytes)

    Returns:
        int
    """
    return unpack_from('q', data, offset)[0]


def write_bit8(data):
    """Write a signed 8 bit integer

    Args:
        data (int)

    Returns:
        bytes: bytes object containing value from data
    """
    return pack('b', data)[1]


def write_bit16(data):
    """Write a signed 16 bit integer

    Args:
        data (int)

    Returns:
        bytes: bytes object containing value from data
    """
    return pack('h', data)[1]


def write_bit32(data):
    """Write a signed 32 bit integer

    Args:
        data (int)

    Returns:
        bytes: bytes object containing value from data
    """
    return pack('l', data)[1]


def write_bit64(data):
    """Write a signed 64 bit integer

    Args:
        data (int)

    Returns:
        bytes: bytes object containing value from data
    """
    return pack('q', data)[1]
