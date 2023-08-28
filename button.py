#!/usr/bin/env python

import signal
import buttonshim
import sys
import time

print("""
Button SHIM: rainbow.py

Light up the LED a different colour of the rainbow with each button pressed.

Press Ctrl+C to exit.

""")

import subprocess, platform
def pingOk(sHost):
    try:
        output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower()=="windows" else 'c', sHost), shell=True)

    except Exception as e:
        return False

    return True

button_was_held = False


@buttonshim.on_press(buttonshim.BUTTON_A)
def button_a(button, pressed):
    buttonshim.set_pixel(0, 0, 255)
    if pingOk('127.0.0.1'):
        sys.argv = [0,"127.0.0.1"]
        exec(open("/usr/local/bin/status_check/all_pi_stats_DHM.py").read())
        buttonshim.set_pixel(0, 200, 0)
        time.sleep(20)
        exec(open("/usr/local/bin/status_check/DHM_update.py").read())
    else:
        buttonshim.set_pixel(200, 0, 0)
        time.sleep(2)
    buttonshim.set_pixel(0, 0, 0)


@buttonshim.on_press(buttonshim.BUTTON_B)
def button_b(button, pressed):
    buttonshim.set_pixel(0, 0, 255)
    if pingOk('192.168.11.160'):
        sys.argv = [0,"192.168.11.160"]
        exec(open("/usr/local/bin/status_check/all_pi_stats_DHM.py").read())
        buttonshim.set_pixel(0, 200, 0)
        time.sleep(20)
        exec(open("/usr/local/bin/status_check/DHM_update.py").read())
        #exec(open("/usr/local/bin/status_check/inky_update.py").read())
    else:
        buttonshim.set_pixel(200, 0, 0)
        time.sleep(2)
    buttonshim.set_pixel(0, 0, 0)


@buttonshim.on_press(buttonshim.BUTTON_C)
def button_c(button, pressed):
    buttonshim.set_pixel(0, 0, 255)
    if pingOk('192.168.11.125'):
        sys.argv = [0,"192.168.11.125"]
        exec(open("/usr/local/bin/status_check/all_pi_stats_DHM.py").read())
        buttonshim.set_pixel(0, 200, 0)
        time.sleep(20)
        exec(open("/usr/local/bin/status_check/DHM_update.py").read())
        #exec(open("/usr/local/bin/status_check/inky_update.py").read())
    else:
        buttonshim.set_pixel(200, 0, 0)
        time.sleep(2)
    buttonshim.set_pixel(0, 0, 0)


@buttonshim.on_press(buttonshim.BUTTON_D)
def button_d(button, pressed):
    buttonshim.set_pixel(0, 0, 255)
    #if pingOk('192.168.195.112'):
    #    sys.argv = [0,"192.168.195.112"]
    #    exec(open("/usr/local/bin/status_check/all_pi_stats_DHM.py").read())
    #    buttonshim.set_pixel(0, 200, 0)
    #    time.sleep(20)
    #    exec(open("/usr/local/bin/status_check/DHM_update.py").read())
        #exec(open("/usr/local/bin/status_check/inky_update.py").read())
    #else:
    #    buttonshim.set_pixel(200, 0, 0)
    #    time.sleep(2)
    buttonshim.set_pixel(0, 0, 0)


# @buttonshim.on_press(buttonshim.BUTTON_E)
# def button_e(button, pressed):
#     buttonshim.set_pixel(0, 0, 255)
#     exec(open("/usr/local/bin/status_check/inky_update.py").read())
#     buttonshim.set_pixel(0, 0, 0)
    
    
@buttonshim.on_press(buttonshim.BUTTON_E)
def press_handler(button, pressed):
    global button_was_held    # So we change the global var defined above
    button_was_held = False   # Reset the button held state


@buttonshim.on_release(buttonshim.BUTTON_E)
def release_handler(button, pressed):
    if not button_was_held:
        print("Short press detected!")
        buttonshim.set_pixel(0, 0, 255)
        exec(open("/usr/local/bin/status_check/DHM_update.py").read())
        #exec(open("/usr/local/bin/status_check/inky_update.py").read())
        buttonshim.set_pixel(0, 0, 0)


@buttonshim.on_hold(buttonshim.BUTTON_E, hold_time=2)
def hold_handler(button):
    global button_was_held
    button_was_held = True
    print("Long press detected!")
    
    buttonshim.set_pixel(0, 0, 255)
    exec(open("/usr/local/bin/status_check/PiholeControl.py").read())
    buttonshim.set_pixel(0, 0, 0)


signal.pause()
