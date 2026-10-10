# 📁 File Organizer — Python

**A simple Python automation tool that organizes files into categorized folders based on their file extensions.**

Keep your Downloads and other directories clean and organized with this lightweight file organizer.

## ✨ Features

- 🖼️ **Image Organization** — Groups images into a dedicated folder.
- 🎬 **Video Organization** — Separates video files automatically.
- 📄 **Document Organization** — Organizes PDFs, Word files, text files, and more.
- 📦 **Other Files** — Places unsupported or uncategorized file types in an `Others` folder.
- ⚡ **Automated File Management** — Reduces the effort of manually sorting files.
- 🐍 **Lightweight & Simple** — Built with Python's standard library.

## 🛠️ Tech Stack

- **Language:** Python
- **OS:** File and directory operations
- **Shutil:** Moving files between folders

## 📂 Project Structure

```text
File-organizer-Python/
├── file_organizer.py
├── README.md
└── .gitignore
```

*Note: Replace `file_organizer.py` with your actual Python script filename if it differs.*

## ⚙️ How It Works

1. Select the directory you want to organize.
2. Define file extensions and their corresponding categories.
3. Scan the directory for files.
4. Identify each file by its extension.
5. Move files into their appropriate folders.

## 📸 Example

**Before:**

```text
Downloads/
├── photo.jpg
├── video.mp4
├── notes.pdf
├── song.mp3
└── script.py
```

**After:**

```text
Downloads/
├── Images/
│   └── photo.jpg
├── Videos/
│   └── video.mp4
├── Documents/
│   └── notes.pdf
├── Audio/
│   └── song.mp3
└── Others/
    ├── script.py
```

*The resulting folders depend on the file categories configured in your script.*

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Basic knowledge of file paths

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/mohdhuzaifaexe/File-organizer-Python-.git
```

**2. Open the project directory**

```bash
cd File-organizer-Python-
```

**3. Run the script**

```bash
python file_organizer.py
```

Replace the script filename in the command if needed.

## ⚠️ Important Notes

- Test the script on a sample directory before using it on important files.
- Back up important data before organizing a large folder.
- Make sure the script handles duplicate filenames and file-moving errors appropriately.

## 🔮 Future Improvements

- Add support for more file categories.
- Provide a graphical user interface (GUI).
- Add a custom directory selection option.
- Handle duplicate filenames safely.
- Generate an organization summary report.
- Add logging and error handling.

## 👨‍💻 Author

**Mohd Huzaifa**

- GitHub: [@mohdhuzaifaexe](https://github.com/mohdhuzaifaexe)

---

⭐ If you find this project useful, consider giving it a star!

*Built with Python to make everyday file management easier.*
