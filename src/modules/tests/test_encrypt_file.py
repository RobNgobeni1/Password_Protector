import config
from pathlib import Path
import shutil, random, string, pandas as pd 
import datetime as dt 
import pikepdf, os 

class EncryptFile():
    def __init__(self):
        self.folder_path = Path(config.TO_BE_PROCESSED)

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

            for file in list_of_files:
                if Path(str(file).lower()).suffix not in config.FILE_TYPES:
                    not_supported_files.append(file)
                else:
                    supported_files.append(file)

            self._remove_not_supported_files(not_supported_files)
            self._encrypt_files(supported_files)

            return "Encryption Done."

        except Exception as e:
            return f"Error: {e}"
        
    def _remove_not_supported_files(self, check_file_list):
        try:
            list_to_be_moved = list(check_file_list)
            for file in list_to_be_moved:

                current_folder = str(file)
                new_folder = str(file).replace(('To Be Processed'),str('Not Processed'))

                shutil.move(current_folder, new_folder) 
        
        except Exception as e:
            return f"Error: {e}"
        

    def _encrypt_files(self, encrypt_file_list):
        password_log = list()
        encrypt = list(encrypt_file_list)

        for file in encrypt:
            random_password = self._generate_random_password()
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
                
            
            # Create Password File
        password_sub_folder = f"{str(config.PASSWORD_FOLDER)}/{dt.datetime.now().strftime("%Y%m%d_%H%M%S")}"

        try:
                # Create sub folder
            Path(password_sub_folder).mkdir(parents=True)
            
                # Move file into Subfolder
            password_df = pd.DataFrame(password_log, columns=['File Name', 'Password'])
            csv_filename = f"{password_sub_folder}/password_log.csv"
            password_df.to_csv(csv_filename, index=False)

            return "Password File saved."

        except Exception as e:
            return f"Error: {e}"
        
        
    def _generate_random_password(self):
        try:
            random_string = string.ascii_letters
            random_numbers = random.randint(100,999)
            random_special_char = "!@#%$^&*()_[]"
            combined_string = random_string + str(random_numbers) + str(random_special_char)
            random_password = str(random.choices(combined_string, k=15)).replace("'","").replace(", ", "").replace("[","").replace("]","")
            return random_password
        except Exception as e:
            return f"Error: {e}."
        
    def _move_encrypted_files(self, file_path):
        try:
            filePath = Path(file_path)

            current_folder = str(filePath)
            new_folder = str(filePath).replace(str('To Be Processed'),str('Processed'))

            shutil.move(current_folder, new_folder) 
        
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

