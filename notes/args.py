def full_name(**names):
    if 'middle' in names.keys():
        return f"{names['first']}{names[middle]}{names['last']} is {age}"
    else:
        return f"{names}"
