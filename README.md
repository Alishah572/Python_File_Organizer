# 📂 File Organizer using Python

A simple and practical Python automation project that organizes files into folders based on their file types. This script helps keep directories clean and structured by automatically sorting files such as images, documents, videos, music, archives, and code files into their respective categories.

Designed with simplicity and usability in mind, this project is beginner-friendly while also including improvements such as duplicate file handling and folder validation.

---

## 🚀 Features

- Automatically organizes files by extension
- Creates folders automatically when needed
- Supports multiple file categories
- Skips existing folders safely
- Prevents overwriting duplicate files
- Validates folder paths before execution
- Clean and beginner-friendly code structure

---

## 📁 Supported Categories

| Category   | File Extensions |
|------------|-----------------|
| Images     | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff` |
| Documents  | `.pdf`, `.doc`, `.docx`, `.txt`, `.ppt`, `.pptx`, `.xls`, `.xlsx` |
| Videos     | `.mp4`, `.mkv`, `.mov`, `.avi`, `.flv` |
| Music      | `.mp3`, `.wav`, `.aac`, `.flac` |
| Archives   | `.zip`, `.rar`, `.tar`, `.gz`, `.7z` |
| Code       | `.py`, `.js`, `.html`, `.css`, `.java`, `.c`, `.cpp`, `.rb`, `.php` |
| Others     | Unsupported or uncategorized files |

---

## 🛠️ Technologies Used

- Python 3
- `os`
- `shutil`

---

## ⚙️ How It Works

The script scans all files inside the selected folder and checks their file extensions. Based on the extension, each file is moved into its matching category folder.

### Example

```text
photo.jpg   → Images/
notes.pdf   → Documents/
song.mp3    → Music/
script.py   → Code/
```

If a folder does not already exist, the script creates it automatically.

---

## 🧠 Additional Improvements

### ✅ Duplicate File Protection

If a file with the same name already exists, the script automatically renames the new file instead of overwriting it.

Example:

```text
photo.jpg
photo(1).jpg
photo(2).jpg
```

### ✅ Folder Validation

The script checks whether the provided path exists and confirms that it is a valid directory before running.

### ✅ Existing Folder Handling

Existing folders are skipped automatically so only files are processed.

---

## ▶️ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/file-organizer.git
cd file-organizer
```

### 2️⃣ Set Your Target Directory

Update the following line inside the script:

```python
target_directory = r"C:\Users\mueed\OneDrive\UpComing"
```

Replace it with the path of the folder you want to organize.

### 3️⃣ Run the Script

```bash
python organizer.py
```

---

## 📷 Example Output

### Before Organization

```text
Downloads/
│
├── photo.jpg
├── notes.pdf
├── movie.mp4
├── song.mp3
├── script.py
```

### After Organization

```text
Downloads/
│
├── Images/
│   └── photo.jpg
│
├── Documents/
│   └── notes.pdf
│
├── Videos/
│   └── movie.mp4
│
├── Music/
│   └── song.mp3
│
├── Code/
│   └── script.py
```

---

## 🔮 Future Improvements

- Graphical User Interface (GUI)
- Drag-and-drop support
- Recursive folder organization
- File size filtering
- Logging system
- Real-time automatic organization

---

## 👨‍💻 Author

**Sayed Muhammad Ali Shah**

- GitHub: https://github.com/Alishah572
- LinkedIn: https://www.linkedin.com/in/sayed-muhammad-ali-shah-b8596828b

---
