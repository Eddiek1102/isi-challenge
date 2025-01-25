class Robot:
    def __init__(self, num_subsystems, num_fans, fan_max_speed):
        """Initializes a new Robot.

        Args:
            num_subsystems (int): Number of subsystems
            num_fans (int): Number of fans
            fan_max_speed (int): The maximum fan speed
        """
        self.num_subsystems = num_subsystems
        self.num_fans = num_fans
        self.fan_max_speed = fan_max_speed
        self.subsystem_temperatures = [20.0] * num_subsystems
    
    
    def __str__(self):
        """Equivalent to Java's toString - Returns string representation of a Robot object.

        Returns:
            str: Describes robot's elements.
        """
        return f"Number of Subsystems: {self.num_subsystems}\nNumber of fans: {self.num_fans}\nFan Max Speed: {self.fan_max_speed}\nSubsystem Temperatures: {self.subsystem_temperatures}"
    
    
if __name__ == "__main__":
    r = Robot(5, 10, 200)
    print(r)