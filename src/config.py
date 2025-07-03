from pathlib import Path 
import sys 

    #Primary Working Directory 
CURRENT_DIRECTORY = Path()

if getattr(sys, 'frozen', False): 
    # Running as a bundled executable 
    CURRENT_DIRECTORY = Path(sys.executable).parent 

else: 
    # Running as a script 
    CURRENT_DIRECTORY = Path(__file__).parent 

    #DIRECTORY
# CURRENT_DIRECTORY = Path(__file__).parent 
MAIN_DIRECTORY = CURRENT_DIRECTORY.parent

    # LOGS 
LOGS_FOLDER = str(MAIN_DIRECTORY) + "/logs"

    # Import Folders
IMPORT_FILES = str(MAIN_DIRECTORY) + "/Import Files"
OUTPUT_FILES = str(MAIN_DIRECTORY) + "/Output Files"
TO_BE_PROCESSED = str(IMPORT_FILES) + "/To Be Processed"
NOT_PROCESSED = str(IMPORT_FILES) + "/Not Processed"
PROCESSED = str(IMPORT_FILES) + "/Processed"
PASSWORD_FOLDER = str(IMPORT_FILES) + "/Password File"
PASSWORD_LENGTH = (15, 16, 17, 18, 19, 20)

    # File Types
FILE_TYPES = ['.pdf']

    #GUI APP COLORS
BACKGROUND_COLOR = "#93C83E"
FRAME_BACKGROUND = "#79378B"
TEXT_COLOR = "#FFFBDE"
FONT_TYPE = "Open Sans"
FONT_SIZE_TITLE = 25
FONT_SIZE_HEADING = 18
FONT_SIZE_BODY = 15

file_list = str(FILE_TYPES).replace('[\'','').replace('\']','').replace('\'','')

    # APP INSTRUCTORS 
APP_DIRECTIONS_HEADING = """
READ THE INSTRUCTIONS BELOW ON HOW TO USE THE APP:
"""

    # LANDING PAGE 
x = '*'*90

APP_DIRECTIONS_BODY  = f"""
*{x}

    1 - Save the file(s) you want to password protect on the folder path - "/Import Files/To Be Processed".\n
    2 - Only the following File Types are to be saved : {file_list}. \n
    3 - Once ready, Click 'Next' to proceed.\n

*{x}
"""

    # BEFORE YOU PROCEED
BEFORE_YOU_PROCEED_HEADER = "\nBEFORE YOU PROCEED:\n"

BEFORE_YOU_PROCEED_BODY = f"""
*{x}

    1 - Make sure you do not have any of the files opened - As this will block the process from encrypting the files.

    WHEN YOU ARE READY:

    Click On 'Proceed' to initialise the encryption process.

*{x}
"""



    # PLEASE WAIT
PLEASE_WAIT_HEADER = "\nPROCESSING...\n"

PLEASE_WAIT_BODY = f"""
*{x}

    ....Processing...

*{x}
"""


    # ENCRYPTION DONE
ENCRYPTION_DONE_HEADER = "\n ENCRYPTION COMPLETE.\n"

ENCRYPTION_DONE_BODY = f"""
*{x}

    1 - Please Check Encrypted File(s) in folder - '/Import Files/Processed'. 

    2 - Password File will be found in the folder - '/Import Files/Password File'. 

    3 - All unsupported files are found in the folder - '/Import Files/Not Processed'.
    
    😊😊Have a Nice Day.😊😊 

*{x}
"""
