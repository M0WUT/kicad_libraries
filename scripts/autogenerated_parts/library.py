from pathlib import Path


class WUTKicadLibrary:
    def __init__(
        self,
        standard_lib_path: Path,
        preferred_lib_path: Path,
        base_component_str: str,
        std_components_str: str,
        pref_components_str: str,
    ):
        with open(standard_lib_path, "w") as std_lib, open(
            preferred_lib_path, "w"
        ) as pref_lib:
            for lib in [std_lib, pref_lib]:
                lib.write(
                    "(kicad_symbol_lib (version 20220914) (generator kicad_symbol_editor)\n"
                )
                lib.write(base_component_str)
            std_lib.write(std_components_str)
            pref_lib.write(pref_components_str)
            for lib in [std_lib, pref_lib]:
                lib.write(")")
