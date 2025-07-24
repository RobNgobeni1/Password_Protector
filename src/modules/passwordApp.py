import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import config
from modules.encrypt_file import EncryptFile
import time as t
import threading

    # LANDING PAGE 
x = '*'*90



class PasswordProtectApp():
    def __init__(self):
        pass 
    
    def create_app(self):

        def before_you_proceed():
            try:
                nextButton.config(text="Proceed", command=next)
                app_Instructions_h1.config(text=config.BEFORE_YOU_PROCEED_HEADER)
                app_Instructions.config(text= f"{config.BEFORE_YOU_PROCEED_BODY}")
                app_Instructions_h1.pack()
                app_Instructions.pack()

            except Exception as e:
                frame.config(background=config.FRAME_BACKGROUND)
                nextButton.pack_forget()
                app_Instructions_h1.config(text="THERE WAS AN ERROR:.\n")
                app_Instructions.config(text= f"Error: {e}.")
            
        def next():
            frame.config(background=config.FRAME_BACKGROUND)
            
            
            nextButton.config(text="Proceed", command=proceed)
            app_Instructions_h1.pack_forget()
            app_Instructions.pack_forget()
            Password_check_yes.config(command=createOwnPassword)
            Password_check_no.config(command=createPasswordForMe)

            password_Prompt.pack()
            Password_check_yes.pack(padx=5, pady=5)
            Password_check_no.pack(padx=5, pady=5)

        def createOwnPassword():
            user_password.config(foreground=config.TEXT_COLOR, background=config.FRAME_BACKGROUND, font=(config.FONT_TYPE, config.FONT_SIZE_BODY))
            user_password.pack(padx= 5, pady= 5)
            enter_password.config(font=(config.FONT_TYPE, config.FONT_SIZE_BODY))
            enter_password.pack(padx= 5, pady= 5)

            return user_password

        def createPasswordForMe():
            user_password.pack_forget()
            enter_password.pack_forget() 

        def proceed():
            try:
                get_password = enter_password.get()
                

                please_wait.pack()
                closeButton.config(state=tk.DISABLED)
                thread = threading.Thread(target=run_encrypt, args=(get_password, ))
                thread.start()
                nextButton.pack_forget()
                password_Prompt.pack_forget()
                Password_check_yes.pack_forget()
                Password_check_no.pack_forget()
                user_password.pack_forget()
                enter_password.pack_forget()
                password_button_frame.pack_forget()

            except Exception as e:
                frame.config(background=config.FRAME_BACKGROUND)
                nextButton.pack_forget()
                app_Instructions_h1.config(text="THERE WAS AN ERROR:.\n")
                app_Instructions.config(text= f"Error: {e}.")

        def run_encrypt(password):
            try:

                results = EncryptFile(password).run_encryption()

                t.sleep(1)

                frame.config(background=config.FRAME_BACKGROUND)

                app_Instructions_h1.config(text=config.ENCRYPTION_DONE_HEADER)
                app_Instructions.config(
                    text= f"""
*{x}

    Processed Files : {results[0]}
    Unprocessed Files : {results[1]}

    1 - Please Check Encrypted File(s) in folder - '/Import Files/Processed'. 

    2 - Password File will be found in the folder - '/Import Files/Password File'. 

    3 - All unsupported files are found in the folder - '/Import Files/Not Processed'.
    
    😊😊Have a Nice Day.😊😊 

*{x}
"""
                    )
                app_Instructions_h1.pack()
                app_Instructions.pack()
                please_wait.pack_forget()
                password_Prompt.pack_forget()
                Password_check_yes.pack_forget()
                Password_check_no.pack_forget()
                user_password.pack_forget()
                enter_password.pack_forget()
                password_button_frame.pack_forget()

                closeButton.config(state=tk.NORMAL)

            except Exception as e:
                frame.config(background=config.FRAME_BACKGROUND)
                nextButton.pack_forget()
                app_Instructions_h1.config(text="THERE WAS AN ERROR:.\n")
                app_Instructions.config(text= f"Error: {e}.")

        def quit():
            root.destroy()

        try:
            root = tk.Tk()
            root.title("File Encryptions App")
            root.state('zoomed')
            root.config(background= config.BACKGROUND_COLOR)
            label_text = tk.Label(root, text = 'FILE ENCRYPTION', background=config.BACKGROUND_COLOR, foreground=config.TEXT_COLOR, font = (config.FONT_TYPE, config.FONT_SIZE_TITLE))
            label_text.pack(pady=15)

            frame = tk.Frame(root, bg=config.FRAME_BACKGROUND)
            
            app_Instructions_h1 = tk.Label(frame, text=config.APP_DIRECTIONS_HEADING, background=config.FRAME_BACKGROUND,  fg=config.TEXT_COLOR, font = (config.FONT_TYPE, config.FONT_SIZE_HEADING))
            app_Instructions = tk.Label(frame, text=config.APP_DIRECTIONS_BODY,  background=config.FRAME_BACKGROUND, fg=config.TEXT_COLOR, font = (config.FONT_TYPE, config.FONT_SIZE_BODY))
            
            frame.pack()
            app_Instructions_h1.pack()
            app_Instructions.pack()

            button_frame = tk.Frame(root, bg=config.FRAME_BACKGROUND)

            nextButton = tk.Button(button_frame, text="Next", command=before_you_proceed, width=10, height=1, font=(config.FONT_TYPE, config.FONT_SIZE_BODY))
            closeButton = tk.Button(button_frame, text="Close", command=quit , width=10, height=1, font=(config.FONT_TYPE, config.FONT_SIZE_BODY))


            nextButton.pack(side="left", padx=5, pady=5)
            closeButton.pack(side="left", padx=6, pady=5)
            button_frame.pack(pady=10)

            please_wait = tk.Label(frame,text=config.PLEASE_WAIT_BODY , background=config.FRAME_BACKGROUND, font=(config.FONT_TYPE, config.FONT_SIZE_BODY), fg=config.TEXT_COLOR)

            # Choose Password
            password_button_frame = tk.Frame(frame, bg=config.FRAME_BACKGROUND)
            password_button_frame.pack(pady=10)

            password_Prompt = tk.Label(password_button_frame, text="Do you want to provide your own Password?", foreground=config.TEXT_COLOR, background=config.FRAME_BACKGROUND, font=(config.FONT_TYPE, config.FONT_SIZE_BODY))
            Password_check_yes = tk.Button(password_button_frame, text="Yes", font=(config.FONT_TYPE, config.FONT_SIZE_BODY), width=10, height=1)
            Password_check_no = tk.Button(password_button_frame, text="No", font=(config.FONT_TYPE, config.FONT_SIZE_BODY), width=10, height=1)

            # Enter Password
            user_password = tk.Label(frame, text="Enter your Password")
            enter_password = tk.Entry(frame, show="*")

            
            root.mainloop()

        except Exception as e:
            return f"Error: {e}"
