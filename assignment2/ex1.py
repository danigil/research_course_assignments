import sys
import regex

email_pattern = "[a-zA-Z0-9]+([_.-]{1}[a-zA-Z0-9]+)*@[a-zA-Z0-9]+(-{1}[a-zA-Z0-9]+)*\.[a-zA-Z]{2,}"


def is_valid_address(address: str) -> bool:
    return regex.fullmatch(email_pattern,address)


def print_email_addresses(name: str):
    """
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    """
    if regex.fullmatch("[a-zA-Z0-9]+.txt", name):
        with open(name,'r') as file:
            for line in file:
                #print(f"current line: {line}",end="")
                m = regex.search(email_pattern,line,partial=True)
                print(m)
                """
                if m is not None:
                    print (m.group())
                    """


    else:
        print("ERROR: TERMINATING | argument name needs to be of the following form:\t{filename}.txt")
        raise Exception
    """
    else:
        print("ERROR: TERMINATING | Not enough arguments/too many arguments")
        raise Exception
    """

if __name__ == '__main__':
    print_email_addresses("emails.txt")