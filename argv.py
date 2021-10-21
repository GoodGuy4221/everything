import sys

# print(sys.argv)
app, *args = sys.argv
print(app, *args, sep='\n')

# args = sys.argv[:1]
# print(args)
