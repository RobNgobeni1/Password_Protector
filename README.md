# PDF Encryption App

A simple desktop application that password-protects PDF files with an easy-to-use graphical interface.

## Features

• **Batch Processing** - Encrypt multiple PDF files at once
• **Custom Passwords** - Use your own password or generate secure random ones
• **Automatic Organization** - Files are sorted into processed/unprocessed folders
• **Password Logging** - CSV file tracks all passwords for easy reference
• **User-Friendly GUI** - Simple step-by-step interface

## Screenshots

*Add screenshots of your app interface here*

## Installation

### Requirements

```
Python 3.7+
tkinter (usually included with Python)
pikepdf
pandas
pypdf
```

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/pdf-encryption-app.git
cd pdf-encryption-app
```

2. **Install dependencies**
```bash
pip install pikepdf pandas pypdf
```

3. **Run the application**
```bash
python main.py
```

## How to Use

### Step 1: Prepare Your Files
• Place PDF files in the `/Import Files/To Be Processed/` folder
• Only `.pdf` files are supported
• Make sure files are not open in other applications

### Step 2: Launch the App
• Run `python main.py`
• The app creates all necessary folders automatically

### Step 3: Choose Password Option
• **Custom Password**: Enter your own password when prompted
• **Random Password**: Let the app generate a secure password

### Step 4: Process Files
• Click "Proceed" to start encryption
• Wait for processing to complete

### Step 5: Access Results
• **Encrypted files**: Found in `/Import Files/Processed/[timestamp]/`
• **Password log**: Saved in `/Import Files/Password File/[timestamp]/password_log.csv`
• **Unsupported files**: Moved to `/Import Files/Not Processed/[timestamp]/`

## Folder Structure

```
pdf-encryption-app/
├── main.py                    # Main application entry point
├── config.py                  # Configuration settings
├── modules/
│   ├── encrypt_file.py        # Core encryption logic
│   ├── mkdir.py              # Folder creation utility
│   └── passwordApp.py        # GUI application
├── Import Files/
│   ├── To Be Processed/      # Drop your PDF files here
│   ├── Processed/            # Encrypted files output
│   ├── Not Processed/        # Unsupported files
│   └── Password File/        # Password logs (CSV format)
└── Output Files/             # Additional output directory
```

## Technical Details

### Security Features
• **Random Password Generation**: 15-20 character passwords using letters, numbers, and special characters
• **PDF Encryption**: Uses pikepdf library for robust PDF encryption
• **Password Protection**: Both user and owner passwords set to the same value

### File Processing
• **Supported Format**: PDF files only
• **File Extension**: Automatically converts extensions to lowercase
• **Error Handling**: Already encrypted PDFs are moved to "Not Processed"
• **Batch Processing**: Handles multiple files in one operation

### GUI Framework
• Built with tkinter for cross-platform compatibility
• Responsive design with custom color scheme
• Threading prevents GUI freezing during processing

## Example Usage

### Processing 3 PDF files with custom password:

1. **Before**: Place files in `/Import Files/To Be Processed/`
   ```
   document1.pdf
   report.pdf
   presentation.pdf
   ```

2. **Run app**: Choose "Yes" for custom password, enter "MySecurePass123"

3. **After processing**:
   ```
   /Import Files/Processed/20250724_143022/
   ├── document1 - encrypted.pdf
   ├── report - encrypted.pdf
   └── presentation - encrypted.pdf
   
   /Import Files/Password File/20250724_143022/password_log.csv
   File Name,Password
   document1.pdf,MySecurePass123
   report.pdf,MySecurePass123
   presentation.pdf,MySecurePass123
   ```

## Configuration

Edit `config.py` to customize:

• **File types**: Currently supports `.pdf` only
• **Password length**: Random passwords are 15-20 characters
• **GUI colors**: Background, frame, and text colors
• **Font settings**: Font family and sizes

```python
# Example customization
FILE_TYPES = ['.pdf']  # Add more types if needed
PASSWORD_LENGTH = (15, 16, 17, 18, 19, 20)  # Password length range
BACKGROUND_COLOR = "#93C83E"  # Main background color
```

## Troubleshooting

### Common Issues

**"File already encrypted" error**
• PDFs with existing passwords are moved to "Not Processed"
• Remove existing password protection first

**"Permission denied" error**  
• Close PDF files in other applications
• Check file/folder permissions

**"No files found" message**
• Ensure files are in correct folder: `/Import Files/To Be Processed/`
• Verify files have `.pdf` extension

**App won't start**
• Check Python version (3.7+ required)
• Install missing dependencies: `pip install pikepdf pandas pypdf`

### File Locations

All timestamped folders use format: `YYYYMMDD_HHMMSS`

• Processed files: `/Import Files/Processed/[timestamp]/`
• Password logs: `/Import Files/Password File/[timestamp]/password_log.csv`
• Failed files: `/Import Files/Not Processed/[timestamp]/`

## Development

### Project Structure
• **main.py**: Entry point and folder initialization
• **config.py**: All configuration constants
• **encrypt_file.py**: Core encryption logic and file handling
• **passwordApp.py**: GUI interface using tkinter
• **mkdir.py**: Utility for folder creation

### Key Classes
• `EncryptFile`: Handles PDF encryption and file management
• `PasswordProtectApp`: Creates and manages GUI interface
• `MakeFolder`: Utility for creating directory structure

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create Pull Request

## Support

For issues and questions:
• Open an issue on GitHub
• Check the troubleshooting section above
• Review closed issues for similar problems

---

**Note**: This application is designed for legitimate document protection purposes. Users are responsible for compliance with local laws and regulations.

## 📞 Contact

**Robert Ngobeni**
- Email: RNgobeni1@outlook.com
- LinkedIn: [linktr.ee/Just_BobNgobs](https://linktr.ee/Just_BobNgobs)
- GitHub: [@RobNgobeni1](https://github.com/RobNgobeni1)

---

*"Securing documents with enterprise-grade encryption made simple."*
