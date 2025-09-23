import hashlib

def get_file_hash(filename):
    h = hashlib.sha256()
    with open(filename, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

if __name__ == "__main__":
    filename = input("Enter filename to check integrity: ")
    original_hash = get_file_hash(filename)
    print(f"Original SHA256 hash: {original_hash}")

    input("Modify the file if you want, then press Enter to recheck...")

    new_hash = get_file_hash(filename)
    print(f"New SHA256 hash: {new_hash}")

    if new_hash == original_hash:
        print("✅ File integrity verified. No changes detected.")
    else:
        print("⚠️ File integrity FAILED. The file has been modified!")
