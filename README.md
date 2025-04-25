Илюха напиши тут инструкцию. Как качать, как юзать и т.д., eсли что загружать через Release, они справа. ТОЛЬКО НА НА АНГЛИЙСКОМ. То что ниже это пример от гпт.

![logo](img/png/logo128x128.png)

# MediaGroup Tool

A Python application for processing images, allowing users to change DPI, resize images, and add MediaGroup and/or TUSUR logos. The program uses a graphical interface (tkinter) for selecting input and output folders and a console interface for selecting processing options.

## Features
- Change DPI of images.
- Resize images with specified DPI.
- Add MediaGroup logo (bottom-left), TUSUR logo (bottom-right), or both.
- Cross-platform: Works on Windows, macOS, and Linux.
- Can be packaged into a single executable file using PyInstaller with a custom icon.

## Prerequisites
- Python 3.6 or higher (tkinter is included in the standard library).
- Two text files with base64-encoded PNG logos: `mediagroup_logo.txt` and `tusur_logo.txt` (included in the project root).

## Installation

### 1. Clone or Download the Project
Clone the repository or download the project files:
```bash
git clone https://github.com/yourusername/mediagroup-tool.git
cd mediagroup-tool
```
The project includes:
- `mg-tool.py` (main script)
- `mediagroup_logo.txt` (MediaGroup logo in base64)
- `tusur_logo.txt` (TUSUR logo in base64)
- `requirements.txt` (dependencies)
- `img/` (folder with icons and PNGs)
  - `logo512x512.ico` (icon for Windows)
  - `logo512x512.icns` (icon for macOS)
  - `png/` (various PNG sizes of the logo)

### 2. Create a Virtual Environment
It's recommended to use a virtual environment to isolate dependencies.

On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install the required packages using `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Running the Program
1. Activate the virtual environment (if not already activated).
2. Run the program:
   ```bash
   python mg-tool.py
   ```
3. Follow the GUI prompts:
   - Select the input folder containing images (.jpg, .jpeg).
   - Select the output folder for processed images.
4. Use the console menu to choose an action:
   - Change DPI
   - Change resolution and DPI
   - Add logos (MediaGroup, TUSUR, or both)
   - Exit

## Using the Prebuilt Executable
You can download prebuilt executables from the [Releases](https://github.com/yourusername/mediagroup-tool/releases) section on the right. Each executable comes with a custom icon for easy recognition.

- **Windows (`mg-tool.exe`)**: Download and double-click to run.
- **Linux (`mg-tool`)**: Download, make it executable, and run:
  ```bash
  chmod +x mg-tool
  ./mg-tool
  ```
- **macOS (`mg-tool-macos`)**: Download, make it executable, and run:
  ```bash
  chmod +x mg-tool-macos
  ./mg-tool-macos
  ```

After launching:
1. Select the input folder with your images (.jpg, .jpeg) using the graphical dialog.
2. Select the output folder for processed images.
3. Use the console menu to choose an action (change DPI, resize, add logos, or exit).

## Building an Executable
To create a single executable file for distribution (no Python installation required):

1. Install PyInstaller (if not already installed):
   ```bash
   pip install pyinstaller
   ```
2. Build the executable with a custom icon:
   - On Windows:
     ```bash
     pyinstaller --onefile --add-data "mediagroup_logo.txt;." --add-data "tusur_logo.txt;." --icon img/logo512x512.ico mg-tool.py
     ```
   - On macOS:
     ```bash
     pyinstaller --onefile --add-data "mediagroup_logo.txt:." --add-data "tusur_logo.txt:." --icon img/logo512x512.icns mg-tool.py
     ```
   - On Linux:
     ```bash
     pyinstaller --onefile --add-data "mediagroup_logo.txt:." --add-data "tusur_logo.txt:." mg-tool.py
     ```
3. Find the executable in the `dist/` folder (`mg-tool.exe` on Windows, `mg-tool` on macOS/Linux).

## Troubleshooting
- **Logo not found**: Ensure `mediagroup_logo.txt` and `tusur_logo.txt` are in the project root (or embedded correctly in the executable).
- **GUI not showing**: Verify that Python includes tkinter (run `python -m tkinter` to test). If missing, install it (e.g., `sudo apt-get install python3-tk` on Ubuntu).
- **Images not processing**: Check that input images are in .jpg or .jpeg format and that the output folder is writable.
