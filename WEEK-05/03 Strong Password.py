def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    (lower, upper, special, number) = (False, False, False, False)
    for character in password:
        if numbers.find(character) != -1: number = True
        if lower_case.find(character) != -1: lower = True
        if upper_case.find(character) != -1: upper = True
        if special_characters.find(character) != -1: special = True
    
    count = 0
    if number is False: count += 1
    if lower is False: count += 1
    if upper is False: count += 1
    if special is False: count += 1
    
    if len(password) + count < 6:
        return count + (6 - (len(password) + count))
    else:
        return count

# Kunal Wadhwa
# 6621 1445 5286
