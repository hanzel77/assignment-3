import os

path = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(path, "indata.txt")

f = open(file_path, "rt")

result = 0
for num in f:
    result += int(num)

result = "{:.2f}".format(result)

print(result)