import sys
sys.path.append("..")

from Generator import GenIM
# use the api to generate the inst
from utils import FileOperation
from Gentest import IMTest
import argparse

'''
@@ version1 : generate all instructions and can be compiled but not sim about them @@

Example:
test it: /usr/bin/python3.6 API.py --test --iter 1000 --ecall
gen it : /usr/bin/python3.6 API.py --iter 1000 --mul --ecall

only gen arith : /usr/bin/python3.6 API.py --iter 1000 --arith

next version 1.2 :
(1) fix the asm file format (√)
(2) sim the generator assembly and get the log
(3) Update the ReadMe 
'''


def randomTest(testMul = False,withECALL = False,iter = 100,onlyArith = False,initial = False):
    gen = GenIM.RandomIMGenerator(withECALL= withECALL, withMul=testMul, reName=True,
                                  iter=iter, CurInst=0,onlyArith=onlyArith)
    assert not testMul,"test mul using another way"
    gen.RandomProduce(initial=initial)
    FileOperation.convertAll(gen.Instructions_list_assembly, gen.Instructions_list_binary,
                             gen.Instructions_list_hex, gen.Instructions_list_type, filenamePrefix="test", newfile=True)
    IMTest.test_R_I("../Gentest/File/test.hex", "../Gentest/File/test.s", "../Gentest/File/test.type")
    print("Random test success:)")


# can gen mul and ecall/ebreak instruction
def randomGen(testMul = False,withECALL = False,iter = 100,onlyArith=False,initial = False):
    gen = GenIM.RandomIMGenerator(withECALL= withECALL, withMul=testMul, reName=True,
                                  iter=iter, CurInst=0,onlyArith=onlyArith)
    gen.RandomProduce(initial=initial)
    FileOperation.convertAll(gen.Instructions_list_assembly, gen.Instructions_list_binary,
                             gen.Instructions_list_hex, gen.Instructions_list_type, filenamePrefix="test", newfile=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= "generate the instruction or test it")
    parser.add_argument('--test',action='store_true',help="test it")
    parser.add_argument('--mul',action='store_true',help="gen with mul")
    parser.add_argument('--ecall',action='store_true',help="gen with ecall")
    parser.add_argument('--iter',type = int, required=True ,help="inst number")
    parser.add_argument('--arith',action='store_true',help = "gen the arith inst")
    parser.add_argument('--init',action='store_true',help = "gen with initial inst reg")
    args = parser.parse_args()

    withECALL = args.ecall
    testMul = args.mul
    iter = args.iter

    if(args.test):
        randomTest(withECALL= withECALL,iter = iter,onlyArith=args.arith,initial = args.init)
    else:
        randomGen(withECALL=withECALL,iter = iter,testMul = testMul,onlyArith=args.arith,initial = args.init)


