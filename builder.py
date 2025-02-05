import os
import markdown
from pathlib import Path
import shutil
import re

def fix_html_files(directory):
    """
    Recursively search through directory and fix HTML head/body tag structure
    
    Args:
        directory (str): Root directory to start search
    """
    # Pattern to search for
    old_pattern = r'</head>\s*<body>\s*<p><link href="../../whirlwind\.css" rel="stylesheet"></p>'
    # Replacement text
    new_pattern = '<link href="../../whirlwind.css" rel="stylesheet"> </head> <body>'
    
    # Walk through all files in directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):  # Only process HTML files
                filepath = os.path.join(root, file)
                
                # Read file content
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if pattern exists and needs to be replaced
                if re.search(old_pattern, content):
                    # Make replacement
                    new_content = re.sub(old_pattern, new_pattern, content)
                    
                    # Write back to file
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Fixed file: {filepath}")

def convert_md_to_html(md_path, output_dir):
    """
    Convert a markdown file to HTML and save it in the corresponding directory
    under the output folder.
    """
    # Read markdown content
    with open(md_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    # Convert markdown to HTML without converting emphasis (italic) and without <p> tags
    html_content = markdown.markdown(md_content, extensions=['fenced_code', 'tables', 'def_list'])

    # Create HTML template
    html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{md_path.stem}</title>
    <style>
        body {{
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }}
    </style>

    <!-- Include MathJax with explicit inline math support -->
    <script type="text/x-mathjax-config">
      MathJax.Hub.Config({{
        tex2jax: {{
          inlineMath: [ ['$','$'], ["\\(","\\)"] ],
          processEscapes: true
        }}
      }});
    </script>
    
    <script type="text/javascript"
            src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
    </script>
    
</head>
<body>
    {html_content}
</body>
</html>
"""

    # Get the relative path parts after the current directory
    try:
        relative_parts = md_path.relative_to(Path.cwd()).parts
    except ValueError:
        # If the file is in the current directory, just use the filename
        relative_parts = (md_path.name,)

    # Create output path
    output_path = output_dir.joinpath(*relative_parts[:-1], f"{md_path.stem}.html")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Write HTML file
    with open(output_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_template)
    
    # Clean up the HTML file
    clean_html_file(output_path)

def clean_html_file(html_path):
    """
    Search for specific tags and remove surrounding <p>...</p> tags.
    Also perform additional tag replacements and fix head/body tag structure.
    """
    # Tags to remove surrounding <p>...</p>
    tags_to_remove_p = [
        'conjecture', 'construction', 'corollary', 'definition', 'example',
        'exercise', 'lemma', 'problem', 'proposition', 'theorem', 'remark',
        'src', 'proof', 'solution', 'whirlheader', '/conjecture', '/construction', 
        '/corollary', '/definition', '/example', '/exercise', '/lemma', 
        '/problem', '/proposition', '/theorem', '/remark', '/src', '/proof', 
        '/solution', '/whirlheader'
    ]
    
    with open(html_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Step 1: Clean <p><tag></p> and <p></tag></p> for tags in tags_to_remove_p
    for tag in tags_to_remove_p:
        content = re.sub(rf'<p><{tag}></p>', rf'<{tag}>', content)
        content = re.sub(rf'<p></{tag}></p>', rf'</{tag}>', content)

    # Step 2: Replace all <em> and </em> with underscores (_)
    content = re.sub(r'<em>', '_', content)
    content = re.sub(r'</em>', '_', content)

    # Step 3: Remove <p><whirlheader> and </whirlheader></p> (and keep content inside)
    content = re.sub(r'<p><whirlheader>', '<whirlheader>', content)
    content = re.sub(r'</whirlheader></p>', '</whirlheader>', content)

    # Step 4: Fix head/body tag structure
    old_pattern = r'</head>\s*<body>\s*<p><link href="../../whirlwind\.css" rel="stylesheet"></p>'
    new_pattern = '<link href="../../whirlwind.css" rel="stylesheet"> </head> <body>'
    content = re.sub(old_pattern, new_pattern, content)

    # Write the cleaned content back to the file
    with open(html_path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    # Create site directory path
    site_dir = Path('site')
    
    # Remove existing site directory if it exists
    if site_dir.exists():
        print("Deleting existing 'site' directory...")
        shutil.rmtree(site_dir)
    
    # Create the 'site' directory
    site_dir.mkdir(exist_ok=True)
    print("Created new 'site' directory.")
    
    # Find all markdown files in current directory and subdirectories
    for md_file in Path('.').rglob('*.md'):
        # Skip files in the site directory if they exist
        if 'site' not in md_file.parts:
            print(f"Converting: {md_file}")
            convert_md_to_html(md_file, site_dir)

if __name__ == "__main__":
    main()
