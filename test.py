import sys
import os

# Ensure the root directory is on the path so `src` can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

from src.app.pdf_generator import generate_pdf_from_markdown

def test():
    md = "# Hello\nThis is a test of **markdown** to PDF conversion."
    try:
        pdf_bytes = generate_pdf_from_markdown(md)
        print(f"Success! PDF generated with size: {len(pdf_bytes)} bytes")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test()
