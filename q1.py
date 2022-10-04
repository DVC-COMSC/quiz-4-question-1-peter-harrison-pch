counter = 0
remember = 0 

for i in range(10):
    num = int(input())
    if num % 2 == 0:
        if remember == 0:
            remember = 1
        elif remember == 1:
            counter = counter + 1
            remember = 2
    elif num % 2 == 1:
        remember = 0

print(counter)

# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
