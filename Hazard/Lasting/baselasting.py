from Hazard.hazard import Hazard

class Lasting(Hazard):
    def __init__(self):
        super().__init__()

        self.tps = 1
        self.duration = None
        self.hazTick = 0
        self.appliedThisTick = False
    
    def applyOnEnter(self, effectInfo):
        if effectInfo.applied:
            pass
    
    def applyOnLeave(self, effectInfo):
        pass

    def determineEffectState(self):
        pass

    def update(self, tick):
        if not self.appliedThisTick:
            self.hazTick = 0
        else:
            self.hazTick += 1
            
        