# 5. Break, Continue, and Pass Statements
# 1. Use a  for  loop to print numbers from 1 to 10, but stop the loop if the number is 7 (use  break ).
for i in range(1, 11):
    if i == 7:
        break
    print(i)

# 2. Print numbers from 1 to 10, skipping the number 5 (use  continue ).
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# 3. Write a loop that goes through numbers 1 to 5, but does nothing for number 3 (use  pass ).
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
