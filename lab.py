# Nama: Hanzel Oclihar Tjiam
# NIM: 221402064

# Soal 2
class Person:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def BMI_Value(self):
        bmi = float((self.weight / (self.height)**2))
        return bmi
    
    def __eq__(self, other):
        if self.weight == other.weight and self.height == other.height:
            return True
        else:
            return False

x = Person(65, 1.65)
y = Person(70, 1.75)
z = Person(65, 1.65)

print(x == y)
print(z == x)