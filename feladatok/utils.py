def dms_to_deg(dms):
    '''
    Convert from degree-minute-second format to degree.

    Args:
        dms: an array like element with 3 element

    Returns:
        Degree in float.
    '''

    return dms[0] + dms[1] / 60 + dms[2] / 3600

def deg_to_dms(deg):
    '''
    Convert from  degree to degree-minute-second format.

    Args:
        deg: the degree in number

    Returns:
        A tuple: (deg, min, sec).
    '''

    degree = int(deg)

    minute = int((deg - degree) * 60)

    second = (deg - degree - minute / 60) * 3600

    return (degree, minute, second)
