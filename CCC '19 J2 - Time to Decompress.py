for _ in range(int(input())):
    text = ""
    string_input =input()
    len_string = len(string_input)
    space_num = string_input.count(" ")+1
    num = string_input[:len_string-space_num]
    char = string_input[-1]
    for _ in range(int(num)):
            text= text+str(char)
    print(text)
