'''
#Super Function example
class GC:

    def __init__(self):
        print("in GC init")

    def CH1(self):
        print("Asus RTX3060")

    def CH2(self):
        print("Zotac RTX3080")

class GB(GC):

    def __init__(self):
        super().__init__()
        print("in GB init")

    def CH3(self):
        print("Msi RTX3080S 8GB")

gc1 = GB()
'''
#MRO(Method Resolution Order)which starts from left to right
class GC:

    def __init__(self):
        print("in GC init")

    def CH1(self):
        print("Asus confg1 RTX3060")

    def CH2(self):
        print("Zotac RTX3080")

class GB:

    def __init__(self):
        print("in GB init")

    def CH3(self):
        print("Msi confg1 RTX3080S 8GB")

class Product(GC,GB):

    def __init__(self):
        super().__init__()
        print("in Product init")

    def CH4(self):
       print("Nvidia Product")

    def CH(self):
        super().CH2()

gc1 = Product()
gc1.CH()
