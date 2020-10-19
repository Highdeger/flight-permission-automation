import tkinter as tk
from tkinter import ttk
import functools
fp = functools.partial


class VerticalScrolledFrame:
    new_row_index = 0
    variables = dict()
    widgets = dict()
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _checkbox_active_fgcolor = '#cc0000'
    _checkbox_active_bgcolor = '#d9d9d9'

    def __init__(self, width, height):

        self.root = tk.Tk()
        pos_x = int((self.root.winfo_screenwidth() - width) / 2)
        pos_y = int((self.root.winfo_screenheight() - height) / 2)
        self.root.geometry('{0:d}x{1:d}+{2:d}+{3:d}'.format(width, height, pos_x, pos_y))

        self.frame = tk.Frame(self.root, bg=self._bgcolor)
        self.frame.config(padx=8, pady=8)
        self.frame.grid(row=0, column=0, sticky=tk.N+tk.S+tk.W+tk.E)

        self.canvas = tk.Canvas(self.frame, bg=self._bgcolor)
        self.canvas.config(width=width - 32, height=height - 60)
        self.canvas.pack(side='left', fill='x')

        self.vscrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.vscrollbar.pack(side='left', fill='y')

        self.container = tk.Frame(self.canvas, bg=self._bgcolor)
        self.container.config(padx=8, pady=8)
        self.container.bind(
            '<Configure>',
            lambda event: self.canvas.configure(scrollregion=self.canvas.bbox('all'))
        )

        self.canvas.create_window((0, 0), window=self.container, anchor='nw')
        self.canvas.configure(yscrollcommand=self.vscrollbar.set)
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))
        self.canvas.configure(highlightthickness=0)

        self.frame_buttons = tk.Frame(self.root, bg=self._bgcolor)
        self.frame_buttons.config(padx=8, pady=8)
        self.frame_buttons.grid(row=1, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

        self.button_next = tk.Button(self.frame_buttons, text='Next')
        self.button_next.configure(bg=self._bgcolor, fg=self._fgcolor)
        # self.button_next.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E)
        self.button_next.pack(side='right')
        f = tk.Frame(self.frame_buttons)
        f.configure(width=16, height=16)
        f.pack(side='right')
        f.configure(bg=self._bgcolor)
        self.button_verify = tk.Button(self.frame_buttons, text='Verify')
        self.button_verify.configure(bg=self._bgcolor, fg=self._fgcolor)
        # self.button_verify.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E)
        self.button_verify.pack(side='right')

        self.canvas.bind('<Enter>', self._bind_to_mousewheel)
        self.canvas.bind('<Leave>', self._unbind_from_mousewheel)

    def add_label(self, text, description=None, font_name='DejaVu Sans', font_size=14, font_type='normal', padx=0, pady=0):
        lbl = tk.Label(self.container, text=text,
                       bg=self._bgcolor, fg=self._fgcolor,
                       font=(font_name, font_size, font_type),
                       padx=padx, pady=pady)
        lbl.grid(row=self.new_row_index, column=0, sticky=tk.N + tk.S + tk.W)
        self.new_row_index += 1
        self.widgets[str(lbl.winfo_id())] = ('label', self.new_row_index - 1, description, lbl)
        return str(lbl.winfo_id()), lbl

    def add_checkbox(self, text, description, command, padx=0, pady=0):
        chb = tk.Checkbutton(self.container, text=text,
                             bg=self._bgcolor, fg=self._fgcolor,
                             activebackground=self._checkbox_active_bgcolor,
                             activeforeground=self._checkbox_active_fgcolor,
                             padx=padx, pady=pady,
                             highlightthickness=0)
        chb.configure(command=fp(command, str(chb.winfo_id())))
        self.variables[str(chb.winfo_id())] = tk.IntVar()
        chb.configure(variable=self.variables[str(chb.winfo_id())])
        chb.grid(row=self.new_row_index, column=0, sticky=tk.N + tk.S + tk.W)
        self.new_row_index += 1
        self.widgets[str(chb.winfo_id())] = ('checkbox', self.new_row_index - 1, description, chb)
        return str(chb.winfo_id()), chb

    def add_radio(self, texts, values, description, command, padx=0, pady=0):
        if len(texts) != len(values):
            raise Exception('texts and values must have same length.')
        radio_list = list()
        var = tk.StringVar()
        for x in range(len(texts)):
            temp = tk.Radiobutton(self.container, text=texts[x], value=values[x],
                                  bg=self._bgcolor, fg=self._fgcolor,
                                  activebackground=self._checkbox_active_bgcolor,
                                  activeforeground=self._checkbox_active_fgcolor,
                                  padx=padx, pady=pady,
                                  highlightthickness=0)
            temp.configure(command=fp(command, str(temp.winfo_id())))
            self.variables[str(temp.winfo_id())] = var
            temp.configure(variable=self.variables[str(temp.winfo_id())])
            temp.grid(row=self.new_row_index, column=0, sticky=tk.N + tk.S + tk.W)
            self.new_row_index += 1
            self.widgets[str(temp.winfo_id())] = ('radio', self.new_row_index - 1, description, temp)
            radio_list.append((str(temp.winfo_id()), temp))
        return radio_list

    def add_entry(self, text, description, padx=0, pady=0):
        f = tk.Frame(self.container, padx=padx, pady=pady)
        f.configure(bg=self._bgcolor)

        lbl = tk.Label(f, text=text+': ',
                       bg=self._bgcolor, fg=self._fgcolor)
        lbl.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W)
        ent = tk.Entry(f,
                       bg=self._bgcolor, fg=self._fgcolor)
        self.variables[str(ent.winfo_id())] = tk.StringVar()
        ent.configure(textvariable=self.variables[str(ent.winfo_id())])
        ent.grid(row=0, column=1, sticky=tk.N + tk.S + tk.E)

        f.grid(row=self.new_row_index, column=0, sticky=tk.N + tk.S + tk.W)
        self.new_row_index += 1
        self.widgets[str(ent.winfo_id())] = ('checkbox', self.new_row_index - 1, description, ent)
        return str(ent.winfo_id()), ent

    def add_spinner(self, text, description, choices, default_index=None, padx=0, pady=0):
        f = tk.Frame(self.container, padx=padx, pady=pady)
        f.configure(bg=self._bgcolor)

        lbl = tk.Label(f, text=text + ': ',
                       bg=self._bgcolor, fg=self._fgcolor)
        lbl.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W)
        spn_var = tk.StringVar()
        if default_index is not None:
            spn_var.set(choices[default_index])
        spn = tk.OptionMenu(f, spn_var, *choices)
        spn.configure(bg=self._bgcolor, fg=self._fgcolor)
        self.variables[str(spn.winfo_id())] = spn_var
        spn.grid(row=0, column=1, sticky=tk.N + tk.S + tk.E)

        f.grid(row=self.new_row_index, column=0, sticky=tk.N + tk.S + tk.W)
        self.new_row_index += 1
        self.widgets[str(spn.winfo_id())] = ('checkbox', self.new_row_index - 1, description, spn)
        return str(spn.winfo_id()), spn

    def add_frame(self, h=20, w=20):
        frm = tk.Frame(self.container)
        frm.configure(height=h, width=w)
        frm.configure(bg=self._bgcolor)
        frm.grid(row=self.new_row_index, column=0, sticky=tk.N + tk.S + tk.W)
        self.new_row_index += 1

    def get_variable(self, widget_id):
        return self.variables[widget_id]

    def get_widget(self, widget_id):
        return self.widgets[widget_id]

    def _on_mousewheel(self, event, scroll):
        self.canvas.yview_scroll(int(scroll), 'units')

    def _bind_to_mousewheel(self, event):
        self.canvas.bind_all('<Button-4>', fp(self._on_mousewheel, scroll=-1))
        self.canvas.bind_all('<Button-5>', fp(self._on_mousewheel, scroll=1))

    def _unbind_from_mousewheel(self, event):
        self.canvas.unbind_all('<Button-4>')
        self.canvas.unbind_all('<Button-5>')


class SplashFrame:
    def __init__(self, width, height):
        self.root = tk.Tk()
        pos_x = int((self.root.winfo_screenwidth() - width) / 2)
        pos_y = int((self.root.winfo_screenheight() - height) / 2)
        self.root.geometry('{0:d}x{1:d}+{2:d}+{3:d}'.format(width, height, pos_x, pos_y))

        self.frame = tk.Frame(self.root)
        self.frame.config(padx=48, pady=48)
        self.frame.pack(side='top', fill='both')

        self.label_title = tk.Label(self.frame, text='Welcome')
        self.label_title.configure(font=('DejaVu Sans', 36, 'normal'))
        self.label_title.pack(side='top')

        self.label_subtitle = tk.Label(self.frame, text='UAS Operation Procedures')
        self.label_subtitle.configure(font=('DejaVu Sans', 22, 'normal'))
        self.label_subtitle.pack(side='top')

        f = tk.Frame(self.frame)
        f.configure(width=50, heigh=50)
        f.pack(side='top')

        self.button_start = tk.Button(self.frame, text='Start')
        self.button_start.pack(side='top')
        self.button_start.configure(command=self.close_window)

    def close_window(self):
        self.root.destroy()
