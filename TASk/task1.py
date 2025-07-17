class Avtomobil:
    def __init__(self, marka, il, reng):
        self.marka = marka 
        self.il = il
        self.reng = reng 
    def tesvir(self):
        print(f"Bu avtomobil {self.marka} markalidir, {self.il}-ci ilindir, {self.reng} renglidir.")
menim_avtomobilim = Avtomobil("Toyota", 2015, "qirmizi")
menim_avtomobilim.tesvir()