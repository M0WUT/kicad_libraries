def add_base_symbol(footprint):
    return f"""    
  (symbol "R" (pin_numbers hide) (pin_names (offset 0)) (in_bom yes) (on_board yes)
    (property "Reference" "R" (at 2.032 0 90)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "" (at 0 0 90)
      (effects (font (size 1.27 1.27)))
    )
    (property "Footprint" "" (at -1.778 0 90)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Manufacturer" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Tolerance" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_keywords" "R res resistor" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_description" "Generic Resistor Symbol" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (symbol "R_0_1"
      (rectangle (start -1.016 -2.54) (end 1.016 2.54)
        (stroke (width 0.254) (type default))
        (fill (type none))
      )
    )
    (symbol "R_1_1"
      (pin passive line (at 0 3.81 270) (length 1.27)
        (name "~" (effects (font (size 1.27 1.27))))
        (number "1" (effects (font (size 1.27 1.27))))
      )
      (pin passive line (at 0 -3.81 90) (length 1.27)
        (name "~" (effects (font (size 1.27 1.27))))
        (number "2" (effects (font (size 1.27 1.27))))
      )
    )
  )"""


def add_symbol(value: str, mpn, footprint):
    part_number = f"KOA {mpn}"
    return f"""    
  (symbol "{part_number}" (extends "R")
    (property "Reference" "R" (at 2.032 0 90)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "{value}" (at 0 0 90)
      (effects (font (size 1.27 1.27)))
    )
    (property "MPN" "{mpn}" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Footprint" "{footprint}" (at -1.778 0 90)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Manufacturer" "KOA Speer" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Tolerance" "1%" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Datasheet" "https://www.koaspeer.com/pdfs/RK73H.pdf" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_description" "{value} Resistor" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
  )"""


E24_VALUES = {
    1: [0, 1, 2, 3, 5, 6, 8],
    2: [0, 2, 4, 7],
    3: [0, 3, 6, 9],
    4: [3, 7],
    5: [1, 6],
    6: [2, 8],
    7: [5],
    8: [2],
    9: [1],
}

PACKAGE_DEFINITONS = {"0402": "1ETTP", "0603": "1JTTD", "0805": "2ATTD"}
FOOTPRINT_DEFINITIONS = {
    "0402": "Resistor_SMD:R_0402_1005Metric",
    "0603": "Resistor_SMD:R_0603_1608Metric",
    "0805": "Resistor_SMD:R_0805_2012Metric",
}


for package in PACKAGE_DEFINITONS:
    package_code = PACKAGE_DEFINITONS[package]
    footprint = FOOTPRINT_DEFINITIONS[package]
    with open(f"Resistors_KOA_{package}.kicad_sym", "w+") as file:
        file.write(
            "(kicad_symbol_lib (version 20220914) (generator kicad_symbol_editor)\n"
        )
        file.write(add_base_symbol(footprint))

        # Zero ohm resistor
        file.write(
            add_symbol(
                value=f"0R0",
                mpn=f"RK73Z{package_code}",
                footprint=footprint,
            )
        )
        for first_number, second_numbers in E24_VALUES.items():
            for second_number in second_numbers:
                # single ohms
                file.write(
                    add_symbol(
                        value=f"{first_number}R{second_number}",
                        mpn=f"RK73H{package_code}{first_number}R{second_number}0F",
                        footprint=footprint,
                    )
                )
                # tens of ohms
                file.write(
                    add_symbol(
                        value=f"{first_number}{second_number}R",
                        mpn=f"RK73H{package_code}{first_number}{second_number}R0F",
                        footprint=footprint,
                    )
                )
                # hundreds of ohms
                file.write(
                    add_symbol(
                        value=f"{first_number}{second_number}0R",
                        mpn=f"RK73H{package_code}{first_number}{second_number}00F",
                        footprint=footprint,
                    )
                )
                # kohms
                file.write(
                    add_symbol(
                        value=f"{first_number}k{second_number}",
                        mpn=f"RK73H{package_code}{first_number}{second_number}01F",
                        footprint=footprint,
                    )
                )
                # tens of kohms
                file.write(
                    add_symbol(
                        value=f"{first_number}{second_number}k",
                        mpn=f"RK73H{package_code}{first_number}{second_number}02F",
                        footprint=footprint,
                    )
                )
                # hundreds of kohms
                file.write(
                    add_symbol(
                        value=f"{first_number}{second_number}0k",
                        mpn=f"RK73H{package_code}{first_number}{second_number}03F",
                        footprint=footprint,
                    )
                )
                # Mohms
                file.write(
                    add_symbol(
                        value=f"{first_number}M{second_number}",
                        mpn=f"RK73H{package_code}{first_number}{second_number}04F",
                        footprint=footprint,
                    )
                )
        file.write(")")
