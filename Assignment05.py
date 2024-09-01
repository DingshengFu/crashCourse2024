#超类 LogicGate
class LogicGate:
    def __init__(self, name):
        self.name = name
        self.output = None

    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class  BinaryGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)
        self.pinA = None
        self.pinB = None

    def getPinA(self): 
        return int(input("Enter Pin A input for gate " + self.getName() + "-->")) 

    def getPinB(self): 
        return int(input("Enter Pin B input for gate " + self.getName() + "-->"))
    
class UnaryGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)
        self.pin = None

    def getPin(self): 
        return int(input("Enter Pin input for gate " + self.getName() + "-->"))

class AndGate(BinaryGate): 
    def __init__(self, name): 
        super().__init__(name) 

    def performGateLogic(self): 
        a = self.getPinA() 
        b = self.getPinB() 
        if a==1 and b==1: 
            return 1 
        else: 
            return 0
        
class OrGate(BinaryGate): 
    def __init__(self, name):
        super().__init__(name) 

    def performGateLogic(self): 
        a = self.getPinA() 
        b = self.getPinB() 
        if a==1 or b==1: 
            return 1 
        else: 
            return 0 
        
class NotGate(UnaryGate): 
    def __init__(self, name): 
        super().__init__(name) 

    def performGateLogic(self): 
        a = self.getPin() 
        if a==1: 
            return 0 
        else: 
            return 1 


# Test the gates    
class TestGates: 
    def main(): 
        andGate = AndGate("AND") 
        orGate = OrGate("OR") 
        notGate = NotGate("NOT") 

        print("Output of AND gate is", andGate.getOutput()) 
        print("Output of OR gate is", orGate.getOutput()) 
        print("Output of NOT gate is", notGate.getOutput()) 

    if __name__ == "__main__": 
        main()



