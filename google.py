import webbrowser
import sys

url = 'http://www.google.com/search?q='

# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
#chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# Linux
chrome_path = '/usr/bin/firefox %s'

def create_querr
print(sys.argv[1:])

webbrowser.get(chrome_path).open(url)