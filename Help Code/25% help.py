def cube(number):
    return number * number * number

def by_three(number):
    if (number/3):
        print "It's divisible by 3!"
        return cube(number)

def main():
    user_number = input('Enter a number: ')
    by_three(user_number)

if __name__ == "__main__":
    main()
