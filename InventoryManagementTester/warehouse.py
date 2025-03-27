import pallet as p



class bay:
    def __init__(self, id, pallets):
        self.id = id
        self.pallets = []

    def insert(self, pallet):
        self.pallets.append(pallet)

class warehouse: 
    bays = {}
    def __init__(self):
        temp = []
        for c in "abcde":
            for i in "12345":
                temp.append(c+i)

        for i in range(len(temp)):
            self.bays.update({temp[i]:[]})




        
        