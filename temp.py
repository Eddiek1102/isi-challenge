import tkinter as tk
from tkinter import ttk
import threading
import time
from robot import Robot

def update_temperatures(bot, temperature_bars, root):
    """Periodically update the temperatures on the GUI."""
    bot.increase_system_temperature()
    bot.decrease_system_temperature()

    # Update the GUI with the new temperatures
    for i, temp in enumerate(bot.subsystem_temperatures):
        temperature_bars[i].set(temp)

    # Schedule the next update
    root.after(500, update_temperatures, bot, temperature_bars, root)

def main():
    """Main function to set up the robot system and GUI."""

    # Set robot system's parameters according to user input
    num_subsystems, num_fans, user_input_received = 0, 0, False
    while not user_input_received:
        try:
            num_subsystems = int(input("Number of subsystems: "))
            num_fans = int(input("Number of fans: "))
            user_input_received = True
        except ValueError:
            print("Please enter an integer.")

    # Create a new Robot object
    bot = Robot(num_subsystems, num_fans, 300)

    # Set up the GUI's main frame
    root = tk.Tk()
    root.geometry("1080x720")
    root.title("ISI Robot Temperature Visualization")

    # Add a title label
    title_label = ttk.Label(root, text="Robot Subsystem Temperature Visualization", font=("Arial", 18))
    title_label.pack(pady=10)

    # Create a frame for the temperature bars
    temp_frame = ttk.Frame(root)
    temp_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    # Create temperature bars for each subsystem
    temperature_bars = []
    for i in range(bot.num_subsystems):
        # Label for each subsystem
        subsystem_label = ttk.Label(temp_frame, text=f"Subsystem {i + 1}", font=("Arial", 12))
        subsystem_label.grid(row=i, column=0, padx=10, pady=5, sticky="W")

        # Progress bar to represent the temperature
        temp_var = tk.DoubleVar(value=bot.subsystem_temperatures[i])
        temp_bar = ttk.Progressbar(temp_frame, orient="horizontal", length=400, mode="determinate", \
                                   variable=temp_var, maximum=120)
        temp_bar.grid(row=i, column=1, padx=10, pady=5)
        temperature_bars.append(temp_var)

        # Temperature value label
        temp_value_label = ttk.Label(temp_frame, textvariable=temp_var, font=("Arial", 12))
        temp_value_label.grid(row=i, column=2, padx=10, pady=5)

    # Start the periodic temperature update
    root.after(500, update_temperatures, bot, temperature_bars, root)

    # Display the GUI
    root.mainloop()

if __name__ == "__main__":
    main()
