from pathlib import Path
from typing import Generator

from library import WUTKicadLibrary


def add_base_fuse():
    return """
  (symbol "Fuse"
    (pin_numbers
      (hide yes)
    )
    (pin_names
      (hide yes)
    )
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "F"
      (at 0 2.54 0)
      (do_not_autoplace)
      (effects
        (font
          (size 1.27 1.27)
        )
      )
    )
    (property "Value" "f"
      (at 0 -2.54 0)
      (do_not_autoplace)
      (effects
        (font
          (size 1.27 1.27)
        )
      )
    )
    (property "Footprint" ""
      (at 0 0 0)
      (effects
        (font
          (size 1.27 1.27)
        )
        (hide yes)
      )
    )
    (property "Datasheet" ""
      (at 0 0 0)
      (effects
        (font
          (size 1.27 1.27)
        )
        (hide yes)
      )
    )
    (property "Description" ""
      (at 0 0 0)
      (effects
        (font
          (size 1.27 1.27)
        )
        (hide yes)
      )
    )
    (symbol "Fuse_0_1"
      (rectangle
        (start -2.54 0.762)
        (end 2.54 -0.762)
        (stroke
          (width 0.254)
          (type default)
        )
        (fill
          (type none)
        )
      )
      (polyline
        (pts
          (xy -2.54 0) (xy 2.54 0)
        )
        (stroke
          (width 0)
          (type default)
        )
        (fill
          (type none)
        )
      )
    )
    (symbol "Fuse_1_1"
      (pin passive line
        (at -3.81 0 0)
        (length 1.27)
        (name "~"
          (effects
            (font
              (size 1.27 1.27)
            )
          )
        )
        (number "1"
          (effects
            (font
              (size 1.27 1.27)
            )
          )
        )
      )
      (pin passive line
        (at 3.81 0 180)
        (length 1.27)
        (name "~"
          (effects
            (font
              (size 1.27 1.27)
            )
          )
        )
        (number "2"
          (effects
            (font
              (size 1.27 1.27)
            )
          )
        )
      )
    )
    (embedded_fonts no)
  )
  """


def add_fuse(
    manufacturer,
    mpn,
    package_description,
    footprint,
    height,
    datasheet,
    rated_current,
    fuse_type,
):
    return f"""
  (symbol "{manufacturer} {mpn}" (extends "Fuse")
    (property "Reference" "F" (at 0 2.54 0) (do_not_autoplace)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "{rated_current}" (at 0 -2.54 0) (do_not_autoplace)
      (effects (font (size 1.27 1.27)))
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
    (property "Height" "{height}mm" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_description" "{rated_current} {fuse_type} {package_description} Fuse" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
  )
"""


def add_fuses(library_dir: Path, worksheet_values: Generator):
    standard_lib_path = library_dir / "fuse_auto_wut.kicad_sym"
    preferred_lib_path = library_dir / "aaa_fuse_auto_wut.kicad_sym"

    std_strs = []
    pref_strs = []

    for (
        manufacturer,
        mpn,
        rated_current,
        preferred,
        package_description,
        footprint,
        height,
        datasheet,
        fuse_type,
    ) in worksheet_values:
        target_str_list = pref_strs if preferred == "Y" else std_strs
        if manufacturer == "Manufacturer":
            continue
        target_str_list.append(
            add_fuse(
                manufacturer,
                mpn,
                package_description,
                footprint,
                height,
                datasheet,
                rated_current,
                fuse_type,
            )
        )

    _ = WUTKicadLibrary(
        standard_lib_path,
        preferred_lib_path,
        add_base_fuse(),
        "".join(std_strs),
        "".join(pref_strs),
    )
