

def is_none(x):
    """ Is none

    True/False is value is None

    Parameters
    ----------
    x : An object

    Returns
    -------
    True if x is None, otherwise False
    """
    return x is None


def exists(x, where="local"):
    """ Exists

    Description
    -----------
    Checks if an object exists by the name of the object

    Parameters
    ----------
    x : str
        The name of an object as a string
    where : str, "local" (default), "global", or "builtin"
        Where to search for the object.  If not one of the three above, raises
        and exception

    Returns
    -------
    If object is found, True, otherwise False


    References
    ----------
    Adapted from: https://stackoverflow.com/a/6386015/12126576
    """

    import __builtin__
    import sys

    if where == "local":
        res = x in sys.getframe(1).f_locals
    elif where == "global":
        res = x in sys.getframe(1).f_globals
    elif where == "builtin":
        res = x in vars(__builtin__)
    else:
        raise Warning("`where` should be one of: 'local', 'global', 'builtin'")

    return(res)


def print_time(x):
    """ Print the current

    Description
    -----------
    Appends the current time into a print statement

    Parameters
    ----------
    x : String
        A message to be printed
    """
    from datetime import datetime
    ts = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    print(f"[{ts}] {x}", flush=True)
    return None


def round_by(x, by, method="round"):
    """ Round by

    Description
    -----------
    Rounds a number by another

    Parameters
    ----------
    x : numeric
        A number or list to round
    by : numeric
        The number or list by which to round
    method : string
        The method of rounding to use: round, ceiling, or floor

    Returns
    -------
    A list of rounded numbers
    """
    from math import floor, ceil

    x = as_list(x)
    by = as_list(by)

    FUN = {
        "round": round,
        "ceiling": ceil,
        "floor": floor,
    }

    if method not in ["round", "ceiling", "floor"]:
        raise Exception('`by` must be one of: "round", "ceiling", "floor"')

    try:
        return [FUN[method](i / b) * b for b in by for i in x]
    except KeyError:
        raise Exception('`method` must be one of: "round", "ceiling", "floor"')


def unnest(x):
    """ Unnest

    Description
    -----------
    Unnests a list of lists

    Parameters
    ----------
    x : list
        A list to be unnested

    Returns
    -------
    The values of `x` as separate elements

    Examples
    --------
    x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    unnest(x) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

    x = [[1], [2, [3, 4]]]
    unnest(x) # [1, 2, 3, 4]
    """
    res = [j for i in as_list(x) for j in as_list(i)]

    while any([isinstance(i, list) for i in res]):
        res = unnest(res)

    return res


def as_list(x):
    if not isinstance(x, list):
        x = [x]
    return x


def which(x):
    """ Which (is True)

    Description
    -----------
    Returns a numeric list of which elements are True

    Parameters
    ----------
    x : list, bool
        A list of bools

    Returns
    -------
    True or False

    Examples
    --------
    which(True) # [0]
    which([True, False, None, True, False]) # [0, 3]
    """
    x = as_list(x)
    out = []
    if not is_boolean(x):
        raise ValueError("x must be boolean")
    for i in range(0, len(x)):
        if x[i]:
            out.append(i)
    return out


def is_boolean(x):
    """ Is boolean?

    Description
    -----------
    Evaluates an object or list as boolean

    Returns
    -------
    True or False

    Examples
    --------
    is_boolean(True) # True
    is_boolean([1, 2, True, False]) # False
    is_boolean([True, None, False, True]) # True
    """
    if isinstance(x, list):
        return all([is_boolean(i) for i in x])
    return is_none(x) or isinstance(x, bool)
