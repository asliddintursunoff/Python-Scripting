import sys
from PIL import Image
import os

from PIL.ImageOps import expand

try:     
    file_path = sys.argv

    os.makedirs(f"{file_path[2]}" , exist_ok = True)

    if len(os.listdir(f"./{file_path[1]}"))!=0:
        for i in os.listdir(f'./{file_path[1]}'):
            print(i)
            img = Image.open(f"./{file_path[1]}/{i}")

            img.save(f"{file_path[2]}/{i[:-4]}.png" ,'png' )
    else:
        print("Directory is empty!!!\nPlease place some images first!!!")
except IndexError:
    print("\nPlease enter directory path!!! \n")
except FileNotFoundError:
    print("\nFile not found!!!\nPlease enter true directory of images!!\n")


