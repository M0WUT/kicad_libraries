from pathlib import Path
from typing import Generator


def add_base_resistor(library):
    library.write(
        """    
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
    )


def add_resistor(
    library,
    manufacturer,
    mpn,
    value,
    package_description,
    footprint,
    height,
    tolerance,
    datasheet,
):
    library.write(
        f"""    
  (symbol "{manufacturer} {mpn}" (extends "R")
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
    (property "Manufacturer" "{manufacturer}" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Tolerance" "{tolerance}" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Datasheet" "{datasheet}" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Height" "{height}mm" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_description" "{value} +-{tolerance} {package_description} Resistor" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
  )"""
    )


def add_resistors(library_dir: Path, worksheet_values: Generator):
    standard_lib_path = library_dir / "resistor_auto_wut.kicad_sym"
    preferred_lib_path = library_dir / "aaa_resistor_auto_wut.kicad_sym"

    with open(standard_lib_path, "w") as std_lib, open(
        preferred_lib_path, "w"
    ) as pref_lib:
        for lib in [std_lib, pref_lib]:
            add_base_resistor(lib)

        for (
            manufacturer,
            mpn,
            value,
            preferred,
            package_description,
            footprint,
            height,
            tolerance,
            datasheet,
        ) in worksheet_values:
            if manufacturer == "Manufacturer":
                continue
            add_resistor(
                pref_lib if preferred == "Y" else std_lib,
                manufacturer,
                mpn,
                value,
                package_description,
                footprint,
                height,
                tolerance,
                datasheet,
            )
