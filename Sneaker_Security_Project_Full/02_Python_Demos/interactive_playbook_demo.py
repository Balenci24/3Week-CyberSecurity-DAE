""" 
Interactive Mini Security Policy Demo
- Password Strength Checker (Confidentiality)
- Playbook Menu System (CIA Triad Showcase)
"""

import re

def check_password_strength(password):
    strength = 0
    remarks = []
    
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters.")
    
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add at least one uppercase letter.")
    
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Add at least one lowercase letter.")
    
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks.append("Add at least one number.")
    
    if re.search(r"[@$!%*?&]", password):
        strength += 1
    else:
        remarks.append("Add at least one special character (@$!%*?&).")
    
    levels = {
        0: "Very Weak",
        1: "Weak",
        2: "Moderate",
        3: "Strong",
        4: "Very Strong",
        5: "Excellent"
    }
    
    print(f"Password Strength: {levels[strength]}")
    if remarks:
        print("Suggestions:")
        for remark in remarks:
            print("-", remark)


def playbook_menu():
    while True:
        print("\n--- Mini Security Policy Playbook ---")
        print("1. Password Policy (Confidentiality)")
        print("2. Incident Response (Integrity)")
        print("3. Backup Plan (Availability)")
        print("4. Password Strength Checker")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            print("\nPassword Policy:")
            print("- Minimum 8 characters, mix of uppercase, lowercase, numbers, special characters.")
            print("- Do not reuse passwords across accounts.")
            print("- Change passwords every 90 days.")
        
        elif choice == "2":
            print("\nIncident Response Steps:")
            print("1. Detect suspicious activity in logs.")
            print("2. Contain the incident to prevent spread.")
            print("3. Eradicate the root cause (malware, compromised account).")
            print("4. Recover systems from clean backups.")
            print("5. Document the incident and lessons learned.")
        
        elif choice == "3":
            print("\nBackup Plan:")
            print("- Daily automated backups of customer and transaction data.")
            print("- Store backups in a secure offsite location.")
            print("- Test restoration process every month.")
        
        elif choice == "4":
            pwd = input("Enter a password to check: ")
            check_password_strength(pwd)
        
        elif choice == "5":
            print("Exiting Playbook Demo. Stay Secure!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    playbook_menu()
