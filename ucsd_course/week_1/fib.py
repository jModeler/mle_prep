## testing out fibonacci number patterns
def fib(n):
    # return the sequence of fibonacci numbers
    if n == 0:
        res = [0]
    elif n == 1:
        res = [0, 1]
    if n > 1:
        res = [0] * (n + 1)
        res[1] = 1
        for ii in range(2, n + 1):
            res[ii] = res[ii - 1] + res[ii - 2]
    return res


def remainder_sequence(fib, divisor, n):
    fib_series = fib(n)
    return fib_series % divisor
