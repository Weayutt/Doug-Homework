def distance_from_zero(arg):
    return type(arg) == int or type(arg) == float
    if type == int or float:
        return abs(10)
    else:
        return "Nope"

print distance_from_zero(-10)
print distance_from_zero(1.0)
print distance_from_zero(-1.0)