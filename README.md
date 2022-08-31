PyEmail Backend
===============
[![GitHub Clones](https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count&url=https://gist.githubusercontent.com/MisterSoandSo/1a51ed347f57857e2304f54123de2759/raw/clone.json&logo=github)]()
[![View Count](https://img.shields.io/badge/dynamic/json?color=success&label=Views&query=uniques&url=https://gist.githubusercontent.com/MisterSoandSo/1a51ed347f57857e2304f54123de2759/raw/clone.json&logo=github)]()

A Python based SMTP library for backend and automatation purposes. This projects aims to be a modern, Python3-compatible, well-documented library for
sending emails via remote servers.

## Supported functionality
TBD .... Project is still in early stages of developement. Come back later for ore details

## Supported Python versions
PyEmail is compatible with (at least) the following Python implementations:
* Python 3.9
* Python 3.10

~ Any other versions will be noted on a later date. ~

## Install
All required library should be default on Python 3.10 unless otherwise stated.

## Usage

```python
from PyEmail import PyEmail

#Creates the email class. Initialization needs the email and password
test = PyEmail('a*******@gmail.com','****************')

#Write a simple email. Requires recipient(s), subject and body.
test.writePlainText('a******@outlook.com','Test Script','Hi This is an automated test message')
#or
test.writePlainText(['a******@outlook.com','b******@gmail.com'],'Test Script','Hi This is an automated test message')


#Reads in file and attachs onto email.
test.addAttachments(r"filepath")

#Sends email to recipient(s)
test.sendMail()

```
## Contact
I can be reached by mail as noted on my overview.

## License
[GNU-3](https://choosealicense.com/licenses/gpl-3.0/)
