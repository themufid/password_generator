import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(password):
    with open('passwords.txt', 'a') as f:
        f.write(password + '\n')
    print("Password berhasil disimpan.")

if __name__ == "__main__":
    while True:
        try:
            length = int(input("Masukkan panjang kata sandi (minimal 6 karakter): "))
            if length < 6:
                print("Panjang kata sandi harus minimal 6 karakter.")
                continue
            break
        except ValueError:
            print("Masukkan angka yang valid untuk panjang kata sandi.")

    use_uppercase = input("Gunakan huruf besar? (y/n): ").lower() == 'y'
    use_lowercase = input("Gunakan huruf kecil? (y/n): ").lower() == 'y'
    use_digits = input("Gunakan angka? (y/n): ").lower() == 'y'
    use_symbols = input("Gunakan simbol? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
    print("Kata sandi yang dihasilkan:", password)

    save_option = input("Apakah Anda ingin menyimpan kata sandi ini? (y/n): ").lower()
    if save_option == 'y':
        save_password(password)
