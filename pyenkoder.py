import base64
import gzip
import random

def print_banner():
    banner = r"""
 ____        _____       _  __         _
|  _ \ _   _| ____|_ __ | |/ /___   __| | ___ _ __
| |_) | | | |  _| | '_ \| ' // _ \ / _` |/ _ \ '__|
|  __/| |_| | |___| | | | . \ (_) | (_| |  __/ |
|_|    \__, |_____|_| |_|_|\_\___/ \__,_|\___|_|
       |___/
   Python Script Obfuscator, Sheikh Nightshader
    """
    colors = [31, 32, 33, 34, 35, 36]
    for line in banner.split("\n"):
        print(f"\033[1;{random.choice(colors)}m{line}\033[0m")

def encode_script(file_path):
    try:
        with open(file_path, "rb") as f:
            file_content = f.read()
        compressed_content = gzip.compress(file_content)
        encoded_content = base64.b64encode(compressed_content).decode("utf-8")
        obfuscated_script = f'''
import base64, gzip
exec(gzip.decompress(base64.b64decode("{encoded_content}")))
'''
        return obfuscated_script
    except Exception as e:
        print(f"Error :( : {e}")
        return None

def main():
    print_banner()
    file_path = input("Python script to encode: ").strip()

    obfuscated_script = encode_script(file_path)
    if obfuscated_script:
        print("\n[+] Encoded Script :) :\n")
        print(obfuscated_script)
    else:
        print("\n[-] Failed to Encode :( ")

if __name__ == "__main__":
    main()
