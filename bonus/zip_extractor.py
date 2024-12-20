import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, "r") as archive:
        archive.extractall(dest_dir)



# if __name__ == "__main__":
#     extract_archive(r"D:\python\module-1\bonus\dest\compressed.zip", 
#                     r"D:\python\module-1\bonus\files")
