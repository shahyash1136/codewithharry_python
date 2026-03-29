import os


def arrage_files(files, ext):
    file_With_Ext = [file for file in files if file.endswith(ext)]
    print(file_With_Ext)
    # i = 1
    # for file in file_With_Ext:
    #     os.rename(file, f"photo-{i}{ext}")
    #     i += 1
    if not (os.path.exists("images")):
        os.mkdir("images")
    for i, file in enumerate(file_With_Ext):
        os.rename(file, f"images/photo-{i+1}{ext}")


if __name__ == "__main__":
    files = os.listdir()
    arrage_files(files, ".jpg")
