

Python 3 Script to automatically check Amazon for Xbox Series X stock every ~30 seconds and then order it when it shows up. This script could be used for any other product as well.

### Requirements

Requires chromedriver.exe matching your version of chrome, which can be downloaded here: https://chromedriver.chromium.org/home

Download the chromedriver.exe file and place in this directory

requries `psutil` and `selenium` packages. 

run `py -m pip install -r requirements.txt` to install these packages

### Usage

When you run `python try_buying_xbox.py`, the script will open a Chrome window to amazon.ca. On first run, it will check for a `cookies.pkl` file and then ask you to login if no cookie file is found. Login to Amazon and press enter for the script to proceed. 

This will save the cookies for any future runs. The cookies may expire eventually in which case you'll need to delete the old `cookies.pkl` file and rerun the script and login again. 

Once running, the script will keep checking the page for an Xbox, and when it finds one, it will add it to cart and then place the order. Adding the item to cart might fail, in which case it will go back to the page and try again.

Sometimes, the python script becomes unattached from the Chrome window. When this happens, the old window will be closed and a new window will be started. 

If there are any unexpected failures it will open a debug prompt.

