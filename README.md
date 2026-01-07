# House-Creator: Pixel-House Scene
## Description
Users can choose house colors, door styles, roof shapes, roof materials, and optional scenery elements.  
The program generates a pixel-based image from scratch and saves it as a JPG file.

This project demonstrates low-level image generation using manual pixel placement and basic geometric shapes.

---

## Features
- Interactive GUI using EasyGUI
- Customizable house colors
- Multiple door colors and styles
- Flat or gable roof options with different materials
- Optional tree and sky elements
- Image generation using PPM format
- Automatic conversion to JPG

---

## Demo
![House Creator Demo](demo.gif)

---

## Technical Highlights
- Manual pixel-level rendering (no graphics engines)
- Custom implementations of rectangles, circles, and triangles
- PPM image generation and conversion using Pillow
- Cross-platform file handling for macOS and Windows
- Executable packaging using PyInstaller

---

## How It Works
- The program builds an image as a 2D array of RGB pixel dictionaries
- Shapes such as rectangles, circles, and triangles are drawn manually
- The image is written to a PPM file and then converted to JPG using Pillow
- All graphics are generated programmatically (no external images)

---

## Design Decisions
- PPM format was chosen to demonstrate raw image generation
- Shapes were implemented using pixel math instead of libraries
- Output files are written to user-accessible directories to comply with OS sandboxing rules
- GUI-based interaction was chosen to improve accessibility for non-technical users

---

## Output
Follow the on-screen prompts. The generated image will be saved in the same directory. 

## How to Run

### Requirements
- Python 3.x
- Required libraries:
  - easygui
  - pillow (PIL)

Install dependencies:
```bash
pip install easygui pillow
