# Attendance-Management-System
🚀 Python desktop app for smart attendance tracking! Load TSV files, automatically detect names, select attendees with clicks, and export to timestamped CSV. Perfect for events, classes, or meetings! 📊✅💾 Built with pandas &amp; Tkinter.

# 🎯 Attendance Management System

A Python-based desktop application for managing and tracking attendance using TSV datasets.

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-green.svg)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI%20Interface-orange.svg)

## 📋 Table of Contents
- [✨ Features](#-features)
- [🚀 Quick Start](#-quick-start)
- [📁 Project Structure](#-project-structure)
- [🎮 How to Use](#-how-to-use)
- [🔧 Installation](#-installation)
- [💾 File Format](#-file-format)
- [📸 Screenshots](#-screenshots)
- [🤝 Contributing](#-contributing)

## ✨ Features

| Feature | Description | Emoji |
|---------|-------------|--------|
| **Smart Data Detection** | Automatically finds name columns in your TSV files | 🔍 |
| **Bulk Operations** | Select/Deselect all with one click | ⚡ |
| **Real-time Counter** | Live count of selected attendees | 📊 |
| **CSV Export** | Save attendance with timestamps | 💾 |
| **User-Friendly GUI** | Clean and intuitive interface | 🎨 |
| **Error Handling** | Comprehensive error messages | 🛡️ |

## 🚀 Quick Start

### 1. 📥 Clone & Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/attendance-system.git
cd attendance-system

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install pandas
```

### 2. 🗂️ Prepare Your Data
Place your TSV file in the project directory. Supported column names for names:
- `name`, `nombre`, `first_name`, `last_name`, `full_name`, `person`

### 3. ▶️ Run the Application
```python
python attendance_system.py
```

## 📁 Project Structure
```
attendance-system/
│
├── 📄 attendance_system.py    # Main application file
├── 📄 requirements.txt        # Dependencies
├── 📄 README.md              # This file
├── 📂 data/                  # Your TSV files go here
│   └── 📄 your_data.tsv
└── 📂 exports/               # Generated attendance files
    └── 📄 asistencias_20231201_143022.csv
```

## 🎮 How to Use

### 🖱️ Interface Guide

| Element | Purpose | Action |
|---------|---------|--------|
| **🔵 Select All** | Mark everyone as present | One-click selection |
| **🔴 Deselect All** | Clear all selections | Reset attendance |
| **💾 Save Attendance** | Export to CSV | Creates timestamped file |
| **👥 People List** | View all names | Click to select/deselect |
| **📈 Counter** | See selected count | Updates in real-time |

### 📝 Step-by-Step Workflow

1. **🚀 Launch the app** - Run `python attendance_system.py`
2. **📂 Load your data** - System automatically detects names
3. **✅ Select attendees** - Click names or use "Select All"
4. **💾 Save results** - Click "Save Attendance" 
5. **📁 Check exports** - Find CSV file in the same directory

## 🔧 Installation

### Prerequisites
- Python 3.6 or higher
- pip package manager

### Dependencies
Create a `requirements.txt` file:
```txt
pandas>=1.3.0
```

Install with:
```bash
pip install -r requirements.txt
```

## 💾 File Format

### 📥 Input (TSV)
Your TSV file should contain at least one column with person names:
```tsv
name        department    email
John Doe    Sales         john@company.com
Jane Smith  Marketing     jane@company.com
```

### 📤 Output (CSV)
Generated attendance files include:
```csv
Nombre,Asistencia,Fecha_Registro,Timestamp
John Doe,Presente,2023-12-01 14:30:22,2023-12-01 14:30:22.123456
```

## 📸 Screenshots

*(Add your screenshots here)*
```
🖼️ [Application Main Window]
- Clean interface with blue theme
- Scrollable list of names
- Colorful action buttons

🖼️ [Success Message]
- Export confirmation
- Attendance summary
- File location details
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| **❌ File not found** | Check file path and extension (.tsv) |
| **❌ No names detected** | Verify your TSV has a name column |
| **❌ Module errors** | Run `pip install pandas` |

## 🤝 Contributing

We welcome contributions! 🎉

1. 🍴 Fork the project
2. 🌿 Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔃 Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 🏆 Acknowledgments

- Built with ❤️ using Python
- Icons by [Shields.io](https://shields.io)
- Made for easy attendance tracking 🎯

---

**⭐ Don't forget to star this repo if you find it useful!**

---

### 🔄 Update Your Code

Here's the updated code with better comments and emojis:

```python
# 🎯 ATTENDANCE MANAGEMENT SYSTEM
# 📅 Version: 1.0
# 👨‍💻 Author: Your Name
# 📧 Contact: your.email@domain.com
# 🐛 Issues: https://github.com/yourusername/attendance-system/issues

import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import os

class SistemaAsistencias:
    def __init__(self, archivo_tsv):
        """
        🚀 INITIALIZE ATTENDANCE SYSTEM
        Args:
            archivo_tsv (str): Path to TSV data file
        """
        self.archivo_tsv = archivo_tsv
        self.df_original = None
        self.df_asistencias = None
        self.personas_seleccionadas = set()
        
        self.cargar_datos()      # 📥 Load data
        self.crear_interfaz()    # 🎨 Create GUI
    
    def cargar_datos(self):
        """📥 LOAD DATA FROM TSV FILE"""
        try:
            self.df_original = pd.read_csv(self.archivo_tsv, sep='\t')
            print("✅ Data loaded successfully!")
            print(f"📊 Available columns: {self.df_original.columns.tolist()}")
        except Exception as e:
            messagebox.showerror("❌ Error", f"Failed to load file: {e}")
            return
    
    # ... (rest of the code with similar emoji comments)

# 🎯 MAIN EXECUTION
if __name__ == "__main__":
    print("🚀 Starting Attendance Management System...")
    print("📋 Make sure your TSV file is in the correct path!")
    main()
```

This GitHub-ready version includes:
- 🎯 Clear emoji-based sections
- 📋 Comprehensive usage instructions
- 🔧 Setup guidelines
- 🐛 Troubleshooting tips
- 🤝 Contribution guidelines
- 📸 Placeholders for screenshots

Would you like me to add any specific sections or modify anything for your GitHub repository?
