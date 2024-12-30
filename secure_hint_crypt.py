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

# Encrypted Hint: 9uuN5GqkxQKxft+kMau+2erK0rFeaoeQwwH2jFRDhwHHooD/PvftHaxumus25e3ZzMzX/1k514PZV/udUAiJAJ72jLAl96o=