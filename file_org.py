import os
import shutil

file_categories = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "documents": [".pdf", ".docx", ".doc"],
    "texts": [".txt", ".md", ".rtf"],
    "data": [".xls", ".xlsx", ".csv"],
    "videos": [".mp4", ".mov", ".avi", ".mkv"],
    "audios": [".mp3", ".wav", ".aac", ".flac"],
    "archives": [".zip", ".rar",  ".tar", ".gz"],
    "software_tools": [".exe"]
}

def organize_files(directory):
    """Organizes files in the given directory based on their extensions."""
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory")
        return
    for category in file_categories:
        folder_path = os.path.join(directory, category)
        os.makedirs(folder_path, exist_ok=True)
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isdir(file_path):
            continue  # Skip directories

        file_moved = False
        for category, extensions in file_categories.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(directory, category, filename))
                file_moved = True
                break
        if not file_moved:
            shutil.move(file_path, os.path.join(directory, "software_tools", filename))

directory_to_organize = input("Enter the directory path to organize: ")

organize_files(directory_to_organize)