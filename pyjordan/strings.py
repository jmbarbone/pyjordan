from pyjordan.tools import unnest, as_list


def str_replace_all(x, replacements):
    """ Dictionary replacements

    Description
    -----------
    Replaces strings found in dictionary.  The replacement is made in the order
      in which the replacements in the dictionary are provided.  This opens up
      opportunities for patterns created after serial replacement to be detected
      and replaced again.

    Parameters
    ----------
    x : string
        The text to replace
    replacements : dictionary
        The dictionary of items to replace

    Returns
    -------
    The same string passed with the text found substituted.

    Reference
    ---------
    https://stackoverflow.com/a/6117042

    Warnings
    --------
    Python dictionaries don't have a reliable order for iteration. This solution
      only solves your problem if:
    * order of replacements is irrelevant
    * it's ok for a replacement to change the results of previous replacements

    Inefficient if `text` is too big or there are many pairs in the dictionary.

    Example
    -------
    x = "The quick brown fox"
    d = {'brown': 'green', 'quick': 'slow', 'fox': 'platypus'}
    str_replace_all(x, d)
    """

    from collections import OrderedDict

    dic = OrderedDict(dic)

    for i, j in dic.items():
        text = text.replace(i, j)

    return text


def paste_combine(x, sep="", collate=True):
    """Paste combine

    Description
    -----------
    Combine strings together, with or without collation.  List passed must have

    Parameters
    ----------
    x : String, list
        A list of list of strings
    sep : String
        A character separation to use for the string combinations
    collate : Logical
        If True will collate strings, otherwise not

    Returns
    -------
    A list of strings

    Examples
    --------
    x = ["a", "b", "c"]
    y = [1, 2, 3]
    paste_combine([x, y])
    paste_combine([x, y], sep = "_")
    paste_combine([x, y], collate=False)
    paste_combine([["a", "b"], [1, 2], ["?", "!"]])
    """

    n = len(x)

    if n == 0:
        Exception("List is of length 0")
    elif n == 1:
        return(x)
    else:
        res = do_paste_combine(x[0], x[1], collate=collate, sep=sep)

    if n == 2:
        return res

    for i in range(2, n):
        res = do_paste_combine(res, x[i], collate=collate, sep=sep)

    return res


def do_paste_combine(x, y, sep="", collate=True):
    x = as_list(x)
    y = as_list(y)

    if collate:
        return [f"{i}{sep}{j}" for i in x for j in y]
    else:
        return unnest([[f"{i}{sep}{j}" for i in x] for j in y])
