import tkinter as tk
import config
from modules.encrypt_file import EncryptFile

class PasswordProtectApp():
    def __init__(self):
        pass 
    
    def create_app(self):
        
        def next():
            frame.config(background=config.FRAME_BACKGROUND)
            nextButton.config(text="Proceed", command=proceed)
            app_Instructions_h1.config(text=config.BEFORE_YOU_PROCEED_HEADER)
            app_Instructions.config(text=config.BEFORE_YOU_PROCEED_BODY)

        def quit():
            root.destroy()

        def proceed():

            frame.config(background=config.FRAME_BACKGROUND)
            nextButton.pack_forget()
            app_Instructions_h1.config(text=config.PLEASE_WAIT_HEADER)
            app_Instructions.config(text=config.PLEASE_WAIT_BODY)

            try:
                EncryptFile().run_encryption()
                # results = EncryptFile().run_encryption()

                frame.config(background=config.FRAME_BACKGROUND)
                nextButton.config(text="")
                app_Instructions_h1.config(text=config.ENCRYPTION_DONE_HEADER)
                app_Instructions.config(text= f"{config.ENCRYPTION_DONE_BODY}")
                # app_Instructions.config(text= f"{config.ENCRYPTION_DONE_BODY} \n Encrypted Files - {results[0]} & Not Processed Files - Encrypted Files - {results[1]} \n 😊😊Have a Nice Day.😊😊")

            except Exception as e:
                frame.config(background=config.FRAME_BACKGROUND)
                nextButton.pack_forget()
                app_Instructions_h1.config(text="THERE WAS AN ERROR:.\n")
                app_Instructions.config(text= f"Error: {e}.")



        try:
            root = tk.Tk()
            root.title("Password Protect")
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

            nextButton = tk.Button(button_frame, text="Next", command=next, width=10, height=2)
            closeButton = tk.Button(button_frame, text="Close", command=quit , width=10, height=2)


            nextButton.pack(side="left", padx=5, pady=5)
            closeButton.pack(side="left", padx=6, pady=5)
            button_frame.pack(pady=10)

            
            root.mainloop()

        except Exception as e:
            return f"Error: {e}"
