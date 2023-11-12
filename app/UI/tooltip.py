from app import *

class ToolTip(object):
    """
    create a tooltip for a given widget
    * lines format = [text:str, font:tuple, color:str, padx:int=4, pady=2]
    * NOTE: padx and y are optional but both are required when one is used
    """
    def __init__(self, app, widget, fg_color:str, lines:list, waittime:int = 350, offset_x = 0, offset_y = 18):
        self.waittime = waittime     #miliseconds
        self.widget = widget
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)

        self.id = None
        self.app = app
        self._frame = None
        self._tooltip_shown = False

        self.color = fg_color
        self.lines = lines
        self.offset_y = offset_y
        self.offset_x = offset_x

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hide_tooltip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.show_tooltip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def show_tooltip(self, event=None):
        self._tooltip_shown = True
        #Window
        self._frame = Frame(
            self.app,
            width=100, height=45,
            fg_color=self.color, 
            corner_radius=0
        )
        self._frame.propagate(False)

        #ToolTip
        for line in self.lines:
            text = line[0]
            font = line[1]
            color = line[2]
            px, py = (4, 1)
            if len(line) > 3:
                px = line[3]
                py = line[4]

            if type(text) == str:
                label = Label(
                    self._frame,
                    height=0,
                    text=text,
                    font=font,
                    text_color=color,
                    justify='center',
                    fg_color=self.color
                )
                label.pack(side='top', fill='x', expand=True, padx=px, pady=py)
            else:
                label = Label(
                    self._frame,
                    height=0,
                    textvariable=text,
                    font=font,
                    text_color=color,
                    justify='center',
                    fg_color=self.color
                )
                label.pack(side='top', fill='x', expand=True, padx=px, pady=py)

        self._frame.place(in_=self.widget, x=((self.widget.winfo_width() // 2) - 50) + self.offset_x, y=self.offset_y)

    def hide_tooltip(self, event=None):
        tw = self._frame
        self._frame = None
        if tw:
            tw.destroy()
        self._tooltip_shown = False