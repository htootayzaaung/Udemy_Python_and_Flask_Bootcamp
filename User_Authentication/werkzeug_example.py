from werkzeug.security import generate_password_hash, check_password_hash

hashed_password = generate_password_hash(password = "mypassword")

print("mypassword: ", hashed_password)

print(check_password_hash((hashed_password), "wrong"))

print(check_password_hash((hashed_password), "mypassword"))