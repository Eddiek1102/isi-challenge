# This is the main file used to simulate a running program

import tkinter as tk
from tkinter import ttk
from isi_robot import Robot

def update_system(root, bot, temperature_bars, fan_levels) -> None:
    """Periodically updates the temperatures and fan spin levels on the GUI
    """
    bot.decrease_system_temperature()
    bot.increase_system_temperature()
    
    # Update the GUI with the new temperatures
    for i, temperature in enumerate(bot.subsystem_temperatures):
        temperature_bars[i].set(temperature)
        fan_levels[i].set(bot.fan_speed_rates[i])
    
    # Set schedule for next update
    root.after(500, update_system, root, bot, temperature_bars, fan_levels)

def main():
    """ Main function used to simulate a running program
        and set-up the GUI.
    """
    
    # Set robot system's parameters according to user input
    num_subsystems, num_fans, user_input_received = 0, 0, False
    while not user_input_received:
        # Try to get input from user until input is valid
        try:
            num_subsystems = int(input("Number of subsystems: "))
            num_fans = int(input("Number of fans: "))
            user_input_received = not user_input_received
        except ValueError:
            print("Please enter an integer.")
    
    # Create new Robot object
    bot = Robot(num_subsystems, num_fans, 300)
    
    # Set up GUI's main frame
    root = tk.Tk()
    root.geometry("1080x720")
    root.title("ISI Challenge")
    
    # Title label
    title_label = ttk.Label(root, text = "Temperature Visualization")
    title_label.pack(padx = 0, pady = 10)
    
    # Frames for temperature bars for temperature bars
    temperature_frame = ttk.Frame(root)
    temperature_frame.pack(fill = tk.BOTH, expand = True, padx = 20, pady = 20)
    
    # Temperature bars for each subsystem
    temperature_bars = []
    # Fan levels for each subsystem
    fan_levels = []
    for i in range(bot.num_subsystems):
        # Labels for each subsystem
        subsystem_label = tk.Label(temperature_frame, text = f"Subsystem {i}")
        subsystem_label.grid(row = i, column = 0, padx = 10, pady = 5, sticky = "W")
        
        # Progress bar to represent the temperature
        temperature_var = tk.DoubleVar(value = bot.subsystem_temperatures[i])
        temperature_bar = ttk.Progressbar(temperature_frame, orient = "horizontal", length = 400, mode = "determinate", variable = temperature_var, maximum = 120)
        temperature_bar.grid(row = i, column = 1, padx = 10, pady = 5)
        temperature_bars.append(temperature_var)
        
        # Temperature value label
        temperature_value_label = ttk.Label(temperature_frame, textvariable = temperature_var)
        temperature_value_label.grid(row = i, column = 2, padx = 10, pady = 5)
        
        # Fan level label
        fan_level_var = tk.DoubleVar(value = bot.fan_speed_rates[i])
        fan_levels.append(fan_level_var)
        fan_level_label = ttk.Label(temperature_frame, textvariable = fan_level_var)
        fan_level_label.grid(row = i, column = 3, padx = 10, pady = 5)
      
    # Start periodic temperature updates
    root.after(500, update_system, root, bot, temperature_bars, fan_levels)
    
    # print(bot)
    
    # Display GUI
    root.mainloop()

if __name__ == "__main__":
    main()