def cube(number):
<<<<<<< HEAD
    return number*number*number
def by_three(number):
    if number == number/3():
        return "by_three"
    else:
        return "False"
=======
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
>>>>>>> origin/master
