"""

Filename: on_target.py
Description: A Simple day planner to track tasks on the go. It uses a simple 
             TSV to add tasks and their duration. A simple user interface to
             start/pause and end tasks to keep you  on target. Program implements
             Model - View+Controller pattern, the View and Controller is 
             combined for simplicity
Usage: python on_target.py
Recommended Python Version: 3.+             
Created: Wed Apr  8 17:24:02 2020 PDT
Version: 1.0
"""
import random
import time as t
from tkinter import *
import tkinter as tk
from tkinter import ttk
from time import strftime
  
LIGHT_COLORS = [
    'snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 
    'old lace', 'linen', 'antique white', 'papaya whip', 'blanched almond', 
    'bisque', 'peach puff', 'navajo white', 'lemon chiffon', 'mint cream', 
    'azure', 'alice blue', 'lavender', 'lavender blush', 'misty rose', 'gray', 
    'light grey', 'cornflower blue', 'dodger blue', 'deep sky blue', 'sky blue', 
    'light sky blue', 'steel blue', 'light steel blue', 'light blue', 
    'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 
    'turquoise', 'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 
    'aquamarine', 'dark sea green',  'medium sea green', 'light sea green', 
    'pale green', 'spring green', 'lawn green', 'medium spring green', 
    'green yellow', 'lime green', 'yellow green', 'khaki', 'pale goldenrod', 
    'light goldenrod yellow', 'light yellow', 'yellow', 'gold', 
    'light goldenrod','sandy brown', 'dark salmon', 'salmon', 'light salmon', 
    'orange', 'dark orange', 'light coral', 'tomato', 'orange red', 'hot pink', 
    'pink', 'light pink', 'snow2', 'snow3', 'seashell2', 'seashell3', 
    'AntiqueWhite1', 'AntiqueWhite2', 'AntiqueWhite3', 'bisque2', 'bisque3', 
    'PeachPuff2', 'PeachPuff3', 'NavajoWhite2', 'NavajoWhite3',  'LemonChiffon2', 
    'LemonChiffon3', 'cornsilk2', 'cornsilk3', 'ivory2', 'ivory3', 'honeydew2', 
    'honeydew3', 'LavenderBlush2', 'LavenderBlush3', 'MistyRose2', 'MistyRose3',
    'azure2', 'azure3', 'azure4', 'DodgerBlue2', 'DodgerBlue3', 'SteelBlue1', 
    'SteelBlue2', 'SteelBlue3', 'DeepSkyBlue2', 'DeepSkyBlue3', 'SkyBlue1', 
    'SkyBlue2', 'SkyBlue3', 'LightSkyBlue1', 'LightSkyBlue2', 'LightSkyBlue3', 
    'SlateGray1', 'SlateGray2', 'SlateGray3', 'LightSteelBlue1', 'LightSteelBlue2', 
    'LightSteelBlue3', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightCyan2', 
    'LightCyan3', 'PaleTurquoise1', 'PaleTurquoise2', 'PaleTurquoise3', 
    'CadetBlue1', 'CadetBlue2', 'CadetBlue3', 'turquoise1', 'turquoise2', 
    'turquoise3', 'cyan2', 'cyan3', 'DarkSlateGray1', 'DarkSlateGray2', 
    'DarkSlateGray3', 'aquamarine2', 'DarkSeaGreen1', 'DarkSeaGreen2', 
    'DarkSeaGreen3', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 
    'PaleGreen2', 'PaleGreen3', 'SpringGreen2', 'SpringGreen3', 'green2', 
    'green3', 'chartreuse2', 'chartreuse3', 'OliveDrab1', 'OliveDrab2', 
    'DarkOliveGreen1', 'DarkOliveGreen2', 'DarkOliveGreen3', 'khaki1', 'khaki2',
    'khaki3', 'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3',
    'LightYellow2', 'LightYellow3', 'yellow2', 'yellow3', 'gold2', 'gold3', 
    'goldenrod1', 'goldenrod2', 'goldenrod3', 'DarkGoldenrod1', 'DarkGoldenrod2',
    'DarkGoldenrod3', 'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'IndianRed1', 
    'IndianRed2', 'IndianRed3', 'sienna1', 'sienna2', 'sienna3', 'burlywood1',
    'burlywood2', 'burlywood3', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2', 'salmon3', 
    'salmon4', 'LightSalmon2', 'orange2', 'orange3', 'DarkOrange1', 'DarkOrange2',
    'coral1', 'coral2', 'tomato2', 'HotPink1', 'HotPink2', 'HotPink3', 'pink1', 
    'pink2', 'LightPink1', 'LightPink2', 'LightPink3', 'PaleVioletRed1',
    'PaleVioletRed2', 'orchid1', 'orchid2', 'orchid3', 'plum1',
    'plum2', 'plum3', 'MediumPurple1', 'MediumPurple2', 'thistle1', 'thistle2', 'thistle3',
    'gray45', 'gray46', 'gray47', 'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 
    'gray53', 'gray54', 'gray55', 'gray56', 'gray57', 'gray58', 'gray59', 'gray60', 
    'gray61', 'gray62', 'gray63', 'gray64', 'gray65', 'gray66', 'gray67', 'gray68', 
    'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74', 'gray75', 'gray76', 
    'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83', 'gray84', 
    'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92', 
    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99'
]

