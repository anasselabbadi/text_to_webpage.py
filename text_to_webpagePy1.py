import re

# Open the text file
with open('textfile.txt', 'r') as f:
    text = f.read()

# Define a regular expression to match styling commands
style_regex = re.compile(r'#(make this in the (\w+) and (\w+) and color is (\w+))')

# Replace styling commands with HTML tags
text = style_regex.sub(r'<\2 style="color:\4;"><\3>', text)

# Create the HTML and CSS for the web page
html = '<html><head><style>medal {font-weight: bold;}</style></head><body>' + text + '</body></html>'

# Save the HTML to a file
with open('webpage.html', 'w') as f:
    f.write(html)
