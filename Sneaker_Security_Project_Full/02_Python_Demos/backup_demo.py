import os
import shutil

BACKUP_FOLDER = "backup"

def backup_file(file_path):
    os.makedirs(BACKUP_FOLDER, exist_ok=True)
    shutil.copy(file_path, BACKUP_FOLDER)
    print(f"✅ Backed up {file_path} to {BACKUP_FOLDER}/")

def restore_file(file_path):
    backup_path = os.path.join(BACKUP_FOLDER, os.path.basename(file_path))
    if os.path.exists(backup_path):
        shutil.copy(backup_path, file_path)
        print(f"✅ Restored {file_path} from backup.")
    else:
        print("⚠️ No backup found for this file.")

if __name__ == "__main__":
    file_path = input("Enter filename to backup/restore: ")

    choice = input("Do you want to (b)ackup or (r)estore? ").lower()
    if choice == "b":
        backup_file(file_path)
    elif choice == "r":
        restore_file(file_path)
    else:
        print("Invalid choice. Use 'b' or 'r'.")
