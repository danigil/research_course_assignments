import regex

email_pattern = r"([a-zA-Z0-9]+)([_.-]{1}[a-zA-Z0-9]+)*@([a-zA-Z0-9])+(-{1}[a-zA-Z0-9]+)*\.([a-zA-Z]{2,})"

def create_fuzzies():
    from itertools import product

    for perm in list(product([False, True], repeat=3)):
        if perm in ((False, False, False), (True, True, True)):
            continue
        else:
            default = "\S*"

            ret = f'{r"([a-zA-Z0-9]+)([_.-]{1}[a-zA-Z0-9]+)*" if perm[0] else default}' \
                  f'@{r"([a-zA-Z0-9])+(-{1}[a-zA-Z0-9]+)*" if perm[1] else default}\.{r"([a-zA-Z]{2,})" if perm[2] else default}'
            yield ret

def print_email_addresses(name: str):
    valid = []
    fuzzy = []
    if regex.fullmatch("[a-zA-Z0-9]+.txt", name):
        with open(name, 'r') as file:
            for line in file:
                valid.append(regex.search(email_pattern, line))
                fuzzy += [regex.search(current_fuzzy, line) for current_fuzzy in create_fuzzies()]

        valid = set(map(lambda x: x.group(), filter(lambda x: x is not None, valid)))
        fuzzy = set(map(lambda x: x.group(), filter(lambda x: x is not None, fuzzy))) - valid

        print("Valid email addresses: ")
        for email in valid:
            print(email)

        print(" ")

        print("Invalid email addresses: ")
        for email in fuzzy:
            print(email)



    else:
        print("ERROR: TERMINATING | argument name needs to be of the following form:\t{filename}.txt")
        raise Exception

if __name__ == '__main__':
    print_email_addresses("emails.txt")
    # create_fuzzies()
    # for i in create_fuzzies():
    #    print(i)
