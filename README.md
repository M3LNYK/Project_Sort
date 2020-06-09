# Project_Sort

**Project_Sort** is a pet-project which main purpose was to learn Python, Git and make 
something that can make my life and hopefully someones else better. In addition 
this program can sort your photos in an ordered by date structure. **Project_Sort** 
is supposed to make copies in sorted directories and is not able to delete your 
files, but be aware of available space on your disk!

## Instalation

To use this program should be enough to run main.py, then the grafical user 
interface should open. The idea of gui is based on traffic lights and should 
be pretty obvious. `Red button` responds for choosing folder with files to sort, 
`Yellow button` - responds for choosing destination folder for sorted 
files/directories. `Grey button` means you haven't choosen folder with files to
sort or destiantion folder. `Green button` appears on place of `Grey button` 
after correctly choosing all folders and starts the program execution when 
pressed.

## Usage 

In this project I used libraries for Python, they are shown below:
```python
import exifread
import glob
import os
import cv2
from tkinter import *
from tkinter.filedialog import askdirectory
```

## Contact
If you need you can contact me by *mail*: `vikmel19@gmail.com`
or in *Telegram*: `M3LNYK`

## Contributing
Pull requests are welcome. For major changes, please open an issue first 
to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
