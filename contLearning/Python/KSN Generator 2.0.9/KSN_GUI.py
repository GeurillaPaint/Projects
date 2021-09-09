# Widgets for KSN Generator
from ksn_config import *

master.title("KSN Generator")
center_window()
style.theme_use('clam')

rccheck.grid(row=0, sticky=W, pady=3, columnspan=2)
mlcheck.grid(row=0, column=0, sticky=W, padx=150)
pincheck.grid(row=1, sticky=W, pady=3)
sredcheck.grid(row=1, column=0, sticky=W, padx=150)
convert_button.grid(row=4, column=0, sticky=W, pady=5, padx=15)
exit_button.grid(row=4, column=0, sticky=W+N, pady=5, padx=235)
clear_button.grid(row=4, column=0, sticky=W+N, pady=5, padx=125)
serial_label.grid(row=2, pady=11, sticky=N+E+W,)
serial_label.config(background='gray94')
bin_label.grid(row=3, pady=10, sticky=N+E+W)
bin_label.config(background='gray94')
serial_box.grid(row=2, column=0, padx=50, pady=11, rowspan=1, columnspan=2)
bin_box.grid(row=3, column=0, padx=80, pady=10, rowspan=1, columnspan=2)

if var1.get() == 0 and var2.get() == 0:
    bin_box.insert("end-1c",
    '''For Merchant Link SRED, please press 
conversion without entering a serial number.

Rapid Connect PIN currently unavailable.

For Merchant Link PIN and Rapid Connect SRED,please enter the last 11 digits of the
Device S/N without the hash. Then, select 
the KSN Type and choose PIN/SRED.
    '''
                   )

master.mainloop()
