
<p align="center"><img src="https://raw.githubusercontent.com/kixygod/mg-tool/refs/heads/main/img/png/logo512x512.png" width="180"></p>
<h1 align="center">MediaGroup Tool</h1>
<p align="center">
  A Python application designed for image editing: changing DPI, resizing resolution, and adding MediaGroup/TUSUR watermarks.
</p>


## Features
- Change image DPI.
- Resize resolution.
- Add MediaGroup, TUSUR, or both watermarks.

## Installation

Visit the [Releases](https://github.com/kixygod/mg-tool/releases) section.  
Download the appropriate version for your OS: `.exe` for Windows, or no extension for macOS and Linux-like systems.

## Usage
1. Move the program to a convenient location.
2. Run the program.
3. Follow these steps:
   - Select the folder containing the images to process (.jpg, .jpeg).
   - Choose the output folder for processed images.
4. Use the console menu to select the desired action:
   - Change DPI
   - Change resolution and DPI
   - Add watermarks (MediaGroup, TUSUR, or both)
   - Exit
  
## Working with Watermarks
- **Adding Watermarks**: Select the watermark option in the console menu to add MediaGroup, TUSUR, or both watermarks to your images.
- **Placing**: The program automatically places the watermark(s) on the images.
- **Supported Formats**: Watermarks are applied to `.jpg` and `.jpeg` images only.
- **Review**: Check the output folder to review the watermarked images after processing.


## Running on macOS and Linux
  1. Download the macOS/Linux binary from the Releases section.
  2. Move the binary to a convenient location.
  3. Open a terminal and navigate to the program’s directory:
     ```bash
     cd /path/to/downloaded/mg-tool
     ```
  4. Make the binary executable:
     ```bash
     chmod +x mg-tool
     ```
  5. Run the program:
     ```bash
     ./mg-tool
     ```

## Building an Executable
To create a single executable file for distribution (no Python installation required):

1. Install PyInstaller (if not already installed):
   ```bash
   pip install pyinstaller
   ```
2. Build the executable:
   - On Windows:
     ```bash
     pyinstaller --onefile --add-data "mediagroup_logo.txt:." --add-data "tusur_logo.txt:." --icon img/logo512x512.icns mg-tool.py
     ```
   - On macOS/Linux:
     ```bash
     pyinstaller --onefile --add-data "mediagroup_logo.txt:." --add-data "tusur_logo.txt:." --icon img/logo512x512.icns mg-tool.py
     ```
3. Find the executable in the `dist/` folder (`mg-tool.exe` on Windows or `mg-tool` on macOS/Linux).
4. Distribute the executable along with `mediagroup_logo.txt` and `tusur_logo.txt` (they are embedded in the executable but may be useful for reference).
