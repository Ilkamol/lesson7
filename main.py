def palindrom_check(string):
    if string == string[::-1]:
        return True
    else:
        return False