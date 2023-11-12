from app import *

from app.UI.tooltip import ToolTip

class HomePage(Frame):
    def __init__(self, master):

        self.app = master

        super().__init__(master, fg_color=BRAND_PRIMARY_DK, bg_color=BACKGROUND_2, corner_radius=10, width=self.app.width - 5, height=self.app.height - 112)
        self.propagate(False)

        #Date
        date_label = Button(
            self,
            textvariable = self.app.date,
            font=H2,
            fg_color=BRAND_PRIMARY_DK,
            hover_color=BRAND_PRIMARY,
            text_color='pink',
            width=100,
            command=self.app.open_stats_page
        )
        date_label.pack(side='top', fill='x', pady=2, padx=5)
        ttp = ToolTip(
            self.app, 
            date_label, 
            BACKGROUND,
            [
                ['Today', ('Calibri', 17), 'white'],
                ['Open Stats', ('Calibri', 16), 'grey'],
            ],
            offset_y=-40, offset_x= self.app.settings.get('tooltip_x_offset')
        )
        
        #? >> UI | Total Keys Pressed
        total_frame = Frame(self, fg_color=BRAND_PRIMARY_DK)
        total_frame.pack(side='top', fill='x', pady=(2, 5), padx=2)

        total_keys_label = Entry(
            total_frame,
            textvariable=self.app.total_keys_pressed,
            corner_radius=100,
            width=400,
            height=20,
            fg_color=BRAND_PRIMARY_DK,
            border_color=BRAND_PRIMARY_DK,
            font=COUNT,
            text_color=BACKGROUND_3,
            justify='center'
        )
        total_keys_label.pack(side='top', fill='x', pady=(5,1), padx=10)
        total_keys_label.configure(state='disabled')
        ttp = ToolTip(
            self.app, 
            total_keys_label, 
            BACKGROUND,
            [   
                ['Session', ('Calibri', 17), 'white'],
                ['Total Keys', ('Calibri', 17), 'white']
            ],
            offset_y=-35, offset_x= self.app.settings.get('tooltip_x_offset')
        )

        keys_label = Label(
            self,
            text = f"KEYSTROKES",
            font=H4,
            fg_color=BRAND_PRIMARY_DK,
            text_color=BACKGROUND_3,
            width=100,
            justify='center'
        )
        keys_label.place(relx=0.5, rely=0.24, x=-50)

        #? >> UI | Simple Stats
        stats_frame = Frame(self, fg_color=BRAND_PRIMARY_DK, height=75)
        stats_frame.propagate(False)
        stats_frame.pack(side='top', fill='x',  pady=(15,5), padx=2)
        
        #? >> KEYS THIS MIN
        frame = Frame(stats_frame, fg_color=BACKGROUND_3, corner_radius=3, width=100)
        frame.propagate(False)
        frame.pack(side='left', pady=2, padx=6, fill='x')
        _keys_this_min = Entry(
            frame,
            textvariable=self.app.keys_this_min,
            corner_radius=100,
            width=400,
            height=20,
            fg_color=BACKGROUND_3,
            border_color=BACKGROUND_3,
            font=TITLE,
            text_color=BRAND_PRIMARY,
            justify='center'
        )
        _keys_this_min.pack(side='top', fill='x', pady=1, padx=2)
        _keys_this_min.configure(state='disabled')
        _keys_this_min_label = Label(
            frame,
            text = f"KEYS THIS MIN",
            font=H5,
            fg_color=BACKGROUND_3,
            text_color=BRAND_PRIMARY,
            width=100,
            justify='center'
        )
        _keys_this_min_label.pack(side='top', fill='x', padx=2, pady=0)

        #? >> AVG KEYS
        frame2 = Frame(stats_frame, fg_color=BACKGROUND_3, corner_radius=3, width=100)
        frame2.propagate(False)
        frame2.pack(side='left', pady=2, padx=6, fill='x')
        _avg_keys_min = Entry(
            frame2,
            textvariable=self.app.avg_keys_min,
            corner_radius=100,
            width=400,
            height=20,
            fg_color=BACKGROUND_3,
            border_color=BACKGROUND_3,
            font=TITLE,
            text_color=BRAND_PRIMARY,
            justify='center'
        )
        _avg_keys_min.pack(side='top', fill='x', pady=1, padx=2)
        _avg_keys_min.configure(state='disabled')
        _avg_keys_min_label = Label(
            frame2,
            text = f"AVG KEYS/MIN",
            font=H5,
            fg_color=BACKGROUND_3,
            text_color=BRAND_PRIMARY,
            width=100,
            justify='center'
        )
        _avg_keys_min_label.pack(side='top', fill='x', padx=2, pady=0)

        self._avg_min_notify_dot = Frame(frame2, fg_color=BACKGROUND_3, width=6, height=6, corner_radius=100)
        self._avg_min_notify_dot.propagate(False)
        self._avg_min_notify_dot.place(relx=1, rely=0.1, x=-12)

        #? >> AVG KEYS HOUR
        frame3 = Frame(stats_frame, fg_color=BACKGROUND_3, corner_radius=3, width=100)
        frame3.propagate(False)
        frame3.pack(side='left', pady=2, padx=6, fill='x')
        _avg_keys_hour = Entry(
            frame3,
            textvariable=self.app.avg_keys_hour,
            corner_radius=100,
            width=400,
            height=20,
            fg_color=BACKGROUND_3,
            border_color=BACKGROUND_3,
            font=TITLE,
            text_color=BRAND_PRIMARY,
            justify='center'
        )
        _avg_keys_hour.pack(side='top', fill='x', pady=1, padx=2)
        _avg_keys_hour.configure(state='disabled')
        _avg_keys_hour_label = Label(
            frame3,
            text = f"AVG KEYS/HR",
            font=H5,
            fg_color=BACKGROUND_3,
            text_color=BRAND_PRIMARY,
            width=100,
            justify='center'
        )
        _avg_keys_hour_label.pack(side='top', fill='x', padx=2, pady=0)

        self._avg_hr_notify_dot = Frame(frame3, fg_color=BACKGROUND_3, width=6, height=6, corner_radius=100)
        self._avg_hr_notify_dot.propagate(False)
        self._avg_hr_notify_dot.place(relx=1, rely=0.1, x=-12)

        #? >> Unique Keys
        frame4 = Frame(self, fg_color=BACKGROUND_3, corner_radius=3, width=100, height=70)
        frame4.propagate(False)
        frame4.pack(side='top', pady=2, padx=8, fill='x')
        _total_unique = Entry(
            frame4,
            textvariable=self.app.total_unique_keys_pressed,
            corner_radius=100,
            width=self.app.width - 20,
            height=20,
            fg_color=BACKGROUND_3,
            border_color=BACKGROUND_3,
            font=TITLE,
            text_color=BRAND_PRIMARY,
            justify='center'
        )
        _total_unique.pack(side='top', fill='x', pady=1, padx=2)
        _total_unique.configure(state='disabled')
        _total_unique_label = Label(
            frame4,
            text = f"TOTAL UNIQUE KEYS",
            font=H5,
            fg_color=BACKGROUND_3,
            text_color=BRAND_PRIMARY,
            width=100,
            justify='center'
        )
        _total_unique_label.pack(side='top', fill='x', padx=2, pady=0)

        #? >> UI | Simple Stats
        top_keys_frame = Frame(self, fg_color=BRAND_PRIMARY_DK, height=75)
        top_keys_frame.propagate(False)
        top_keys_frame.pack(side='top', fill='x', expand=True,  pady=5, padx=2)
        
        #? >> TOP KEYS
        frame5 = Frame(top_keys_frame, fg_color=BACKGROUND_3, corner_radius=3, width=100)
        frame5.propagate(False)
        frame5.pack(side='left', pady=2, padx=6, fill='x')
        _top_key = Entry(
            frame5,
            textvariable=self.app.top_key,
            corner_radius=100,
            width=400,
            height=20,
            fg_color=BACKGROUND_3,
            border_color=BACKGROUND_3,
            font=TITLE,
            text_color=BRAND_PRIMARY,
            justify='center'
        )
        _top_key.pack(side='top', fill='x', pady=1, padx=2)
        _top_key.configure(state='disabled')
        ttp = ToolTip(
            self.app, 
            _top_key, 
            BACKGROUND,
            [
                [self.app.top_key, ('Calibri', 10), 'white']
            ],
            offset_y=-50, offset_x= self.app.settings.get('tooltip_x_offset')
        )

        _top_key_label = Label(
            frame5,
            text = f"1ST",
            font=H5,
            fg_color=RANK1,
            text_color='black',
            width=100,
            corner_radius=3,
            justify='center'
        )
        _top_key_label.pack(side='top', fill='x', padx=2, pady=0)

        frame6 = Frame(top_keys_frame, fg_color=BACKGROUND_3, corner_radius=3, width=100)
        frame6.propagate(False)
        frame6.pack(side='left', pady=2, padx=6, fill='x')
        _middle_key = Entry(
            frame6,
            textvariable=self.app.middle_key,
            corner_radius=100,
            width=400,
            height=20,
            fg_color=BACKGROUND_3,
            border_color=BACKGROUND_3,
            font=TITLE,
            text_color=BRAND_PRIMARY,
            justify='center'
        )
        _middle_key.pack(side='top', fill='x', pady=1, padx=2)
        _middle_key.configure(state='disabled')
        ttp = ToolTip(
            self.app, 
            _middle_key, 
            BACKGROUND,
            [
                [self.app.middle_key, ('Calibri', 10), 'white']
            ],
            offset_y=-50, offset_x= self.app.settings.get('tooltip_x_offset')
        )

        _middle_key_label = Label(
            frame6,
            text = f"2ND",
            font=H5,
            fg_color=RANK2,
            text_color='black',
            width=100,
            corner_radius=3,
            justify='center'
        )
        _middle_key_label.pack(side='top', fill='x', padx=2, pady=0)

        frame7 = Frame(top_keys_frame, fg_color=BACKGROUND_3, corner_radius=3, width=100)
        frame7.propagate(False)
        frame7.pack(side='left', pady=2, padx=6, fill='x')
        _bottom_key = Entry(
            frame7,
            textvariable=self.app.bottom_key,
            corner_radius=100,
            width=400,
            height=20,
            fg_color=BACKGROUND_3,
            border_color=BACKGROUND_3,
            font=TITLE,
            text_color=BRAND_PRIMARY,
            justify='center'
        )
        _bottom_key.pack(side='top', fill='x', pady=1, padx=2)
        _bottom_key.configure(state='disabled')
        ttp = ToolTip(
            self.app, 
            _bottom_key, 
            BACKGROUND,
            [
                [self.app.bottom_key, ('Calibri', 10), 'white']
            ],
            offset_y=-50, offset_x= self.app.settings.get('tooltip_x_offset')
        )

        _bottom_key_label = Label(
            frame7,
            text = f"3RD",
            font=H5,
            fg_color=RANK3,
            text_color='black',
            width=100,
            corner_radius=3,
            justify='center'
        )
        _bottom_key_label.pack(side='top', fill='x', padx=2, pady=0)
