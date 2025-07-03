import tkinter as tk
from pathlib import Path

def add_text_label(window = 'root', label_text = 'This is a label'):
    try:
        Label = (f"{window}, text={label_text}")
        return Label
    except Exception as e:
        return f"Error: {e}"
    

    
# text = add_text_label('root', 'welcome to App' ) 
# print(text)