import hashlib                          
import base64

def custom_encrypt(plaintext, key):
    key = hashlib.sha256(key.encode()).digest()
    ciphertext = bytes([ord(c) ^ key[i % len(key)] for i, c in enumerate(plaintext)])
    return base64.b64encode(ciphertext).decode('utf-8')

if __name__ == "__main__":
    hint = "No Hint for you :)"
    key = "No Key for you :)"  # 01101000 01100001 01110010 01100100 00101101 01100101 01111000 01110100 01110010 01100101 01101101 01100101 01101100 01111001 00101101 01101110 01101111 00101101 01110111 01100001 01111001 00101101 01110100 01101111 00101101 01110011 01101111 01101100 01110110 01100101 00101101 01101001 01110100 00100001 00100001 00100001

    encrypted_hint = custom_encrypt(hint, key)
    print(f"Encrypted Hint: {encrypted_hint}")

# Encrypted Hint: /+6K8zWk5QC8PfjrMuKp2djX2eBMPpLCwRLu2FIMghfX8ZfjcOviTu893u03rK6KiMTDtkEvlonPE7eMXkOZF5A=
