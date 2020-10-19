import tkinter as tk
from util.Gui import VerticalScrolledFrame, SplashFrame
from json import dumps
from time import sleep
import functools
fp = functools.partial


f_width = 760
f_height = 430
result_dict = dict()


def toggler(widget_id):
    var = win.get_variable(widget_id).get()
    desc = win.get_widget(widget_id)[2]
    result_dict[desc] = var
    log_result()
    print(result_dict)


def log_result():
    json = dumps(result_dict)
    with open('log.txt', 'w') as f:
        f.write(json)
        f.close()


def draw_scrollable_form(win):
    win.add_label('Mission Registration', font_size=24)

    win.add_frame(40)
    win.add_label('Mission Scope')
    win.add_radio(['Project (Internal)', 'Project (External)',
                   'Education (Workshop)', 'Education (Creative Inquiry)', 'Education (Others)',
                   'Training'],
                  ['project-internal', 'project-external',
                   'education-workshop', 'education-creative-inquiry', 'education-others',
                   'training'],
                  'mission-scope', toggler, padx=64)

    win.add_frame()
    win.add_label('Equipment')
    equipments = ['Equipment 1', 'Equipment 2', 'Equipment 3', 'Equipment 4', 'Equipment 5', 'Equipment 6',
                  'Equipment 7', 'Equipment 8', 'Equipment 9', 'Equipment 10', 'Equipment 11', 'Equipment 12']
    for equip in equipments:
        win.add_checkbox(equip, equip.lower().replace(' ', '-'), toggler, padx=64)

    win.add_frame()
    win.add_label('Crew Members')
    t = 'Member 1'
    e1 = win.add_entry(t, t.lower().replace(' ', '-'), padx=64)
    v = win.get_variable(e1[0])
    v.trace('w', lambda name, index, mode: toggler(e1[0]))
    t = 'Member 2'
    e2 = win.add_entry(t, t.lower().replace(' ', '-'), padx=64)
    v = win.get_variable(e2[0])
    v.trace('w', lambda name, index, mode: toggler(e2[0]))
    t = 'Member 3'
    e3 = win.add_entry(t, t.lower().replace(' ', '-'), padx=64)
    v = win.get_variable(e3[0])
    v.trace('w', lambda name, index, mode: toggler(e3[0]))

    win.add_frame()
    win.add_label('Flight Location/Area')
    s1 = win.add_spinner('Airspace', 'airspace',
                         ['A', 'B', 'C', 'D', 'E', 'G'], padx=64)

    win.root.mainloop()


if __name__ == '__main__':

    splash = SplashFrame(f_width, f_height)
    splash.root.mainloop()

    win = VerticalScrolledFrame(f_width, f_height)
    draw_scrollable_form(win)