DARK_COLORS = [
    'dark slate gray', 'dim gray', 'slate gray', 'light slate gray', 'midnight blue', 
    'navy', 'dark slate blue', 'slate blue', 'medium slate blue', 'light slate blue', 
    'medium blue', 'royal blue', 'blue', 'dark green', 'dark olive green', 
    'dark sea green', 'sea green', 'forest green', 'olive drab', 'dark khaki', 
    'goldenrod', 'dark goldenrod', 'rosy brown', 'indian red', 'saddle brown',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 
    'maroon', 'medium violet red', 'violet red', 'medium orchid', 'dark orchid', 
    'dark violet', 'blue violet', 'purple', 'medium purple', 'snow4', 'seashell4', 
    'AntiqueWhite4', 'bisque4', 'PeachPuff4', 'NavajoWhite4', 'LemonChiffon4', 
    'cornsilk4', 'ivory4', 'honeydew4', 'LavenderBlush4', 'MistyRose4', 'azure4', 
    'SlateBlue1', 'SlateBlue2', 'SlateBlue3', 'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 
    'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4', 'DodgerBlue2', 'DodgerBlue3', 
    'DodgerBlue4', 'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue3', 'SkyBlue4', 'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue3', 'LightSteelBlue4', 'LightBlue4', 'LightCyan4', 
    'PaleTurquoise4', 'CadetBlue4', 'turquoise4', 'cyan4', 'DarkSlateGray4', 'aquamarine4', 
    'DarkSeaGreen4', 'PaleGreen4', 'SpringGreen4', 'green4', 'chartreuse4', 'OliveDrab4', 
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki4', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow4', 'yellow4', 'gold4', 'goldenrod3', 'goldenrod4', 'DarkGoldenrod3', 
    'DarkGoldenrod4', 'RosyBrown3', 'RosyBrown4', 'IndianRed3', 'IndianRed4', 'sienna4', 
    'burlywood3', 'burlywood4', 'wheat4', 'tan4', 'chocolate3', 'firebrick4', 'brown4', 
    'salmon4', 'LightSalmon3', 'LightSalmon4', 'orange4', 'DarkOrange3', 'DarkOrange4',
    'coral4', 'tomato3', 'tomato4', 'OrangeRed4', 'red2', 'DeepPink2', 'DeepPink3', 
    'DeepPink4', 'HotPink3', 'HotPink4', 'pink3', 'pink4', 'LightPink3', 'LightPink4', 
    'PaleVioletRed1', 'PaleVioletRed4', 'maroon1', 'maroon2', 'maroon3', 'maroon4', 
    'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4', 'magenta2', 'magenta3', 
    'magenta4', 'orchid4', 'plum3', 'plum4', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
    'MediumPurple3', 'MediumPurple4', 'thistle3', 'thistle4', 'gray1', 'gray2', 'gray3', 
    'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10', 'gray11', 'gray12', 
    'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19', 'gray20', 'gray21', 
    'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28', 'gray29', 'gray30', 
    'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37', 'gray38', 
    'gray39', 'gray40', 'gray42', 'gray43', 'gray44'
]

class Schedule:
    """
    Reads schedule from the input file and manages Schedule related actions.
    """

    def __init__(self, file_name):
        """
        Init code to read today.tsv and populate internal structures.
        """
        f = open(file_name, 'r')
        self.lines = f.readlines()
        f.close()
        self.tasks = []
        self.progress = []
        self.read_schedule()
        self.init_schedule()
        self.current_task = None
        self.current_start = None
        self.paused = True        

    def read_schedule(self):
        """
        TSV input format: Task name, duration
        Note:
            - Task name - Can be creative ways to represent the task
            - duration - Format <int value><h|m> h - stands for hour/s, m - minutes
        """
        for line in self.lines:
            line = line.strip()
            if line != "":
                (task_name, duration) = line.split('\t')
                duration = Schedule.get_normalized(duration)
                if duration:
                    self.tasks.append((task_name, duration))
    
    def init_schedule(self):
        """
        Initalize progress data structure
        """
        for i in range(len(self.tasks)):
            # (NOT STARTED/PAUSED/DONE, percent_completed)
            self.progress.append([True, self.tasks[i][1]])

    @classmethod
    def get_normalized(cls, duration):
        """
        Normalize all durations in terms of hours and minutes to one
        normal form - in minutes.
        """
        if duration:
            duration = duration.lower()
            value = None
            if duration.endswith('h'):
                value = int(duration[:-1])*60
            else:
                if duration.endswith('m'):
                    value = int(duration[:-1])
                else:
                    value = int(duration)
            return value 

    @classmethod
    def get_percentage(cls, current, duration):
        """
        Compute the percentage finished for a task in terms of allocated duration.
        """
        if duration:
            n = (duration-current) * 100
            d = duration
            return int(n/d)    

