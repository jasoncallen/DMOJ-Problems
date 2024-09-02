entries = int(input())
char_to_delete = []
word_list = []
for i in range(entries):
    line = input().split(" ")
    char_to_delete.append(line[0])
    line.pop(0)
    new_line = ' '.join(line)
    word_list.append(new_line)

new_word = ""
for i in range(len(char_to_delete)):
    length = len(word_list[i])
    slice_front = int(char_to_delete[i]) - 1
    new_word = word_list[i]
    new_word = new_word[:slice_front] + new_word[int(char_to_delete[i]):]
    word_list[i] = new_word

word_count = 1
for w in word_list:
    print(str(word_count)+ " " + w)
    word_count += 1
