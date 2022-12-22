def fizzbuzz():
    """funct that prints the numbers from 1 to 100 separated by a space
       For mul of three print Fizz and for multiples of five print Buzz.
       For mul of both three and five print FizzBuzz"""
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end=" ")
        elif number % 3 == 0:
            print("Fizz", end=" ")
        elif number % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(f"{number}", end=" ")
