"""
Implement pow(x, n).
"""


def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if not n:
        return 1

    if n == 1:
        return x

    if n % 2:
        return x * myPow(x, n - 1)

    if n < 0:
        return myPow(1 / x, -n)

    return myPow(x * x, n / 2)


print(myPow(2, 10))
