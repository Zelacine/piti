import RPi.GPIO as G # reference the GPIO library
G.setmode(G.BCM)     # use the 'BCM' numbering scheme for the pins
G.setup(18, G.OUT)   # Set pin 18 as an Output
G.output(18, True)   # Turn it on
raw_input('Press return to exit')
G.cleanup()  
