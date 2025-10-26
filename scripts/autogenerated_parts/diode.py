from pathlib import Path
from typing import Generator

from library import WUTKicadLibrary


def add_base_normal_diode():
    return """  (symbol "D" (pin_names hide) (in_bom yes) (on_board yes)
    (property "Reference" "D" (at 0 2.54 0) (do_not_autoplace)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "diode" (at 0 -2.54 0) (do_not_autoplace)
      (effects (font (size 1.27 1.27)))
    )
    (property "Footprint" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Datasheet" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Manufacturer" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "MPN" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (symbol "D_0_1"
      (polyline
        (pts
          (xy -1.27 1.27)
          (xy -1.27 -1.27)
        )
        (stroke (width 0.254) (type default))
        (fill (type none))
      )
      (polyline
        (pts
          (xy 1.27 0)
          (xy -1.27 0)
        )
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (polyline
        (pts
          (xy 1.27 1.27)
          (xy 1.27 -1.27)
          (xy -1.27 0)
          (xy 1.27 1.27)
        )
        (stroke (width 0.254) (type default))
        (fill (type none))
      )
    )
    (symbol "D_1_1"
      (pin passive line (at -3.81 0 0) (length 2.54)
        (name "K" (effects (font (size 1.27 1.27))))
        (number "1" (effects (font (size 1.27 1.27))))
      )
      (pin passive line (at 3.81 0 180) (length 2.54)
        (name "A" (effects (font (size 1.27 1.27))))
        (number "2" (effects (font (size 1.27 1.27))))
      )
    )
  )
  """


def add_normal_diode(
    manufacturer,
    mpn,
    package_description,
    footprint,
    height,
    datasheet,
    rated_current,
):
    return f"""
  (symbol "{manufacturer} {mpn}" (extends "D")
    (property "Reference" "D" (at 2.54 2.54 0)
      (effects (font (size 1.27 1.27)) (justify left))
    )
    (property "Value" "{mpn}" (at 2.54 0 0)
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
    (property "Height" "{height}mm" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_description" "{package_description} {rated_current} Diode" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
  )
"""


def add_diodes(library_dir: Path, worksheet_values: Generator):
    standard_lib_path = library_dir / "diode_auto_wut.kicad_sym"
    preferred_lib_path = library_dir / "aaa_diode_auto_wut.kicad_sym"

    std_strs = []
    pref_strs = []

    for (
        manufacturer,
        mpn,
        preferred,
        package_description,
        footprint,
        height,
        datasheet,
        rated_current,
        type,
    ) in worksheet_values:
        target_str_list = pref_strs if preferred == "Y" else std_strs
        if manufacturer == "Manufacturer":
            continue

        if type == "Normal":
            target_str_list.append(
                add_normal_diode(
                    manufacturer,
                    mpn,
                    package_description,
                    footprint,
                    height,
                    datasheet,
                    rated_current,
                )
            )
        else:
            raise NotImplementedError(f"Unsupported Diode type: {type}")

    _ = WUTKicadLibrary(
        standard_lib_path,
        preferred_lib_path,
        add_base_normal_diode(),
        "".join(std_strs),
        "".join(pref_strs),
    )
