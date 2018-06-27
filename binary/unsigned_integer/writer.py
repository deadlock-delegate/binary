from struct import pack


def write_bit8(data):
    return pack('C', data)


def write_bit16(data, endianness=False):
    """Write an unsigned 16 bit integer

    Args:
        data (int)

    Returns:
        bytes: bytes object containing value from data
    """

    if endianness is True:
        value = pack('n', data)  # big-endian
    elif endianness is False:
        value = pack('v', data)  # little-endian
    elif endianness is None:
        value = pack('S', data)  # machine byte order
    else:
        raise Exception('Invalid value "{}" for endianness given'.format(endianness))
    return value


def write_bit32(data, endianness=False):
    """Write an unsigned 32 bit integer

    Args:
        data (int)

    Returns:
        bytes: bytes object containing value from data
    """
    if endianness is True:
        value = pack('N', data)  # big-endian
    elif endianness is False:
        value = pack('V', data)  # little-endian
    elif endianness is None:
        value = pack('L', data)  # machine byte order
    else:
        raise Exception('Invalid value "{}" for endianness given'.format(endianness))
    return value


def write_bit64(data, endianness=False):
    """Write an unsigned 64 bit integer

    Args:
        data (int)

    Returns:
        bytes: bytes object containing value from data
    """
    if endianness is True:
        value = pack('J', data)  # big-endian
    elif endianness is False:
        value = pack('P', data)  # little-endian
    elif endianness is None:
        value = pack('Q', data)  # machine byte order
    else:
        raise Exception('Invalid value "{}" for endianness given'.format(endianness))
    return value
