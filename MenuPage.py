from typing import List
from tkinter import Label, ttk
from datetime import datetime
from MenuOption import MenuOption
from State import State


BACKGROUND_COLOUR = "black"
DEFAULT_STYLE = "default"
DEFAULT_FONT = "Terminal"
SELECTION_TEXT = "To select an item, press the number or the first letter of the name : "




DEFAULT_SELECTED_INDEX = 0 
DEFAULT_UNSELECTED = [" ", "_"]

DEFAULT_TERMINAL = "Terminal"

BOUND_KEYBINDS = ["<KeyPress>", "<Configure>"]
class MenuPage():
    
    menu_options : dict[int, ttk.Label]
    selected_index : int

    selected_colour : str
    unselected_colour : str

    def __init__(self, menu_labels : List[MenuOption], menu_name : str, font: str = DEFAULT_FONT, unselected_colour : str = "gray", selected_colour : str = "gold", style = "menu", default_selected_index = DEFAULT_SELECTED_INDEX):
        # self.menu_options = menu_options
        self.selected_colour = selected_colour
        self.unselected_colour = unselected_colour
        self.selected_index = default_selected_index
        
        self.font = font
        self.text_label = ""
        self.drawn = False

        self.menu_labels = menu_labels
        self.style = style
        self.menu_name = menu_name
    
    def set_focus(self, state : State, previous_page = None):
        self.state = state
        if previous_page is not None:
            self.previous_page = previous_page

        for keybind in BOUND_KEYBINDS:
            self.state.get_root().bind(keybind, self.on_key_press)
        self.general_setup(self.state)
        
        self.drawn = True
        self.draw()
        self.update_time()
    
    def defocus(self, revert = False):
        
        for keybind in BOUND_KEYBINDS:
            self.state.get_root().unbind(keybind)

        self.drawn = False
        for widget in self.state.get_root().winfo_children():
            widget.destroy()

        if revert:
            self.previous_page.set_focus(self.state)
        

        

       

    def draw(self):
        if self.drawn:
            
            if self.text_label_text in [" ", "_"]:
                self.text_label_text = " " if self.text_label_text == "_" else "_"
                self.text_label.config(text=f"{SELECTION_TEXT}{self.text_label_text.ljust(20)[:20]}")      
                # self.text_label.config(text = f"{SELECTION_TEXT}{self.text_label_text}")
            self.state.get_root().after(400, lambda: self.draw())

       
    
    def update_time(self):
        if self.drawn:
            current_time = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
            self.bottom_label.config(text=f"F1 HELP --- F4 EXIT --- BackSpace back --- {current_time}")
            self.state.get_root().after(1000, self.update_time)
        
    
    def on_resize(self, _):
        if self.state.has_window_size_changed():
            self.update_labels()

    def update_labels(self):
        """Update positions and layout of the labels dynamically."""

        self.separator_line.place(relx=0, rely=0.07, relwidth=1.0)
        self.green_streak_frame.place(relx=0.0, rely=0, relwidth=2.0, relheight=0.05)
        self.menu_name_label.place(relx=0.02, rely=0.5, anchor="w") 


        # Get current window size
        width, height = self.state.get_window_size()

        # Resize the label frame to be 50% of the window's size
        self.label_frame.place(relx=0.5, rely=0.5, anchor="center", width=width * 0.5, height=height * 0.5)

        # Update the positions of menu labels dynamically
        for idx, label in self.menu_options.items():
            label.place(relx=0.5, rely=0.3 + 0.1 * idx, anchor="center")

        
        self.bottom_label.place(relx=0.5, rely=0.97, relwidth=1.0)
        self.selected_label.place(relx=0.5, rely=0.9, anchor="center")

        
        


    def general_setup(self, state):
        self.general_frame = ttk.Frame(state.get_root(), style=state.get_style(self.style))
        self.general_frame.pack(fill="both", expand=True)  # Make the frame take up the full space of the root
        self.green_streak_frame = ttk.Frame(state.get_root(), height=40, style=state.get_style("green"))
        self.green_streak_frame.place(relx=0.0, rely=0, relwidth=2.0)

        self.menu_name_label = Label(self.green_streak_frame, text=(self.menu_name).upper(), font=(self.font, 12), fg="black", bg="green")
        self.menu_name_label.place(relx=0.02, rely=0.5, anchor="w") 

        

        # Add a thin line separator underneath the menu name
        self.separator_line = ttk.Separator(self.general_frame, orient='horizontal')
        self.separator_line.place(relx=0.5, rely=0.1, relwidth=1.0)

        # width, height = state.get_window_size()
        
        
        self.label_frame = ttk.Frame(state.get_root(), padding=20, style=state.get_style(self.style))
        # self.label_frame.place(width=(width / 2), height=(height / 2))

        self.initialise_labels(self.menu_labels, self.label_frame)
        self.update_menu()

        self.text_label_text = " "
        self.text_label = Label(self.general_frame, text=f"{SELECTION_TEXT}{self.text_label_text}", 
                              font=(self.font, 10), fg="gold", bg="black")
        self.text_label.place(relx=0.5, rely=0.9, anchor="center", relwidth=1.0)

        current_time = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
        self.bottom_label = Label(self.general_frame, text=f"F1 HELP --- F4 EXIT --- {current_time}", 
                              font=(self.font, 10), fg="white", bg="black")
        self.update_time()

        
        self.bottom_label.place(relx=0.5, rely=0.97, anchor="center", relwidth=1.0)
        self.update_labels()

        
        
    def initialise_labels(self, menu_labels: List[MenuOption], frame: ttk.Frame, font_size = 15, font = DEFAULT_TERMINAL,  background_c = "black", foreground_c = "gray"):

        self.menu_options = {}
        for idx, menu_option in enumerate(menu_labels):
            label = Label(frame, text=f"{idx} {str.upper(menu_option.name)}", font=(font, font_size), anchor="w", width=30, bg=background_c, fg=foreground_c)
            label.place(rely=0.3*(0.05*idx), relx = 0.1)  # Make the labels fill the width of the frame
            label.bind("<Button-1>", lambda event, idx=idx: menu_option.redirect(idx))  # Click to select
            self.menu_options[idx] = label

        self.selected_label = Label(frame, text="", font=(font, font_size), bg=background_c, fg=foreground_c)
        self.selected_label.pack(pady=20)



        


    def on_key_press(self, event):
        
        
        if event.keysym == 'Down':
            self.selected_index = (self.selected_index + 1) % len(self.menu_options)
            self.update_menu()
        elif event.keysym == 'Up':
            self.selected_index = (self.selected_index - 1) % len(self.menu_options)
            self.update_menu()

        elif event.keysym == 'BackSpace':

            if self.text_label_text in DEFAULT_UNSELECTED:
                if self.previous_page is not None:
                    self.defocus(revert=True)
            else:
                self.text_label_text = self.text_label_text[:-1]
                self.text_label_text = self.text_label_text
            self.text_label.config(text=f"{SELECTION_TEXT}{self.text_label_text.ljust(20)[:20]}")            

                

        elif event.keysym == 'Return':
            selected_index = self.selected_index
            if self.text_label_text not in DEFAULT_UNSELECTED:

                if self.text_label_text.isdigit() and int(self.text_label_text) in self.menu_options:
                    self.selected_index = int(self.text_label_text)
                    selected_index = self.selected_index
                    self.update_menu()
                else:
                    pass
            
            try:
                self.defocus()
                self.menu_labels[selected_index].redirect.set_focus(self.state, previous_page = self)
                
            except:
                self.set_focus(self.state)
                pass
                # self.set_focus(self.state, previous_page = self)
            self.text_label_text = " "
            
            
            
            # self.selected_label.config(text=f"Selected: {self.menu_options[selected_index].cget("text")}")
           
            
        elif event.keysym.isdigit():
            if self.text_label_text in DEFAULT_UNSELECTED:
                self.text_label_text = ""
            num = event.keysym
            self.text_label_text = self.text_label_text + num
            self.text_label.config(text=f"{SELECTION_TEXT}{self.text_label_text.ljust(20)[:20]}")      
            # self.text_label.config(text=f"{SELECTION_TEXT}{self.text_label_text}")
        # elif event.keysym == 'BackSpace':
        #     self.text_label_text = self.text_label_text[:-1]
        #     if self.text_label_text == "":
        #         self.text_label_text = " "


   
    def update_menu(self):
        for i, label in enumerate(self.menu_options.values()):
            # Update the color for selected and unselected labels
            label.config(fg=self.selected_colour if i == self.selected_index else self.unselected_colour)

