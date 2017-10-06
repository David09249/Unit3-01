# Created by: David Wang
# Created on: 02-Oct-2017
# Created for: ICS3U
# Daily Assignment - Unit3-01
# This program displays an if statement

import ui

CORRECT_NUMBER = 5

def check_number_touch_up_inside(sender):
    # check the number entered
    
    # input
    number_entered = int(view['number_textfield'].text)
    
    # process
    if number_entered == CORRECT_NUMBER :
        # output
        view['correct_label'].text = "Got it correct!"
    
view = ui.load_view()
view.present('full_sheet')
