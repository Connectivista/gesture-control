with open('index.html', 'r') as f:
    content = f.read()
content = content.replace("http://localhost:8888/index.html", "https://connectivista.github.io/gesture-control/")
content = content.replace("http://localhost:8888/callback", "https://connectivista.github.io/gesture-control/")
with open('index.html', 'w') as f:
    f.write(content)
print("Bitti:", content.count("connectivista.github.io"))
