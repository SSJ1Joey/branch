print('Hello, would you like to do some grading today?\n')
print('*' * 47)

answer = int(input('What is the score of your thing? [0-100]: '))
if answer not in range(0, 101):
    print("Please enter a number between 0 and 100..")
elif answer in range(90, 101):
    print('A')
elif answer in range(80, 90):
    print('B')
elif answer in range(70, 80):
    print('C')
elif answer in range (60, 70):
    print('D')
else:
    print('F')
