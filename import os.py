import os

arquivo1 = open ("text.txt", 'w')

print(os.path.relpath(arquivo1.name))