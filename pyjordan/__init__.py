def find_file(path, pattern):

    """File finder
    Finds a file in the "path" directory that matches the "pattern"
    Keyword arguments:
    path -- the path of the file to look in
    pattern -- a pattern to search for
    Example:
    find_file("C:/Python/Python36", "*exe")
    """

    import os
    import warnings
    import fnmatch

    if os.path.isdir(path):
        result = []
        for root, dirs, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    result.append(os.path.join(root, name))
        return result

    else:
        warnings.warn("\nPath not found " + path)

    return None


def find_file_recursive(path, pattern, tries=100):
    """File finder - recursive
    Continues to search for a file for file with a certain number of tries.
    This is useful for when files are being downloaded and you want to check
      every second.  After each trie the os waits a
    Keyword arguments:
    path -- the path of the file to look in
    pattern -- a pattern to search for
    tries -- the number of attempts to search for the file
    """
    
    import time

    t = 0
    found_file = find_file(path=path, pattern=pattern)

    while len(found_file) == 0:
        time.sleep(1)
        found_file = find_file(path=path, pattern=pattern)
        t += 1
        txt = "File:" + path + pattern + " not found, attempt number {}"
        print(txt.format(t))

        if t == tries:
            txt = "Broken after {} tries"
            print(txt.format(t))
            raise Exception("Could not find file: ", path + pattern)
            return None
            break

    return found_file
    