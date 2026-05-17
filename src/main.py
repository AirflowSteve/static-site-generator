from textnode import TextNode, TextType
from htmlnode import *
from markdown_blocks import *
import os
from shutil import copy, rmtree


def copy_static(dir_path):
    directories = os.listdir(dir_path)
    for directory in directories:
        path_ = os.path.join(dir_path, directory)
        dest_path = path_.replace("static", "public")
        print(f" * {path_} -> {dest_path}")
        
        if os.path.isfile(path_):
            copy(path_, dest_path)
            continue
        os.mkdir(dest_path)
        copy_static(path_)
    return None
    

def main():
    public_path = "public"
    print("Deleting public directory...")
    if os.path.exists(public_path):
        rmtree(public_path)
    
    print("Copying static files to public directory...")
    os.mkdir(public_path)
    copy_static("static")


main()

