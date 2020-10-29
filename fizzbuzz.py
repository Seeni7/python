def fizzBuzz():
    # Write your code here
    for i in  range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif 1 % 3 == 0:
            print ('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(str(i))