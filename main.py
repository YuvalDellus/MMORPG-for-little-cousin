import pyautogui as py
import time
import math
import pyperclip
import re
from numpy import random

import winsound

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second

import Recorder

py.PAUSE = 0.2
py.FAILSAFE = False

CELSIS_POND = 541, 172
CELSIS_CHEST = 1058, 763

BOX_WIDTH = 40
GREYS_LIST = (130, 133, 131, 137, 111, 123, 100, 92, 88, 79, 42)
LAST_INV_BOX = 1507, 394
FIRST_PET_INV = 1233, 495

CAPTCHA_POSITION = 1013, 399
CAPTCHA_COLOR = 195, 53, 29
CENTER_POSITION = 824, 461

PATH = "C:\\Users\\yuval\\PycharmProjects\\pythonProject\\Scripts\\%s.txt"

print(py.size())

COLORS = {
    "344, 809": (213, 168, 95),
    "643, 838": (224, 180, 115),
    "1498, 770": (231, 182, 120),
    "1491, 769": (146, 97, 54),
    "1493, 626": (155, 119, 78),
    "1498, 398": (140, 89, 44),
    "1529, 237": (216, 173, 104),
    "735, 415": (1, 1, 1),
    "250, 775": (1, 1, 1),
    "201, 744": (1, 1, 1),
    "311, 246": (1, 1, 1),
    "341, 217": (1, 1, 1),
    "336, 211": (1, 1, 1),
    "336, 212": (1, 1, 1),
    "872, 171": (1, 1, 1),
    "1228, 220": (1, 1, 1),
    "959, 305": (1, 1, 1),
    "1135, 260": (1, 1, 1),

}


# ------------------------------ Tools ---------------------------

def captcha_check():
    global cur_captcha
    global start_all
    start = time.time()

    # if py.pixelMatchesColor(693, 402, (227, 227, 2)):
    if py.pixelMatchesColor(715, 451, (255, 255, 0)):
        winsound.Beep(frequency, duration)  # make a beep
        if cur_captcha < 4:
            if py.alert("You got captcha to dismiss", "Captcha Alert", timeout=20000) == "OK":
                time.sleep(25)
                cur_captcha = cur_captcha + 1 if cur_captcha < 4 else cur_captcha
                print("@@@@@@ You clicked Captcha, Took: %s You left %s points @@@@@@" % (
                time.time() - start, cur_captcha))
                return
        else:
            winsound.Beep(frequency, duration)  # make a beep
            winsound.Beep(frequency, duration)  # make a beep
z
        time.sleep(rand_time(20, -10, 10))
        left_click(1013, 399)  # click x
        left_click(824, 586)  # click no
        left_click(1008, 454)  # click x
        cur_captcha -= 1
        print("###### Clicked Captcha, Took: %s You left %s points ######" % (time.time() - start, cur_captcha))

        if cur_captcha < -1:  # just a test, need -2/-3z
            exit_game()
            total = round(time.time() - start_all)
            hours, minutes = divmod(total, 60)
            minutes, sec = divmod(hours, 60)
            if hours < 0:
                hours = "0%s" % hours
            if minutes < 0:
                minutes = "0%s" % minutes
            if sec < 0:
                sec = "0%s" % sec

            print("\nTook total: %s:%s:%s hours" % (hours, minutes, sec))
            exit("No more captcha points")


def scatter(x, y):
    a = random.randint(-5, 5)
    b = random.randint(-5, 5)
    while a ^ 2 + b ^ 2 > 10:
        a = random.randint(-5, 5)
        b = random.randint(-5, 5)
    return x + a, y + b


def rand_time(dur, down=0, up=2):
    return dur + random.randint(down, up)


def left_click(x, y):
    # sx, sy = x, y
    sx, sy = scatter(x, y)
    py.moveTo(sx, sy, rand_time(1), py.easeOutElastic)
    time.sleep(0.7)
    py.leftClick(sx, sy)


def exit_game():
    # print(time.strftime("%H:%M:%S", time.gmtime()))
    left_click(1655, 12)  # X button


