import os, shutil

def organize_files(folder):
    if not os.path.exists(folder):
        print("Folder not found")
        return

    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if os.path.isfile(path):
            ext = os.path.splitext(file)[1][1:] or "others"
            target = os.path.join(folder, ext)
            os.makedirs(target, exist_ok=True)
            shutil.move(path, os.path.join(target, file))

    print("Files organized successfully.")
