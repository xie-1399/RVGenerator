import sys
sys.path.append("..")
# use the api to generate the inst
import GenIM
from utils import FileOperation
from Test import IMTest
import argparse

'''
@@ version1 : generate all instructions and can be compiled but not sim about them @@

Example:
test it: /usr/bin/python3.6 API.py --test --iter 1000 --ecall
gen it : /usr/bin/python3.6 API.py --iter 1000 --mul --ecall
'''


def randomTest(testMul = False,withECALL = False,iter = 100):
    gen = GenIM.RandomIMGenerator(withECALL= withECALL, withMul=testMul, reName=True,
                                  iter=iter, CurInst=0)
    assert not testMul,"test mul using another way"
    gen.RandomProduce()
    FileOperation.convertAll(gen.Instructions_list_assembly, gen.Instructions_list_binary,
                             gen.Instructions_list_hex, gen.Instructions_list_type, filenamePrefix="test", newfile=True)
    IMTest.test_R_I("../Test/File/test.hex", "../Test/File/test.s", "../Test/File/test.type")
    print("Random test success:)")


# can gen mul and ecall/ebreak instruction
def randomGen(testMul = False,withECALL = False,iter = 100):
    gen = GenIM.RandomIMGenerator(withECALL= withECALL, withMul=testMul, reName=True,
                                  iter=iter, CurInst=0)
    gen.RandomProduce()
    FileOperation.convertAll(gen.Instructions_list_assembly, gen.Instructions_list_binary,
                             gen.Instructions_list_hex, gen.Instructions_list_type, filenamePrefix="test", newfile=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= "generate the instruction or test it")
    parser.add_argument('--test',action='store_true',help="test it")
    parser.add_argument('--mul',action='store_true',help="gen with mul")
    parser.add_argument('--ecall',action='store_true',help="gen with ecall")
    parser.add_argument('--iter',type = int, required=True ,help="inst number")
    args = parser.parse_args()

    withECALL = args.ecall
    testMul = args.mul
    iter = args.iter

    if(args.test):
        randomTest(withECALL= withECALL,iter = iter)
    else:
        randomGen(withECALL=withECALL,iter = iter,testMul = testMul)


