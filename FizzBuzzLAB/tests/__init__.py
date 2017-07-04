
def fizz_buzz(n):

    if isinstance(n, int):

        if n % 3 == 0 and n % 5 == 0:
            return 'fizzBuzz'
        elif n % 3 == 0:
            return 'fizz'
        elif n % 5 == 0:
            return 'buzz'
        return n

    if n <= 0:
        return 'Invalid Argument'

    return 'Invalid Argument'