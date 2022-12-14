import sys


def load(file) -> list:
    """Opens text file as a list, converts to lower letters.

    :param file: .txt file
    :return: list
    """
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print('{}\nError opening {}. Terminating program.'.format(e, file), file=sys.stderr)
        sys.exit(1)
