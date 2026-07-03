from pathlib import Path

CATEGORY_MAP = {
    "Images": {".jpg", ".jpeg", ".png", ".gif"},
    "Documents": {".pdf", ".docx", ".txt"},
    "Videos": {".mp4", ".mov", ".avi"},
    "Audio": {".mp3", ".wav", ".flac"},
    "Archives": {".zip", ".rar", ".7z"},
    "Code": {".py", ".js", ".html", ".css"},
    }

def categorize(filename: str) -> str:
    # "vacation.jpg" -> ".jpg"
    # ".JPG" and ".jpg" are treated the same
    extension = Path(filename).suffix.lower()

    for category, extensions in CATEGORY_MAP.items():
        if extension in extensions:
            return category

    # Any other file type, which is not in the MAP
    return "Other"