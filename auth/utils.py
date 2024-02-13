from django.core.exceptions import ValidationError

def password_validation(password: str):
    '''Validates password'''
    if 25 >= len(password) >= 8:
        return
    else:
        raise ValidationError(message="password length must be between 8 and 25")

def username_validation(username: str):
    '''Validates username'''
    if len(username) > 25 or len(username) < 3:
        raise ValidationError(message="username length must be between 3 and 25")
    for char in username:
        if not char.isalnum() and char!="_":
            raise ValidationError(message="username can only have alphabet, numbers and underscores")
    
    return None
