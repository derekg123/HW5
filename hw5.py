import re

sample = open("regex_sum_36716.txt", "r")
sample = sample.read()
strnumbers = re.findall('[0-9]+', sample)
numbers = []
for x in strnumbers:
    numbers.append(int(x))
print(sum(numbers))
