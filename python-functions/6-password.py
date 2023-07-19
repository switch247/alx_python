def validate_password(password):
    if len(password) < 8:
        return False
    has_up = False
    has_low = False
    has_dig = False
    for char in password:
        if char.isupper():
            has_up = True
        elif char.islower():
            has_low = True
        elif char.isdigit():
            has_dig = True
        else:
            pass
    if not (has_up and has_low and has_dig):
        return False
    if ' ' in password:
        return False
    return True