def open_game():
    left_click(1434, 1031)  # ^
    left_click(1413, 955)  # Steam
    left_click(1480, 666)  # Game
    time.sleep(9)
    left_click(1503, 200)  # Full size window
    left_click(635, 575)  # Register

    press("z")


def restarter():
    print("@@@ Restarting position @@@")
    left_click(820, 563)
    wait(1)
    left_click(1050, 441)
    wait(9)
    press('z')
    digging_reval()


def check_position():
    if py.pixelMatchesColor(786, 445, (201, 174, 104)): exit(-4)


def KeyBreak():
    ## NOT WORKING ##

    print('Press Ctrl-C to quit.')
    try:
        while True:
            open_game()
            fishing_Celsis()
    except KeyboardInterrupt:
        print("\n")
        exit(-2)


def take_sample(start):
    x, y = start
    py.moveTo(x, y)
    py.mouseInfo()

    pixel_data = pyperclip.paste()
    print(pixel_data)


def search_screen(object):
    obj_location = py.locateOnScreen('Celsis_Teleport.PNG', region=(625, 498, 798, 549))
    print(obj_location)

    # obj_location = None
    # while(obj_location == None):
    #     obj_location = py.locateOnScreen('test.png')
    # print(object+".PNG")
    # print((obj_location))


def cheack_life():
    # left_click(759, 9)
    times = 0
    refocus = True
    while (py.pixelMatchesColor(486, 176, (191, 92, 75))):

        captcha_check()
        times += 1

        if times > 15 and refocus:
            py.getWindowsWithTitle("RPG MO - Early Access")[0].minimize()  # trying to regain focus to window
            py.getWindowsWithTitle("RPG MO - Early Access")[0].maximize()
            time.sleep(1)
            py.press("c")
            refocus = False

        if times > 30:
            left_click(1352, 279)  # teleport scroll, in inv(2, 4)
            print(time.strftime("%H:%M:%S", time.gmtime()))
            exit("No more potions\n")

        if times % 2: print("Life restored %s" % times)

        py.press('q')
        time.sleep(0.5)


def calculate_where_to_click(right=0, left=0, up=0, down=0):
    new_x = CENTER_POSITION[0] + (right * 45) - (left * 40) + (up * 45) - (down * 40)
    new_y = CENTER_POSITION[1] + (right * 30) - (left * 17) - (up * 17) + (down * 30)

    return (new_x, new_y)


def calculate_where_to_click_human():
    while (True):

        print("To exit enter X")
        right, left, up, down = 0, 0, 0, 0

        right = input("How many blocks Right?\n")
        if right == "0":
            left = input("How many blocks Left?\n")
            if left == "x":
                exit("Done calculate")
        elif right == "x":
            exit("Done calculate")

        up = input("How many blocks Upt?\n")
        if up == "0":
            down = input("How many blocks Down?\n")
            if down == "x":
                exit("Done calculate")
        elif up == "x":
            exit("Done calculate")

        right = int(right)
        left = int(left)
        up = int(up)
        down = int(down)

        new_x = CENTER_POSITION[0] + (right * 45) - (left * 45) + (up * 45) - (down * 45)
        new_y = CENTER_POSITION[1] + (right * 22.5) - (left * 22.5) - (up * 22.5) + (down * 22.5)

        print("New block at: (%s, %s)" % (new_x, new_y))
        py.moveTo(new_x, new_y)


def get_pixel_colour(i_x, i_y):
    import PIL.ImageGrab
    return PIL.ImageGrab.grab().load()[i_x, i_y]


def two_pixel_check():
    a = py.pixelMatchesColor(301, 217, (207, 142, 40))
    b = py.pixelMatchesColor(294, 216, (224, 159, 56))
    # print("a: ", a, "b: ", b)
    return (a or b)


# ------------------------------ Commands -------------------------

def pet_maneuver(direction, duration=2):
    if direction == "up":
        op = "down"
    elif direction == "down":
        op = "up"
    elif direction == "left":
        op = "right"
    elif direction == "right":
        op = "left"

    print("=== pet maneuver ===")
    press(direction, duration + 0.2)
    press("v")
    press(op, duration)


def deposit_all(): py.press('z')


