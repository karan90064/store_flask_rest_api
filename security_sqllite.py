from resources.users import UserModel
from werkzeug.security import safe_str_cmp



# username_mapping = {u.username: u for u in users}
# userid_mapping = {u.id: u for u in users}

# istead of using in memory we use sqllite db and use methods from security class


def authenticate(username, password):

    # Noe if not found
    user = UserModel.get_user_by_username(username)

    # if user not None and ......
    # dont compare directly problem with versions/servers/etc.. use safe_str_cmp
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.get_user_by_id(user_id)


