import webbrowser

q_list =["bts","iu","blackpink","winner"]

url = "https://google.com/search?&q="

for q in q_list:
    webbrowser.open(url+q)