def wait(duration, mission="Walking"):
    start = time.time()
    prev = 0
    while time.time() - start < duration:
        cur = math.floor(time.time() - start)
        if cur > prev: print(math.floor(time.time() - start), " / %s  %s" % (duration, mission))
        prev = cur


def walk_to(point_x, point_y, duration, mine):
    print("I'm walking I'm walking")
    # x, y = scatter(point_x, point_y)
    left_click(point_x, point_y)
    time.sleep(duration)
    captcha_check()

    if mine != "0":
        py.press("z")


def press(key, duration=0.2):
    py.keyDown(key)
    time.sleep(duration)
    py.keyUp(key)


def kill_at(point_x, point_y, dur):
    print("kill started at ", point_x, point_y)
    # x, y = scatter(point_x, point_y)
    left_click(point_x, point_y)

    beat = 0

    while not two_pixel_check():  # wait encounter

        beat += 1
        if beat % 2:
            print("Going to find some troubles")

        time.sleep(1)
        captcha_check()

    beat = 0

    while two_pixel_check():  # wait fight to end
        beat += 1
        if beat % 2:
            print("Fuck that bitch")

        # cheack_life()
        time.sleep(0.5)
        captcha_check()

    captcha_check()
    cheack_life()


def mine(point_x, point_y, source_x, source_y, dur):
    # x, y = scatter(point_x, point_y)
    left_click(point_x, point_y)
    time.sleep(dur)
    beat = 0

    while find_first_full_inv()[2] != 0:
        beat += 1
        if beat % 2:
            print("First digging %s" % beat)

        if beat > 30:
            break

        time.sleep(7)
        captcha_check()

    time.sleep(1)
    py.press("v")
    time.sleep(1)
    print("Filled inv")
    beat = 0
    sx, sy = scatter(source_x, source_y)
    left_click(sx, sy)

    while find_first_full_inv()[2] != 0:
        beat += 1
        if beat % 2:
            print("Second digging %s" % beat)
            if beat > 20:
                break

        time.sleep(7)
        captcha_check()


# ------------------------------ Inventory -----------------------

def check_last_empty():
    return py.pixelMatchesColor(1507, 394, (130, 130, 130))


def find_first_full_inv():
    # cur_x = 1507
    # cur_y = 400
    cur_x = 1450
    cur_y = 447
    empty_amount = 0
    while py.pixel(cur_x, cur_y)[0] in GREYS_LIST:
        cur_x -= 40
        empty_amount += 1
        if cur_x < 1214:
            cur_x = 1507
            cur_y -= 40
            if cur_y < 222: return None

    return cur_x, cur_y, empty_amount


def search_inventory():
    pass


def center_up_inv():
    pass


# ------------------------------ Celsis -------------------------
def fishing_Celsis(loop=0):
    print("------------------- loop: %s -------------------" % loop)

    fishing_number = 0
    loop += 1
    walk_to(CELSIS_POND[0], CELSIS_POND[1])  # Pond

    while (find_first_full_inv()[2] != 0):
        print("first fishing %s" % fishing_number)
        fishing_number += 1
        time.sleep(10)
        captcha_check()
        if fishing_number > 11: break  # sometimes get jewel in last spot

    py.press('v')
    press("left", 0.5)

    fishing_number = 0

    while (find_first_full_inv()[2] != 0):
        print("second fishing %s" % fishing_number)
        fishing_number += 1
        time.sleep(10)
        captcha_check()
        if fishing_number > 7: break  # sometimes get jewel in last spot

    walk_to(CELSIS_CHEST[0], CELSIS_CHEST[1])  # chest
    deposit_all()
    fishing_Celsis(loop)


