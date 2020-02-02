import mido
import random
import webbrowser
import csv
import os
from pathlib import Path
from time import sleep

class Launchkey:
    row_0 = [96, 97, 98, 99, 100, 101, 102, 103, 104]  # LED indices, first row
    row_1 = [112, 113, 114, 115, 116, 117, 118, 119, 120]  # LED incides, second row
    pads_index_ref = [row0, row1]
    pads_colors = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    color_red = 1
    color_green = 16
    color_orange = 17
    midi_in = None
    midi_out = None

    # read_csv(file = 'KeyBindings.csv'): reads a csv file. (in the context of Excel) Every cell in the file
    #   corresponds to a pad on the launchkey. The first word in the a given cell (red, green, or orange)
    #   represents the color of the pad. The second word in the cell represents a command that the pad will
    #   be assigned to. The third word in the cell corresponds to an argument that the command (might) need
    # returns an array of lambda functions that can be assigned to the launchkey pads
    def read_csv(file = 'KeyBindings.csv'):
        path_to_csv = Path(__file__).parent / file

        with open(path_to_csv) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                for cell in row:
                    print(cell)
                print('end of line')

    def __init__(file = 'KeyBindings.csv'):
        self.midi_in = mido.open_output("MIDIOUT2 (Launchkey Mini) 2")
        self.midi_out = mido.open_input("MIDIIN2 (Launchkey Mini) 1")

        
    

    # set_pad_colors(): sets the colors on the Launchkey's pads to the
    #   coresponding colors in the padsColors array 
    def set_pad_colors():
        print()

def write_led(led_id, color_vel):
    midi_out.send(mido.Message('note_on', channel=0, note=led_id, velocity=color_vel))
 
def random_color():
    red_or_green = bool(random.randint(0, 1))  # Making sure the number is always >0 for one component
    return random.randint(int(red_or_green), 3) + \
           random.randint(int(not red_or_green), 3) * 16



def read_csv
 
if __name__ == "__main__":
    read_csv()
    try:
        print(mido.get_input_names())
        midi_out = mido.open_output("MIDIOUT2 (Launchkey Mini) 2")  # Launchkey InControl port
        midi_out.send(mido.Message.from_bytes([0x90, 0x0C, 0x7F]))  # Switch to "InControl" mode
        midi_in = mido.open_input("MIDIIN2 (Launchkey Mini) 1");
    
        while True:
            color = random_color()

            for msg in midi_in.iter_pending():
                print(msg)
            
            for index, led in enumerate(row1):
                # Set current LED color
                write_led(row1[index], red)
                write_led(row2[index], color)
                
                # Turn off last set LEDs
                write_led(row1[index - 1], 0)
                write_led(row2[index - 1], 0)
                sleep(0.1)
 
    except KeyboardInterrupt:
        pass
 
 
for led in leds:
    write_led(led, 0)  # Turn off all LEDs
midi_out.send(mido.Message.from_bytes([0x90, 0x0C, 0x00]))  # Disable "InControl" mode
midi_in.close()
midi_out.close()