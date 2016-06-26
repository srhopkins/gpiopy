import RPi.GPIO as gpio


from time import sleep


alternate = lambda n: 0 if n else 1


class Light(object):
    """ Light object
    """
    def __init__(self, pin):
        self.pin = pin
        self.state = 0
        # not sure how to track this state, is it global?
        gpio.setmode(gpio.BCM)
        gpio.setup(self.pin, gpio.OUT)


    def output(self, n):
        gpio.output(self.pin, n) 


    def off(self):
        self.state = 0
        self.output(self.state)


    def on(self):
        self.state = 1
        self.output(self.state)

  
    def alternate(self, t):
        while True:
            self.state = alternate(self.state)
            self.output(self.state)
            sleep(t)

 
