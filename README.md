
![logo](img/png/logo128x128.png)

# MediaGroup Tool

A Python application designed for image editing: changing DPI, resizing resolution, and adding MediaGroup/TUSUR watermarks.

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
     cd /path/to/mediagroup-tool
     ```
  4. Make the binary executable:
     ```bash
     chmod +x mg-tool
     ```
  5. Run the program:
     ```bash
     ./mg-tool
     ```