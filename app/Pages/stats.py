from app import *

from app.UI.tooltip import ToolTip

class StatsPage(Frame):
    def __init__(self, master):

        self.app = master

        super().__init__(
            master,
            fg_color=BRAND_PRIMARY_DK, 
            bg_color=BACKGROUND_2, 
            corner_radius=10, 
            width=self.app.width - 5, 
            height=self.app.height - 112, 
        )
        self.propagate(False)
        
        #STATS HEADER
        stats_title= Label(
            self,
            text= 'Stats',
            font=H2,
            fg_color=BRAND_PRIMARY_DK,
            text_color='pink',
            width=100,
        )
        stats_title.pack(side='top', fill='x', pady=(10,4), padx=5)

        #STATS WEEKLY
        self.day_bars = {}
        self.key_totals = {}
        self.week_frame = Frame(self, fg_color=BACKGROUND_3, corner_radius=5)
        self.week_frame.pack(side='top', fill='both', expand=True, pady=2, padx=2)

        #SUNDAY
        sun_keys = tk.StringVar()
        sun_frame = Frame(self.week_frame, fg_color=BACKGROUND_3)
        sun_frame.pack(side='left', padx=2, pady=1, fill='both', expand=True)

        sun_label = Label(sun_frame, text='SUN', font=H4, text_color='white', justify='center')
        sun_label.pack(side='bottom', fill='x', pady=(1, 5), padx=2)

        sun_bar = Frame(sun_frame, fg_color='grey', width=35, height=2, corner_radius=2)
        sun_bar.propagate(False)
        sun_bar.pack(side='bottom')
        self.day_bars['sun'] = sun_bar
        
        self.key_totals['sun'] = sun_keys
        ttp = ToolTip(
            self.app,
            sun_bar,
            BACKGROUND,
            [
                [sun_keys, ('Calbri', 17, 'italic', 'bold'), 'white']
            ],
            offset_y=-50, waittime = 150, offset_x= self.app.settings.get('tooltip_x_offset')
        )

        #MONDAY
        mon_keys = tk.StringVar()
        mon_frame = Frame(self.week_frame, fg_color=BACKGROUND_3)
        mon_frame.pack(side='left', padx=2, pady=1, fill='both', expand=True)

        mon_label = Label(mon_frame, text='MON', font=H4, text_color='white', justify='center')
        mon_label.pack(side='bottom', fill='x', pady=(1, 5), padx=2)

        mon_bar = Frame(mon_frame, fg_color='grey', width=35, height=2, corner_radius=2)
        mon_bar.propagate(False)
        mon_bar.pack(side='bottom')
        self.day_bars['mon'] = mon_bar

        self.key_totals['mon'] = mon_keys
        ttp = ToolTip(
            self.app,
            mon_bar,
            BACKGROUND,
            [
                [mon_keys, ('Calbri', 17, 'italic', 'bold'), 'white']
            ],
            offset_y=-50, waittime = 150, offset_x= self.app.settings.get('tooltip_x_offset')
        )

        #TUESDAY
        tue_keys = tk.StringVar()
        tue_frame = Frame(self.week_frame, fg_color=BACKGROUND_3)
        tue_frame.pack(side='left', padx=2, pady=1, fill='both', expand=True)

        tue_label = Label(tue_frame, text='TUE', font=H4, text_color='white', justify='center')
        tue_label.pack(side='bottom', fill='x', pady=(1, 5), padx=2)

        tue_bar = Frame(tue_frame, fg_color='grey', width=35, height=2, corner_radius=2)
        tue_bar.propagate(False)
        tue_bar.pack(side='bottom')
        self.day_bars['tue'] = tue_bar

        self.key_totals['tue'] = tue_keys
        ttp = ToolTip(
            self.app,
            tue_bar,
            BACKGROUND,
            [
                [tue_keys, ('Calbri', 17, 'italic', 'bold'), 'white']
            ],
            offset_y=-50, waittime = 150, offset_x= self.app.settings.get('tooltip_x_offset')
        )
        
        #WEDNESDAY
        wed_keys = tk.StringVar()
        wed_frame = Frame(self.week_frame, fg_color=BACKGROUND_3)
        wed_frame.pack(side='left', padx=2, pady=1, fill='both', expand=True)

        wed_label = Label(wed_frame, text='WED', font=H4, text_color='white', justify='center')
        wed_label.pack(side='bottom', fill='x', pady=(1, 5), padx=2)

        wed_bar = Frame(wed_frame, fg_color='grey', width=35, height=2, corner_radius=2)
        wed_bar.propagate(False)
        wed_bar.pack(side='bottom')
        self.day_bars['wed'] = wed_bar

        self.key_totals['wed'] = wed_keys
        ttp = ToolTip(
            self.app,
            wed_bar,
            BACKGROUND,
            [
                [wed_keys, ('Calbri', 17, 'italic', 'bold'), 'white']
            ],
            offset_y=-50, waittime = 150, offset_x= self.app.settings.get('tooltip_x_offset')
        )

        #THURSDAY
        thu_keys = tk.StringVar()
        thu_frame = Frame(self.week_frame, fg_color=BACKGROUND_3)
        thu_frame.pack(side='left', padx=2, pady=1, fill='both', expand=True)

        thu_label = Label(thu_frame, text='THU', font=H4, text_color='white', justify='center')
        thu_label.pack(side='bottom', fill='x', pady=(1, 5), padx=2)

        thu_bar = Frame(thu_frame, fg_color='grey', width=35, height=2, corner_radius=2)
        thu_bar.propagate(False)
        thu_bar.pack(side='bottom')
        self.day_bars['thu'] = thu_bar

        self.key_totals['thu'] = thu_keys
        ttp = ToolTip(
            self.app,
            thu_bar,
            BACKGROUND,
            [
                [thu_keys, ('Calbri', 17, 'italic', 'bold'), 'white']
            ],
            offset_y=-50, waittime = 150, offset_x= self.app.settings.get('tooltip_x_offset')
        )

        #FRIDAY
        fri_keys = tk.StringVar()
        fri_frame = Frame(self.week_frame, fg_color=BACKGROUND_3)
        fri_frame.pack(side='left', padx=2, pady=1, fill='both', expand=True)

        fri_label = Label(fri_frame, text='FRI', font=H4, text_color='white', justify='center')
        fri_label.pack(side='bottom', fill='x', pady=(1, 5), padx=2)

        fri_bar = Frame(fri_frame, fg_color='grey', width=35, height=2, corner_radius=2)
        fri_bar.propagate(False)
        fri_bar.pack(side='bottom')
        self.day_bars['fri'] = fri_bar

        self.key_totals['fri'] = fri_keys
        ttp = ToolTip(
            self.app,
            fri_bar,
            BACKGROUND,
            [
                [fri_keys, ('Calbri', 17, 'italic', 'bold'), 'white']
            ],
            offset_y=-50, waittime = 150, offset_x= self.app.settings.get('tooltip_x_offset')
        )

        #SATURDAY
        sat_keys = tk.StringVar()
        sat_frame = Frame(self.week_frame, fg_color=BACKGROUND_3)
        sat_frame.pack(side='left', padx=2, pady=1, fill='both', expand=True)

        sat_label = Label(sat_frame, text='SAT', font=H4, text_color='white', justify='center')
        sat_label.pack(side='bottom', fill='x', pady=(1, 5), padx=2)

        sat_bar = Frame(sat_frame, fg_color='grey', width=35, height=2, corner_radius=2)
        sat_bar.propagate(False)
        sat_bar.pack(side='bottom')
        self.day_bars['sat'] = sat_bar

        self.key_totals['sat'] = sat_keys
        ttp = ToolTip(
            self.app,
            sat_bar,
            BACKGROUND,
            [
                [sat_keys, ('Calbri', 17, 'italic', 'bold'), 'white']
            ],
            offset_y=-50, waittime = 150, offset_x= self.app.settings.get('tooltip_x_offset')
        )

        #SET BARS HEIGHT
        today = self.app.get_time(f'%a').lower()
        if self.app.stats.get('weekly'):
            for day in self.day_bars:
                self.key_totals[day].set(f'{self.app.stats["weekly"][day]:,}')
                day_num = 2 + ( int(self.key_totals[day].get().replace(',','')) // 250)
                self.day_bars[day].configure(height=day_num)
                if day == today:
                    self.day_bars[day].configure(fg_color=BRAND_PRIMARY)
                else:
                    self.day_bars[day].configure(fg_color='grey')

        #STATS TOTAL KEYS
        self.total_keys_alltime = tk.StringVar()
        total_keys_alltime_frame = Frame(self, fg_color=BACKGROUND_3, corner_radius=3, width=100, height=70)
        total_keys_alltime_frame.propagate(False)
        total_keys_alltime_frame.pack(side='top', pady=5, padx=2, fill='x')
        _total = Entry(
            total_keys_alltime_frame,
            textvariable=self.total_keys_alltime,
            corner_radius=100,
            width=self.app.width - 20,
            height=20,
            fg_color=BACKGROUND_3,
            border_color=BACKGROUND_3,
            font=TITLE,
            text_color=BRAND_PRIMARY,
            justify='center'
        )
        _total.pack(side='top', fill='x', pady=1, padx=2)
        _total.configure(state='disabled')
        _total_label = Label(
            total_keys_alltime_frame,
            text = f"TOTAL KEYS ALL-TIME",
            font=H5,
            fg_color=BACKGROUND_3,
            text_color=BRAND_PRIMARY,
            width=100,
            justify='center'
        )
        _total_label.pack(side='top', fill='x', padx=2, pady=0)

        #Home Btn
        home_btn = Button(
            self, 
            text = '',
            width=20, height=20,
            fg_color=BRAND_PRIMARY_DK,
            bg_color=BRAND_PRIMARY_DK,
            hover_color=BRAND_PRIMARY,
            image=ICONS[1],
            command= self.app.close_stats_page
        )
        home_btn.place(relx=0, rely=0, x=5, y=5)
        home_btn.lift()
        ttp = ToolTip(
            self.app, 
            home_btn, 
            BACKGROUND,
            [
                ['Home', ('Calibri', 17), 'white'],
            ],
            offset_y=-40, offset_x= self.app.settings.get('tooltip_x_offset')
        )