from markdown_blocks import *
from extract_header import extract_title
import os

def generating_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()
    md_node = markdown_to_html_node(markdown)
    html = md_node.to_html()
    title = extract_title(markdown)
    html_page = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    html_page = html_page.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    dest_dir_path = os.path.dirname(dest_path) 
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    file = open(dest_path, "w")
    file.write(html_page)
    file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    directories = os.listdir(dir_path_content)
    for item in directories:
        item_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(item_path):
            dest_path = dest_path.replace(".md", ".html")
            generating_page(item_path, template_path, dest_path, basepath)
            continue
        
        generate_pages_recursive(item_path, template_path, dest_path, basepath)
    return None
