import random
from cryptography.fernet import Fernet

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

def encrypt_script(file_path, key):
    try:
        with open(file_path, "rb") as f:
            file_content = f.read()
        fernet = Fernet(key)
        encrypted_content = fernet.encrypt(file_content)
        encrypted_script = f'''
from cryptography.fernet import Fernet
key = {repr(key)}
encrypted_data = {repr(encrypted_content)}
exec(Fernet(key).decrypt(encrypted_data).decode('utf-8'))
'''
        return encrypted_script
    except Exception as e:
        print(f"Error: {e}")
        return None

def save_encrypted_script(output_path, encrypted_script):
    try:
        with open(output_path, "w") as f:
            f.write(encrypted_script)
        print(f"[+] Enkrypted script saved to: {output_path}")
    except Exception as e:
        print(f"Error :( : {e}")

def main():
    print_banner()
    file_path = input("Python script to enkrypt: ")

    key = Fernet.generate_key()
    encrypted_script = encrypt_script(file_path, key)
    if encrypted_script:
        output_path = file_path + ".krypt.py"
        save_encrypted_script(output_path, encrypted_script)
        print(f"\n[+] Enkrypted the script :D saved to: {output_path}")
    else:
        print("\n[-] Failed to enkrypt :(")

if __name__ == "__main__":
    main()
