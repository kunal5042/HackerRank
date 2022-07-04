
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    am_or_pm = s[-2:]
    if am_or_pm == 'PM':
        hour = int(s[0:2])
        if hour != 12:
            hour += 12
        return str(hour) + s[2:-2]
    else:
        if int(s[0:2]) == 12:
            return '00' + s[2:-2]

    return s[0:-2]

# Kunal Wadhwa