def cooking_celsis():
    captcha_check()
    empty_pet = True
    if py.pixelMatchesColor(858, 411, (238, 141, 54)):
        print("1")
        fish_position = 858, 411
    elif py.pixelMatchesColor(812, 410, (36, 26, 22)):
        print("2")
        fish_position = 812, 410
    elif py.pixelMatchesColor(777, 407, (131, 152, 165)):
        print("3")
        fish_position = 777, 407
    elif py.pixelMatchesColor(730, 408, (250, 2, 2)):
        print("4")
        fish_position = 730, 408
    elif py.pixelMatchesColor(690, 415, (230, 207, 166)):
        fish_position = 690, 415
        print("5")
    else:
        print("finished all fishes")
        exit(0)

    left_click(fish_position[0], fish_position[1])  # first load
    py.press('x')

    if find_first_full_inv()[2] == 0:
        empty_pet = False
        py.press('v')
        left_click(658, 409)  # full load
        py.press('x')

    left_click(1310, 239)  # pick fish
    press('up', 1)
    wait(1)

    while not py.pixelMatchesColor(1297, 224, (66, 162, 107)):
        print("first cooking")
        time.sleep(10)
        # wait(10, "first cooking")

    if not empty_pet:  # start second cooking process
        py.press('c')
        left_click(find_first_full_inv()[0:2])
        press('up', 1)
        print("second cooking")
        time.sleep(50)
        # wait(50, "second cooking")

    press('down', 1)
    py.press('z')
    cooking_celsis()


# ------------------------------ Reval ---------------------------

def digging_reval(loop=0):
    print("------------------- loop: %s -------------------" % loop)
    print("------------------- dagged: %s -----------------" % (loop * 58))
    loop += 1
    digging_number = 0

    start = time.time()

    captcha_check()

    left_click(520, 587)  # point in city
    captcha_check()
    # time.sleep(2)
    left_click(925, 193)  # digging site
    time.sleep(9)
    captcha_check()

    while (find_first_full_inv()[2] != 0):
        print("first digging %s" % digging_number)
        digging_number += 1
        time.sleep(10)
        captcha_check()
        if digging_number > 11: break  # sometimes get jewel in last spot

    py.press('v')
    ## captcha gap ##
    press('left')
    digging_number = 0

    while (find_first_full_inv()[2] != 0):
        print("second digging %s" % digging_number)
        digging_number += 1
        time.sleep(10)
        captcha_check()
        if digging_number > 7: break  # sometimes get jewel in last spot

    left_click(728, 605)  # point near fence
    # time.sleep(2)                             ## captcha gap ##
    left_click(1049, 441)  # chest
    time.sleep(9)
    captcha_check()

    check_position()

    py.press('z')
    print("----- Took: %s " % (time.time() - start))
    if (time.time() - start) < 40: restarter()
    digging_reval(loop)


def digging_gold_reval(loop=0):
    print("------------------- loop: %s -------------------" % loop)
    start = time.time()

    digging_number = 0
    loop += 1
    walk_to(344, 809)
    walk_to(643, 838)
    walk_to(1498, 770)
    walk_to(1491, 769)
    walk_to(1493, 626)
    walk_to(1498, 398)
    walk_to(1529, 237)
    walk_to(735, 415)  # fight
    time.sleep(25)
    captcha_check()

    #  digging

    py.press('i')
    left_click(691, 391)  # digging
    time.sleep(2)

    while (find_first_full_inv()[2] != 0):
        print("first digging %s" % digging_number)
        digging_number += 1
        time.sleep(10)
        captcha_check()
        # if digging_number > 11: break  # sometimes get jewel in last spot

    py.press('v')
    ## captcha gap ##
    press('left')
    digging_number = 0

    while (find_first_full_inv()[2] != 0):  # leaving space for loot from snake
        print("second digging %s" % digging_number)
        digging_number += 1
        time.sleep(5)
        captcha_check()
        # if digging_number > 7 : break  # sometimes get jewel in last spot

    # # going back

    py.press('i')
    time.sleep(3)

    # left_click(868,491)  # fighting
    press('right', 2)
    time.sleep(25)
    captcha_check()
    walk_to(250, 775, 3)
    walk_to(201, 744)
    walk_to(311, 246)
    walk_to(341, 217)
    walk_to(336, 211)
    walk_to(336, 212)
    walk_to(872, 171)
    walk_to(1228, 220)
    walk_to(959, 305)
    walk_to(1135, 260)  # chest

    py.press('z')
    print("----- Took: %s " % (time.time() - start))

    digging_gold_reval(loop)


# ------------------------------ Dorpat ---------------------------

