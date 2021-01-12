

def is_none(x):
    x is None


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


def print_time(message):
    from datetime import datetime
    ts = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    print(f"[{ts}] {message}", flush=True)
    return None
