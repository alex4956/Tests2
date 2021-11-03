import sys
# if sys.version_info[0:2] != (2, 6):
#     raise Exception('Requires python 2.6')

x0 = sys.version_info
x = sys.version_info[0:3]

print(x0)
print(x)


