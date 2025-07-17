import os
import shutil
import ctypes

def organize_desktop():
    desktop_path = os.path.expanduser("~/Desktop")
    files_by_extension = {}

    for filename in os.listdir(desktop_path):
        filepath = os.path.join(desktop_path, filename)
        if os.path.isfile(filepath):
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in files_by_extension:
                files_by_extension[file_ext] = []
            files_by_extension[file_ext].append(filepath)

    for file_ext, filepaths in files_by_extension.items():
        folder_name = f"{file_ext[1:].upper()} Files" if file_ext else "No Extension"
        folder_path = os.path.join(desktop_path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        for filepath in filepaths:
            try:
                shutil.move(filepath, folder_path)
            except Exception as e:
                pass  # Ignore errors (e.g., file already moved)

    # Show confirmation popup
    ctypes.windll.user32.MessageBoxW(0, "Your desktop has been organized successfully!", "Success", 0)

if __name__ == "__main__":
    organize_desktop()
