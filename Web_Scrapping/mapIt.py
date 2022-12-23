import webbrowser
import sys ,pyperclip
#A programme to get the address on Google Maps by just launching the programme from command line with the address as argument
address = "delhi"
if len(sys.argv) > 1:

    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/" + address)    
