from pathlib import Path

class MakeFolder():
    def __init__(self, folderPath):
        self.folderPath = Path(folderPath)


    def create_directory(self):
        if self.folderPath.exists():
            return f"Folder Path :{self.folderPath} already exists."
        
        else:
            try:
                self.folderPath.mkdir(parents=True)
                return f"Folder Path : {self.folderPath} created."
            except Exception as e:
                return f"Error: {e}."
            
