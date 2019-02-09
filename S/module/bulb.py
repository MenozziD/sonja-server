from yeelight import Bulb
#bulb=Bulb("192.168.1.14")
#bulb.turn_off()

def cmd_off():
  bulb=Bulb("192.168.1.14")
  bulb.turn_off()

def cmd_on():
  bulb=Bulb("192.168.1.14")
  bulb.turn_on()  

def cmd_toggle():
  bulb=Bulb("192.168.1.14")
  bulb.toggle()

def set_rgb_bright(r,g,b,l):
  bulb=Bulb("192.168.1.14")
  bulb.set_brightness(l)
  bulb.set_rgb(r,g,b)
  
