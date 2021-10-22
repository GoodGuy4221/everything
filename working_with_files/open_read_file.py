f_name = 'file.txt'

file = open(f_name, 'r', encoding='utf-8')
print(type(file))
print(dir(file))
open(f_name, 'rb')

# option 1
# in generator mode, for big files
# IO operation
# for line in file:
#     print(line.strip())
#   # print(line, end='')


# option 2
# reads all file
# for binary file
# big string
# file_content = file.read()
# print(file_content)
# for symbol in file_content:
#     print(symbol)
# for line in file_content.splitlines():
#     print(line)


# option 3
# reads all file
# file_content = file.readlines()
# file_content = map(str.strip, file_content)
# for line in file_content:
#     # print(line.strip())
#     print(line)

# file_content = file.read(16)
# for symbol in file_content:
#     print(symbol)

# while True:
#     chunk = file.read(16)
#     print(chunk, end='')
#     print(f'\n{file.tell()}')
#     if not chunk:
#         break

file.close()
