from textnode import TextNode, TextType
from htmlnode import *
from markdown_blocks import *
import os
from shutil import copy, rmtree
from extract_header import extract_title
from generate_pages import generating_page, generate_pages_recursive
import sys

def copy_static(dir_path):
    directories = os.listdir(dir_path)
    for directory in directories:
        path_ = os.path.join(dir_path, directory)
        dest_path = path_.replace("static", "docs")
        print(f" * {path_} -> {dest_path}")
        
        if os.path.isfile(path_):
            copy(path_, dest_path)
            continue
        os.mkdir(dest_path)
        copy_static(path_)
    return None


def main():
    if len(sys.argv) < 2:
        basepath = "/"
    else:
        basepath = sys.argv[1]


    public_path = "docs"
    print("Deleting docs directory...")
    if os.path.exists(public_path):
        rmtree(public_path)
    
    print("Copying static files to docs directory...")
    os.mkdir(public_path)
    copy_static("static")

    generate_pages_recursive("content", "template.html", "docs", basepath)


main()

