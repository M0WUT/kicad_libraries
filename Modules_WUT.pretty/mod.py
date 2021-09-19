import re
with open("Xilinx_Kria_SM-K26-XCL2GC_SOM.kicad_mod", 'r') as file, \
    open("test.kicad_mod", 'w') as outFile:
    x = 0
    for line in file:
        newString = line
        if line.lstrip().startswith("(pad") and \
                '" smd circle' in line:
            xCoord = float(line.split("at ")[1].split(" ")[0])
            
            
            outFile.write(newString.replace('\" smd', '_1\" smd' if xCoord < 0 else '_2\" smd'))
        else:
            outFile.write(line)



