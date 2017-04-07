import Zero
import Events
import Property
import VectorMath

class TreySymbol:
    def DefineProperties(self):
        self.Start = Property.Bool(True)
        self.Start2 = Property.Bool(False)

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)

    def OnLogicUpdate(self, UpdateEvent):
        Trey = self.Space.FindObjectByName("Trey")
        
        if(Trey):
            if(self.Start == True):
                self.Owner.Sprite.Visible = True
                self.Start2 = True
                self.Start = False
        else:
            if(self.Start2 == True):
                self.Owner.Sprite.Visible = False
                self.Start = True
                self.Start2 = False

Zero.RegisterComponent("TreySymbol", TreySymbol)