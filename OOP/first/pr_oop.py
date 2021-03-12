class Element:
    
    
    def agrigate_state (self, t, konv):
        if konv == 'f':
            t = Iron.convert_to_c(self, t)
        elif konv == 'k':
            t = Iron.convert_to_k(self, t)
        if t < self.t_solid:
            return 'solid'
        elif t > self.t_gas:
            return 'gas'
        else:
            return 'liquid'




    def convert_to_c(self, t):
        return (t - 32) * 5 / 9
d
    def convert_to_k(self, t):
        return 273.15 + t


class Iron(Element):
    t_solid = 1537
    t_gas = 2861
    






elem= Iron()

print(elem.agrigate_state(1460, 'f'))
