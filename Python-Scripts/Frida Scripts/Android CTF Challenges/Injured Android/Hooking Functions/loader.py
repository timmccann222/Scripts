# loader.py
import frida
import time

device = frida.get_usb_device() # get android device
pid = device.spawn(["com.android.insecurebankv2"]) 
device.resume(pid)
time.sleep(1) # Without it Java.perform silently fails
session = device.attach(pid)
script = session.create_script(open("frida_js_script.js").read())
script.load()

# Prevent the python script from terminating
raw_input()
