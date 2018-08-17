from tkinter import *
from uldaq import (get_daq_device_inventory, DaqDevice, InterfaceType,
                   AiInputMode, Range, AInFlag)
import matplotlib.pyplot as plt

#key down function
def click():
    try:
        # Get a list of available DAQ devices
        devices = get_daq_device_inventory(InterfaceType.USB)
        # Create a DaqDevice Object and connect to the device
        daq_device = DaqDevice(devices[0])
        daq_device.connect()
        daq_device.flash_led(3)
        # Get AiDevice and AiInfo objects for the analog input subsystem
        ai_device = daq_device.get_ai_device()
        ai_info = ai_device.get_info()
        print(ai_info)
        # Read and display voltage values for all analog input channels
        for channel in range(1):
            data = ai_device.a_in(channel, AiInputMode.SINGLE_ENDED,
                                  Range.BIP10VOLTS, AInFlag.DEFAULT)
            print('Channel', channel, 'Data:', data)

        daq_device.disconnect()
        daq_device.release()

    except ULException as e:
        print('\n', e)  # Display any error messages
    
    outputMsg.delete(0.0, END)
    outputMsg.insert(END, data)

#### main
window = Tk()
window.title('Desert Speed Labs - Dyno v1')
window.configure(background='black')

#### logos
logo = PhotoImage(file='DSL_1280p.gif')
Label(window, image=logo, bg='black') .grid(row=0, column=0, sticky=N)

#### label
Label(window, text='MANUAL TEST MODE', bg='black', fg='white', font='none 12') .grid(row=1, column=0, sticky=W)

#### text entry
textEntry = Entry(window, width=20, bg='white')
textEntry.grid(row=2, column=0, sticky=W)

#### submit button that calls the 'click' function
Button(window, text='SAMPLE', width='6', command=click) .grid(row=3, column=0, sticky=W)

#### second label
Label(window, text='\nAnalog Voltage', bg='black', fg='white', font='none 12') .grid(row=4, column=0, sticky=W)

#### text output
outputMsg = Text(window, width=75, height=6, wrap=WORD, background='white')
outputMsg.grid(row=5, column=0, columnspan=2, sticky=W)


#### run main loop
window.mainloop()