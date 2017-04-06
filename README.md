# Cookie Clicker Bot
A multi-platform bot which helps you farm them cookies in the web game [Cookie Clicker.](http://orteil.dashnet.org/cookieclicker/)

## About
A light-weight bot which does not require a lot of understading to use. The bot records the coordinates you give it and then clicks on those coordinates. Brief instructions on using the bot:
> NOTE: A dialog box appears whenever the bot requires values to be entered.
1. Enter the interval between each click performed on the cookie.
2. Enter the amount of clicks you want the bot to perform on the cookie.
3. Enter the amount of buttons you see in the Cookie Clicker Store without scrolling down. -> buttons_no(variable)
4. Wait 3 secs(time given to open up your browser) and place your cursor on the cookie until you hear a "ding" sounf effect.
5. Move your cursor to the last button you see in the store(without scrolling) and wait for the "ding."
6. Move your cursor to the second-last button you see in the store and wait for the "ding."
7. Keep moving your cursor till the first button visible.

The bot will then click on the cookie for the amount of clicks you entered with an interval of the amount you entered. It'll then proceed to click on each of the coordinates you placed your mouse on. The bot will then repeat the process until it is stopped.

> IMPORTANT: To STOP the bot, you will have to force you cursor to move to the upper-left corner of the screen. Otherwise, the bot will keep going.

## Dependencies
This bot uses:
- A GUI automation libary `pyautogui` for the automation which has other [dependencies.](https://github.com/asweigart/pyautogui#dependencies) 
- A game library called `pygame` to load the audio.

To use this bot you will need to install both the libraries(with their respective dependencies.) To install them open your command prompt and run the following commands:

`pip install pyautogui` and `pip install pygame`

> NOTE: While using `pip` all the other dependencies of both the libraries will be downloaded.

## Intended Usage
This bot is not intended for usage over a long period of time as you need to click on upgrades periodically to drastically boost production. This bot does not boost production drastically.

It is however quite useful to get started with a Cookie Clicker session.

## Initial Restrictions
Initially this bot was meant to locate the buttons on screen using screenshots of the buttons input by the user. The feature was removed due to the following reasons:
1. Time taken to locate the images would vary with the speed of the machine.
2. Some buttons would get recognized even when they were not active.
3. Taking a screenshot of all the buttons visible on the screen was tedious and if not done properly would hinder the bots accuracy.
