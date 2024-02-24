import numpy as np

class Perceptron:
    # どっちも1の時だけ1を返す
    def AND(x1:int, x2:int)->int:
        w1, w2, theta = 0.5, 0.5, 0.7
        tmp = x1*w1 + x2*w2
        if tmp <= theta:
            return 0
        elif tmp > theta:
            return 1
        

    # どっちかが1の時1を返す
    def OR(x1:int, x2:int)->int:
        w1, w2, theta = 0.5, 0.5, 0.3
        tmp = x1*w1 + x2*w2
        if tmp <= theta:
            return 0
        elif tmp > theta:
            return 1
    
    def NAND(x1:int, x2:int)->int:
        w1, w2, theta = -0.5, -0.5, -0.7
        tmp = x1*w1 + x2*w2
        if tmp <= theta:
            return 0
        elif tmp > theta:
            return 1
        
    def AND_WITH_BIAS(x1:int, x2:int)->int:
        x = np.array([x1, x2])
        w = np.array([0.5, 0.5])
        b = -0.7
        tmp = np.sum(w*x) + b
        if tmp <= 0:
            return 0
        else:
            return 1
    
    def XOR(x1:int, x2:int)->int:
        s1 = instance.NAND(x1, x2)
        s2 = instance.OR(x1, x2)
        y = instance.AND(s1, s2)
        return y
        
instance = Perceptron
print(instance.AND(0, 0))
print(instance.AND(1, 0))
print(instance.AND(0, 1))
print(instance.AND(1, 1))

print(instance.OR(0, 0))
print(instance.OR(1, 0))
print(instance.OR(0, 1))
print(instance.OR(1, 1))

print(instance.NAND(0, 0))
print(instance.NAND(1, 0))
print(instance.NAND(0, 1))
print(instance.NAND(1, 1))

print(instance.AND_WITH_BIAS(0, 0))
print(instance.AND_WITH_BIAS(1, 0))
print(instance.AND_WITH_BIAS(0, 1))
print(instance.AND_WITH_BIAS(1, 1))

print(instance.XOR(0, 0))
print(instance.XOR(1, 0))
print(instance.XOR(0, 1))
print(instance.XOR(1, 1))