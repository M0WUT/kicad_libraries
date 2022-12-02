import re
from dataclasses import dataclass

# Tool for mostly converting Xilinx pinout files into Kicad symbols by Dan M0WUT
banks = {}


    

@dataclass(frozen=True)
class Pin:
    pin: str
    name: str

@dataclass
class Bank:
    bank: int
    bank_io_type: str
    pins: list[Pin]

def split_on_arbitrary_spaces(x: str) -> str:
    """
    Takes a string using a arbitrary number of spaces as separators
    and returns a list of the values
    """
    return re.split(r'\s\s+', x)

def write_header(output_file, part_number):
    output_file.write(f"""
  (symbol "{part_number}" (in_bom yes) (on_board yes)
    (property "Reference" "U" (id 0) (at 0 2.54 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "{part_number}" (id 1) (at 0 5.08 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Footprint" "" (id 2) (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Datasheet" "" (id 3) (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_locked" "" (id 4) (at 0 0 0)
      (effects (font (size 1.27 1.27)))
    )
"""
    )


number_of_pins = 0
with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            if "Device/Package" in line:
                # First line, extract part number
                part_number = line.split(" ")[1].upper()
                print(part_number)
                output_file = open(f"{part_number}.kicad_sym", 'w')
                write_header(output_file, part_number)
            elif "Pin Name" in line:
                # Headings row
                headings = split_on_arbitrary_spaces(line)
                pin_index = headings.index("Pin")
                name_index = headings.index("Pin Name")
                bank_index = headings.index("Bank")
                io_type_index = headings.index("I/O Type")
            elif "Total Number of Pins" in line:
                # Final line
                assert number_of_pins == int(line.split(", ")[1])
            else:
                # Regular pin declaration line
                data = split_on_arbitrary_spaces(line)
                pin = data[pin_index]
                name = data[name_index]
                # Format Bank
                try:
                    bank = int(data[bank_index])
                except:
                    bank = data[bank_index]

                # Format name
                if "_" in name:
                    # remove last _<bank-number>
                    if ("VCCO" not in name) and ("_" in name):
                        name = "_".join(name.split("_")[:-1])
                
                io_type = data[io_type_index]

                # Power pins have no bank ("N/A") but separate out the grounds
                if name == "GND":
                    bank = "GND"

                if bank not in banks:
                    # New bank, add a sub-symbol
                    banks[bank] = Bank(bank, None, [Pin(pin, name)])
                    if "VCCO" not in name:
                        # Power pins don't have io_types
                        banks[bank].bank_io_type = io_type
                else:
                    # Already existing bank, check the IO is the same type
                    if "VCCO" not in name and banks[bank].bank_io_type:
                        assert io_type == banks[bank].bank_io_type
                    banks[bank].pins.append(Pin(pin, name))

                number_of_pins += 1

bank_counter = 0
for _, bank in banks.items():
    bank_counter += 1
    output_file.write(f"""
    (symbol "{part_number}_{bank_counter}_0"
      (text "Bank {bank.bank} ({bank.bank_io_type})" (at 0 0 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol "{part_number}_{bank_counter}_1"
"""
    )
    pin_position = -5.08
    vcco_pin_position = -5.08

    for pin in bank.pins:

        if ("VCCO" in pin.name):
            pin_type = "power_in"
            output_file.write(f"""
        (pin {pin_type} line (at -25.4 {vcco_pin_position} 0) (length 5.08)
            (name "{pin.name}" (effects (font (size 1.27 1.27))))
            (number "{pin.pin}" (effects (font (size 1.27 1.27))))
        )
"""
            )
            vcco_pin_position = round(vcco_pin_position - 2.54, 2)
        else:
            if pin.name == "GND":
                pin_type = "power_in"
            else:
                pin_type = "passive"
    
            output_file.write(f"""
        (pin {pin_type} line (at 25.4 {pin_position} 180) (length 5.08)
            (name "{pin.name}" (effects (font (size 1.27 1.27))))
            (number "{pin.pin}" (effects (font (size 1.27 1.27))))
        )
"""
            )
            pin_position = round(pin_position - 2.54, 2)
    output_file.write(f"""
      (rectangle (start -20.32 -2.54) (end 20.32 {min(vcco_pin_position, pin_position) })
        (stroke (width 0) (type default) (color 0 0 0 0))
        (fill (type background))
      )
"""
    )
    output_file.write("    )\n")
output_file.write("  )")


    


