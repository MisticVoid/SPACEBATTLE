class KeyState:
    def __init__(self,actionSingleClick=None,actionHold=None):
        self.pressed = False
        self.used = False
        self.actionSingleClick = actionSingleClick
        self.actionHold = actionHold

    def press(self)->None:
        self.pressed = True

    def use(self)->None:
        self.used = True

    def release(self)->None:
        self.pressed = False
        self.used = False

    def hold(self)->bool:
        return self.pressed

    def singleClick(self)->bool:
        return self.pressed and not self.used

    def singleUse(self)->bool:
        if self.pressed and not self.used:
            self.used=True
            return True
        return False

    def execSingle(self, *args, **kwargs):
        if self.singleUse():
            self.actionSingleClick(*args, **kwargs)

    def execHold(self, *args, **kwargs):
        if self.pressed:
            self.actionHold(*args, **kwargs)
