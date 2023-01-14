def save(file, palindrome_list: list):
    """Saves

    :param palindrome_list: list
    :param file: .txt file
    """
    with open(file, 'w') as out_file:
        for palindrome in palindrome_list:
            out_file.write(f"{palindrome}\n")


def save_multi(file, palindrome_list: list):
    """Saves

    :param palindrome_list: list
    :param file: .txt file
    """
    with open(file, 'w') as out_file:
        for first, second in palindrome_list:
            out_file.write(f'{first} {second}\n')
