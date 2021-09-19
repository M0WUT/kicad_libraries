from collections import defaultdict
x = -2.54

pins = {}
results = defaultdict(dict)

with open("kria_k26_connector_1.csv") as conn1:
    for line in conn1:
        pinNum, aPin, bPin, cPin, dPin = line.strip().split(",")
        pins[f"A{pinNum}_1"] = aPin
        pins[f"B{pinNum}_1"] = bPin
        pins[f"C{pinNum}_1"] = cPin
        pins[f"D{pinNum}_1"] = dPin

with open("kria_k26_connector_2.csv") as conn1:
    for line in conn1:
        pinNum, aPin, bPin, cPin, dPin = line.strip().split(",")
        pins[f"A{pinNum}_2"] = aPin
        pins[f"B{pinNum}_2"] = bPin
        pins[f"C{pinNum}_2"] = cPin
        pins[f"D{pinNum}_2"] = dPin


for pinNumber in pins.keys():
    pinName = pins[pinNumber]
    if "MODE" in pinName and "_C2M" in pinName:
        number = pinName.lstrip("MODE").rstrip("_C2M")
        pinName = f"PS_MODE{number}"

    if "HPA" in pinName:
        results["Bank 66"][pinNumber] = pinName
    elif "HDA" in pinName:
        results["Bank 45"][pinNumber] = pinName
    elif "HPB" in pinName:
        results["Bank 65"][pinNumber] = pinName
    elif "HDB" in pinName:
        results["Bank 43"][pinNumber] = pinName
    elif "HPC" in pinName:
        results["Bank 64"][pinNumber] = pinName
    elif "HDC" in pinName:
        results["Bank 44"][pinNumber] = pinName
    elif ("PS_" in pinName) or ("JTAG" in pinName) or (pinName == "Reserved"):
        results["Sideband"][pinNumber] = pinName
    elif ("PWR" in pinName) or ("VCCOEN" in pinName):
        results["Power Management"][pinNumber] = pinName
    elif ("FWUEN" in pinName) or "I2C" in pinName:
        results["Bank 500"][pinNumber] = pinName
    elif "MIO" in pinName:
        suffix = pinName.lstrip("MIO")
        if "_" in suffix:
            mioNum = int(suffix.split("_")[0])
        else:
            mioNum = int(suffix)
        if 52 <= mioNum and mioNum <= 77:
            results["Bank 502"][pinNumber] = pinName
        elif 26 <= mioNum and mioNum <= 51:
            results["Bank 501"][pinNumber] = pinName
        else:
            raise NotImplementedError(pinName)
    elif ("GTR" in pinName):
        results["GTR"][pinNumber] = pinName
    elif ("GTH" in pinName):
        results["GTH"][pinNumber] = pinName
    
    elif ("VCC" in pinName) or ("GND" in pinName):
        results["Power"][pinNumber] = pinName
    else:
        print(results)
        raise NotImplementedError(f"Don't know where to file pin {pinNumber} ({pinName})")

index = 1
with open("test.txt", 'w') as file:
    for key in results.keys():
        file.write(
            f"    (symbol \"Xilinx_Kria_SM-K26-XCL2GC_SOM_{index}_1\"\n"
        )
        index += 1
        x = 0
        for pinNumber in results[key].keys():
            pinName = results[key][pinNumber]

            file.write(
                f"      (pin passive line (at -7.62 {round(x, 2)} 0) (length 7.62)\n"
                f"        (name \"{pinName}\" (effects (font (size 1.27 1.27))))\n"
                f"        (number \"{pinNumber}\" (effects (font (size 1.27 1.27))))\n"
                f"      )\n"
            )
            x -= 2.54
        file.write("    )\n")

       
      
                
                


