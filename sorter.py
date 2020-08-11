import os
import shutil
import datetime


def modification_date(filename):
    t = os.path.getctime(filename)
    return datetime.datetime.fromtimestamp(t)


def is_folder_created(f_folder, pwd_folders):
    for folder in pwd_folders:
        if f_folder == folder:
            return True
    return False


def create_date_folder(f, pwd, date_folders):
    creation_date = modification_date(f)

    folder = f"{creation_date.month}-XX-{creation_date.year}"

    if not is_folder_created(folder, date_folders):
        os.mkdir(pwd + folder)
        return True
    return False


def determine_date_folder(f):
    creation_date = modification_date(f)
    return f"{creation_date.month}-XX-{creation_date.year}"


def create_ext_folder(f, pwd):
    ext_folders = [f for f in os.listdir(
        pwd) if os.path.isdir(os.path.join(pwd, f))]

    folder = os.path.splitext(f)[1].upper()[1:] + " Folder"

    if not is_folder_created(folder, ext_folders):
        os.mkdir(pwd + folder)
        return True
    return False


def determine_ext_folder(f):
    return os.path.splitext(f)[1].upper()[1:] + " Folder"


pwd = r"C:\Users\pschultz\Downloads" + "\\"

pwd_files = [f for f in os.listdir(
    pwd) if os.path.isfile(os.path.join(pwd, f))]

date_folders = [f for f in os.listdir(
    pwd) if os.path.isdir(os.path.join(pwd, f))]

for f in pwd_files:
    file_dir = pwd

    if create_date_folder(pwd + f, pwd, date_folders):
        date_folders = [f for f in os.listdir(
            pwd) if os.path.isdir(os.path.join(pwd, f))]

    file_dir += determine_date_folder(pwd + f) + "\\"

    create_ext_folder(pwd + f, file_dir)

    file_dir += determine_ext_folder(pwd + f) + "\\"

    shutil.move(pwd + f, file_dir + f)
