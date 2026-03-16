import markdown
from xhtml2pdf import pisa
from io import BytesIO

def generate_pdf_from_markdown(md_text: str) -> bytes:
    # Convert markdown to HTML
    html_content = markdown.markdown(md_text, extensions=['extra', 'codehilite'])
    
    # CSS wrapper for a structured and clean look
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            @page {{
                size: A4;
                margin: 2cm;
            }}
            body {{
                font-family: Helvetica, Arial, sans-serif;
                font-size: 12pt;
                line-height: 1.6;
                color: #333333;
            }}
            h1, h2, h3, h4 {{
                color: #1a1a1a;
                margin-top: 24pt;
                margin-bottom: 12pt;
            }}
            h1 {{
                font-size: 24pt;
                border-bottom: 2pt solid #1a1a1a;
                padding-bottom: 4pt;
            }}
            h2 {{
                font-size: 18pt;
                border-bottom: 1pt solid #cccccc;
                padding-bottom: 4pt;
            }}
            p {{
                margin-bottom: 12pt;
            }}
            ul, ol {{
                margin-bottom: 12pt;
                padding-left: 20pt;
            }}
            li {{
                margin-bottom: 6pt;
            }}
            code {{
                font-family: "Courier New", Courier, monospace;
                background-color: #f4f4f4;
                padding: 2px 4px;
                font-size: 10pt;
                border-radius: 4px;
            }}
            pre {{
                background-color: #f4f4f4;
                padding: 12pt;
                border-radius: 4px;
                font-family: "Courier New", Courier, monospace;
                font-size: 10pt;
                line-height: 1.4;
                white-space: pre-wrap;
            }}
            blockquote {{
                border-left: 4pt solid #cccccc;
                margin-left: 0;
                padding-left: 12pt;
                color: #666666;
                font-style: italic;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Generate PDF
    result_file = BytesIO()
    pisa_status = pisa.CreatePDF(
        BytesIO(styled_html.encode('utf-8')),
        dest=result_file
    )
    
    if pisa_status.err:
        raise Exception("Failed to generate PDF")
        
    return result_file.getvalue()
