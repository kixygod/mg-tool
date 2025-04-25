Илюха напиши тут инструкцию. Как качать, как юзать и т.д., eсли что загружать через Release, они справа. ТОЛЬКО НА НА АНГЛИЙСКОМ. То что ниже это пример от гпт.

# MediaGroup Tool

A Python application for processing images, allowing users to change DPI, resize images, and add MediaGroup and/or TUSUR logos. The program uses a graphical interface (tkinter) for selecting input and output folders and a console interface for selecting processing options.

## Features
- Change DPI of images.
- Resize images with specified DPI.
- Add MediaGroup logo (bottom-left), TUSUR logo (bottom-right), or both.
- Cross-platform: Works on Windows, macOS, and Linux.
- Can be packaged into a single executable file using PyInstaller.

## Prerequisites
- Python 3.6 or higher (tkinter is included in the standard library).
- Two text files with base64-encoded PNG logos: `mediagroup_logo.txt` and `tusur_logo.txt` (must be placed in the same directory as `mg-tool.py`).

## Installation

### 1. Clone or Download the Project
Download the project files, including:
- `mg-tool.py`
- `mediagroup_logo.txt`
- `tusur_logo.txt`
- `requirements.txt`

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

### 4. Prepare Logo Files
Ensure `mediagroup_logo.txt` and `tusur_logo.txt` are in the same directory as `mg-tool.py`. These files should contain base64-encoded PNG images of the MediaGroup and TUSUR logos, respectively.

To generate base64 files from PNG logos:
```python
import base64

# For MediaGroup
with open("path/to/mediagroup_logo.png", "rb") as image_file:
    encoded = base64.b64encode(image_file.read()).decode('utf-8')
    with open("mediagroup_logo.txt", "w", encoding="utf-8") as txt_file:
        txt_file.write(encoded)

# For TUSUR
with open("path/to/tusur_logo.png", "rb") as image_file:
    encoded = base64.b64encode(image_file.read()).decode('utf-8')
    with open("tusur_logo.txt", "w", encoding="utf-8") as txt_file:
        txt_file.write(encoded)
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
You can download prebuilt executables from the [Releases](https://github.com/yourusername/mediagroup-tool/releases) section on the right.

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
2. Build the executable:
   - On Windows:
     ```bash
     pyinstaller --onefile --add-data "mediagroup_logo.txt;." --add-data "tusur_logo.txt;." mg-tool.py
     ```
   - On macOS/Linux:
     ```bash
     pyinstaller --onefile --add-data "mediagroup_logo.txt:." --add-data "tusur_logo.txt:." mg-tool.py
     ```
3. Find the executable in the `dist/` folder (`mg-tool.exe` on Windows or `mg-tool` on macOS/Linux).
4. Distribute the executable along with `mediagroup_logo.txt` and `tusur_logo.txt` (they are embedded in the executable but may be useful for reference).

## Troubleshooting
- **Logo not found**: Ensure `mediagroup_logo.txt` and `tusur_logo.txt` are in the same directory as `mg-tool.py` (or embedded correctly in the executable).
- **GUI not showing**: Verify that Python includes tkinter (run `python -m tkinter` to test). If missing, install it (e.g., `sudo apt-get install python3-tk` on Ubuntu).
- **Images not processing**: Check that input images are in .jpg or .jpeg format and that the output folder is writable.
