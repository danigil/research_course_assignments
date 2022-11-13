from doctest import testmod

import regex

email_pattern = r"([a-zA-Z0-9]+)([_.-]{1}[a-zA-Z0-9]+)*@([a-zA-Z0-9])+(-{1}[a-zA-Z0-9]+)*\.([a-zA-Z]{2,})"

def create_fuzzies():
    """
        create_fuzzies
        supplementery method that generates fuzzy email patterns (patterns for regex that violate the ruleset partly)

        >>> [print(fuzz) for fuzz in create_fuzzies()]
        \S*@\S*\.([a-zA-Z]{2,})
        \S*@([a-zA-Z0-9])+(-{1}[a-zA-Z0-9]+)*\.\S*
        \S*@([a-zA-Z0-9])+(-{1}[a-zA-Z0-9]+)*\.([a-zA-Z]{2,})
        ([a-zA-Z0-9]+)([_.-]{1}[a-zA-Z0-9]+)*@\S*\.\S*
        ([a-zA-Z0-9]+)([_.-]{1}[a-zA-Z0-9]+)*@\S*\.([a-zA-Z]{2,})
        ([a-zA-Z0-9]+)([_.-]{1}[a-zA-Z0-9]+)*@([a-zA-Z0-9])+(-{1}[a-zA-Z0-9]+)*\.\S*
        [None, None, None, None, None, None]
    """
    from itertools import product

    for perm in (product([False, True], repeat=3)):

        if perm in ((False, False, False), (True, True, True)):
            continue
        else:

            default = "\S*"

            ret = f'{r"([a-zA-Z0-9]+)([_.-]{1}[a-zA-Z0-9]+)*" if perm[0] else default}' \
                  f'@{r"([a-zA-Z0-9])+(-{1}[a-zA-Z0-9]+)*" if perm[1] else default}\.{r"([a-zA-Z]{2,})" if perm[2] else default}'
            yield ret

def print_email_addresses(name: str):
    """
    print_email_addresses
    takes string that represents a text file name to open
    the function prints a list of all valid email addresses, and a list of all invalid addresses.

    >>> print_email_addresses("email_test.txt")
    Valid email addresses:
    abc.def@mail.com
    <BLANKLINE>
    Invalid email addresses:
    def@@mail..c
    """
    valid = []
    fuzzy = []
    if regex.fullmatch("\S+.txt", name):
        with open(name, 'r') as file:
            for line in file:
                valid.append(regex.search(email_pattern, line))
                fuzzy += [regex.search(current_fuzzy, line) for current_fuzzy in create_fuzzies()]

        valid = set(map(lambda x: x.group(), filter(lambda x: x is not None, valid)))
        fuzzy = set(map(lambda x: x.group(), filter(lambda x: x is not None, fuzzy))) - valid

        print("Valid email addresses:")
        for email in valid:
            print(email)

        print(" ")

        print("Invalid email addresses:")
        for email in fuzzy:
            print(email)



    else:
        print("ERROR: TERMINATING | argument name needs to be of the following form:\t{filename}.txt")
        raise Exception

if __name__ == '__main__':
    testmod(name='assignment3_ex1', verbose=True)

