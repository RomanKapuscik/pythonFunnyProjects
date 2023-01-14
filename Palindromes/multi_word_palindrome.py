"""Find all multi-word palindromes"""
import time
import load_dictionary
import save_file

word_list = load_dictionary.load('2of12.txt')


def find_multi_word_palindromes(words: list):
    """Finds all multi-word palindromes possible to create using words from given dictionary.

    :param words: list (list of words from dictionary)
    :return: list (list of multi-word palindromes)
    """
    pali_list = []
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list


stat_time = time.time()

multi_word_palindromes = find_multi_word_palindromes(word_list)
multi_word_palindromes_sorted = sorted(multi_word_palindromes)

save_file.save_multi('multi_word_palindromes.txt', multi_word_palindromes_sorted)

print(f'Number of palindromes find: {len(multi_word_palindromes_sorted)}')
for first, second in multi_word_palindromes_sorted:
    print(f'{first} {second}')

end_time = time.time()

print(f'Runtime for this program was {end_time - stat_time} seconds.')
