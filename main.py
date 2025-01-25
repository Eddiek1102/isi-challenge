# This is the main file used to simulate a running program

import tkinter as tk
from isi_robot import Robot
    

def main():
    """ Main function used to simulate a running program
        and set-up the GUI.
    """
    num_subsystems, num_fans, fan_max_speed = 0, 0, 0
    
    # Set up GUI's main frame
    root = tk.Tk()
    root.geometry("1280x720")
    root.title("ISI Challenge")
    
    # Create a label and entry to set the number of subsystems
    subsystems_label = tk.Label(root, text = "Enter number of subsystems: ")
    subsystems_label.pack(padx = 0, pady = 5)
    subsystems_entry = tk.Entry(root)
    subsystems_entry.pack(padx = 0, pady = 10)
    
    # Create a label and entry to set the number of fans
    fans_label = tk.Label(root, text = "Enter number of fans")
    fans_label.pack(padx = 0, pady = 5)
    fans_entry = tk.Entry(root)
    fans_entry.pack(padx = 0, pady = 10)
    
    # Display GUI
    root.mainloop()

if __name__ == "__main__":
    main()