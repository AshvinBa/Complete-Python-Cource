f=open('file.txt')

t=f.read()

# print(f.readlines())
# print(f.readline())

# for line in f:
#     print(line)
  
  
if 'Software field' in t:
    print('Found')
    # f.close()

else:
    print('Not Found')
    # f.close()

# asg=open('anothr.txt')
# asg.write("Please Send me a file")
# asg.close()

asg = open('another.txt', 'w')
asg.write("Please Send me a file")
asg.close()
