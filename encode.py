import base64
import gzip
import argparse

def encode_script(file_path):
    with open(file_path, "rb") as f:
        file_content = f.read()

    compressed_content = gzip.compress(file_content)

    encoded_content = base64.b64encode(compressed_content).decode("utf-8")

    obfuscated_script = f'''
import base64, gzip
exec(gzip.decompress(base64.b64decode("{encoded_content}")))
'''

    return obfuscated_script

def main():
    parser = argparse.ArgumentParser(description="Python Script Encoder")
    parser.add_argument("file", help="Path to the Python file to encode")
    args = parser.parse_args()

    obfuscated_script = encode_script(args.file)
    print("Encoded Python Script:\n")
    print(obfuscated_script)

if __name__ == "__main__":
    main()
