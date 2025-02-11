from tkinter import Tk, ttk
from MenuPage import MenuPage
from State import State
from MenuOption import MenuOption

# --- Function to handle menu navigation ---

BACKGROUND_COLOUR = "black"






TRANSFERS_AND_MENUS_OPTIONS = [
        MenuOption("Example 1", print),
        MenuOption("Example 2", print),
        MenuOption("Example 3", print),
        MenuOption("Example 4", print),
        MenuOption("Example 5", print)
    ]

TRANSFERS_AND_MENUS_OPTIONS_NAME = "Transfer and Menus"

TRANSFERS_AND_MENU = MenuPage(TRANSFERS_AND_MENUS_OPTIONS, TRANSFERS_AND_MENUS_OPTIONS_NAME)

STANDING_ORDERS_NAME = "Standing Orders"

STANDING_ORDERS = MenuPage(TRANSFERS_AND_MENUS_OPTIONS, STANDING_ORDERS_NAME)

ACCOUNT_NAMES_NAME = "Account Names"

ACCOUNT_NAMES= MenuPage(TRANSFERS_AND_MENUS_OPTIONS, ACCOUNT_NAMES_NAME)

DESIGN_REPORTS_NAME = "Design Reports"

DESIGN_REPORTS= MenuPage(TRANSFERS_AND_MENUS_OPTIONS, DESIGN_REPORTS_NAME)

GENERAL_LEDGER_OPTIONS_NAME = "General Ledger Options"

GENERAL_LEDGER_OPTIONS = MenuPage(TRANSFERS_AND_MENUS_OPTIONS, GENERAL_LEDGER_OPTIONS_NAME)


GENERAL_LEDGER_OPTIONS = [
        MenuOption("Transfers and Journals", TRANSFERS_AND_MENU),
        MenuOption("Standing Orders", STANDING_ORDERS),
        MenuOption("Account Names", ACCOUNT_NAMES),
        MenuOption("Design Reports", DESIGN_REPORTS),
        MenuOption("General Lodger Options", GENERAL_LEDGER_OPTIONS)
    ]

GENERAL_LEDGER_NAME = "General Ledger"

BASE_MENU = MenuPage(GENERAL_LEDGER_OPTIONS, GENERAL_LEDGER_NAME)






def main(state):
    BASE_MENU.set_focus(state)
    
    
    state.get_root().mainloop()

if __name__ == "__main__":
    __root = Tk()
    __root.attributes('-fullscreen', True)
    __name = "Firework Management Software"

    s = ttk.Style()
    # --- Configure the default TFrame style ---
    s.configure('TFrame', background=BACKGROUND_COLOUR)
    

    # --- Configure a custom style for the first frame with gold text ---
    s.configure('menu.TFrame', background=BACKGROUND_COLOUR)

    s.configure('green.TFrame', background="green")

    __styles = {
        "default" : 'TFrame',
        "menu" : 'menu.TFrame',
        "green" : "green.TFrame"
    }

    state = State(__name, __root, __styles)

    
    # state.get_root().geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    state.get_root().title(state.get_name())
    state.get_root().configure(bg=BACKGROUND_COLOUR)  # Set the entire background to black

   
    main(state)