"""Find palindromes in dictionary txt file"""
import load_dictionary

word_list = load_dictionary.load('2of12.txt')
pail_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pail_list.append(word)

print(f'Number of palindromes found = {len(pail_list)}')
print(*pail_list, sep='\n')
