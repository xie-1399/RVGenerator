# using the riscv-newop to test some

from rvnewop import RV32

def test_RVI(file):
    isa_model = RV32("32I")


def test_RV32IM(file):
    isa_model = RV32("32IM")


if __name__ == '__main__':
    isa_model = RV32("32IM")
    print(isa_model.decodeHex("f2d20e23"))