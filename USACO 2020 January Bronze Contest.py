input_file = open('word.in', 'r')
output_file = open('word.out','w')

no_of_words, max_chars = input_file.readline().split()
words = input_file.readline().split()

chars_count = 0
line = ''
print(int(max_chars))
for word in words:
    if chars_count + len(word) <= int(max_chars):
        line = line + word + " "
        chars_count += len(line)
    else:
        output_file.write(line[:-1] + '\n')
        line = word + " "
        chars_count = len(word)

output_file.write(line[:-1] + '\n')

input_file.close()
output_file.close()
