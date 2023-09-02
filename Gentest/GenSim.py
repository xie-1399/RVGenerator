import sys
sys.path.append("..")

import os
from Generator import API
RiscvtoolPath = "/opt/riscv/bin/"

# the version 1.2 will support sim the instruction and get the results log
# the first version can just simulation the arith instruction


def compileAsm(filePath,outPath):
    #.s -> excuable
    assert filePath.endswith(".s"),"must set the assemble file to simulation"
    linkedPath = "./File/link.lds"
    fileName = filePath.split("/")[-1].split(".")[0]
    destout = outPath + fileName + ".o"
    dest = outPath + fileName

    riscvas = RiscvtoolPath + "riscv64-unknown-elf-as"
    riscvld = RiscvtoolPath + "riscv64-unknown-elf-ld"
    print("convert the assmble file output")
    try:
        os.system(riscvas + " -march=rv32i -mabi=ilp32 -o {dest} {source}".format(dest = destout,source = filePath))
    except:
        raise Exception("riscvas the assmbler fail")
    print("link the elf")
    try:
        os.system(riscvld + " -m elf32lriscv -o {elf} {dest}".format(elf = fileName,dest = destout))
    except:
        raise Exception("link the elf fail")


def spikeSimulation(elfFile):
    spikePath = RiscvtoolPath + "spike"
    os.system(f"{spikePath} --isa=RV32I pk {elfFile}")


def simArith():
    #Gen inst first
    API.randomGen(withECALL=False, iter=100, testMul=False, onlyArith=True)

    #compile the code
    compileAsm("./File/test.s","./")

    # simulation with the spike
    spikeSimulation("./test")
if __name__ == '__main__':
    simArith()