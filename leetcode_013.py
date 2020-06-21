import functools


def roman_to_int(s):
    """

    :param s: string
    :return: int
    """
    store = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    return functools.reduce(lambda sum, i: sum + (-store[s[i]] if store[s[i]] < store[s[i + 1]] else store[s[i]]),
                            reversed(range(len(s) - 1)), store[s[-1]])


if __name__ == '__main__':
    print(list(reversed(range(len([1,2,3,4])))))
    print(roman_to_int("III")) #3
    print(roman_to_int("IV")) #4
    print(roman_to_int("IX")) #9
    print(roman_to_int("LVIII")) #58
    print(roman_to_int("MCMXCIV")) #1994
