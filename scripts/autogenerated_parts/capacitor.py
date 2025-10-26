from pathlib import Path
from typing import Generator

from library import WUTKicadLibrary


def add_base_capacitor():
    return """  (symbol "C" (pin_numbers hide) (pin_names (offset 0)) (in_bom yes) (on_board yes)
    (property "Reference" "C" (at 2.54 2.54 0) (do_not_autoplace)
      (effects (font (size 1.27 1.27)) (justify left))
    )
    (property "Value" "" (at 2.54 0 0) (do_not_autoplace)
      (effects (font (size 1.27 1.27)) (justify left))
    )
    (property "Footprint" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Datasheet" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Voltage" "" (at 2.54 -2.54 0) (do_not_autoplace)
      (effects (font (size 1.27 1.27) (color 0 100 100 1)) (justify left))
    )
    (symbol "C_0_1"
      (polyline
        (pts
          (xy -2.032 -0.762)
          (xy 2.032 -0.762)
        )
        (stroke (width 0.508) (type default))
        (fill (type none))
      )
      (polyline
        (pts
          (xy -2.032 0.762)
          (xy 2.032 0.762)
        )
        (stroke (width 0.508) (type default))
        (fill (type none))
      )
    )
    (symbol "C_1_1"
      (pin passive line (at 0 3.81 270) (length 2.794)
        (name "~" (effects (font (size 1.27 1.27))))
        (number "1" (effects (font (size 1.27 1.27))))
      )
      (pin passive line (at 0 -3.81 90) (length 2.794)
        (name "~" (effects (font (size 1.27 1.27))))
        (number "2" (effects (font (size 1.27 1.27))))
      )
    )
  )
"""


def add_capacitor(
    manufacturer,
    mpn,
    value,
    package_description,
    footprint,
    height,
    tolerance,
    datasheet,
    voltage,
    dielectric,
):
    return f"""
  (symbol "{manufacturer} {mpn}" (extends "C")
    (property "Reference" "C" (at 2.54 2.54 0) (do_not_autoplace)
      (effects (font (size 1.27 1.27)) (justify left))
    )
    (property "Value" "{value}" (at 2.54 0 0) (do_not_autoplace)
      (effects (font (size 1.27 1.27)) (justify left))
    )
    (property "Footprint" "{footprint}" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Datasheet" "{datasheet}" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Voltage" "{voltage}" (at 2.54 -2.54 0) (do_not_autoplace)
      (effects (font (size 1.27 1.27) (color 0 100 100 1)) (justify left))
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
    (property "Dielectric" "{dielectric}" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Height" "{height}mm" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_description" "{value} {tolerance} {voltage} {package_description} {dielectric} Capacitor" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
  )
"""


def add_base_polarised_capacitor():
    return """  (symbol "C_Pol" (pin_numbers hide) (pin_names hide) (in_bom yes) (on_board yes)
    (property "Reference" "C" (at 2.54 2.54 0) (do_not_autoplace)
      (effects (font (size 1.27 1.27)) (justify left))
    )
    (property "Value" "" (at 2.54 0 0) (do_not_autoplace)
      (effects (font (size 1.27 1.27)) (justify left))
    )
    (property "Footprint" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Datasheet" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Voltage" "50V" (at 2.54 -2.54 0) (do_not_autoplace)
      (effects (font (size 1.27 1.27) (color 0 100 100 1)) (justify left))
    )
    (property "Manufacturer" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "MPN" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)))
    )
    (symbol "C_Pol_0_1"
      (rectangle (start -2.286 0.508) (end 2.286 1.016)
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (polyline
        (pts
          (xy -1.778 2.286)
          (xy -0.762 2.286)
        )
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (polyline
        (pts
          (xy -1.27 2.794)
          (xy -1.27 1.778)
        )
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (rectangle (start 2.286 -0.508) (end -2.286 -1.016)
        (stroke (width 0) (type default))
        (fill (type outline))
      )
    )
    (symbol "C_Pol_1_1"
      (pin passive line (at 0 3.81 270) (length 2.794)
        (name "~" (effects (font (size 1.27 1.27))))
        (number "1" (effects (font (size 1.27 1.27))))
      )
      (pin passive line (at 0 -3.81 90) (length 2.794)
        (name "~" (effects (font (size 1.27 1.27))))
        (number "2" (effects (font (size 1.27 1.27))))
      )
    )
  )
  """


def add_polarised_capacitor(
    manufacturer,
    mpn,
    value,
    package_description,
    footprint,
    tolerance,
    height,
    datasheet,
    voltage,
    dielectric,
):
    return f"""  (symbol "{manufacturer}_{mpn}" (extends "C_Pol")
    (property "Reference" "C" (at 2.54 2.54 0) (do_not_autoplace)
      (effects (font (size 1.27 1.27)) (justify left))
    )
    (property "Value" "{value}" (at 2.54 0 0) (do_not_autoplace)
      (effects (font (size 1.27 1.27)) (justify left))
    )
    (property "Footprint" "{footprint}" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Datasheet" "{datasheet}" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Voltage" "{voltage}" (at 2.54 -2.54 0) (do_not_autoplace)
      (effects (font (size 1.27 1.27) (color 0 72 72 1)) (justify left))
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
    (property "Dielectric" "{dielectric}" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Height" "{height}mm" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_description" "{value} {tolerance} {voltage} {package_description} {dielectric} Capacitor" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
  )
  """


def add_capacitors(library_dir: Path, worksheet_values: Generator):
    standard_lib_path = library_dir / "capacitor_auto_wut.kicad_sym"
    preferred_lib_path = library_dir / "aaa_capacitor_auto_wut.kicad_sym"

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
        polarised,
        voltage,
        dielectric,
    ) in worksheet_values:
        if manufacturer == "Manufacturer":
            continue
        target_str_list = pref_strs if preferred == "Y" else std_strs
        if polarised == "Y":
            target_str_list.append(
                add_polarised_capacitor(
                    manufacturer,
                    mpn,
                    value,
                    package_description,
                    footprint,
                    height,
                    tolerance,
                    datasheet,
                    voltage,
                    dielectric,
                )
            )
        else:
            target_str_list.append(
                add_capacitor(
                    manufacturer,
                    mpn,
                    value,
                    package_description,
                    footprint,
                    height,
                    tolerance,
                    datasheet,
                    voltage,
                    dielectric,
                )
            )
    _ = WUTKicadLibrary(
        standard_lib_path,
        preferred_lib_path,
        add_base_capacitor() + add_base_polarised_capacitor(),
        "".join(std_strs),
        "".join(pref_strs),
    )
