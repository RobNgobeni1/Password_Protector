import config
from pathlib import Path
import shutil, random, string, pandas as pd 
import datetime as dt 
import pikepdf, os, secrets, pypdf

class EncryptFile():
    def __init__(self, get_password):
        self.get_password = get_password
        self.folder_path = Path(config.TO_BE_PROCESSED)
        self.Processed_folder = str(config.PROCESSED) + '/' + dt.datetime.now().strftime("%Y%m%d_%H%M%S") + '/' 
        self.Not_processed_folder = str(config.NOT_PROCESSED) + '/' + dt.datetime.now().strftime("%Y%m%d_%H%M%S") + '/' 
        self.Password_folder = str(config.PASSWORD_FOLDER) + '/' + dt.datetime.now().strftime("%Y%m%d_%H%M%S")

    def run_encryption(self):
        try:
            initial_files = self._get_file_list()
            final_list =  self._check_file_type(initial_files)

            return final_list
        
        except Exception as e:
            return f"Error: {e}"
        
    def _rename_file_Ext_to_lowerCase(self, files):
        try:
            files_rename = list(files)
            new_list = list()

            for file in files_rename:
                old = str(file)
                new = str(file).replace(Path(file).suffix, str(Path(file).suffix).lower())

                os.rename(old, new)
                new_list.append(new)

            return new_list

        except Exception as e:
            return f"Error: {e}"    
        
    def _get_file_list(self):
        try:
            get_list = list(self.folder_path.iterdir())

            return self._rename_file_Ext_to_lowerCase(get_list)
             
        except Exception as e:
            return f"Error: {e}"
        
    def _check_file_type(self, file_list):
        try:
            
            list_of_files = list(file_list)
            not_supported_files = list()
            supported_files = list()
                
                # Check for file ext not supported and if not encrypted
            for file in list_of_files:
                try:
                    if Path(str(file).lower()).suffix not in config.FILE_TYPES:
                        not_supported_files.append(file)
                    else:
                        with pikepdf.open(file) as pdf:
                            if file not in supported_files: supported_files.append(file) # Add the file if not already there

                except pikepdf.PasswordError:
                        if file not in not_supported_files: not_supported_files.append(file) # Add the file if not already there

                except Exception as e:
                    print(f"Error: {e}")

                
            self._remove_not_supported_files(not_supported_files)
            self._encrypt_files(supported_files)

            files = list()
            files.append(len(supported_files))
            files.append(len(not_supported_files))

            return files

        except Exception as e:
            return f"Error: {e}"
        
    def _remove_not_supported_files(self, check_file_list):
        try:
            list_to_be_moved = list(check_file_list)
            for file in list_to_be_moved:

                current_folder = str(file)

                if not Path(self.Not_processed_folder).exists():
                    Path(self.Not_processed_folder).mkdir(parents=True)
                
                new_folder = str(self.Not_processed_folder) +  '/' + str(Path(file).name)

                shutil.move(current_folder, new_folder) 
        
        except Exception as e:
            return f"Error: {e}"
        

    def _encrypt_files(self, encrypt_file_list):
        password_log = list()
        encrypt = list(encrypt_file_list)

        for file in encrypt:

            check_password = self.get_password.lstrip().rstrip()
            random_password = ''
            
            if check_password == "":
                random_password = self._generate_random_password()
                password_log.append((Path(file).name, random_password))

            else:
                random_password = check_password
                password_log.append((Path(file).name, random_password))

                #Encrypt Files
            # Add other Files Types
                # 1. Open the existing PDF
            try:    
                input_pdf = str(file)
                output_file = input_pdf.replace(".pdf", " - encrypted.pdf")

                with pikepdf.open(input_pdf) as pdf:
                    pdf.save(output_file, encryption= pikepdf.Encryption(user=random_password, owner=random_password))
                
                self._move_encrypted_files(output_file)
                self._delete_old_files(input_pdf)
            
            except Exception as e:
                return f"Error: {e}."
                
        try:
            if len(password_log) != 0:
                if not Path(self.Password_folder).exists():
                    Path(self.Password_folder).mkdir(parents=True)
                
                password_df = pd.DataFrame(password_log, columns=['File Name', 'Password'])
                csv_filename = f"{self.Password_folder}/password_log.csv"
                password_df.to_csv(csv_filename, index=False)

                return "Password File saved."

        except Exception as e:
            return f"Error: {e}"
        
        
    def _generate_random_password(self):
        try:
            
                # Get Random Length for Password
            password_length = random.choice(config.PASSWORD_LENGTH)

                # Create a random sets of strings 
            random_string = string.ascii_letters
            random_numbers = random.randint(100,999)
            random_special_char = "!@#%$^&*()_[]"
            combined_string = random_string + str(random_numbers) + str(random_special_char)

                # Generate Password
            random_password = ''.join(secrets.choice(combined_string) for _ in range(password_length))

            return random_password
        except Exception as e:
            return f"Error: {e}."
        
    def _move_encrypted_files(self, file_path):
        try:
            filePath = Path(file_path)
            current_folder = str(filePath)
            
            if not Path(self.Processed_folder).exists():
                Path(self.Processed_folder).mkdir(parents=True)

            new_folder_done = str(self.Processed_folder) +  '/' + str(Path(filePath).name)

            shutil.move(current_folder, new_folder_done)
        
        except Exception as e:
            return f"Error: {e}"
        
    def _delete_old_files(self, file_path):
        try:
            filePath = Path(file_path)
            current_folder = str(filePath)
            Path(current_folder).unlink()
            
            return f"File {current_folder}, Deleted. "
        
        except Exception as e:
            return f"Error: {e}"
