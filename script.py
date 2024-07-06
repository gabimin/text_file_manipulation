text_file = input('File: ')
opt1 = '1 Replace line breaks with spaces'
opt2 = '2 Replace dots with dots and line breaks'
opt3 = '3 Trim leading white spaces'
try:
    handle = open(text_file)
    content = handle.read()
except:
    print('File not found')
    quit() 
print(f'Options:\n{opt1}\n{opt2}\n{opt3}\n')
option = input()
if option == '1':
    mod = content.replace('\n', ' ')
    handle = open('sprint.txt', 'w')
    esc = handle.write(mod)
    handle.close()
elif option == '2':
    mod2 = content.replace('.', '.\n')
    handle = open('sprint.txt', 'w')
    esc = handle.write(mod2)
    handle.close()
elif option == '3':
    lines = content.splitlines()
    trimmed_lines = []
    for line in lines:
        trimmed_lines.append(line.lstrip())
    mod3 = "\n".join(trimmed_lines)
    handle = open('sprint.txt', 'w')   
    esc = handle.write(mod3)
    handle.close()
else:
    print('Bad input')
    quit() 

handle2 = open(text_file)
print(handle2.read()) 
