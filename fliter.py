
import numpy as np



class Filter():

    def __init__(self,InputSignal,OutSignal,SigmaX,KernalSize,FilterType):
        self.InputSignal = InputSignal
        self.SigmaX = SigmaX
        self.OutSignal = OutSignal
        self.KernalSize =KernalSize
        self.FilterType = FilterType

    def GuassFilter(self):
        '''一维GUASSFliter'''
        kernal = np.zeros((1, self.KernalSize))
        centerX = self.KernalSize // 2
        sum = 0

        for i in range(0, self.KernalSize):
            kernal[0][i] = np.exp(- (((i-centerX)*(i-centerX)) / (2.0*self.SigmaX*self.SigmaX))*(1-(i-centerX)*(i-centerX)/(self.SigmaX*self.SigmaX)))
            sum += kernal[0][i]


        for i in range(0, self.KernalSize):
            kernal[0][i] = kernal[0][i] / sum


        for r in range(0, len(self.InputSignal)):
            if (r - self.KernalSize // 2 >= 0 and r + self.KernalSize // 2 <= len(self.InputSignal)-1):
                for i in range(0, self.KernalSize):
                    sum += kernal[0][i] * self.InputSignal[r - self.KernalSize//2+i]

        self.OutSignal.pop(0)
        self.OutSignal.append(sum)
        return self.OutSignal


    def MineFliter(self):
        '''最小值Fliter'''
        kernal = np.zeros((self.KernalSize, self.KernalSize))
        centerX = self.KernalSize // 2
        KernalList = []
        MinNumber = 0

        for r in range(0, len(self.InputSignal)):
            KernalList.clear()
            if (r - self.KernalSize // 2 >= 0 and r + self.KernalSize // 2 <= len(self.InputSignal)-1):
                for i in range(0, self.KernalSize):
                    KernalList.append(self.InputSignal[r - self.KernalSize//2+i])
                MinNumber = min(KernalList)
            self.OutSignal.pop(0)
            self.OutSignal.append(MinNumber)



        return self.OutSignal



    def main(self):
        if self.FilterType == 0:
            OutSignal = self.GuassFilter()
        if self.FilterType == 1:
            OutSignal = self.MineFliter()
        return OutSignal





