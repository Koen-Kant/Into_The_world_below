import sys
import subprocess
import math


class Artist:
    def __init__(self, size):
        self.console_width = size*4
        self.console_height = size*2

    def print_line(self, full=False, text=None):
        if full and text:
            if len(text) % 2 == 1:
                text = text + " "
            fill = (self.console_width-len(text)-2)/2
            str_out = "#"*fill + " "+text+" "+"#"*fill
        else:
            if len(text) % 2 == 1:
                text = text + " "
            fill = (self.console_width - len(text) - 2) / 2
            str_out = "#" + " " * fill + text + " "*fill + "#"
        print str_out

    def text_block(self, text):
        text_loop = len(text)/float((self.console_width-4))
        begin_char = 0
        end_char = self.console_width-4
        for i in range(int(math.ceil(text_loop))):
            self.print_line(text=text[begin_char:end_char])
            begin_char += self.console_width-4
            end_char += self.console_width - 4
        self.full_line()
        self.empty_line()

    def empty_line(self):
        print "#" + " "*(self.console_width-2) + "#"

    def full_line(self):
        print "#"*self.console_width

    def clear_screen(self):
        print "\n"*self.console_height

    def text_void(self):
        print "\n"*(self.console_height/2)

    def end_clear(self):
        sys.stdout.write("\33[H\33[2J")

    def prompt(self, in_val):
        out = raw_input(in_val)
        self.full_line()
        print "\n"*3
        self.full_line()
        return out

    def wait_prompt(self):
        raw_input("$: ")
        print "\n"*3
        self.full_line()

    def start_music(self, song):
        subprocess.call(["mpg123 -q --loop -1 " + song + " &"], shell=True)

    def switch_music(self, song):
        self.kill_music()
        self.start_music(song)

    def kill_music(self):
        out = subprocess.check_output("ps -e | grep mpg123", shell=True)
        subprocess.call(["kill " + out.split(' ')[1]], shell=True)
        subprocess.call(["kill " + out.split(' ')[0]], shell=True)

