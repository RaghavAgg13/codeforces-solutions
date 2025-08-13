keyboard = 'qwertyuiopasdfghjkl;zxcvbnm,./'

dir = input()
s = input()
s_ = ''
for i in range(len(s)):
    if dir == 'R':
        s_ += keyboard[keyboard.index(s[i])-1]
    else:
        s_ += keyboard[keyboard.index(s[i])+1]

print(s_)