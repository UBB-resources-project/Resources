import sys

def decode_filenames(encoded_str):
    try:
        # Decode from latin1 to utf-8
        decoded_str = encoded_str.encode('latin1').decode('utf-8')
        return decoded_str
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    encoded_str = sys.argv[1]
    print(decode_filenames(encoded_str))
