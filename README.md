# bicocca-lesson-booker
Automatic bot for booking lessons in unimib

## Description
This is a proof of concept for using a scraper (selenium) for creating an automatic booking bot for a unimib account,
The bot is still very WIP, so it doesen't work yet.

## Requirements
In order to use this program you will need the following python dependencies:
- `python-dotenv`
- `selenium`

In addiction to the python dependencies, you must have a valid selenium driver, for help regarding installing a
driver visit [the selenium manual](https://selenium-python.readthedocs.io/installation.html#drivers)

## How to use
For using this program you need to create a file named `.env` inside the project working directory with the following content:
```
username = "university-email-here"
password = "university-password-here"
```
change university-email-here with your university email address, and university-password-here with your uni account password
