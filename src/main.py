import os

from copystatic import copy_static_to_public
from generate_page import generate_page

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(PROJECT_ROOT, "static")
PUBLIC_DIR = os.path.join(PROJECT_ROOT, "public")
CONTENT_DIR = os.path.join(PROJECT_ROOT, "content")
TEMPLATE_PATH = os.path.join(PROJECT_ROOT, "template.html")


def main():
    copy_static_to_public(STATIC_DIR, PUBLIC_DIR)
    generate_page(
        os.path.join(CONTENT_DIR, "index.md"),
        TEMPLATE_PATH,
        os.path.join(PUBLIC_DIR, "index.html"),
    )


main()
