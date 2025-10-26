from pathlib import Path
from typing import Generator

from library import WUTKicadLibrary


def add_base_resistor() -> str:
    return """
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
  )
  """


def add_resistor(
    manufacturer,
    mpn,
    value,
    package_description,
    footprint,
    height,
    tolerance,
    datasheet,
) -> str:
    return f"""
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
    (property "ki_description" "{value} {tolerance} {package_description} Resistor" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
  )
  """


def add_resistors(library_dir: Path, worksheet_values: Generator):
    standard_lib_path = library_dir / "resistor_auto_wut.kicad_sym"
    preferred_lib_path = library_dir / "aaa_resistor_auto_wut.kicad_sym"

    std_strs = []
    pref_strs = []

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

        target_str_list = pref_strs if preferred == "Y" else std_strs

        target_str_list.append(
            add_resistor(
                manufacturer,
                mpn,
                value,
                package_description,
                footprint,
                height,
                tolerance,
                datasheet,
            )
        )

    _ = WUTKicadLibrary(
        standard_lib_path,
        preferred_lib_path,
        add_base_resistor(),
        "".join(std_strs),
        "".join(pref_strs),
    )
