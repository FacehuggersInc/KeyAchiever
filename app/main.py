
from app import *
from app.UI.tooltip import ToolTip
from app.Pages.home import HomePage
from app.Pages.stats import StatsPage
from app.Pages.settings import SettingsPage

class KeyAchiever(CTk):
    def __init__(self):
        #? >> INIT
        super().__init__(fg_color=BACKGROUND_2)
        self.title(APP_NAME)
        self.protocol('WM_DELETE_WINDOW', self.quit_app)

        #Load Settings
        self.settings = {
            'topmost':False,
            'start_hidden':False,
            'start_of_week': 'sun',
            'tooltip_x_offset': 0,
        }
        if os.path.exists('Data\\achieve_settings.json'):
            with open('Data\\achieve_settings.json', 'r') as json_file:
                self.settings = json.load(json_file)

        #Size and Position
        self.width = 350
        self.s_width = self.winfo_screenwidth()

        self.height = 490
        self.s_height = self.winfo_screenheight()
        
        #If Last Pos
        if self.settings.get('last_win_pos'):
            pos = self.settings.get('last_win_pos')
            self.geometry(f'{self.width}x{self.height}+{pos[0]}+{pos[1]}')
        else:
            self.CENTER_POSITION = (
                (self.s_width // 2) - (self.width // 2),
                (self.s_height // 2) - (self.height // 2)
            )
            self.geometry(f'{self.width}x{self.height}+{self.CENTER_POSITION[0]}+{self.CENTER_POSITION[1]}')
        
        self.resizable(False, False)
        self.minsize(self.width, self.height)

        #Title bar Color
        HWND = windll.user32.GetParent(self.winfo_id())
        windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref( c_int(int(BACKGROUND_2.replace('#',''), 16)) ), sizeof(c_int))

        #Title Bar Icon
        self.iconbitmap(default='Icons\\keycap.ico')

        #App Vars
        self.USER_ACTIVE = False
        self.LAST_USER_ACTIVE_TIME = None

        self.VISIBLE = True
        self.ICON = None

        #? >> UI | HEADER
        header = Frame(self, fg_color=BACKGROUND_2, corner_radius=0)
        header.pack(side='top', fill='x', pady=(5,0))
        self.APP_ICON = Button(
            header,
            text = '',
            image=ICONS[0],
            width=25,
            corner_radius=100,
            fg_color=BACKGROUND_2,
            hover_color=BRAND_PRIMARY,
            command=self.manual_reset
        )
        self.APP_ICON.propagate(False)
        self.APP_ICON.pack(side='top')
        ttp = ToolTip(
            self, 
            self.APP_ICON, 
            BACKGROUND,
            [
                ['RESET', ('Calibri', 17), 'red'],
                ['Today\'s Stats', ('Calibri', 17), 'red'],
            ],
            offset_y=75, offset_x= self.settings.get('tooltip_x_offset')
            
        )

        LOGO = Label(
            header,
            text = f'{APP_NAME}',
            font=TITLE,
            text_color='pink',
            width=100,
            justify='center',
        )
        LOGO.pack(side='top', fill='x', pady=(2,5))

        #Home Btn
        self.settings_btn = Button(
            self, 
            text = '',
            width=20, height=20,
            fg_color=BACKGROUND_2,
            bg_color=BACKGROUND_2,
            hover_color=BRAND_PRIMARY,
            image=ICONS[2],
            command= self.open_settings_page
        )
        self.settings_btn.place(relx=1, rely=0, x=-45, y=5)

        #? >> APP
        #DATE
        self.today =  self.get_time(f'%a').lower()
        self.date = tk.StringVar()
        self.date.set(f"Today, {self.get_time(f'%A')}")
        
        #LOAD DATA
        self.week_to_be_reset = False
        self.stats = {
            'total_keys':0,
            'total_unique_keys':0,
            'highest_avg_min': 0,
            'highest_avg_hour': 0,
            'highest_avg_week':0,
            'highest_week_total':0,
            'weekly': {'sun':0, 'mon':0, 'tue':0, 'wed':0, 'thu':0, 'fri':0, 'sat':0},
        }
        if os.path.exists('Data\\achieve_stats.json'):
            with open('Data\\achieve_stats.json', 'r') as json_file:
                self.stats = json.load(json_file)

        #TOTALS
        self.total_unique_keys_pressed = tk.StringVar()
        self.total_unique_keys_pressed.set(0)

        self.total_keys_pressed = tk.StringVar()
        self.total_keys_pressed.set(0)

        #AVGS
        self.keys_this_min = tk.StringVar()
        self.keys_this_min.set(0)

        self.highest_avg_min = 0
        self.avg_keys_min = tk.StringVar()
        self.avg_keys_min.set(0)

        self.highest_avg_hour = 0
        self.avg_keys_hour = tk.StringVar()
        self.avg_keys_hour.set(0)

        #TOP KEYS
        self.top_key = tk.StringVar()
        self.middle_key = tk.StringVar()
        self.bottom_key = tk.StringVar()

        #KEYS
        self.keys = {}
        self.recent_key = tk.StringVar()
        self.last_time = None
        self.all_keystrokes_per_min = []
        self.keys_per_min = []

        #PAGES
        self.home_page = HomePage(self)
        self.home_page.pack(side='top', fill='both', expand=True, pady=5, padx=5)

        self.stats_page_pos = 0
        self.stats_page_animating = False
        self.stats_page = StatsPage(self)
        self.stats_page.place(relx=0, rely=1)

        self.settings_page_pos = -self.height
        self.settings_page_animating = False
        self.settings_page = SettingsPage(self)
        self.settings_page.place(relx=0, rely=0, x=2.5, y=-self.height)

    ##LISTENER
    def on_press(self, key):
        """Listener Key pressed"""
        self.USER_ACTIVE = True
        self.LAST_USER_ACTIVE_TIME = self.get_time(f'%m %d %H %M')

        total = int( self.total_keys_pressed.get().replace(',','') ) + 1
        self.total_keys_pressed.set( f'{total:,}' )
        self.keys_this_min.set( int(self.keys_this_min.get()) + 1 )

        key = str(key).replace("'","").strip()
        if 'KeyCode' in key:
            key = key.split('.')[1].strip()
        if 'Key' in key:
            key = key.split('.')[1].strip()

        key_exists = self.keys.get(key)
        if not key_exists:
            self.keys[key] = 1
        else:
            self.keys[key] += 1

        sorted_keys = sorted(self.keys.items(), key=lambda item: item[1], reverse=True)

        if not self.recent_key.get() == key and not key in [k[0] for k in sorted_keys[:8]]:
            self.total_unique_keys_pressed.set( int(self.total_unique_keys_pressed.get()) + 1 )

        if len(sorted_keys) >= 3:
            self.top_key.set(sorted_keys[0][0])
            self.middle_key.set(sorted_keys[1][0])
            self.bottom_key.set(sorted_keys[2][0])

        del sorted_keys

        self.recent_key.set(key)

    ##PAGES
    #Settings
    def close_settings_animation(self):
        self.settings_page_animating = True
        self.settings_page_pos -= 12
        self.settings_page.place(relx=0, rely=0, x=2.5, y=self.settings_page_pos)
        if not self.settings_page_pos <= -(self.height): 
            self.after(10, self.close_settings_animation)
        else:
            self.settings_page_animating = False
            self.settings_page_pos = -(self.height)
    def close_settings_page(self):
        if not self.settings_page_animating:
            self.close_settings_animation()

    def open_settings_animation(self):
        self.settings_page_animating = True
        self.settings_page_pos += 12
        self.settings_page.place(relx=0, rely=0, x=2.5, y=self.settings_page_pos)
        if not self.settings_page_pos >= 0: 
            self.after(10, self.open_settings_animation)
        else:
            self.settings_page_animating = False
            self.settings_page_pos = 0
    def open_settings_page(self):
        if not self.settings_page_animating:
            self.open_settings_animation()

    #stats
    def close_page_animation(self):
        self.stats_page_animating = True
        self.stats_page_pos -= 12
        self.stats_page.place(relx=0, rely=1, x=2.5, y=-(self.stats_page_pos))
        if not self.stats_page_pos <= 0: 
            self.after(10, self.close_page_animation)
        else:
            self.stats_page_animating = False
    def close_stats_page(self):
        if not self.stats_page_animating:
            self.close_page_animation()
    
    def open_page_animation(self):
        self.stats_page_animating = True
        self.stats_page_pos += 12
        self.stats_page.place(relx=0, rely=1, x=2.5, y=-(self.stats_page_pos))
        if not self.stats_page_pos >= 375: 
            self.after(10, self.open_page_animation)
        else:
            self.stats_page_animating = False
    def open_stats_page(self):
        if not self.stats_page_animating:
            #Reset Week Bars
            if self.week_to_be_reset:
                self.week_to_be_reset = False
                for day in self.stats_page.day_bars:
                    self.stats_page.key_totals[day].set(f'0')
                    day_num = 2
                    self.stats_page.day_bars[day].configure(height=day_num)

            #Update Stats
            temp_all_keys = int(self.stats['total_keys']) + int(self.total_keys_pressed.get().replace(',',''))
            self.stats_page.total_keys_alltime.set(f'{temp_all_keys:,}')

            temp_weekly = self.stats['weekly'][self.today] + int(self.total_keys_pressed.get().replace(',',''))
            if self.stats.get('weekly'):
                for day in self.stats_page.day_bars:
                    if day == self.today:
                        self.stats_page.key_totals[day].set(f'{temp_weekly:,}')
                        day_num = 2 + (temp_weekly // 250)
                        self.stats_page.day_bars[day].configure(height=day_num)
                    if day == self.today:
                        self.stats_page.day_bars[day].configure(fg_color=BRAND_PRIMARY)
                    else:
                        self.stats_page.day_bars[day].configure(fg_color='grey')

            self.open_page_animation()

    ##APP
    #Main
    def update(self):
        #Check Visibility and Iconify if not visible
        if self.INITIAL_UPDATE: #once the app updates once
            if not self.winfo_viewable() and not self.ICON:
                self.toggle_window()

        #Update ICON Title
        if self.ICON:
            self.ICON._title = f'{self.total_keys_pressed.get()} keys | {APP_NAME} v{APP_VERSION} '
            self.ICON._update_title()

        #Reset Week Totals
        if self.settings.get('start_of_week') == self.today:
            self.calc_week()

        #Get Current Time
        time = self.get_time(f'%m %d %H %M')
        time_parts = time.split(' ')
        day = int(time_parts[1])
        hour = int(time_parts[2])
        minute = int(time_parts[3])

        #Check Last User Activity
        if self.LAST_USER_ACTIVE_TIME:
            user_time_parts = self.LAST_USER_ACTIVE_TIME.split(' ')
            last_user_min = int(user_time_parts[3])
            if minute - last_user_min >= 5:
                self.USER_ACTIVE = False

        #Compare Times
        if self.last_time and self.USER_ACTIVE:
            last = self.last_time.split(' ')
            last_day = int(last[1])
            last_hour = int(last[2])
            last_minute = int(last[3])

            if not day > last_day:

                #Check Hours
                if hour > last_hour:
                    #Reset Date
                    self.date.set(f"Today, {self.get_time(f'%A')}")

                    #Set HR Notify Dot On
                    if len(self.all_keystrokes_per_min) == 59: self.home_page._avg_hr_notify_dot.configure(fg_color=BRAND_PRIMARY)

                    #Calc Words Per Hour
                    if len(self.all_keystrokes_per_min) >= 60:
                        #Reset HR Notify Dot
                        self.home_page._avg_hr_notify_dot.configure(fg_color=BACKGROUND_3)

                        all_keys = 0
                        for keys_set in self.all_keystrokes_per_min:
                            all_keys += keys_set
                        
                        avg_hr = all_keys // len(self.all_keystrokes_per_min)

                        self.avg_keys_hour.set(avg_hr)
                        if avg_hr > self.highest_avg_hour:
                            self.highest_avg_hour = avg_hr

                        self.all_keys_per_min = []
                
                #Check Minutes
                if minute > last_minute:

                    #Set MIN Notify Dot On
                    if len(self.keys_per_min) == 6: self.home_page._avg_min_notify_dot.configure(fg_color=BRAND_PRIMARY)

                    #Calc AVG keys per min
                    if len(self.keys_per_min) >= 7:
                        #Reset HR Notify Dot
                        self.home_page._avg_min_notify_dot.configure(fg_color=BACKGROUND_3)

                        all_keys = 0
                        for set in self.keys_per_min:
                            all_keys += set
                        avg = all_keys // len(self.keys_per_min)
                        self.avg_keys_min.set(avg)
                        if avg > self.highest_avg_min:
                            self.highest_avg_min = avg
                        self.keys_per_min = []
                    
                    #Append and Reset
                    self.all_keystrokes_per_min.append(int(self.keys_this_min.get()))
                    self.keys_per_min.append(int(self.keys_this_min.get()))
                    self.keys_this_min.set('0')

            else: 
                self.reset()

        #Toggle INITIAL UPDATE
        if not self.INITIAL_UPDATE:
            self.INITIAL_UPDATE = True

        #Set Last Time to Time
        self.last_time = time
        if self.UPDATING: self.after(800, self.update)

    def save_week_to_file(self, week_total, week_avg):
        week_data = {}

        month = self.get_time('%b').upper()
        date = self.get_time('%Y %m %d')
        parts = date.split(' ')
        week = datetime.date(int(parts[0]), int(parts[1]), int(parts[2])).isocalendar().week

        week_data['week_of_the_year'] = week
        week_data['date'] = date
        week_data['total'] = week_total
        week_data['avg'] = week_avg
        week_data['week'] = self.stats['weekly']

        if not os.path.exists('Data\\Weeks'):
            os.mkdir('Data\\Weeks')

        if not os.path.exists(f'Data\\Weeks\\{month}'):
            os.mkdir(f'Data\\Weeks\\{month}')

        with open(f'Data\\Weeks\\{month}\\week_{week}.json', 'w') as json_file:
            json.dump(week_data, json_file, indent=4)

    def calc_week(self):
        #Check if weekdays have amounts greater than 0
        days_with_totals = 0
        for day in self.stats['weekly']:

            #If Day total is greater than 0, add to total
            if self.stats['weekly'].get(day) > 0: 
                days_with_totals +=1
            else:
                #add to total if day is start of week
                if day == self.settings.get('start_of_week'):
                    days_with_totals += 1

        #Calc and Reset
        if days_with_totals >= 7:
            self.week_to_be_reset = True

            #Calc Total
            week_total = 0
            for day in self.stats['weekly']:
                week_total += self.stats['weekly'].get(day)

            if self.stats.get('highest_week_total'):  
                if week_total > self.stats.get('highest_week_total'):
                    self.stats['highest_week_total'] = week_total
            else:
                self.stats['highest_week_total'] = week_total

            #Calc Avg
            week_avg = week_total // 7

            if self.stats.get('highest_avg_week'):  
                if week_avg > self.stats.get('highest_avg_week'):
                    self.stats['highest_avg_week'] = week_avg
            else:
                self.stats['highest_avg_week'] = week_avg

            #Save Week
            self.save_week_to_file(week_total, week_avg)

            #Reset Week
            self.stats['weekly'] = {'sun':0, 'mon':0, 'tue':0, 'wed':0, 'thu':0, 'fri':0, 'sat':0}

            self.reset()

    def get_time(self, format:str) -> str:
        now = datetime.datetime.now()
        return str(now.strftime(format))

    #Core
    def toggle_window(self):
        if not self.VISIBLE:
            #Show
            self.VISIBLE = True
            if self.ICON: 
                self.ICON.stop()
                del self.ICON
                gc.collect()
                self.ICON = None
            self.deiconify()
        else:
            #Hide
            self.VISIBLE = False
            self.withdraw()

            icon = Image.open('Icons/keycap.png')

            #Start Sys Icon
            self.ICON = pystray.Icon(
                'KeyAchieverIcon',
                icon,
                f'{APP_NAME} | {APP_VERSION}',
                pystray.Menu(
                    pystray.MenuItem('Show', self.toggle_window, default=True),
                    pystray.Menu.SEPARATOR,
                    pystray.MenuItem('Quit App', self.quit_app)
                )
            )
            self.ICON.run_detached()

            #Notify
            t = win11toast.notify(f'{APP_NAME} minimized to system tray ...', 'Left Click me in the tray to view me quickly again', icon=f'{ROOT_FOLDER}\\Icons\\keycap.png', app_id=f'{APP_NAME}')

            #Clear Mem
            del t
            del icon
            gc.collect()

    def manual_reset(self):
        self.reset(False)
        self.stats['weekly'][self.today] = 0

    def reset(self, save=True):
        if save: self.save()

        self.date.set(f"Today, {self.get_time(f'%A')}")
        self.today = self.get_time(f'%a').lower()
        self.keys = {}
        self.recent_key.set('')
        self.total_keys_pressed.set('0')
        self.all_keystrokes_per_min = []
        self.keys_per_min = []
        self.avg_keys_min.set('0')
        self.avg_keys_hour.set('0')
        self.keys_this_min.set('0')
        self.total_unique_keys_pressed.set('0')

        #Reset Week Bars
        if self.stats.get('weekly'):
            for day in self.stats_page.day_bars:
                if day == self.today:
                    self.stats_page.key_totals[day].set(f'{self.stats["weekly"][day]}')
                    day_num = 2 + (self.stats_page.key_totals[day] // 250)
                    self.stats_page.day_bars[day].configure(height=day_num)
                if day == self.today:
                    self.stats_page.day_bars[day].configure(fg_color=BRAND_PRIMARY)
                else:
                    self.stats_page.day_bars[day].configure(fg_color='grey')

        gc.collect()

    def listener_thread(self):
        self.listener =  Listener(on_press=self.on_press)
        self.listener.start()

    def save(self):
        #Save Stats Data
        today = self.get_time(f'%a').lower()
        data = self.stats
        
        data['total_keys'] = int(self.stats['total_keys']) + int(self.total_keys_pressed.get().replace(',',''))
        data['total_unique_keys'] = int(self.stats['total_unique_keys']) + int(self.total_unique_keys_pressed.get())
        data['highest_avg_min'] = self.highest_avg_min
        data['highest_avg_hour'] = self.highest_avg_hour
        if self.stats.get('highest_avg_week'): data['highest_avg_week'] = self.stats['highest_avg_week']
        if self.stats.get('highest_week_total'):  data['highest_week_total'] = self.stats['highest_week_total']
        data['weekly'] = self.stats['weekly']
        data['weekly'][today] = self.stats['weekly'][today] + int(self.total_keys_pressed.get().replace(',',''))

        self.stats = data

        with open('Data\\achieve_stats.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        #Save Settings Data
        self.settings['last_win_pos'] = [self.winfo_x(), self.winfo_y()]

        with open('Data\\achieve_settings.json', 'w') as json_file:
            json.dump(self.settings, json_file)

    def quit_app(self):
        #Stop Icon
        if self.ICON: 
            self.ICON.stop()

        self.UPDATING = False

        #Quit Key Listener
        self.listener.stop()

        #Save Data
        self.save()

        #Quit
        if self.ICON:
            if not self.ICON._running :self.quit()
            else: print('OOPS DIDNT QUIT')
        else:
            self.quit()

    def run(self):
        #Start Keyboard Listener
        self.threaded_listener = Thread(target=self.listener_thread)
        self.threaded_listener.start()

        #Apply Data Values
        if self.stats.get('highest_avg_min'):
            self.highest_avg_min = self.stats.get('highest_avg_min')
        
        if self.stats.get('highest_avg_hour'):
            self.highest_avg_hour = self.stats.get('highest_avg_hour')

        #Start Update Loop
        self.UPDATING = True
        self.INITIAL_UPDATE = False
        self.update()

        #Apply Settings
        if self.settings['topmost'] == True:
            self.attributes('-topmost', True)

        if self.settings['start_hidden'] == True:
            self.after(100, self.toggle_window)

        #App Loop
        self.mainloop()