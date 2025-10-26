from pathlib import Path
from typing import Generator

from library import WUTKicadLibrary


def add_base_led():
    return """  (symbol "LED" (pin_numbers hide) (pin_names hide) (in_bom yes) (on_board yes)
    (property "Reference" "LD" (at 0 2.54 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "LED" (at 0 -2.54 0) (do_not_autoplace)
      (effects (font (size 1.27 1.27)))
    )
    (property "Footprint" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Datasheet" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (symbol "LED_0_1"
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
        )
        (stroke (width 0.254) (type default))
        (fill (type none))
      )
      (polyline
        (pts
          (xy -1.27 1.27)
          (xy -1.27 -1.27)
          (xy 1.27 0)
          (xy -1.27 1.27)
        )
        (stroke (width 0.254) (type default))
        (fill (type none))
      )
      (polyline
        (pts
          (xy 1.778 0.762)
          (xy 3.302 2.286)
          (xy 2.54 2.286)
          (xy 3.302 2.286)
          (xy 3.302 1.524)
        )
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (polyline
        (pts
          (xy 3.048 0.762)
          (xy 4.572 2.286)
          (xy 3.81 2.286)
          (xy 4.572 2.286)
          (xy 4.572 1.524)
        )
        (stroke (width 0) (type default))
        (fill (type none))
      )
    )
    (symbol "LED_1_1"
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


def add_led(
    manufacturer,
    mpn,
    value,
    package_description,
    footprint,
    height,
    datasheet,
):
    return f"""  (symbol "{manufacturer}_{mpn}" (extends "LED")
    (property "Reference" "LD" (at 0 2.54 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "{value}" (at 0 -2.54 0) (do_not_autoplace)
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
    (property "ki_description" "{value} {package_description} LED" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
  )"""


def add_leds(library_dir: Path, worksheet_values: Generator):
    standard_lib_path = library_dir / "led_auto_wut.kicad_sym"
    preferred_lib_path = library_dir / "aaa_led_auto_wut.kicad_sym"

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
    ) in worksheet_values:
        target_str_list = pref_strs if preferred == "Y" else std_strs
        if manufacturer == "Manufacturer":
            continue
        target_str_list.append(
            add_led(
                manufacturer,
                mpn,
                value,
                package_description,
                footprint,
                height,
                datasheet,
            )
        )

    _ = WUTKicadLibrary(
        standard_lib_path,
        preferred_lib_path,
        add_base_led(),
        "".join(std_strs),
        "".join(pref_strs),
    )
