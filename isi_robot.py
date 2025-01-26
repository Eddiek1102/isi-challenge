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
    
    def __str__(self) -> str:
        """Equivalent to Java's toString - Returns string representation of a Robot object.

        Returns:
            str: Describes robot's elements.
        """
        return f"Number of Subsystems: {self.num_subsystems}\nNumber of fans: {self.num_fans}\nFan Max Speed: {self.max_fan_speed}\nSubsystem Temperatures: {self.subsystem_temperatures}"
    
    def increase_system_temperature(self) -> None:
        """Increases the subsystems' temperature
        """
        # Base amount for temperature increase (0.25 degrees celsius)
        base = 0.25
        # Iterate through the subsystem's temperatures and increase them
        for i, temperature in enumerate(self.subsystem_temperatures):
            # Get random multiplier for temp increase between subsystems so that temperature change is not uniform
            mult = float(random.randint(1, 10))
            # Keep temperature within reasonable range for GUI purposes
            if temperature < -20:
                self.subsystem_temperatures[i] = -20
            elif temperature > 120:
                self.subsystem_temperatures[i] = 120
            else:
                self.subsystem_temperatures[i] += (base * mult)
            
    
    def decrease_system_temperature(self) -> None:
        """Decreases the subsystems' temperature
        """
        # Base multiplier used to determine temperature decrease according to fan speed
        base = 0.05
        # Iterate through the subsystems' temperatures and decrease them
        for i, temperature in enumerate(self.subsystem_temperatures):
            # Get random multiplier for temp decrease between subsystems so that temperature change is not uniform
            mult = float(random.randint(1, 10))
            # If temp below 25 degrees, run fans at 20% max speed
            if temperature < 25:
                fan_speed = self.max_fan_speed * 0.2
                self.subsystem_temperatures[i] -= float(fan_speed * base * mult)
            # If temp above 75 degrees, run fans at 100% max speed
            elif temperature > 75:
                self.subsystem_temperatures[i] -= float(self.max_fan_speed * base * mult)
            # If temp is between [25, 75] degrees, run fans at a percentage of the maximum
            else:
                # fan speed = (max fan speed) * (0.2 + 0.8 * ((temperature - 25) /50))
                fan_speed = self.max_fan_speed * (0.2 + 0.8 * ((temperature - 25) / 50))
                self.subsystem_temperatures[i] -= float(fan_speed * base * mult)
                
            
        
        
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