def killing_crusader(loop=0):
    """
    Killing Crusader MOB in Dungeon,
    Starting position: First white tile in the hallway, need first crusader.
    """
    print("------------------- loop: %s -------------------" % loop)
    loop += 1
    cheack_life()

    while (not py.pixelMatchesColor(868, 461, (199, 148, 28))):  # wait for first spawn
        time.sleep(3)

    start = time.time()

    kill_at(874, 493)
    kill_at(1045, 574)
    kill_at(1002, 595)
    kill_at(1004, 509)
    kill_at(916, 374)
    kill_at(959, 297)
    kill_at(1047, 490)
    kill_at(1179, 323)
    kill_at(868, 532)
    kill_at(1050, 478)
    kill_at(1005, 550)
    cheack_life()

    walk_to(562, 339, 1)
    walk_to(509, 635, 1)
    walk_to(693, 402, 1)
    walk_to(471, 651, 1)
    kill_at(739, 418)
    kill_at(604, 350)
    walk_to(740, 424, 1)  # start position

    print("----- Took: %s " % (time.time() - start))

    killing_crusader(loop)


# ------------------------------ Executive ------------------------ #

def parser(command="move"):
    pattern = "\(([0-9]+)\, ([0-9]+)\) ([0-9]+\.[0-9]+) (\S) \(([0-9]+)\, ([0-9]+)\, ([0-9]+)\) (0|\(([0-9]+)\, ([0-9]+)\))"
    m = re.compile(pattern)
    f = open(PATH % command, "r")
    line = f.readline()
    command_list = []

    while line:
        parts = m.match(line)
        x, y, dur, kind = parts[1], parts[2], parts[3], parts[4]
        color = (parts[5], parts[6], parts[7])
        if parts[8] == "0":
            source = 0
        else:
            source = (parts[9], parts[10])

        print((x, y, dur, kind, color, source))

        # if kind == "W":
        #     kind = 1
        # elif kind == "F":
        #     kind = 2
        # elif kind == "M":
        #     kind = 3

        command_list.append(int(x))
        command_list.append(int(y))
        command_list.append(math.ceil(float(dur)))
        command_list.append(kind)
        command_list.append(color)
        command_list.append(source)

        line = f.readline()

    f.close()
    return command_list


def prompt(command="move"):
    count = 0
    loop = 0
    dig = False

    start = time.time()

    scene = random.randint(1, 4)
    scene = 2
    print("-------- Scenario: %s --------------------" % scene)
    exe = command % scene
    command_list = parser(exe)

    while (True):

        if count == 0:
            print("------------------- loop %s -------------------" % loop)

        x = command_list[count]
        y = command_list[count + 1]
        dur = command_list[count + 2]
        kind = command_list[count + 3]
        color = command_list[count + 4]
        r, g, b = int(color[0]), int(color[1]), int(color[2])
        source = command_list[count + 5]

        if kind == "W":
            walk_to(x, y, dur, source)

        elif kind == "F":
            start_move = time.time()
            while not py.pixelMatchesColor(x, y, (r, g, b)):

                if (time.time() - start_move > dur):
                    print("It's looks like someone Chickened  out")

                time.sleep(1)
                captcha_check()

            kill_at(x, y, dur)

        elif kind == "M":
            mine(x, y, int(source[0]), int(source[1]), dur)
            dig = True

        else:
            exit("Wrong kind: %s" % kind)

        count += 6
        if count >= len(command_list):
            count = 0
            loop += 1
            total = round(time.time() - start)
            minutes, sec = divmod(total, 60)
            if sec < 10:
                sec = "0%s" % sec

            if dig:
                print("------------------- dagged: %s" % (loop * 45))
            print("------------------- Took: %s:%s minutes" % (minutes, sec))
            dig = False
            start = time.time()
            # scene = random.randint(1, 4)
            # print("-------- Scenario: %s --------------------" % scene)
            # exe = command % scene
            # command_list = parser(exe)


def cheack_scatter(x, y, repeats=100):
    for i in range(repeats):
        new_x, new_y = scatter(x, y)
        py.moveTo(new_x, new_y)
        time.sleep(0.1)


if __name__ == '__main__':
    start_all = time.time()
    cur_captcha = 4
    prompt("sand_Reval_%s")
    # py.mouseInfo()
    # Recorder.Recorder("sand_Reval_4")
