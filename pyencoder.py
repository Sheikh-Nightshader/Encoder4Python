import base64
import gzip
import argparse
import random

def print_banner():
    banner = """
 ____        _____                     _
|  _ \ _   _| ____|_ __   ___ ___   __| | ___ _ __
| |_) | | | |  _| | '_ \ / __/ _ \ / _` |/ _ \ '__|
|  __/| |_| | |___| | | | (_| (_) | (_| |  __/ |
|_|    \__, |_____|_| |_|\___\___/ \__,_|\___|_|
       |___/
     Python Script Encoder, Sheikh Nightshader
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
        print(f"Error: {e}")
        return None

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="Encode a Python script with Base64 and Gzip.")
    parser.add_argument("file", help="Path to the Python file to encode.")
    args = parser.parse_args()

    obfuscated_script = encode_script(args.file)
    if obfuscated_script:
        print("\n[+] Encoded Script:\n")
        print(obfuscated_script)
    else:
        print("\n[-] Failed to encode the script. Check the file path or file format.")

if __name__ == "__main__":
    main()
