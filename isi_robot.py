# Contains implementation of the robot system class and its relevant methods.
import random

class Robot:
    def __init__(self, num_subsystems, num_fans, max_fan_speed):
        """Initializes a new Robot.

        Args:
            num_subsystems (int): Number of subsystems
            num_fans (int): Number of fans
            fan_max_speed (int): The maximum fan speed
        """
        self.num_subsystems = num_subsystems
        self.num_fans = num_fans
        self.max_fan_speed = max_fan_speed
        self.subsystem_temperatures = [80.0] * num_subsystems
        self.fan_speed_rates = [0.50] * num_subsystems
    
    def __str__(self) -> str:
        """Equivalent to Java's toString - Returns string representation of a Robot object.
           Mainly for testing.

        Returns:
            str: Describes robot's elements.
        """
        return f"Number of Subsystems: {self.num_subsystems}\nNumber of fans: {self.num_fans}\nFan Max Speed: {self.max_fan_speed}\nSubsystem Temperatures: {self.subsystem_temperatures}"
    
    def set_subsystem_rpm(self, percent: float, index: int) -> None:
        """Changes a certain subsystem's fan rpm.
           Ex: set_subsystem_rpm(25.5, 3) -> 3rd subsystem's fans run at 25.5% of the max rpm.

        Args:
            percent (float): New rpm percentage (percentage of maximum rpm).
            index (int): The index of the specific subsystem.
        """
        percent /= 100.0
        self.fan_speed_rates[index] = float(percent * self.max_fan_speed)
    
    def increase_system_temperature(self) -> None:
        """Increases the subsystems' temperature
        """
        # Base amount for temperature increase (0.25 degrees celsius)
        base = 0.5
        # Iterate through the subsystem's temperatures and increase them
        for i, temperature in enumerate(self.subsystem_temperatures):
            # Get random multiplier for temp increase between subsystems so that temperature change is not uniform
            mult = float(random.randint(1, 10))
            # Keep temperature within reasonable range for GUI purposes
            if temperature >= -30 and temperature <= 150:
                self.subsystem_temperatures[i] += float(mult * base)
    
    def decrease_system_temperature(self) -> None:
        """Decreases the subsystems' temperature
        """
        # Base multiplier used to determine temperature decrease according to fan speed
        base = 0.01
        # Iterate through the subsystems' temperatures and decrease them
        for i, temperature in enumerate(self.subsystem_temperatures):
            # If temp below 25 degrees, run fans at 20% max speed
            if temperature < 25:
                self.fan_speed_rates[i] = float(0.2 * self.max_fan_speed)
            # If temp above 75 degrees, run fans at 100% max speed
            elif temperature > 75:
                self.fan_speed_rates[i] = float(self.max_fan_speed)
            # If temp is between [25, 75] degrees, run fans at a percentage of the maximum
            else:
                pass
            # Decrease the temperatures using the new fan rpm
            self.subsystem_temperatures[i] -= float(base * self.fan_speed_rates[i])
                
            
        
        
if __name__ == "__main__":
    """Ignore everything here. Used for testing purposes when developing.
    """
    bot = Robot(10, 10, 300)
    print(bot)
    
    # Testing increase/decrease temperature functions
    while True:
        command = input("u/d: ")
        if command == "u":
            bot.increase_system_temperature()
            print(bot.subsystem_temperatures)
        elif command == "d":
            bot.decrease_system_temperature()
            print(bot.subsystem_temperatures)
        else:
            break
    
    print(bot)