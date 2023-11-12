from app import *

class LabeledSwitch(Frame):
    def __init__(
        self,
        master,
        text:str,
        font:tuple,
        fg_color:str,
        switch_fg_color_off:str,
        switch_fg_color_on:str,
        switch_btn_color:str,
        switch_btn_hover:str,
        switch_on_side:str = 'right',
        command=None
    ):
        #Init
        super().__init__(master, fg_color=fg_color, corner_radius=5)

        self.switch_state = tk.StringVar()
        self.switch_state.set('off')
        self._text = text
        self._font = font
        self._off_color = switch_fg_color_off
        self._on_color = switch_fg_color_on
        self.cmd = command
        if self.cmd == None:
            self.cmd = self.dummy

        if switch_on_side == 'left':
            label_on_side = 'right'
        else:
            label_on_side = 'left'

        _label = Label(self, text=self._text, font=self._font, fg_color=fg_color)
        _label.pack(side=label_on_side, padx=5, pady=2)

        self._switch_frame = Frame(self, fg_color=self._off_color, corner_radius=5, width=55, height=30)
        self._switch_frame.propagate(False)
        self._switch_frame.pack(side=switch_on_side, padx=2, pady=2)

        self.btn_pos_x = 4
        self.btn_animating = False
        self._switch_btn = Button(
            self._switch_frame,
            text='',
            fg_color=switch_btn_color,
            hover_color=switch_btn_hover,
            width=22, height=22, 
            corner_radius=5,
            command=self._switch
        )
        self._switch_btn.place(relx=0, rely=0, x=5, y=4)

    def _switch_visual_state_on(self):
        self.btn_pos_x += 5
        self._switch_btn.place(relx=0, rely=0, x=5 + self.btn_pos_x, y=4)
        if not self.btn_pos_x >= 20:
            self.btn_animating = True
            self.after(10, self._switch_visual_state_on)
        else:
            self._switch_frame.configure(fg_color=self._on_color)
            self.btn_animating = False

    def _switch_visual_state_off(self):
        self.btn_pos_x -= 5
        self._switch_btn.place(relx=0, rely=0, x=5 + self.btn_pos_x, y=4)
        if not self.btn_pos_x <= 0:
            self.btn_animating = True
            self.after(10, self._switch_visual_state_off)
        else:
            self._switch_frame.configure(fg_color=self._off_color)
            self.btn_animating = False

    def _switch(self, state=None):
        if not self.btn_animating:
            if not state: state = self.switch_state.get()

            if state == 'off':
                self.switch_state.set('on')
                if not self.btn_pos_x >= 20: self._switch_visual_state_on()
            else:
                self.switch_state.set('off')
                if not self.btn_pos_x <= 4: self._switch_visual_state_off()
            if self.cmd: self.cmd()

    def get(self):
        return self.switch_state.get()
    
    def set(self, var:str):
        self.switch_state.set(var)

    def force_toggle(self, state:str):
        if state == 'on':
            self._switch_visual_state_on()
            self.set('on')
        elif state == 'off':
            self._switch_visual_state_off()
            self.set('off')
    
    def dummy(self):
        pass