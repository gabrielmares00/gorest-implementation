import names, random

def user_generator() -> dict:
    """
    Generates dict that contains random user information
    Assumes that id is auto generated when POSTing this to gorest
    """

    user_gender = random.choice(['male', 'female'])
    user_name = names.get_full_name(user_gender)
    user_email = f"{user_name.replace(' ', '_')}@kekmail.com".lower()
    user_status = random.choice(['active', 'inactive'])

    user = {
        "name": user_name,
        "email": user_email,
        "gender": user_gender,
        "status": user_status
    }
    return user
