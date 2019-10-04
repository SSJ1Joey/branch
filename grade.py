print('Hello, would you like to do some grading today?\n')
print('*' * 47)

answer = int(input('What is the score of your thing? [0-100]: '))
if answer not in range(0, 101):
    print("Please enter a number between 0 and 100..")
elif answer in range(90, 95):
    print('A-')
elif answer == 95:
    print('A')
elif answer in range(96, 101):
    print('A+')
elif answer in range(80, 85):
    print('B-')
elif answer == 85:
    print('B')
elif answer in range(86, 90):
    print('B+')
elif answer in range(70, 75):
    print('C-')
elif answer == 75:
    print('C')
elif answer in range(76, 80):
    print('C+')
elif answer in range(60, 65):
    print('D-')
elif answer == 65:
    print('D')
elif answer in range(66, 70):
    print('D+')
else:
    print('F')
