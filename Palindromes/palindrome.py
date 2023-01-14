"""Find palindromes in dictionary txt file"""
import load_dictionary
import save_file

word_list = load_dictionary.load('slowa.txt')
pail_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pail_list.append(word)

save_file.save('palindromes.txt', pail_list)

print(f'Number of palindromes found = {len(pail_list)}')
print(*pail_list, sep='\n')
