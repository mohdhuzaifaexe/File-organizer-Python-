import os
import shutil

# 👇 Folder path jahan se files organize karni hain
source_folder = '/sdcard/Download'  # Change this path if needed

# 👇 Folder types and their extensions
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx', '.xlsx'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Compressed': ['.zip', '.rar', '.7z'],
    'Scripts': ['.py', '.js', '.html', '.css'],
    'Others': []
}

# ✅ Create folders if not exist
for folder in file_types.keys():
    folder_path = os.path.join(source_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# 🔄 Move files to respective folders
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    
    if os.path.isfile(file_path):
        moved = False
        for folder, extensions in file_types.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                dest_path = os.path.join(source_folder, folder, filename)
                shutil.move(file_path, dest_path)
                print(f"Moved: {filename} ➜ {folder}")
                moved = True
                break
        if not moved:
            dest_path = os.path.join(source_folder, 'Others', filename)
            shutil.move(file_path, dest_path)
            print(f"Moved: {filename} ➜ Others")

print("\n✅ File organization complete!")
