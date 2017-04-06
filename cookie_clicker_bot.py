import pyautogui as p
from pygame import mixer
import time

# Drag the mouse to the top left corner of the screen to stop the script.
p.FAILSAFE = True

# Loading the sound.
mixer.init()
ding = mixer.Sound('resources/sounds/ding.wav')

# Accepting the click rate and the interval between each click.
try:
    INTERVAL = float(
        p.prompt(
            text='Enter the interval between each click(each click performed by the mouse on the cookie):\n\nNOTE: An interval lower than 0.1s is not acceptable and is replaced by 0.1s',
            title='Enter the Interval',
            default='0.1'
        )
    )

    CLICKS = int(
        p.prompt(
            text='Enter the amount of clicks you want the mouse the perform: RECOMMENDED: 600(for decent computers)',
            title='Enter the amount of Clicks',
            default='600'
        )
    )

    buttons_no = int(
        p.prompt(
            text='Enter the number of buttons/buildings you want the bot to click on the screen: \n\nNOTE: Take a note of the amount you entered as you will have to guide the bot to click on those many buttons/buildings.',
            title='Number Of Buttons to click',
            default='7'
        )
    )
except TypeError:
    p.alert(text='You did not enter a valid value', title='Error!')
    exit()
except Exception as e:
    p.alert(text='Error: ' + e, title='Error!')
    exit()

# Alert box which warns the user before starting the recording.
p.alert(
    text='After closing this dialog box, you will have 3 secs to open your browser and perform the following actions in this specific order with 2 secs intervals and a "ding" sound effect after each:' +
    '\n\n1. Place your cursor on the cookie, wait for the "ding."' +
    '\n2. Place your cursor on the last visible button in the Cookie Clicker Store, wait for the "ding"' +
    '\n3. Place your cursor on the second-last visible button and so on... till the last building on your screen.' +
    '\n\nNOTE: In this process, you are telling/teaching the bot where to click on the screen.',
    title='Information'
)

# Waiting for the user to open the browser.
time.sleep(3)

# The original position of the mouse.
cookie_x, cookie_y = p.position()
ding.play()

# Waiting.
time.sleep(2)
ding.stop()

# Generating a list to store the coordinate tuples.
coords_list = []

# Learning the positions of the buttons.
for _ in range(buttons_no):
    ding.play()

    coords_list.append(p.position())

    time.sleep(2)
    ding.stop()

try:
    while True:
        # Clicking on the cookie and catching the failsafe exception.
        try:
            p.click(x=cookie_x, y=cookie_y, clicks=CLICKS, interval=INTERVAL)
        except p.FailSafeException:
            print('Bot has been stopped.')
            exit()

        # Click on the buildings.
        for x_pos, y_pos in coords_list:
            p.click(x=x_pos, y=y_pos)
except KeyboardInterrupt:
    print('Bot has been stopped.')

mixer.quit()
