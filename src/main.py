import config
# from pathlib import Path
from modules.mkdir import MakeFolder
from modules.passwordApp import PasswordProtectApp
from modules.encrypt_file import EncryptFile

if __name__ == "__main__":
    folder_list = [
        config.IMPORT_FILES,
        config.TO_BE_PROCESSED,
        config.PROCESSED,
        config.NOT_PROCESSED,
        config.PASSWORD_FOLDER,
        config.LOGS_FOLDER
        ]

    for folder in folder_list:
        MakeFolder(str(folder)).create_directory()

    PasswordProtectApp().create_app()
    