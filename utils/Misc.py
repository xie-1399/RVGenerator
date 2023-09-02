
# useful constant information
import numpy as np

I_OPCODES = dict(LUI='0110111', AUIPC='0010111', JAL='1101111', JALR='1100111', BEQ='1100011', BNE='1100011',
               BLT='1100011', BGE='1100011', BLTU='1100011', BGEU='1100011', LB='0000011', LH='0000011', LW='0000011',
               LBU='0000011', LHU='0000011', SB='0100011', SH='0100011', SW='0100011', ADDI='0010011', SLTI='0010011',
               SLTIU='0010011', XORI='0010011', ORI='0010011', ANDI='0010011', SLLI='0010011', SRLI='0010011',
               SRAI='0010011', ADD='0110011', SUB='0110011', SLL='0110011', SLT='0110011', SLTU='0110011',
               XOR='0110011', SRL='0110011', SRA='0110011', OR='0110011', AND='0110011',ECALL = "1110011",EBREAK = "1110011"
            )

I_FUNCT3 = dict(JALR='000', BEQ='000', BNE='001', BLT='100', BGE='101', BLTU='110', BGEU='111', LB='000', LH='001',
              LW='010', LBU='100', LHU='101', SB='000', SH='001', SW='010', ADDI='000', SLTI='010', SLTIU='011',
              XORI='100', ORI='110', ANDI='111', SLLI='001', SRLI='101', SRAI='101', ADD='000', SUB='000',
              SLL='001', SLT='010', SLTU='011', XOR='100', SRL='101', SRA='101', OR='110', AND='111',ECALL = '000',EBREAK = '000')

M_FUNCT3 = dict(MUL='000',MULH='001', MULHSU='010', MULHU='011',
                DIV='100', DIVU='101', REM='110', REMU='111')

M_OPCODES = dict(MUL='0110011', MULH='0110011',MULHSU='0110011',MULHU='0110011',
                 DIV='0110011', DIVU='0110011', REM='0110011', REMU='0110011')


SHIFT_IMMEDIATE_INSTRUCTION_NAMES = {'SLLI', 'SRLI', 'SRAI'}

# call the I type name
I_TYPE_NAME = {'ADDI','XORI','ORI','ANDI','SLLI','SRLI','SRAI','SLTI','SLTIU','JALR'}
ECALL_EBREAK_NAMES = {'ECALL','EBREAK'}
LOAD_INSTRUCTION_NAMES = {'LB', 'LH', 'LW', 'LBU', 'LHU'}
FULL_I_TYPE_NAME = I_TYPE_NAME.union(LOAD_INSTRUCTION_NAMES).union(ECALL_EBREAK_NAMES)
I_TYPENAME_NOECALL = I_TYPE_NAME.union(LOAD_INSTRUCTION_NAMES)

# call the R type name
I_R_TYPE_NAME = {'ADD','SUB','XOR','OR','AND','SLL','SRL','SRA','SLT','SLTU'}
M_EXTENSION_NAMES = {'MUL', 'MULH', 'MULHSU', 'MULHU', 'DIV', 'DIVU', 'REM', 'REMU'}
R_TYPE_NAME = M_EXTENSION_NAMES.union(I_R_TYPE_NAME)

#use the ArithOnly
ARITH_NAME = {'ADDI','XORI','ORI','ANDI','SLLI','SRLI','SRAI','SLTI','SLTIU'}

#call S type name
STORE_INSTRUCTION_NAMES = {'SB', 'SH', 'SW'}

#call B type name
B_TYPE_NAME = {'BEQ','BNE','BLT','BGE','BLTU','BGEU'}

#call J type name
J_TYPE_NAME = {'JAL'}

#call u type name
U_TYPE_NAME = {'LUI','AUIPC'}

REG_NAME_ORDER = ["x" + str(i) for i in range(0,32)]

REG_NAME = ['zero','ra','sp','gp','tp','t0','t1','t2','s0','s1',
            'a0','a1','a2','a3','a4','a5','a6','a7','s2','s3',
            's4','s5','s6','s7','s8','s9','s10','s11','t3','t4','t5','t6']

