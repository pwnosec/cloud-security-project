import pyotp

# Generate a base32 secret for the user
def generate_2fa_secret():
    return pyotp.random_base32()

# Get a TOTP object
def get_totp(secret):
    return pyotp.TOTP(secret)

# Verify the 2FA token
def verify_2fa_token(secret, token):
    totp = get_totp(secret)
    return totp.verify(token)

# Example usage
if __name__ == "__main__":
    secret = generate_2fa_secret()
    print(f"Your 2FA secret is: {secret}")
    token = input("Enter the 2FA token: ")
    if verify_2fa_token(secret, token):
        print("Token is valid!")
    else:
        print("Invalid token.")
