import sys, re, traceback

try:
    import requests
except:
    print("You need install requests Library")
    sys.exit(1)

try:
    import ui_name
except:
    print("You need ui_name.py file")
    sys.exit(1)

try:
    s = ui_name.simple_record()
    print(s)
except:
    print("Something error")

