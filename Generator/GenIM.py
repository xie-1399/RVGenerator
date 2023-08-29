# use to random generator I type

import random
from utils import Misc
import numpy as np
from Generator import generator

class RandomIMGenerator(generator.RVIMGenerator):
    def __init__(self, reName,withMul, withECALL,iter,CurInst): #start from 0
        super().__init__(reName)
        self.withMul = withMul
        self.withECALL = withECALL
        self.iter = iter
        self.cur = CurInst

    def Gen_r(self,iter = 1,REGISTERS_NUMBER = 32,OnlyMul = False):
        for idx in range(iter):
            name = list(Misc.I_R_TYPE_NAME)[random.randint(0, len(Misc.I_R_TYPE_NAME) - 1)] if not self.withMul else \
                list(Misc.R_TYPE_NAME)[random.randint(0, len(Misc.R_TYPE_NAME) - 1)]
            if(OnlyMul):
                name = list(Misc.M_EXTENSION_NAMES)[random.randint(0, len(Misc.M_EXTENSION_NAMES) - 1)]
            REGISTERS_TO_USE = np.random.randint(0, REGISTERS_NUMBER, size=10)
            self.generator_R(name,randomArray=REGISTERS_TO_USE)

    def Gen_i(self,iter = 1,REGISTERS_NUMBER = 32,withECALL = False):
        for idx in range(iter):
            name = list(Misc.FULL_I_TYPE_NAME)[random.randint(0, len(Misc.FULL_I_TYPE_NAME) - 1)] if self.withECALL \
                else list(Misc.I_TYPENAME_NOECALL)[random.randint(0, len(Misc.I_TYPENAME_NOECALL) - 1)]
            REGISTERS_TO_USE = np.random.randint(0, REGISTERS_NUMBER, size=10)
            self.generator_I(name,randomArray=REGISTERS_TO_USE)

    def Gen_s(self,iter = 1,REGISTERS_NUMBER = 32):
        for idx in range(iter):
            name = list(Misc.STORE_INSTRUCTION_NAMES)[random.randint(0, len(Misc.STORE_INSTRUCTION_NAMES) - 1)]
            REGISTERS_TO_USE = np.random.randint(0, REGISTERS_NUMBER, size=10)
            self.generator_S(name,randomArray=REGISTERS_TO_USE)

    def Gen_b(self,iter = 1,REGISTERS_NUMBER = 32):
        for idx in range(iter):
            name = list(Misc.B_TYPE_NAME)[random.randint(0, len(Misc.B_TYPE_NAME) - 1)]
            REGISTERS_TO_USE = np.random.randint(0, REGISTERS_NUMBER, size=10)
            self.generator_B(name,randomArray=REGISTERS_TO_USE,iter = self.iter,currentInst = self.cur)

    def Gen_j(self,iter = 1,REGISTERS_NUMBER = 32):
        for idx in range(iter):
            name = list(Misc.J_TYPE_NAME)[random.randint(0, len(Misc.J_TYPE_NAME) - 1)]
            REGISTERS_TO_USE = np.random.randint(0, REGISTERS_NUMBER, size=10)
            self.generator_J(name,randomArray=REGISTERS_TO_USE,iter = self.iter,currentInst = self.cur)

    def Gen_u(self,iter = 1,REGISTERS_NUMBER = 32):
        for idx in range(iter):
            name = list(Misc.U_TYPE_NAME)[random.randint(0, len(Misc.U_TYPE_NAME) - 1)]
            REGISTERS_TO_USE = np.random.randint(0, REGISTERS_NUMBER, size=10)
            self.generator_U(name,randomArray=REGISTERS_TO_USE)

    def RandomProduce(self):
        for i in range(self.iter):
            func = [self.Gen_i,self.Gen_r,self.Gen_s,self.Gen_u,self.Gen_j,self.Gen_b]
            genFunc = random.choice(func)
            genFunc()
            self.cur += 1
