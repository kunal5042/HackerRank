#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#
#
def separateNumbers(s):
    result = 'NO'

    for idx in range(len(s)):
        n_digits_number = int(s[:idx+1])
        current = str(n_digits_number)

        if len(current) != len(s):
            next_digit = n_digits_number + 1

            if len(current) < len(s):
                current += str(next_digit)

            while len(current) < len(s):
                next_digit += 1
                current += str(next_digit)

            if current == s:
                result = 'YES ' + str(n_digits_number)
                break

    print(result)
    return result

# Kunal Wadhwa
