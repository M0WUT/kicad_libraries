from pathlib import Path
from typing import Generator


def add_base_cm_choke(library):
    library.write(
        """(symbol "CM_Choke" (pin_numbers hide) (pin_names (offset 0.254) hide) (in_bom yes) (on_board yes)
    (property "Reference" "FL" (at 0 4.445 0) (do_not_autoplace)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "CM_Choke" (at 0 -4.445 0) (do_not_autoplace)
      (effects (font (size 1.27 1.27)))
    )
    (property "Footprint" "" (at 0 1.016 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Datasheet" "~" (at 0 1.016 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_keywords" "EMI filter" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_description" "EMI 2-inductor filter" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_fp_filters" "L_* L_CommonMode*" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (symbol "CM_Choke_0_1"
      (circle (center -3.048 -1.27) (radius 0.254)
        (stroke (width 0) (type default))
        (fill (type outline))
      )
      (circle (center -3.048 1.524) (radius 0.254)
        (stroke (width 0) (type default))
        (fill (type outline))
      )
      (arc (start -2.54 2.032) (mid -2.032 1.5262) (end -1.524 2.032)
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (arc (start -1.524 -2.032) (mid -2.032 -1.5262) (end -2.54 -2.032)
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (arc (start -1.524 2.032) (mid -1.016 1.5262) (end -0.508 2.032)
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (arc (start -0.508 -2.032) (mid -1.016 -1.5262) (end -1.524 -2.032)
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (arc (start -0.508 2.032) (mid 0 1.5262) (end 0.508 2.032)
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (polyline
        (pts
          (xy -2.54 -2.032)
          (xy -2.54 -2.54)
        )
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (polyline
        (pts
          (xy -2.54 0.508)
          (xy 2.54 0.508)
        )
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (polyline
        (pts
          (xy -2.54 2.032)
          (xy -2.54 2.54)
        )
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (polyline
        (pts
          (xy 2.54 -2.032)
          (xy 2.54 -2.54)
        )
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (polyline
        (pts
          (xy 2.54 -0.508)
          (xy -2.54 -0.508)
        )
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (polyline
        (pts
          (xy 2.54 2.54)
          (xy 2.54 2.032)
        )
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (arc (start 0.508 -2.032) (mid 0 -1.5262) (end -0.508 -2.032)
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (arc (start 0.508 2.032) (mid 1.016 1.5262) (end 1.524 2.032)
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (arc (start 1.524 -2.032) (mid 1.016 -1.5262) (end 0.508 -2.032)
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (arc (start 1.524 2.032) (mid 2.032 1.5262) (end 2.54 2.032)
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (arc (start 2.54 -2.032) (mid 2.032 -1.5262) (end 1.524 -2.032)
        (stroke (width 0) (type default))
        (fill (type none))
      )
    )
    (symbol "CM_Choke_1_1"
      (pin passive line (at -5.08 2.54 0) (length 2.54)
        (name "1" (effects (font (size 1.27 1.27))))
        (number "1" (effects (font (size 1.27 1.27))))
      )
      (pin passive line (at 5.08 2.54 180) (length 2.54)
        (name "2" (effects (font (size 1.27 1.27))))
        (number "2" (effects (font (size 1.27 1.27))))
      )
      (pin passive line (at -5.08 -2.54 0) (length 2.54)
        (name "3" (effects (font (size 1.27 1.27))))
        (number "3" (effects (font (size 1.27 1.27))))
      )
      (pin passive line (at 5.08 -2.54 180) (length 2.54)
        (name "4" (effects (font (size 1.27 1.27))))
        (number "4" (effects (font (size 1.27 1.27))))
      )
    )
  )"""
    )


def add_cm_choke(
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
  (symbol "{manufacturer} {mpn}" (extends "CM_Choke")
    (property "Reference" "FL" (at 2.032 0 90)
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
    (property "ki_description" "{value} {rated_current} {package_description} Common Mode Choke" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
  )"""
    )


def add_cm_chokes(library_dir: Path, worksheet_values: Generator):
    standard_lib_path = library_dir / "cm_choke_auto_wut.kicad_sym"
    preferred_lib_path = library_dir / "aaa_cm_choke_auto_wut.kicad_sym"

    with open(standard_lib_path, "w") as std_lib, open(
        preferred_lib_path, "w"
    ) as pref_lib:
        for lib in [std_lib, pref_lib]:
            add_base_cm_choke(lib)

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
            add_cm_choke(
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
