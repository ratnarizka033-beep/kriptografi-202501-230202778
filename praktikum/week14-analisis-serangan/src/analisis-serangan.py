import hashlib

# Fungsi untuk membuat hash MD5
def hash_md5(password):
    return hashlib.md5(password.encode()).hexdigest()

# Contoh password asli
password_asli = "admin123"

# Hash password
hash_target = hash_md5(password_asli)
print("Hash MD5 Target:", hash_target)

# Daftar kata (dictionary attack)
wordlist = [
    "123456", "password", "admin", "admin123", "qwerty",
    "letmein", "12345", "root"
]

# Proses brute force / dictionary attack
def brute_force_md5(hash_target, wordlist):
    for word in wordlist:
        hashed = hash_md5(word)
        print(f"Mencoba: {word} -> {hashed}")
        if hashed == hash_target:
            print("\n[✓] Password ditemukan!")
            print("Password:", word)
            return
    print("\n[✗] Password tidak ditemukan.")

# Eksekusi program
brute_force_md5(hash_target, wordlist)
