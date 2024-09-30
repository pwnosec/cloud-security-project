import bcrypt
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

# Password hashing
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Verify password
def verify_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password)

# Generate token for user
def generate_token(user_id, secret_key, expiration=3600):
    s = Serializer(secret_key, expiration)
    return s.dumps({'user_id': user_id}).decode('utf-8')

# Verify token
def verify_token(token, secret_key):
    s = Serializer(secret_key)
    try:
        data = s.loads(token)
    except:
        return None
    return data['user_id']
