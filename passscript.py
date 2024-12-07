import base64
import random
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.backends import default_backend


def print_banner():
    banner = r"""
 ____        _  __                 _
|  _ \ _   _| |/ /_ __ _   _ _ __ | |_
| |_) | | | | ' /| '__| | | | '_ \| __|
|  __/| |_| | . \| |  | |_| | |_) | |_
|_|    \__, |_|\_\_|   \__, | .__/ \__|
       |___/           |___/|_|
Python Script Enkryptor, Sheikh Nightshader
    """
    colors = [31, 32, 33, 34, 35, 36]
    for line in banner.split("\n"):
        print(f"\033[1;{random.choice(colors)}m{line}\033[0m")


def generate_encrypted_script(input_script_path, output_script_path, password):
    print_banner()

    with open(input_script_path, "rb") as file:
        original_script = file.read()

    salt = b"my_salt_value"
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    fernet = Fernet(key)
    encrypted_script = fernet.encrypt(original_script)

    template = f"""
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

encrypted_script = b\"\"\"{encrypted_script.decode()}\"\"\"
salt = b"my_salt_value"
password = input("Enter the password to run the script: ").encode()

try:
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    derived_key = base64.urlsafe_b64encode(kdf.derive(password))
    fernet = Fernet(derived_key)
    decrypted_script = fernet.decrypt(encrypted_script).decode("utf-8")
    exec(decrypted_script)
except Exception:
    print("Invalid password or script tampered!")
"""

    with open(output_script_path, "w") as output_file:
        output_file.write(template)

    print(f"Encrypted script saved to {output_script_path}")


input_script_path = input("Enter the path of the script to encrypt: ")
output_script_path = input("Enter the output path for the encrypted script: ")
password = input("Enter a password for encryption: ")
generate_encrypted_script(input_script_path, output_script_path, password)
