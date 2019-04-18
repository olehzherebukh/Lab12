import re

def count_operations():
    pattern = r"17/May/2015:(20|1[0-9]|0[1-9]):\d\d.+GET.+presentations.+200"
    file = open("apache_logs.txt", "r")
    counter = 0
    for line in file.readlines():
        if re.search(pattern, line):
            counter += 1
    print(counter)

count_operations()
print(count_operations)
            