# System configuration
# Tweak to control the width, height and theme of the app
WIDTH=534
HEIGHT=260
BACKGROUND1='dark green'  
BACKGROUND2='white'

root = tk.Tk() 
root.title('Simple Planner') 
root.geometry('%sx%s' % (WIDTH, HEIGHT))  

label = tk.Label(root, font = ('monaco', 32, 'bold'), 
            bg = BACKGROUND1, 
            fg = 'snow',
            width=WIDTH) 
label.pack(anchor = 'center')

labelframe = LabelFrame(root, text="Tasks for today", font=('monaco', 18, 'bold'), bg=BACKGROUND2)
labelframe.pack(fill='both', expand="yes")

s = Schedule('today.tsv')
HEIGHT = HEIGHT - 200 + len(s.tasks) * 40
root.geometry('%sx%s' % (WIDTH, HEIGHT))

class ScheduleControllerView:
    """
    Controller+View class to handle both UI and buisness logic and 
    UI elements
    """
    def __init__(self, schedule):
        """
        Initialize the state of the controls
        """
        self.s = schedule
        self.str_pause_btns = []
        self.done_btns = []
        self.bars = []
        self.bar_styles = []
        self.start_pause_funcs = {}
        self.done_funcs = {}        

    @classmethod
    def refresh(cls):
        """
        Refresh method is used to refresh the clock and the progress of the tasks.
        """
        string = strftime('%I:%M:%S %p') 
        label.config(text = string)
        ScheduleControllerView.process_progress(scv)
        label.after(1000, ScheduleControllerView.refresh)

    @classmethod
    def sound_bell(cls, times=1):
        """
        Uses the system bell to sound a notification for user, that he/she has reached a milestone
        """
        for i in range(times):
            print("\a")
            t.sleep(1)

    @classmethod
    def milestones(cls, p):
        """
        Subtle Notification for user at 33% and 66% of their task. Uncomment milestones() call
        to enable this feature. 
        Note: The terminal will scroll when this is enabled.
        """
        if p == 33:
            ScheduleControllerView.sound_bell(1)
        elif p == 66:
            ScheduleControllerView.sound_bell(2)
    
    @classmethod
    def process_progress(cls, controller_view):
        """
        Main handler to process the progress of tasks. 
        It updates the text and percentage of the task completed.
        """
        if not s.paused:
            for task_num in range(len(s.tasks)):
                if not s.progress[task_num][0] and s.current_task != None and s.current_task == task_num:
                    current = int(t.time())
                    if (current - s.current_start) > 60:
                        s.progress[task_num][1] = s.progress[task_num][1]-1
                        s.current_start = current
                p = Schedule.get_percentage(s.progress[task_num][1], s.tasks[task_num][1])
                controller_view.bars[task_num]['value'] = p
                # ScheduleControllerView.milestones(p)
                if p != 0:
                    text = '%s (%s %%)' % (s.tasks[task_num][0], p)
                else:
                    if not s.progress[task_num][0]:
                        text = '%s (%s %%)' % (s.tasks[task_num][0], '0')
                    else:
                        text = '%s' % (s.tasks[task_num][0])
                controller_view.bar_styles[task_num].configure('text.Horizontal.TProgressbar_' + str(task_num), text=text)

    @classmethod
    def get_style(cls, root, index, text, bg, fg):
        """
        Style for the progress bar
        """
        style = ttk.Style(root)
        style.theme_use('default')
        style.layout('text.Horizontal.TProgressbar_' + str(index),
                [('Horizontal.Progressbar.trough',{
                    'children': [
                        ('Horizontal.Progressbar.pbar',{'side': 'left', 'sticky': 'ns'})
                    ],
                    'sticky': 'nswe'
                }),
                ('Horizontal.Progressbar.label', {'sticky': ''})])
        style.configure('text.Horizontal.TProgressbar_' + str(index), text=text, background=bg, foreground=fg, font=('monaco', 14, 'normal'))
        return style

    @classmethod
    def add_button(cls, root, btn_text, on_click_func):
        """
        Helper method to add a button to the frame.
        """
        button = Button(root, text=btn_text, command=on_click_func, font=('monaco', 11, 'bold'))
        button.config(foreground = 'gray24')
        button.pack(pady=6, padx=5, side=RIGHT)
        return  button

    def reset_pause_btn_to_start(self, task_num):
        """
        Handler to reset the PAUSE state of the button back to START
        """
        for index in range(len(self.s.progress)):
            (state, duration) = (self.s.progress[index][0], self.s.progress[index][1]) 
            if index != task_num and state is False:  
                self.s.progress[index][0] = True
                self.str_pause_btns[index]['text'] = 'START'

    def set_to_running(self, task_num):
        """
        Set the task to running, and update state of the controls
        """
        import time
        self.s.progress[task_num][0] = False
        self.s.paused = False
        self.str_pause_btns[task_num]['text'] = 'PAUSE'
        self.s.current_task = task_num
        self.s.current_start = int(time.time())

    def set_to_paused(self, task_num):
        """
        Set the task to paused, and update state of the controls
        """
        self.s.progress[task_num][0] = True
        self.s.paused = True
        self.str_pause_btns[task_num]['text'] = 'START'
        self.s.current_task = None
        self.s.current_start = None

    def mark_task_done(self, task_num):
        """
        Set the task to done, and update state of the controls
        """
        import tkinter as tk
        self.s.progress[task_num][0] = True
        self.s.progress[task_num][1] = 0
        text = s.tasks[task_num][0] + ' (100 %%)'
        self.bar_styles[task_num].configure('text.Horizontal.TProgressbar_' + str(task_num), text=text)
        self.bars[task_num]['value'] = 100
        self.done_btns[task_num]['state'] = tk.DISABLED
        self.str_pause_btns[task_num]['state'] = tk.DISABLED

    @classmethod
    def create_start_pause_handlers(cls, controller_view):
        for i in range(len(controller_view.s.tasks)):
            value = str(i)
            code = \
