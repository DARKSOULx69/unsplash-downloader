# -----------------------------------------------------------------------------
# Copyright (c) 2022, DARKSOUL
# Distributed under the GNU General Public License v3.0
# -----------------------------------------------------------------------------

# import libraries
import os
import webbrowser
from bs4 import BeautifulSoup
from os.path import exists as path_exists
from urllib.request import urlopen, urlretrieve

# check folder already exists or not
if not path_exists("Downloads"):
    os.mkdir("Downloads")

# get url from the user
url= input("Enter URL: ")
print("")

# request page and get page contents
html_page= urlopen(url)
soup= BeautifulSoup(html_page, features= "lxml")

# scrape urls from the website
urls_list= []
for i in soup.find_all("a"):
    img_url= i.get("href")
    if "/download?force=true" in img_url:
        urls_list.append(img_url)

# download images
c= 1
total= len(urls_list)
for i in urls_list:
    i_base= str(i).replace("/download?force=true", "")
    f_name= os.path.basename(i_base)
    download= f"Downloads/{f_name}.png"

    print(f" > Downloading [{c}/{total}]")
    try:
        urlretrieve(i, download)
    except:
        print("Failed to download...!")
    c+= 1

print("Follow & Star my repositoris....!")
webbrowser.open_new_tab("https://github.com/DARKSOULx69")
print("Thank YOU...!")