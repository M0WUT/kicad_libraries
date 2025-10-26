from pathlib import Path
from typing import Generator

from library import WUTKicadLibrary


def add_base_zener():
    return """
  (symbol "ZD" (pin_numbers hide) (pin_names (offset 1.016) hide) (in_bom yes) (on_board yes)
    (property "Reference" "ZD" (at 0 2.54 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "ZD" (at 0 -2.54 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Footprint" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Datasheet" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_keywords" "diode" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_description" "Zener diode" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (symbol "ZD_0_1"
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
          (xy -1.27 -1.27)
          (xy -1.27 1.27)
          (xy -0.762 1.27)
        )
        (stroke (width 0.254) (type default))
        (fill (type none))
      )
      (polyline
        (pts
          (xy 1.27 -1.27)
          (xy 1.27 1.27)
          (xy -1.27 0)
          (xy 1.27 -1.27)
        )
        (stroke (width 0.254) (type default))
        (fill (type none))
      )
    )
    (symbol "ZD_1_1"
      (pin passive line (at -3.81 0 0) (length 2.54)
        (name "K" (effects (font (size 1.27 1.27))))
        (number "1" (effects (font (size 1.27 1.27))))
      )
      (pin passive line (at 3.81 0 180) (length 2.54)
        (name "A" (effects (font (size 1.27 1.27))))
        (number "2" (effects (font (size 1.27 1.27))))
      )
    )
  )"""


def add_zener(
    manufacturer,
    mpn,
    value,
    package_description,
    footprint,
    height,
    datasheet,
):
    return f"""
  (symbol "{manufacturer} {mpn}" (extends "ZD")
    (property "Reference" "ZD" (at 2.54 2.54 0)
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
    (property "Height" "{height}mm" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_description" "{value} {package_description} Zener Diode" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
  )
"""


def add_base_tvs_uni():
    return """  (symbol "TVS_Uni" (pin_numbers hide) (pin_names hide) (in_bom yes) (on_board yes)
    (property "Reference" "D" (at 0 2.54 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Footprint" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Datasheet" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (symbol "TVS_Uni_0_1"
      (polyline
        (pts
          (xy -1.27 0)
          (xy 1.27 0)
        )
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (polyline
        (pts
          (xy 1.27 -1.27)
          (xy 1.27 1.27)
        )
        (stroke (width 0.254) (type default))
        (fill (type none))
      )
      (polyline
        (pts
          (xy -1.27 -1.27)
          (xy -1.27 1.27)
          (xy 1.27 0)
          (xy -1.27 -1.27)
        )
        (stroke (width 0.254) (type default))
        (fill (type none))
      )
    )
    (symbol "TVS_Uni_1_1"
      (polyline
        (pts
          (xy 1.27 -1.27)
          (xy 1.778 -1.27)
        )
        (stroke (width 0.254) (type default))
        (fill (type none))
      )
      (polyline
        (pts
          (xy 1.27 1.27)
          (xy 0.762 1.27)
        )
        (stroke (width 0.254) (type default))
        (fill (type none))
      )
      (pin passive line (at 3.81 0 180) (length 2.54)
        (name "K" (effects (font (size 1.27 1.27))))
        (number "1" (effects (font (size 1.27 1.27))))
      )
      (pin passive line (at -3.81 0 0) (length 2.54)
        (name "A" (effects (font (size 1.27 1.27))))
        (number "2" (effects (font (size 1.27 1.27))))
      )
    )
  )"""


def add_tvs_uni(
    manufacturer,
    mpn,
    value,
    package_description,
    footprint,
    height,
    datasheet,
):
    return f"""
  (symbol "{manufacturer} {mpn}" (extends "TVS_Uni")
    (property "Reference" "D" (at 2.54 2.54 0)
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
    (property "Height" "{height}mm" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_description" "{value} {package_description} TVS Diode" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
  )
"""


def add_tvs_zeners(library_dir: Path, worksheet_values: Generator):
    standard_lib_path = library_dir / "tvs_zener_auto_wut.kicad_sym"
    preferred_lib_path = library_dir / "aaa_tvs_zener_auto_wut.kicad_sym"

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
        datasheet,
        type,
    ) in worksheet_values:
        target_str_list = pref_strs if preferred == "Y" else std_strs
        if manufacturer == "Manufacturer":
            continue
        if type == "Zener":
            target_str_list.append(
                add_zener(
                    manufacturer,
                    mpn,
                    value,
                    package_description,
                    footprint,
                    height,
                    datasheet,
                )
            )
        elif type == "TVS_Unidirectional":
            target_str_list.append(
                add_tvs_uni(
                    manufacturer,
                    mpn,
                    value,
                    package_description,
                    footprint,
                    height,
                    datasheet,
                )
            )
        else:
            raise NotImplementedError(f"Unsupported TVS type: {type}")

    _ = WUTKicadLibrary(
        standard_lib_path,
        preferred_lib_path,
        add_base_tvs_uni() + add_base_zener(),
        "".join(std_strs),
        "".join(pref_strs),
    )
