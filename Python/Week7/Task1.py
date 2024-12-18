# 1. A complex number is a number that can be expressed 
# in the form a + bi, where a and b are real numbers 
# and i is the imaginary unit.
# Create class Complex with attributes, 
# constructors and getters/setters.

class Complex:

    type = 'complex number'

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def getComplex(self):
        return  "{}+{}i".format(self.real, self.imaginary)

    def setReal(self, real):
        self.real = real
    def setImaginary(self, imaginary):
        self.imaginary = imaginary

complexNro = Complex(10,20)
print(complexNro.getComplex())
print(Complex.type)

complexNro.setReal(20)
complexNro.setImaginary(30)
print(complexNro.getComplex())