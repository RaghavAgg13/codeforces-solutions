length = int(input())
x=0
for i in range(length):
   command = input()
   command = command.replace('X', "")
   command += ''
   for j in range(int(len(command) / 2)):
        if command[j*2-2] == command[j*2-2+1] == '+':
            x += 1
            # print(x)
        if command[j*2-2] == command[j*2-2+1] == '-':
            x -= 1
            # print(x)
      
print(x)