from NeuroPy import NeuroPy
import time


mindware = NeuroPy("/dev/ttyUSB0", 115200)

meditation_hist = [ 0, 0, 0, 0, 0]

def attention_callback(value):
    print( "Atencion " + str(value) )
    return None


def meditation_callback(value):
    print("Meditacion " + str(value) )
    return None

def blink_callback(value):
    print("Parpadeo " + str(value) )

# set call back:
mindware.setCallBack("attention",attention_callback)
mindware.setCallBack("meditation",meditation_callback)
mindware.setCallBack("blinkStrength",blink_callback)

# call start method
mindware.start()

try:
    while True:
        time.sleep(0.5)
except:
    print("exit")
    mindware.stop()