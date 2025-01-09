# File: sha256_decrypt.py
import hashlib

def encrypt_sha256(input_text):
    """Membuat hash SHA256 dari teks input."""
    return hashlib.sha256(input_text.encode()).hexdigest()

def verify_sha256(input_text, hash_to_verify):
    """Memverifikasi apakah teks menghasilkan hash SHA256 yang sesuai."""
    return encrypt_sha256(input_text) == hash_to_verify

def main():
    text = input("Masukkan teks asli: ")
    hash_value = input("Masukkan hash SHA256 untuk diverifikasi: ")

    if verify_sha256(text, hash_value):
        print("Hash cocok! Teks asli sesuai dengan hash.")
    else:
        print("Hash tidak cocok! Teks asli tidak sesuai dengan hash.")

if __name__ == "__main__":
    main()

