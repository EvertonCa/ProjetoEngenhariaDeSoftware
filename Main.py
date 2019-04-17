from GUI import GUI
from Handler import Handler

if __name__ == "__main__":
    handler = Handler()
    gui = GUI(handler)
    gui.main_page()
