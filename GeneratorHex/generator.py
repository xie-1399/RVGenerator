from utils import Misc
import numpy as np
import random

# the isa model may not gen the normal run code

class RVIMGenerator():

    def __init__(self):
        self.Instructions_list_binary = []
        self.Instructions_list_assembly = []
        self.Instructions_list_hex = []
        self.Instructions_list_type = []

    def addInstruction(self,instructionBinary, instructionHex, instructionAssembly, instructionType):
        self.Instructions_list_hex.append(instructionHex)
        self.Instructions_list_assembly.append(instructionAssembly)
        self.Instructions_list_binary.append(instructionBinary)
        self.Instructions_list_type.append(instructionType)

    def genRandomReg(self,users1, users2, userd, randomArray):
        rs1 = random.choice(randomArray)
        rs1Binary = "{0:05b}".format(rs1)
        rs2 = random.choice(randomArray)
        rs2Binary = "{0:05b}".format(rs2)
        rd = random.choice(randomArray)
        rd_Binary = "{0:05b}".format(rd)

        if (users1 and users2 and userd):
            return rs1, rs2, rd, rs1Binary, rs2Binary, rd_Binary
        elif (userd and not users1 and not users2):
            return rd, rd_Binary
        elif (users1 and users2 and not userd):
            return rs1, rs2, rs1Binary, rs2Binary
        elif (users1 and userd and not users2):
            return rs1, rd, rs1Binary, rd_Binary

    def BinarytoHex(self,instructionBinary):
        return format(int(instructionBinary, 2), '08x')

    def generator_R(self,name, randomArray):
        # print("Gen R Type")
        try:
            opcode = Misc.I_OPCODES[name] if (name in Misc.I_OPCODES) else Misc.M_OPCODES[name]
            funct3 = Misc.I_FUNCT3[name] if (name in Misc.I_FUNCT3) else Misc.M_FUNCT3[name]
        except:
            raise Exception("please use illegal name to generator R type instruction")

        if (name == 'SUB' or name == "SRA"):
            funct7 = '0100000'
        elif name in Misc.M_EXTENSION_NAMES:
            funct7 = '0000001'
        else:
            funct7 = '0000000'
        rs1, rs2, rd, rs1Binary, rs2Binary, rd_Binary = self.genRandomReg(users1=True, users2=True, userd=True,
                                                                     randomArray=randomArray)
        instructionBinary = funct7 + rs2Binary + rs1Binary + funct3 + rd_Binary + opcode
        instructionHex = self.BinarytoHex(instructionBinary)
        instructionAssembly = str(name).lower() + " " + Misc.REG_NAME_ORDER[rd] + "," + \
                              Misc.REG_NAME_ORDER[rs1] + ',' + Misc.REG_NAME_ORDER[rs2]
        instructionType = 'R'
        self.addInstruction(instructionBinary, instructionHex, instructionAssembly, instructionType)


    def generator_I(self,name, randomArray):
        # print("Gen I Type")
        try:
            opcode = Misc.I_OPCODES[name]
            funct3 = Misc.I_FUNCT3[name]
        except:
            raise Exception("please use illegal name to generator I type instruction")
        rs1, rd, rs1Binary, rd_Binary = self.genRandomReg(users1=True, users2=False, userd=True,
                                                     randomArray=randomArray)
        if name in Misc.SHIFT_IMMEDIATE_INSTRUCTION_NAMES:
            if name == "SRAI":
                imm = '0100000'
            else:
                imm = '0000000'
            shamt_random = np.random.randint(0, 32)  # [0,32)
            shamt_binary = "{0:05b}".format(shamt_random)
            instructionBinary = imm + shamt_binary + rs1Binary + funct3 + rd_Binary + opcode
            instructionHex = self.BinarytoHex(instructionBinary)
            instructionAssembly = str(name).lower() + " " + Misc.REG_NAME_ORDER[rd] + "," + \
                                  Misc.REG_NAME_ORDER[rs1] + ',' + str(shamt_random)
            instructionType = 'I'
        elif name in Misc.LOAD_INSTRUCTION_NAMES:
            memoryOffset = np.random.randint(0, 4095)
            memory_binary = "{0:012b}".format(memoryOffset)
            instructionBinary = memory_binary + rs1Binary + funct3 + rd_Binary + opcode
            instructionHex = self.BinarytoHex(instructionBinary)
            instructionAssembly = str(name).lower() + " " + Misc.REG_NAME_ORDER[rd] + "," + str(memoryOffset) + '(' + \
                                  Misc.REG_NAME_ORDER[rs1] + ')'
            instructionType = 'I'
        elif name in Misc.ECALL_EBREAK_NAMES:
            if (name) == "ECALL":
                imm = '000000000000'
                instructionAssembly = 'ecall'
            else:
                imm = '000000000001'
                instructionAssembly = 'ebreak'
            instructionBinary = imm + rs1Binary + funct3 + rd_Binary + opcode
            instructionHex = self.BinarytoHex(instructionBinary)
            instructionType = 'I'

        else:
            imm_decimal = np.random.randint(0, 4095)
            imm_binary = "{0:012b}".format(imm_decimal)
            instructionBinary = imm_binary + rs1Binary + funct3 + rd_Binary + opcode
            instructionHex = self.BinarytoHex(instructionBinary)
            instructionAssembly = str(name).lower() + " " + Misc.REG_NAME_ORDER[rd] + "," + Misc.REG_NAME_ORDER[
                rs1] + "," + str(imm_decimal)
            instructionType = 'I'
        self.addInstruction(instructionBinary, instructionHex, instructionAssembly, instructionType)

    def generator_S(self,name, randomArray):
        # print('Gen S Type')
        try:
            opcode = Misc.I_OPCODES[name]
            funct3 = Misc.I_FUNCT3[name]
        except:
            raise Exception("please use illegal name to generator S type instruction")
        rs1, rs2, rs1Binary, rs2Binary = self.genRandomReg(users1=True, users2=True, userd=False,
                                                      randomArray=randomArray)
        imm_decimal = 2 * np.random.randint(0, 2047)
        imm_binary = "{0:012b}".format(imm_decimal)
        instructionBinary = imm_binary[0:7] + rs2Binary + rs1Binary + funct3 + imm_binary[7:] + opcode
        instructionAssembly = str(name).lower() + " " + Misc.REG_NAME_ORDER[rs2] + "," + str(imm_decimal) + '(' + \
                              Misc.REG_NAME_ORDER[rs1] + ')'
        instructionHex = self.BinarytoHex(instructionBinary)
        instructionType = 'S'
        self.addInstruction(instructionBinary, instructionHex, instructionAssembly, instructionType)

    def generator_B(self,name,randomArray):
        # print('Gen B Type')
        try:
            opcode = Misc.I_OPCODES[name]
            funct3 = Misc.I_FUNCT3[name]
        except:
            raise Exception("please use illegal name to generator B type instruction")
        rs1, rs2, rs1Binary, rs2Binary = self.genRandomReg(users1=True, users2=True, userd=False,
                                                           randomArray=randomArray)
        # the imm should be in the instruction number and %4 == 0
        imm_decimal = 2 * np.random.randint(0, (len(self.Instructions_list_binary) + 1) * 2)
        while imm_decimal == len(self.Instructions_list_binary) * 4:
            return
        imm_binary = "{0:012b}".format(imm_decimal)
        instructionBinary = imm_binary[0] + imm_binary[2:8] + rs2Binary + rs1Binary + funct3 + \
                             imm_binary[8:] + imm_binary[1] + opcode
        instructionHex = self.BinarytoHex(instructionBinary)
        instructionType = 'B'
        instructionAssembly = str(name).lower() + " " + Misc.REG_NAME_ORDER[rs1] + "," + Misc.REG_NAME_ORDER[rs2] + ',' + str(imm_decimal)
        self.addInstruction(instructionBinary, instructionHex, instructionAssembly, instructionType)

    def generator_U(self,name,randomArray):
        # print("Gen U Type")
        try:
            opcode = Misc.I_OPCODES[name]
        except:
            raise Exception("please use illegal name to generator U type instruction")
        rd, rd_Binary = self.genRandomReg(users1=False,users2=False,userd=True,
                                        randomArray=randomArray)
        imm_decimal = np.random.randint(0, 1048575)
        imm_binary = "{0:020b}".format(imm_decimal)
        instructionBinary = imm_binary + rd_Binary + opcode
        instructionHex = self.BinarytoHex(instructionBinary)
        instructionAssembly = str(name).lower() + ' ' + Misc.REG_NAME_ORDER[rd] + ',' + str(imm_decimal)
        instructionType = 'U'
        self.addInstruction(instructionBinary, instructionHex, instructionAssembly, instructionType)

    def generator_J(self,name,randomArray):
        # print('Gen J Type')
        try:
            opcode = Misc.I_OPCODES[name]
        except:
            raise Exception("please use illegal name to generator J type instruction")
        rd, rd_Binary = self.genRandomReg(users1=False, users2=False, userd=True,
                                          randomArray=randomArray)
        imm_decimal = 2 * np.random.randint(0, (len(self.Instructions_list_binary) + 1) * 2)
        while imm_decimal == len(self.Instructions_list_binary) * 4:
            return
        imm_binary = "{0:020b}".format(imm_decimal)
        instructionBinary = imm_binary[0] + imm_binary[10:] + imm_binary[9] + imm_binary[1:9] + rd_Binary + opcode
        instructionHex = self.BinarytoHex(instructionBinary)
        instructionAssembly = str(name).lower() + ' ' + Misc.REG_NAME_ORDER[rd] + ',' + str(imm_decimal)
        instructionType = 'J'
        self.addInstruction(instructionBinary, instructionHex, instructionAssembly, instructionType)

    def show(self):
        print(self.Instructions_list_binary)
        print(self.Instructions_list_assembly)
        print(self.Instructions_list_hex)
        print(self.Instructions_list_type)


