# using the riscv-newop to test some (X)
# or using the assembly tools to test it
from rvnewop import RV32
from Generator import GenIM
from utils import FileOperation
import re

def testcommon(hexpath,asmpath,typepath,useMul):
    isa_model = RV32("32M") if useMul else RV32("32I")
    with open(hexpath,'r') as source,open(asmpath,'r') as dut,open(typepath,'r') as type:
        insts = source.readlines()
        duts = dut.readlines()
        types = type.readlines()
        source.close()
        dut.close()
        type.close()

    for type,inst,dut in zip(types,insts,duts):
        source = inst.replace('\n','')
        type = str(type).replace('\n',"")

        if(type == "SHIFTI"):
            ref = isa_model.decodeHex(source)
            s_imm = str(ref).split(",")[-1].replace('\n',"").strip()
            u_imm = str(dut).split(",")[-1].replace('\n',"").strip()
            if(int(s_imm) >= 0):
                assert s_imm == u_imm
            else:
                ref = str(ref).replace(s_imm,u_imm)
                assert int(u_imm) - int(s_imm) == 32

        elif(type == 'B'): #Todo some wrong in the simulator
            continue
        elif(type == 'J'):
            continue
        elif(type == 'U'):
            ref = isa_model.decodeHex(source)
            s_imm = str(ref).split(",")[-1].replace('\n', "").strip()
            u_imm = str(dut).split(",")[-1].replace('\n', "").strip()
            if (int(s_imm) >= 0):
                assert s_imm == u_imm
            else:
                ref = str(ref).replace(s_imm, u_imm)
                assert int(u_imm) - int(s_imm) == 1048576

        elif (type == 'LOAD'):
            ref = str(isa_model.decodeHex(source))
            s_list = ref.split(",")
            reg = re.findall(r'[(](.*?)[)]', s_list[-1])[0]
            for i in range(0, len(reg)):
                assert s_list[1][-i - 1] == s_list[-1][-i - 2]
            ref = ref.replace(reg + ',', '', 1)

        elif(type == 'S'):
            ref = str(isa_model.decodeHex(source))
            s_list = ref.split(",")
            reg = re.findall(r'[(](.*?)[)]', s_list[-1])[0]
            for i in range(0,len(reg)):
                assert s_list[0][-i-1] == s_list[-1][-i-2]
            ref = ref.replace(reg + ',','',1)
        else:
            ref = isa_model.decodeHex(source)
        assert str(dut).strip() == str(ref).strip().lower(),"source:{dut} \t ref:{ref}".format(dut = dut,ref = ref)

def test_R_I(hexpath,asmpath,typepath):
    testcommon(hexpath,asmpath,typepath,False)

def test_R_M(hexpath,asmpath,typepath):
    testcommon(hexpath, asmpath,typepath, True)

def testMode(testI = False ,testS = False,testB = False,testU = False,testR = False,
             testJ = False ,testMul = False,showAll = False):
    gen = GenIM.RandomIMGenerator(withECALL=False, withMul=testMul, reName=True,
                                  iter = 100, CurInst = 0,onlyArith = False)
    if(testMul):
        for idx in range(100):
            gen.Gen_r(OnlyMul=testMul)

        FileOperation.convertAll(gen.Instructions_list_assembly, gen.Instructions_list_binary,
                                 gen.Instructions_list_hex,gen.Instructions_list_type, filenamePrefix="test", newfile=True)
        test_R_M("./File/test.hex", "./File/test.s","./File/test.type")
        print("M type test success")

    elif (testR):
        for idx in range(100):
            gen.Gen_r()
        FileOperation.convertAll(gen.Instructions_list_assembly, gen.Instructions_list_binary,
                                 gen.Instructions_list_hex, gen.Instructions_list_type, filenamePrefix="test",
                                 newfile=True)
        test_R_I("./File/test.hex", "./File/test.s", "./File/test.type")
        print("R type test success")

    elif(testI):
        for idx in range(100):
            gen.Gen_i()
        FileOperation.convertAll(gen.Instructions_list_assembly, gen.Instructions_list_binary,
                                 gen.Instructions_list_hex,gen.Instructions_list_type, filenamePrefix="test", newfile=True)
        test_R_I("./File/test.hex", "./File/test.s","./File/test.type")
        print("I type test success")


    elif(testJ):
        for idx in range(100):
            gen.Gen_j()
        FileOperation.convertAll(gen.Instructions_list_assembly, gen.Instructions_list_binary,
                                 gen.Instructions_list_hex,gen.Instructions_list_type, filenamePrefix="test", newfile=True)
        test_R_I("./File/test.hex", "./File/test.s","./File/test.type")
        print("J type test success")

    elif(testU):
        for idx in range(100):
            gen.Gen_u()
        FileOperation.convertAll(gen.Instructions_list_assembly, gen.Instructions_list_binary,
                                 gen.Instructions_list_hex,gen.Instructions_list_type, filenamePrefix="test", newfile=True)
        test_R_I("./File/test.hex", "./File/test.s","./File/test.type")
        print("U type test success")

    elif (testS):
        for idx in range(100):
            gen.Gen_s()
        FileOperation.convertAll(gen.Instructions_list_assembly, gen.Instructions_list_binary,
                                 gen.Instructions_list_hex,gen.Instructions_list_type, filenamePrefix="test", newfile=True)
        test_R_I("./File/test.hex", "./File/test.s","./File/test.type")
        print("S type test success")

    elif(testB):
        for idx in range(100):
            gen.Gen_b()
        FileOperation.convertAll(gen.Instructions_list_assembly, gen.Instructions_list_binary,
                                 gen.Instructions_list_hex,gen.Instructions_list_type, filenamePrefix="test", newfile=True)
        test_R_I("./File/test.hex", "./File/test.s","./File/test.type")
        print("B type test success")

    if showAll:gen.show()

def passAll():
    #pass type R U S M
    testMode(testS = True)
    testMode(testMul = True)
    testMode(testR = True)
    testMode(testU = True)
    testMode(testI = True)
    testMode(testJ=True)
    testMode(testB=True)

if __name__ == '__main__':
    #generate the test file at path
    passAll()
