import hashlib

secret_key = "iqwjasdirjuwjq"

# Initialize the denary value
denary_value = 0

while True:
    # Combine the secret key with the denary value
    combined_string = secret_key + str(denary_value)

    # Calculate the MD5 hash
    md5_hash = hashlib.md5(combined_string.encode()).hexdigest()

    # Check if the hash starts with six zeros
    if md5_hash.startswith("000000"):
        break

    # Increment the denary value
    denary_value += 1

print(f"The smallest denary value is: {denary_value}")
print(f"The MD5 hash starting with six zeros is: {md5_hash}")
