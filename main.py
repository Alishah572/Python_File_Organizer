import os
import shutil

# Define file categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".rb", ".php"],
    "Others": []
}


def get_unique_filename(destination_folder, filename):
    """
    Generates a unique filename if a duplicate exists.
    Example:
    file.txt -> file(1).txt
    """
    name, extension = os.path.splitext(filename)
    counter = 1

    new_filename = filename
    while os.path.exists(os.path.join(destination_folder, new_filename)):
        new_filename = f"{name}({counter}){extension}"
        counter += 1

    return new_filename


def organize_files(folder_path):
    """Organizes files into categorized folders."""

    # Check if path exists
    if not os.path.exists(folder_path):
        print(f"Error: Path does not exist -> {folder_path}")
        return

    # Check if path is a folder
    if not os.path.isdir(folder_path):
        print(f"Error: Provided path is not a directory -> {folder_path}")
        return

    for file in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file)

        # Skip folders automatically
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, file_extension = os.path.splitext(file)
        file_extension = file_extension.lower()

        # Find matching category
        category = "Others"

        for cat_name, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                category = cat_name
                break

        # Create category folder
        destination_folder = os.path.join(folder_path, category)
        os.makedirs(destination_folder, exist_ok=True)

        # Handle duplicate filenames
        unique_filename = get_unique_filename(destination_folder, file)

        destination_path = os.path.join(destination_folder, unique_filename)

        # Move file
        try:
            shutil.move(file_path, destination_path)
            print(f"Moved: {file} -> {category}/{unique_filename}")

        except Exception as e:
            print(f"Error moving {file}: {e}")


# Target folder - Change this to the folder you want to organize
Path = str(input("Enter the path of the folder to organize: "))
target_directory = rf"{Path}"

organize_files(target_directory)

print(f"\nFile organization complete for: {target_directory}")