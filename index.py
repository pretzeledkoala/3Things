import markdown
from bs4 import BeautifulSoup

# Read the markdown content from the file
with open("main/main.md", "r") as f:  # Update with the correct path to your markdown file
    markdown_content = f.read()

# Convert markdown to HTML
html_content = markdown.markdown(markdown_content)

# Use BeautifulSoup to parse and clean the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Add the basic HTML structure to the content using f-strings
html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README</title>
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

            {soup.prettify()}


</body>
</html>
"""

# Write the resulting HTML to an index.html file
with open("index.html", "w") as f:
    f.write(html)

print("Conversion complete! The HTML file has been saved as index.html.")
