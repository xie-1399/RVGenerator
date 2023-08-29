
# this file compile the assemble file / instruction hex file / and binary file

rootPath = "../Gentest/File/"

def convertS(Instructions_list_assembly,filename,newfile = True):
    assert str(filename).endswith(".s") or str(filename).endswith(".S"),"the assembly file should be end with .s or .S"
    writeWay = "w+" if newfile else "a+"
    with open(rootPath + filename,writeWay) as f:
        for index,asm in enumerate(Instructions_list_assembly):
            if(index == len(Instructions_list_assembly) - 1):
                f.write(asm)
            else:
                f.write(asm + '\n')


def convertB(Instructions_list_binary,filename,newfile = True):
    assert str(filename).endswith(".binary"),"the binary file should be end with .binary"
    writeWay = "w+" if newfile else "a+"
    with open(rootPath + filename,writeWay) as f:
        for index,bina in enumerate(Instructions_list_binary):
            if(index == len(Instructions_list_binary) - 1):
                f.write(bina)
            else:
                f.write(bina + '\n')


def convertH(Instructions_list_hex,filename,newfile = True,withPrefix = False):
    assert str(filename).endswith(".hex"),"the assembly file should be end with .hex"
    writeWay = "w+" if newfile else "a+"
    with open(rootPath + filename,writeWay) as f:
        for index,hex in enumerate(Instructions_list_hex):
            hex = '0x' + hex if withPrefix else hex
            if(index == len(Instructions_list_hex) - 1):
                f.write(hex)
            else:
                f.write(hex + '\n')

def convertT(Instructions_list_type,filename,newfile = True):
    assert str(filename).endswith(".type"),"the Type file should be end with .type"
    writeWay = "w+" if newfile else "a+"
    with open(rootPath + filename,writeWay) as f:
        for index,type in enumerate(Instructions_list_type):
            if(index == len(Instructions_list_type) - 1):
                f.write(type)
            else:
                f.write(type + '\n')

# Todo with combine format
def convertCombine(Instructions_list_assembly,Instructions_list_binary,Instructions_list_hex,Instructions_list_type,
               filename,newfile = True):
    assert str(filename).endswith(".asm"), "the combine file should be end with .asm"
    index = 0
    writeWay = "w+" if newfile else "a+"
    with open(rootPath + filename,writeWay) as f:
        for asm,bina,hex,type in zip(Instructions_list_assembly,Instructions_list_binary,Instructions_list_hex,Instructions_list_type):
            if(index == len(Instructions_list_hex) - 1):
                f.write(hex + "\t" + asm + "\t" + bina + '\t' + type)
            else:
                f.write(hex + "\t" + asm + "\t" + bina + '\t' + type + '\n')
            index += 1


def convertAll(Instructions_list_assembly,Instructions_list_binary,Instructions_list_hex,Instructions_list_type,
               filenamePrefix,newfile = True):
    print('------------------------converting----------------------------')
    try:
        convertS(Instructions_list_assembly,filename = filenamePrefix + '.s',newfile = newfile)
        convertH(Instructions_list_hex,filename = filenamePrefix + '.hex',newfile = newfile)
        convertB(Instructions_list_binary,filename = filenamePrefix + '.binary',newfile = newfile)
        convertT(Instructions_list_type,filename = filenamePrefix + '.type',newfile = newfile)
        convertCombine(Instructions_list_assembly,Instructions_list_binary,Instructions_list_hex,Instructions_list_type,
               filename = filenamePrefix + '.asm',newfile = True)

        print("generate Finish!")
    except:
        raise Exception("failed to convert all")

