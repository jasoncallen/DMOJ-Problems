notes = input()

a_minor = 0
c_major = 0

for i in range(len(notes)):
    if i == 0 or notes[i - 1] == '|':
        if notes[i] in 'ADE':
            a_minor = a_minor + 1
        if notes[i] in 'CFG':
            c_major = c_major + 1

if a_minor == c_major:
    if notes[-1] == 'A':
        a_minor = a_minor + 1
    else:
        c_major = c_major + 1

if a_minor > c_major:
    print('A-mol') 
else:
    print('C-dur')