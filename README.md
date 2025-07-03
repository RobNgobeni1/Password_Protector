# Password Protector

A secure Python application for batch PDF encryption with automated file processing and password management.

## 🔒 Overview

Password Protector is a desktop application that automatically encrypts PDF files with randomly generated passwords. Built with security best practices from banking industry experience, it provides a streamlined workflow for protecting sensitive documents.

## ✨ Key Features

• **Batch PDF Encryption** - Process multiple PDF files simultaneously
• **Random Password Generation** - Creates secure passwords using cryptographic methods
• **Automated File Organization** - Sorts files into processed/unprocessed folders
• **Password Logging** - Maintains CSV records of all generated passwords
• **User-Friendly GUI** - Simple Tkinter interface for easy operation
• **Error Handling** - Robust exception management for reliable processing

## 🛠️ Technologies Used

• **Python 3.x** - Core programming language
• **Tkinter** - GUI framework
• **pikepdf** - PDF encryption library
• **pandas** - Data processing and CSV generation
• **pathlib** - Modern file path handling
• **secrets** - Cryptographically secure random generation

## 📁 Project Structure

```
Password_Protector/
├── src/
│   ├── main.py                 # Application entry point
│   ├── config.py               # Configuration settings
│   └── modules/
│       ├── passwordApp.py      # GUI application logic
│       ├── encrypt_file.py     # PDF encryption engine
│       └── mkdir.py            # Directory management
├── import_files/               # Files to be processed
├── processed/                  # Successfully encrypted files
├── not_processed/             # Unsupported or already encrypted files
├── password_logs/             # Password records (CSV files)
└── logs/                      # Application logs
```

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/RobNgobeni1/Password_Protector.git
   cd Password_Protector
   ```

2. **Install required dependencies**
   ```bash
   pip install pikepdf pandas pathlib
   ```

3. **Run the application**
   ```bash
   python src/main.py
   ```

## 📖 How to Use

1. **Place PDF files** in the `import_files` folder
2. **Launch the application** using `python src/main.py`
3. **Follow the GUI prompts** to start encryption
4. **Check results** in organized output folders:
   - `processed/` - Successfully encrypted PDFs
   - `not_processed/` - Files that couldn't be processed
   - `password_logs/` - CSV file with all passwords

## 🔧 Configuration

The application uses a `config.py` file for customization:

• **File Types** - Supported file extensions
• **Password Length** - Range for generated passwords
• **Folder Paths** - Directory structure settings
• **GUI Settings** - Colors, fonts, and layout options

## 🛡️ Security Features

• **Cryptographic Password Generation** - Uses Python's `secrets` module
• **Secure File Handling** - Proper cleanup of temporary files
• **Password Logging** - Encrypted files tracked with corresponding passwords
• **Error Isolation** - Failed encryptions don't affect other files

## 💼 Real-World Application

This project demonstrates enterprise-level security concepts:

• **Banking Industry Standards** - Applies data protection principles from financial services
• **Automated Workflows** - Mirrors ETL processes used in data analysis
• **Audit Trail** - Maintains logs similar to regulatory compliance systems

## 🔍 Technical Highlights

• **Object-Oriented Design** - Clean separation of concerns
• **Exception Handling** - Comprehensive error management
• **Modular Architecture** - Easy to extend and maintain
• **Configuration-Driven** - Flexible settings management

## 🎯 Future Enhancements

• Support for additional file types (Word, Excel)
• Database integration for password storage
• Encryption strength options
• Batch decryption functionality
• Command-line interface

## 👨‍💻 About the Developer

Built by Robert Ngobeni, MIS Analyst with banking and payments industry experience. This project combines practical security knowledge from financial services with modern Python development practices.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for discussion.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

**Robert Ngobeni**
- Email: RNgobeni1@outlook.com
- LinkedIn: [linktr.ee/Just_BobNgobs](https://linktr.ee/Just_BobNgobs)
- GitHub: [@RobNgobeni1](https://github.com/RobNgobeni1)

---

*"Securing documents with enterprise-grade encryption made simple."*
