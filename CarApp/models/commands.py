from gpiozero import Motor

class Commands():
    """ List of GPIOs
    21 - 09
    22 - 25
    23 - 11
    24 - 08
    """

    class CommandNotFound(Exception):
        """Comando não encontrado"""
        pass

    motor_left = Motor(forward=9, backward=25)
    motor_right = Motor(forward=11, backward=8)
    status = "idle"

    def execute(self, command):
        try:
            if command == "forward":
                self.forward()
            elif command == "backward":
                self.backward()
            elif command == "left":
                self.left()
            elif command == "right":
                self.right()
            else:
                raise self.CommandNotFound()
        except:
            pass
        else:
            self.status = command

    def forward(self):
        self.motor_right.forward()
        self.motor_left.forward()

    def backward(self):
        self.motor_right.backward()
        self.motor_left.backward()

    def right(self):
        self.motor_right.backward()
        self.motor_left.forward()

    def left(self):
        self.motor_right.forward()
        self.motor_left.backward()
    
    def stop(self):
        self.motor_right.stop()
        self.motor_left.stop()