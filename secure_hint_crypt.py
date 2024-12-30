import hashlib                          
import base64

def custom_encrypt(plaintext, key):
    key = hashlib.sha256(key.encode()).digest()
    ciphertext = bytes([ord(c) ^ key[i % len(key)] for i, c in enumerate(plaintext)])
    return base64.b64encode(ciphertext).decode('utf-8')

if __name__ == "__main__":
    hint = "No Hint for you :)"
    key = "No Key for you :)"  #.... .- .-. -.. -....- . -..- - .-. . -- . .-.. -.-- -....- -. --- -....- .-- .- -.-- -....- - --- -....- ... --- .-.. ...- . -....- .. - -.-.-- -.-.-- -.-.--

    encrypted_hint = custom_encrypt(hint, key)
    print(f"Encrypted Hint: {encrypted_hint}")

# Encrypted Hint: /+6K8zWk5QC8PfjrMuKp2djX2eBMPpLCwRLu2FIMghfX8ZfjcOviTu893u03rK6KiMTDtkEvlonPE7eMXkOZF5A=
