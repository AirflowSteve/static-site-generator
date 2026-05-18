from textnode import TextNode, TextType
from htmlnode import *
from markdown_blocks import *
import os
from shutil import copy, rmtree
from extract_header import extract_title

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
    
def generating_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()
    md_node = markdown_to_html_node(markdown)
    html = md_node.to_html()
    title = extract_title(markdown)
    html_page = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    dirs_to_create = "".join(dest_path.split("/")[:-1])
    if not os.path.exists(dirs_to_create):
        os.makedirs(dirs_to_create)
    file = open(dest_path, "w")
    file.write(html_page)
    file.close()

def main():
    public_path = "public"
    print("Deleting public directory...")
    if os.path.exists(public_path):
        rmtree(public_path)
    
    print("Copying static files to public directory...")
    os.mkdir(public_path)
    copy_static("static")

    generating_page("content/index.md", "template.html", "public/index.html")


main()

