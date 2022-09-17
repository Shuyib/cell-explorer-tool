# cell-explorer-tool
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Shuyib/cell-explorer-tool/master)

An image explorer tool to look for and refine features from microscopy images from cell biology projects, cytopathology projects, histopathology projects and other image related experiments in a reproducible way. You can open an image preferably JPG format, adjust the coordinates of the image, save the image and parameters used to change the image, rename the image file and write description with the app in the *.ipynb. The tool will give you another more refined image resized to 500 by 500 with a TXT file and a JSON file. 

Project structure
---
The project has the following files:
* LICENSE - an MIT License 
* README.md - an explanation of what the project is about, what kind of data is used and the output.
* image-processing-raw-final.ipynb - has documented code to process images at most 4 for some reason.
* requirements.txt - Has python libraries in specific versions e.g ipywidgets == 7.5.1

**Running on Docker guide**  
---

Build docker image
```bash
docker build -t cell-exp:v0 .
```

Run the Docker image
```bash
docker run -it -p 2323:2323 cell-exp:v0
```
