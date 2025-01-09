# File: sha256_encrypt.py
import hashlib

def encrypt_sha256(input_text):
    """Membuat hash SHA256 dari teks input."""
    sha256_hash = hashlib.sha256(input_text.encode()).hexdigest()
    return sha256_hash

def main():
    text = input("Masukkan teks yang ingin di-hash: ")
    hash_result = encrypt_sha256(text)
    print(f"Hasil hash SHA256: {hash_result}")

if __name__ == "__main__":
    main()

