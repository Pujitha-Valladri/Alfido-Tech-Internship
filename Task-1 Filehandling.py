# Import required modules
import os
import shutil

try:
    # -----------------------------
    # 1. Create and Write to a File
    # -----------------------------
    file = open("sample.txt", "w")
    file.write("Welcome to Alfido Tech Internship\n")
    file.write("Learning Python File Handling")
    file.close()

    print("File created and data written successfully.")

    # -----------------------------
    # 2. Read File Content
    # -----------------------------
    file = open("sample.txt", "r")
    content = file.read()
    print("\nFile Content:")
    print(content)
    file.close()

    # -----------------------------
    # 3. Rename the File
    # -----------------------------
    os.rename("sample.txt", "internship.txt")
    print("\nFile renamed successfully.")

    # -----------------------------
    # 4. Create Folder and Move File
    # -----------------------------
    if not os.path.exists("Documents"):
        os.mkdir("Documents")

    shutil.move("internship.txt", "Documents/internship.txt")
    print("File moved successfully.")

    # -----------------------------
    # 5. Delete File
    # -----------------------------
    os.remove("Documents/internship.txt")
    print("File deleted successfully.")

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print("Unexpected Error:", e)
