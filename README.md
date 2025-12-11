# Personal Productivity Suite (Python CLI)

A modular, command-line based productivity toolkit built entirely with Python.  
This application includes:

- Calculator Tool  
- Notes Manager  
- Timer & Stopwatch  
- File Organizer  
- Unit Converter  
- Backup & Restore System  

The project is structured in a scalable, maintainable way using modules, tests, and documentation folders.

---

## Features

### 1. Calculator
Basic arithmetic: add, subtract, multiply, divide.

### 2. Notes Manager
- Add, view, edit, delete notes
- Search notes by keyword
- Automatic timestamping
- JSON-based storage
- Automatic backups created in `/data/backups`

### 3. Timer & Stopwatch
- Countdown timer
- Optional stopwatch

### 4. File Organizer
Automatically groups files by extension.

### 5. Unit Converter
Includes:
- Length (km ⇆ miles, cm ⇆ inches)
- Weight (kg ⇆ pounds)
- Temperature (C ⇆ F ⇆ K)

---

## Project Structure

```
productivity_suite/
│
├── main.py               # Entry point
├── requirements.txt      # Dependencies
├── modules/              # All tool modules
├── data/                 # Notes data + backups
├── docs/                 # Documentation
├── tests/                # Unit tests
└── examples/             # Usage examples
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/productivity_suite.git
cd productivity_suite
```

### 2. Create a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python3 main.py
```

You will see:

```
==========================================
     PERSONAL PRODUCTIVITY SUITE
==========================================
1. Calculator Tool
2. Notes Manager
3. Timer & Stopwatch
4. File Organizer
5. Unit Converter
6. Backup & Restore
7. Exit
```

---

## Running Tests

```bash
pytest
```

---

## Extensibility

This project is intentionally modular. You can easily add:

- A GUI (Tkinter/PyQt)  
- A Web Dashboard (Flask/Django)  
- Cloud sync for notes  
- Encryption for private notes  

---

## License

MIT License
