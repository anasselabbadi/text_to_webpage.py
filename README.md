# text_to_webpage.py
The script takes a plain text file as input, parses it for specific styling commands, and generates an HTML web page with the text and styling applied. The styling commands are defined in the script using regular expressions, and currently include options for bold and color.
Here is an example of how to use the script:

Create a plain text file, for example, "textfile.txt" that contains the text you want to format and the styling commands.

Run the script:
  $ python text_to_webpage.py

The script will create an HTML file called "webpage.html" that contains the formatted text and styling.

You can open the "webpage.html" file in a web browser to view the formatted text.

example :

textfile.txt content :
  Hello, #make this in the span and bold and color is red
  welcome to #make this in the span and bold
  my website

After running the script the webpage.html content:
  <html><head><style>medal {font-weight: bold;}</style></head><body>
  Hello, <span style="color:red;"><b>welcome to </b></span><span><b>my website</b></span>
  </body></html>
  
  
As you can see it took the text file and applied the commands on it as you have defined in the text file and generated the web page with that styling.
Note that this script is just an example and can be modified to suit your specific requirements and you can add more functionality and styling options to it.
