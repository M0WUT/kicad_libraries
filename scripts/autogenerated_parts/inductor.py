from pathlib import Path
from typing import Generator


def add_base_inductor(library):
    library.write(
        """  (symbol "L" (pin_numbers hide) (pin_names hide) (in_bom yes) (on_board yes)
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
    )


def add_inductor(
    library,
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
    library.write(
        f"""
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
    (property "ki_description" "{value} +-{tolerance} {package_description} {rated_current} Inductor" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
  )
"""
    )


def add_inductors(library_dir: Path, worksheet_values: Generator):
    standard_lib_path = library_dir / "inductor_auto_wut.kicad_sym"
    preferred_lib_path = library_dir / "aaa_inductor_auto_wut.kicad_sym"

    with open(standard_lib_path, "w") as std_lib, open(
        preferred_lib_path, "w"
    ) as pref_lib:
        for lib in [std_lib, pref_lib]:
            add_base_inductor(lib)

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
            if manufacturer == "Manufacturer":
                continue
            add_inductor(
                pref_lib if preferred == "Y" else std_lib,
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
