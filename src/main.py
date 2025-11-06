#Thank you to geophpherie on github, needed to look at their solution to get this done
import os
import sys
import shutil
from pathlib import Path
from textnode import *
from functions import *

print('hello world')

def delete_files_in_dir(directory_path):
    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)
        if os.path.isfile(filepath):
            os.remove(filepath)
            print(f"Deleted file: {filepath}")

def copy_dir_recursive(source_path, destination_path):
    if not destination_path.exists():
        destination_path.mkdir()
    for file in source_path.iterdir():
        new_file = destination_path / file.name
        if file.is_dir():
            copy_dir_recursive(file, new_file)
        else:
            print(f"Copying {file} to {new_file}")
            shutil.copy(file, new_file)

def extract_title(htmlnode):
    elements = htmlnode.children
    if not elements or len(elements) < 1:
        raise Exception("Improper markdown")
    first_element = elements[0]
    if(first_element.tag != "h1" or not first_element.children or len(first_element.children) == 0):
        raise Exception("Improper markdown")
    if first_element.children[0].value is None:
        raise Exception("Improper markdown")
    return first_element.children[0].value    

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = from_path.read_text()
    template = template_path.read_text()
    html = markdown_to_html_node(markdown)
    title = extract_title(html)
    #print(title)
    #print(html.to_html())
    template = (
        template.replace("{{ Title }}", title)
        .replace("{{ Content }}", html.to_html())
    )

    if not dest_path.parent.exists():
        dest_path.parent.mkdir()
    #print(f"dest_path is: {dest_path}")
    dest_path.write_text(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not dest_dir_path.exists():
        dest_dir_path.mkdir()
    for file in dir_path_content.iterdir():
        new_file = dest_dir_path / file.name
        if file.is_dir():
            generate_pages_recursive(file, template_path, new_file)
        else:
            if file.suffix.lower() == ".md":
                generate_page(file, template_path, new_file.with_suffix(".html"))
            else:
                print(f"Ignoring file: {f}")

def main():
    project_root = Path(__file__).parent.parent
    destination_path = project_root / "public"
    source_path = project_root / "static"
    
    #remove dir before copying
    if destination_path.exists():
        #delete_files_in_dir(destination_path)
        shutil.rmtree(destination_path)

    copy_dir_recursive(source_path, destination_path)
    
    from_path = project_root / "content"
    template_path = project_root / "template.html"

    generate_pages_recursive(from_path, template_path, destination_path)
    


main()
