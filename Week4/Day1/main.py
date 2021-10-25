
print('Please enter a number between 1 and 100')
num = int(input())

if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')

elif num % 3 ==0:
    print('Fizz')
elif num % 5 ==0:
    print('Buzz')


