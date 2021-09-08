# KSN Generator framework and configuration
from Tkinter import *
from ttk import *
from ast import literal_eval


master = Tk()
style = Style()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
ehandle = StringVar(master)
serial_label = Label(master, text="        Serial:")
bin_label = Label(master, text="        KSN:")
serial_box = Text(master, height=10, width=45)
bin_box = Text(master, height=10, width=45)
rapidksi = 'FFFF038100'
rapidsred = 'e2f9632de81141e1b47d63600cc98be1'
merchantksi = 'F876543210'
merchsred = '9c595f4769c9301b951b221d82e8c536'
merchpin = '0123456789ABCDEFFEDCBA9876543210'
merchsredksn = 'FFFFFFFF657204000001'
ksicurrent = ''
file_append = ''
zeros = '000000000000000000000'
bdk = ''
bklk = '30313233343536373839414243444546'


def center_window(width=480, height=480):
    """
    Places GUI at center screen.
    """
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    master.geometry('%dx%d+%d+%d' % (width, height, x, y))


def conversion_output():
    """
        Allows GUI functionality between conversion button and text boxes, and contains algorithm for
        creating keys. Essentially the backbone function.
        """
    # if statement for KSN checkbox data functionality
    if var1.get() == 0 and var2.get() == 1:
        ksicurrent = merchantksi
    elif var1.get() == 1 and var2.get() == 0:
        ksicurrent = rapidksi
    else:
        pass

    # if statement for PIN and SRED check box data functionality
    if var3.get() == 1 and var4.get() == 0:
        if var1.get() == 1 and var2.get() == 0:
            bdk = 'UNAVAILABLE'
        elif var1.get() == 0 and var2.get() == 1:
            bdk = merchpin
    elif var3.get() == 0 and var4.get() == 1:
        if var1.get() == 1 and var2.get() == 0:
            bdk = rapidsred
        elif var1.get() == 0 and var2.get() == 1:
            bdk = merchsred

    else:
        pass

    # Serial to Key Conversion
    try:
        # set of variables for s/n conversion to ksn
        stage = [hex(int(x, 16)) if not x.isdigit() else x for x in serial_box.get(1.0, END).split()]
        binconvert = [bin(literal_eval(x.strip())) for x in stage]
        zerostring = [str(x) + zeros for x in binconvert]
        listslice = [x[-40:] for x in zerostring]
        hexconvert = [hex(int(x, 2)) for x in listslice]
        hexslice = [x[2:-1] for x in hexconvert]
        newksi = [ksicurrent + str(x) for x in hexslice]
        dataset = '\nBKLK: ' + bklk + '\nBDK:  ' + bdk
        datalist = ['\nBKLK: ' + bklk, '\nBDK:  ' + bdk]
        sredksn_insert = ['\nBKLK: ' + bklk, 'BDK:  ' + bdk + '\nKSN:  ' + merchsredksn]
        infoset = ['S/N:  ' + str(x) + dataset for x in serial_box.get(1.0, END).split()]
        result = ['KSN:  ' + str(x + '\n') for x in newksi]
        merge = [x for y in zip(infoset, result) for x in y]
     

        # if statement for conversion results
        if result == []:
            if var2.get() == 1 and var4.get() == 1:
                bin_box.delete(1.0, "end-1c")
                bin_box.insert(END, "\n".join(sredksn_insert))
            else:
                bin_box.delete(1.0, "end-1c")
                bin_box.insert(END, "\n".join(datalist))
        elif result != []:
            if var2.get() == 1 and var4.get() == 1:
                bin_box.delete(1.0, "end-1c")
                bin_box.insert(END, "Error: Data entry not required for operation.")
            else:
                bin_box.delete(1.0, "end-1c")
                bin_box.insert(END, "\n".join(merge))

    except ValueError:
        bin_box.delete(1.0, "end-1c")
        bin_box.insert("end-1c", "Error:\nRemove all values not 0-9, A-F.")


def checkbox_handler():
    """
    Handles checkbox warnings in order to maximize resistance to human error.
    """
    if var1.get() == 1 and var2.get() == 1:
        bin_box.delete(1.0, "end-1c")
        bin_box.insert("end-1c", "Error:\nPlease check only ONE KSN Type.")
        if var3.get() == 1 and var4.get() == 1:
            bin_box.delete(1.0, "end-1c")
            bin_box.insert("end-1c", "Error:\nYou've selected every checkbox. Please don't.")
    elif var1.get() == 0 and var2.get() == 1:
        bin_box.delete(1.0, END)
        if var3.get() == 1 and var4.get() == 1:
            bin_box.insert("end-1c", "Error:\nCannot select both PIN and SRED.")
    elif var1.get() == 1 and var2.get() == 0:
        bin_box.delete(1.0, END)
        if var3.get() == 1 and var4.get() == 1:
            bin_box.insert("end-1c", "Error:\nCannot select both PIN and SRED.")
        elif var1.get() == 1 and var3.get() == 1:
            bin_box.insert(END, "Rapid Connect with PIN currently unavailable.")
    elif var1.get() == 0 and var2.get() == 0:
        bin_box.delete(1.0, END)
        if var3.get() == 1 and var4.get() == 1:
            bin_box.insert("end-1c", "Error:\nCannot select both PIN and SRED.")
    else:
        pass


def clear_all():
    '''
    Simple function to clear all text boxes.
    '''
    bin_box.delete(1.0, "end-1c")
    serial_box.delete(1.0, "end-1c")


rccheck = Checkbutton(master, text="Rapid Connect KSN", variable=var1, command=checkbox_handler)
mlcheck = Checkbutton(master, text="Merchant Link KSN", variable=var2, command=checkbox_handler)
pincheck = Checkbutton(master, text="PIN", variable=var3, command=checkbox_handler)
sredcheck = Checkbutton(master, text="SRED", variable=var4, command=checkbox_handler)
convert_button = Button(master, text="Convert", command=conversion_output)
exit_button = Button(master, text="Quit", command=master.quit)
clear_button = Button(master, text="Clear All", command=clear_all)