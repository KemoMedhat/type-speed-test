
import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcom to speed typing test ", curses.color_pair(1))
    stdscr.addstr("\nPress any kay to begin ", curses.color_pair(1))
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr,target,current,wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1,0,f"WPM : {wpm}")
    for i, char in enumerate(current):
        correct = target[i]
        
        if char==correct:
            color = curses.color_pair(1)
        else :
            color = curses.color_pair(2)
        stdscr.addstr(0,i,char,color)

def wpm_test(stdscr):
    target_text = load_file()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)
    while (True):
        time_elapse = max(time.time() - start_time,1)
        wpm = round(len(current_text)/(time_elapse/60) / 5)
        stdscr.clear()
        display_text(stdscr,target_text,current_text,wpm)
        stdscr.refresh()
        if "".join(current_text) == target_text :
            stdscr.nodelay(False)
            break
        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27 :
            break
        if key in ("KEY_BACKSPACE",'\b','\x7f'):
            if len(current_text)>0:
                current_text.pop()
        elif len(current_text)<len(target_text):
            current_text.append(key)

def load_file():
    with open("text.txt","r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK)
    while True :
        start_screen(stdscr)
        wpm_test(stdscr)
        stdscr.addstr(2,0,"Test Completed, Press any key to continue.....",curses.color_pair(1))
        key = stdscr.getkey()
        if ord(key) == 27 :
            break

wrapper(main)
