import pyautogui as py
from pynput.mouse import Listener
from pynput import keyboard
from time import time

PATH = "C:\\Users\\yuval\\PycharmProjects\\pythonProject\\Scripts\\%s.txt"

class Recorder:

    def __init__(self, move_name="move", edit=False):

        self.move_name = move_name
        if not edit: self.clear_file()
        self.move_recorder()

        print("\nMove finished!\n Thank you")

    def clear_file(self):
        g = open(PATH % self.move_name, "w")
        g.write("")  # clean the file
        g.close()

    def on_click(self, x, y, button, pressed):
        if pressed:
            start = str(time())
            # print('{0} at {1} time: {2}'.format('Pressed' if pressed else 'Released', (x, y), (int(time.time()) % 1000)))
            print("clicked")
            print("Timer ticking")
            f = open(PATH % "pixel&time_temp", "w")
            # print(start, "\n{0} {1}".format((x, y), self.get_pixel_colour(x, y)))
            # f.writelines([start, "\n{0}\n{1}".format((x, y), self.get_pixel_colour(x, y))])
            # f.write(start + "\n")
            # f.write(str((x, y)+ "\n"))
            # f.write(str(self.get_pixel_colour(x, y)))
            data = "{0}\n{1}\n{2}".format(start, (x, y), self.get_pixel_colour(x, y))
            f.write(data)
            f.close()
            return False

    def mine_click(self, x, y, button, pressed):

        f = open(PATH % "source_temp", "w")  # extracting click information
        f.write("{0}".format((x, y)))
        f.close()
        print("Source recorded!")
        return False

    def on_press(self, key):
        try:
            if key.char in ["1", "2", "3"]:
                end = time()
                kind = ""
                print("\nStop timer!")

                f = open(PATH % "pixel&time_temp", "r")  # extracting click information
                data = f.readlines()
                start = float(data[0])
                pos = data[1].split("\n")[0]  # I really dont know, stupid coding
                color = data[2]
                source = 0

                f.close()

                if key.char == "1":  # more readable that way
                    kind = "W"
                elif key.char == "2":
                    kind = "F"
                elif key.char == "3":
                    kind = "M"
                    py.alert("On arrival, please click one more time on the mining source")
                    with Listener(on_click=self.mine_click) as listener3:
                        listener3.join()
                    k = open(PATH % "source_temp", "r")  # extracting click information
                    source = k.readline()
                    k.close()

                g = open(PATH % self.move_name, "a")
                g.write("{0} {1} {2} {3} {4}\n".format(pos, (end - start), kind, color, source))  # logging the specific move
                g.close()

                print("\nMove recorded!\n")
                return False
                # return True

        except AttributeError:
            print("Invalid critical key!")
            return False

    def check_another(self):

        ans = py.confirm(text="Record another move?", buttons=["Yes", "No"])
        if ans == "Yes":
            self.move_recorder()
        else:
            return

    def get_pixel_colour(self, i_x, i_y):
        import PIL.ImageGrab
        return PIL.ImageGrab.grab().load()[i_x, i_y]

    def move_recorder(self):
        print("Welcome Recorder! \n\nFor exit press Esc\n")
        print("Manual: first click on point as desire")
        print(" to stop the time in walking command press -1-")
        print(" to stop the time in fighting command press -2-")
        print(" to stop the time in mining command press -3-")

        with Listener(on_click=self.on_click) as listener:
            listener.join()
        with keyboard.Listener(on_press=self.on_press) as listener2:
            listener2.join()

        self.check_another()

    # def initiate(move_name="move"):
    #     g = open("%s.txt" % move_name, "w")
    #     g.write("")  # clean the file
    #     g.close()
    #     move_recorder()
    #
    #     print("\nMove finished!\n Thank you")
