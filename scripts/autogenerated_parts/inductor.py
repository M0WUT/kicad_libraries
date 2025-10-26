from pathlib import Path
from typing import Generator

from library import WUTKicadLibrary


def add_base_inductor():
    return """  (symbol "L" (pin_numbers hide) (pin_names hide) (in_bom yes) (on_board yes)
    (property "Reference" "L" (at -1.27 0 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "" (at 2.54 0 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Footprint" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Datasheet" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (symbol "L_0_1"
      (arc (start 0 -2.54) (mid 0.6323 -1.905) (end 0 -1.27)
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (arc (start 0 -1.27) (mid 0.6323 -0.635) (end 0 0)
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (arc (start 0 0) (mid 0.6323 0.635) (end 0 1.27)
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (arc (start 0 1.27) (mid 0.6323 1.905) (end 0 2.54)
        (stroke (width 0) (type default))
        (fill (type none))
      )
    )
    (symbol "L_1_1"
      (pin passive line (at 0 3.81 270) (length 1.27)
        (name "1" (effects (font (size 1.27 1.27))))
        (number "1" (effects (font (size 1.27 1.27))))
      )
      (pin passive line (at 0 -3.81 90) (length 1.27)
        (name "2" (effects (font (size 1.27 1.27))))
        (number "2" (effects (font (size 1.27 1.27))))
      )
    )
  )
"""


def add_inductor(
    manufacturer,
    mpn,
    value,
    package_description,
    footprint,
    height,
    tolerance,
    datasheet,
    rated_current,
):
    return f"""
  (symbol "{manufacturer} {mpn}" (extends "L")
    (property "Reference" "L" (at 2.54 2.54 0)
      (effects (font (size 1.27 1.27)) (justify left))
    )
    (property "Value" "{value}" (at 2.54 0 0)
      (effects (font (size 1.27 1.27)) (justify left))
    )
    (property "Footprint" "{footprint}" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Datasheet" "{datasheet}" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Manufacturer" "{manufacturer}" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "MPN" "{mpn}" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Tolerance" "{tolerance}" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Height" "{height}mm" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_description" "{value} {tolerance} {package_description} {rated_current} Inductor" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
  )
"""


def add_inductors(library_dir: Path, worksheet_values: Generator):
    standard_lib_path = library_dir / "inductor_auto_wut.kicad_sym"
    preferred_lib_path = library_dir / "aaa_inductor_auto_wut.kicad_sym"

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
        rated_current,
    ) in worksheet_values:
        target_str_list = pref_strs if preferred == "Y" else std_strs
        if manufacturer == "Manufacturer":
            continue
        target_str_list.append(
            add_inductor(
                manufacturer,
                mpn,
                value,
                package_description,
                footprint,
                height,
                tolerance,
                datasheet,
                rated_current,
            )
        )
    _ = WUTKicadLibrary(
        standard_lib_path,
        preferred_lib_path,
        add_base_inductor(),
        "".join(std_strs),
        "".join(pref_strs),
    )
