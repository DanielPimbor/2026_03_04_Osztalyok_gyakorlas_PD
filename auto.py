class Auto:
    def __init__(self, marka_, tipus_, gyartasi_ev, fogyasztas_ = 7.5, uzemanyag_=50):
        self.marka = marka_
        self.tipus = tipus_
        self.gyartasi_ev = gyartasi_ev
        self.sebesseg = 0
        self.fogyasztas = fogyasztas_
        self.uzemanyag= uzemanyag_
    
    def __str__(self):
        return f'{self.marka} {self.tipus} ({self.gyartasi_ev}) sebesség: {self.sebesseg} km/h'
    
    def gyorsit(self, ertek):
        self.sebesseg += ertek
        if self.sebesseg > 200:
            self.sebesseg = 200
            print('200-al mész.')

    def fekezz(self, ertek):
        self.sebesseg -= ertek
        if self.sebesseg < 0:
            self.sebesseg = 0
            print('Megálltál')

#mindegy hogy erteek vagy mennyiseg azzal csak megnevezzuk

    def tankol(self, mennyiseg):
        self.uzemanyag += mennyiseg
        if self.uzemanyag > 50:
            self.uzemanyag = 50
            print('Tele a tank.')