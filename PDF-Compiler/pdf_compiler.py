import os
import img2pdf

files = []
extensions = (".jpg", ".jpeg", ".png")

# os.listdir() returns a list of names of all files and folders inside the current directory
for path in os.listdir():
    if os.path.isfile(path) and path.endswith(extensions):
        files.append(path)

files.sort(key=os.path.getmtime)

with open("document.pdf", "wb") as f:
    pdf = img2pdf.convert(files)
    f.write(pdf)

print("Compiled to document.pdf!")
