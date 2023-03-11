import webbrowser
import sys

url = "http://www.google.com/search?q="

# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
#chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# Linux
chrome_path = '/usr/bin/firefox %s'

def create_querry():
    querry = sys.argv[1:]
    return ' '.join(querry)

def create_url():
    final_url= url + create_querry()    
    webbrowser.get(chrome_path).open(final_url)

create_url()    

