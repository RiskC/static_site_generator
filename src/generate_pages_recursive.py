import os

from pathlib import Path
from generate_page import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    source_dir = os.path.abspath(dir_path_content)
    template_path_abs = os.path.abspath(template_path)
    output_dir = os.path.abspath(dest_dir_path)


    content_entries = os.listdir(source_dir)

    #crawl entries
    for entry in content_entries:
        #check if entry is a file
        source_entry_path = os.path.join(source_dir, entry)
        print(source_entry_path)

        if os.path.isfile(source_entry_path):
            #if entry ends with .md
            if source_entry_path.endswith(".md"):
                output_file_path = os.path.join(output_dir, entry)
                output_html_suffix = Path(output_file_path).with_suffix('.html')
                generate_page(source_entry_path, template_path_abs, output_html_suffix)
        else:
            next_dest_dir = os.path.join(output_dir, entry)
            generate_pages_recursive(source_entry_path,template_path_abs, next_dest_dir)





# os.listdir -> lists the files inside the given directory
# os.path.join -> concatenate path segements
# os.path.isfile -> returns true if the given path is a ifle
# pathlib.Path -> path class
