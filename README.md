# discord-rauff
**R**eport under**a**ge Discord **u**sers **f**rom **f**ile!

## Docs
### How does it work
**discord-rauff** is a program, that takes underage Discord users' User ID, User Tag, incriminating message (i.e. in which they explicitly mention their age) link and other information from TSV file, and then files Discord Trust & Safety reports.
### Requirements
1. [Chromium-based browser](https://en.wikipedia.org/wiki/Chromium_(web_browser)#Active) - manual install
2. [ChromeDriver](https://chromedriver.chromium.org/downloads) - manual install
2. [Selenium 4.3.0](https://www.selenium.dev/selenium/docs/api/py/) - please refer to "How to run/install"
### How to run/install
#### Windows
There is no installation process for Windows. There are two ways to run the script:
1. Run ```pip3 install -r requirements.txt```, then run ```discord-rauff.py``` script [(Python required)](https://www.python.org/downloads/windows/)
2. ~~Run the executable (provided in Releases) in your shell~~ **- BROKEN!**
#### Linux
[Python is required.](https://www.python.org/downloads/source/) You can either simply run the script (1, 2) or install it (3):
1. Run ```pip3 install -r requirements.txt``` or ```make setup```, then run ```discord-rauff.py``` script or ```make run```
2. Run ```make setup_n_run```
2. Run ```doas make install``` or ```sudo make install```, then run ```discord-rauff```. To uninstall, run ```doas make uninstall```
### Synopsis
```discord-rauff [OPTIONS] [ARGUMENTS]```
### Options
```-h --help``` prints help
  
```-i --input --from``` uses the specified file as source instead of default $PWD/data.tsv
  
```-v --verbose``` verbose
### Text file syntax
```csv
Reported_User_ID_0    Reported_User_Tag_0   Reported_Message_Link_0   Additional_Information_0
Reported_User_ID_1    Reported_User_Tag_1   Reported_Message_Link_1   Additional_Information_1
Reported_User_ID_n    Reported_User_Tag_n   Reported_Message_Link_n   Additional_Information_n
```
**For example:**
```csv
312856491839455234  Herr Diesel#1984    https://discord.com/channels/327786974419353600/611628996974739492/1005579461187612722  Not only he's **not** underage, he's also a noob at Python!
```
