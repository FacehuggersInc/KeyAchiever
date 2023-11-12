from app import *

from app.UI.tooltip import ToolTip
from app.UI.switch import LabeledSwitch

class SettingsPage(Frame):
    def __init__(self, master):

        self.app = master

        super().__init__(
            master,
            fg_color=BACKGROUND_2, 
            corner_radius=0, 
            width=self.app.width - 5, 
            height=self.app.height, 
        )
        self.propagate(False)

        settings_title= Label(
            self,
            text= 'Settings',
            font=H2,
            fg_color=BACKGROUND_2,
            text_color='white',
            width=100,
            corner_radius=5
        )
        settings_title.pack(side='top', fill='x', pady=(5,8), padx=5)

        #Topmost Setting
        self.topmost_switch = LabeledSwitch(
            self,
            'Pin on Top',
            H3,
            BACKGROUND_2,
            BACKGROUND,
            BRAND_PRIMARY_DK,
            BRAND_PRIMARY, 
            'white'
        )
        self.topmost_switch.pack(side='top', fill='x', padx=5, pady=2)
        if self.app.settings['topmost'] == True:
            self.topmost_switch.force_toggle('on')

        self.starthidden_switch = LabeledSwitch(
            self,
            'Start in System Tray',
            H3,
            BACKGROUND_2,
            BACKGROUND,
            BRAND_PRIMARY_DK,
            BRAND_PRIMARY, 
            'white'
        )
        self.starthidden_switch.pack(side='top', fill='x', padx=5, pady=2)
        if self.app.settings['start_hidden'] == True:
            self.starthidden_switch.force_toggle('on')

        #Start of the week
        sow_frame = Frame(self, fg_color=BACKGROUND_2, corner_radius=5)
        sow_frame.pack(side='top', fill='x', padx=5, pady=2)

        sow_label = Label(sow_frame, text='Start of Week', font=H3, fg_color=BACKGROUND_2)
        sow_label.pack(side='left', padx=5, pady=2)

        self.start_of_week = tk.StringVar()
        self.start_of_week.set(self.app.settings['start_of_week'])
        start_of_week_entry = Entry(sow_frame, textvariable=self.start_of_week, font=H3, fg_color=BRAND_PRIMARY_DK, border_color=BRAND_PRIMARY_DK, corner_radius=5, width=55, height=30)
        start_of_week_entry.pack(side='right', padx=2, pady=2)

        #Tooltip Offset X
        ttp_offset_frame = Frame(self, fg_color=BACKGROUND_2, corner_radius=5)
        ttp_offset_frame.pack(side='top', fill='x', padx=5, pady=(2,0))

        ttp_offset_label = Label(ttp_offset_frame, text='Tooltip Offset X', font=H3, fg_color=BACKGROUND_2)
        ttp_offset_label.pack(side='left', padx=5, pady=2)

        self.ttp_offset_x = tk.StringVar()
        self.ttp_offset_x.set(self.app.settings['tooltip_x_offset'])
        ttp_offset_x_entry = Entry(ttp_offset_frame, textvariable=self.ttp_offset_x, font=H3, fg_color=BRAND_PRIMARY_DK, border_color=BRAND_PRIMARY_DK, corner_radius=5, width=55, height=30)
        ttp_offset_x_entry.pack(side='right', padx=2, pady=2)

        ttp_offset_note = Label(self, text='* Offset requires Restart after SAVE', font=('Calibri', 16, 'italic'), fg_color=BACKGROUND_2, anchor='w')
        ttp_offset_note.pack(side='top', padx=5, pady=2, fill='x')

        self.save_btn = Button(self, text='SAVE', font=H2, fg_color=BRAND_PRIMARY_DK, hover_color=BRAND_PRIMARY, command=self.save)
        self.save_btn.pack(side='bottom', padx=20, pady=10)

        #Home Btn
        home_btn = Button(
            self, 
            text = '',
            width=20, height=20,
            fg_color=BACKGROUND_2,
            bg_color=BACKGROUND_2,
            hover_color=BRAND_PRIMARY,
            image=ICONS[1],
            command= self.app.close_settings_page
        )
        home_btn.place(relx=1, rely=0, x=-45, y=5)
        home_btn.lift()
        ttp = ToolTip(
            self.app, 
            home_btn, 
            BACKGROUND,
            [
                ['Home', ('Calibri', 17), 'white'],
            ],
            offset_y=35, offset_x= self.app.settings.get('tooltip_x_offset')
        )

        app_ver = Label(
            self, 
            text = f'v{APP_VERSION}',
            font=('Calibri', 12, 'italic'),
            text_color='grey',
            width=20, height=20,
            fg_color=BACKGROUND_2,
            bg_color=BACKGROUND_2,
        )
        app_ver.place(relx=1, rely=1, x=-35, y=-30)

    def set_start_of_week(self, event=None):
        value = self.start_of_week.get()
        days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
        if len(value) == 3 and value in days:
            self.app.settings['start_of_week'] = value.lower()
        else:
            self.start_of_week.set(days[0])

    def set_offset_x(self, event=None):
        value = int(self.ttp_offset_x.get())
        if value:
            self.app.settings['tooltip_x_offset'] = value
        else:
            self.ttp_offset_x.set('0')

    def set_topmost(self):
        topmost = None
        if self.topmost_switch.get() == 'on':
            topmost = True
        else:
            topmost = False
        self.app.attributes('-topmost', topmost)
        self.app.settings['topmost'] = topmost

    def set_start_hidden(self):
        hidden = None
        if self.starthidden_switch.get() == 'on':
            hidden = True
        else:
            hidden = False
        self.app.settings['start_hidden'] = hidden

    def save(self):
        self.set_start_of_week()
        self.set_offset_x()
        self.set_topmost()
        self.set_start_hidden()
        self.app.close_settings_page()