"""
def btn_start_pause_%s(index=%s):
    # Dynamic handler for each button
    # to start and pause the progress of the task
    task_num = index 
    s.current_task=task_num
    controller_view.reset_pause_btn_to_start(task_num)
    isPaused = s.progress[task_num][0]
    if isPaused:
        controller_view.set_to_running(task_num)
    else:
        controller_view.set_to_paused(task_num)
""" % (value, value)
            exec(code, {
                's': controller_view.s, 
                'controller_view' : controller_view}, 
                controller_view.start_pause_funcs)

    @classmethod
    def create_done_handlers(cls, controller_view):
        for i in range(len(controller_view.s.tasks)):
            value = str(i)
            code = \
"""
def btn_done_%s(index=%s):
    # Dynamic handler for each button
    # to mark the task as done
    # Once the task is done, the start/pause is disabled 
    task_num=index
    controller_view.mark_task_done(task_num)
""" % (value, value)
            exec(code, {
            'controller_view' : controller_view}, 
            controller_view.done_funcs)

    @classmethod
    def create_main_panel(cls, controller_view):
        """
        Main panel creation 
        Add progress bars
        Add buttons for start/pause and done
        """
        index = 0
        for (task_name, duration) in s.tasks:
            color = LIGHT_COLORS[random.randint(0, len(LIGHT_COLORS)-1)]
            style = ScheduleControllerView.get_style(labelframe, index, task_name, color, 'black')
            frame = Frame(labelframe, bg=BACKGROUND2)
            frame.pack(side=TOP)
            pbar = ttk.Progressbar(frame, style='text.Horizontal.TProgressbar_' + str(index), length=WIDTH-150)
            pbar['value'] = 0
            pbar.pack(pady=6, padx=5, side=LEFT)
            done_button = ScheduleControllerView.add_button(frame, 'DONE', controller_view.done_funcs['btn_done_%s' % str(index)])
            controller_view.done_btns.append(done_button)
            act_button = ScheduleControllerView.add_button(frame, 'START', controller_view.start_pause_funcs['btn_start_pause_%s' % str(index)])
            controller_view.str_pause_btns.append(act_button)            
            controller_view.bars.append(pbar)
            controller_view.bar_styles.append(style)    
            index += 1                            


scv = ScheduleControllerView(s)
ScheduleControllerView.create_start_pause_handlers(scv)
ScheduleControllerView.create_done_handlers(scv)
ScheduleControllerView.create_main_panel(scv)

ScheduleControllerView.refresh() 

root.mainloop()

