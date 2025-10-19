from pathlib import Path
from typing import Generator


def add_base_ferrite_bead(library):
    library.write(
        """  (symbol "FB" (pin_numbers hide) (pin_names hide) (in_bom yes) (on_board yes)
    (property "Reference" "FB" (at 0 2.921 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "" (at 0 -3.048 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Footprint" "" (at 0.508 -0.254 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Datasheet" "" (at 0.508 -0.254 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (symbol "FB_0_1"
      (polyline
        (pts
          (xy -0.889 0)
          (xy -1.2954 0)
        )
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (polyline
        (pts
          (xy 1.27 0)
          (xy 0.7874 0)
        )
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (polyline
        (pts
          (xy -0.2794 -1.8288)
          (xy -1.4986 -1.1176)
          (xy 0.2032 1.8288)
          (xy 1.4224 1.1176)
          (xy -0.2794 -1.8288)
        )
        (stroke (width 0) (type default))
        (fill (type none))
      )
    )
    (symbol "FB_1_1"
      (pin passive line (at -2.54 0 0) (length 1.27)
        (name "~" (effects (font (size 1.27 1.27))))
        (number "1" (effects (font (size 1.27 1.27))))
      )
      (pin passive line (at 2.54 0 180) (length 1.27)
        (name "~" (effects (font (size 1.27 1.27))))
        (number "2" (effects (font (size 1.27 1.27))))
      )
    )
  )"""
    )


def add_ferrite_bead(
    library,
    manufacturer,
    mpn,
    value,
    package_description,
    footprint,
    height,
    datasheet,
    rated_current,
):
    library.write(
        f"""    
  (symbol "{manufacturer} {mpn}" (extends "FB")
    (property "Reference" "FB" (at 2.032 0 90)
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
    (property "Datasheet" "{datasheet}" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Height" "{height}mm" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Rated Current" "{rated_current}" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_description" "{value}@100MHz {rated_current} {package_description} Ferrite Bead" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
  )"""
    )


def add_ferrite_beads(library_dir: Path, worksheet_values: Generator):
    standard_lib_path = library_dir / "ferrite_bead_auto_wut.kicad_sym"
    preferred_lib_path = library_dir / "aaa_ferrite_bead_auto_wut.kicad_sym"

    with open(standard_lib_path, "w") as std_lib, open(
        preferred_lib_path, "w"
    ) as pref_lib:
        for lib in [std_lib, pref_lib]:
            add_base_ferrite_bead(lib)

        for (
            manufacturer,
            mpn,
            value,
            preferred,
            package_description,
            footprint,
            height,
            datasheet,
            rated_current,
        ) in worksheet_values:
            if manufacturer == "Manufacturer":
                continue
            add_ferrite_bead(
                pref_lib if preferred == "Y" else std_lib,
                manufacturer,
                mpn,
                value,
                package_description,
                footprint,
                height,
                datasheet,
                rated_current,
            )
