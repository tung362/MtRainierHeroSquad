import Zero
import Events
import Property
import VectorMath

class SedrickSymbol:
    def DefineProperties(self):
        self.Start = Property.Bool(True)
        self.Start2 = Property.Bool(False)

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)

    def OnLogicUpdate(self, UpdateEvent):
        Sedrick = self.Space.FindObjectByName("Sedrick")
        
        if(Sedrick):
            if(self.Start == True):
                self.Owner.Sprite.Visible = True
                self.Start2 = True
                self.Start = False
        else:
            if(self.Start2 == True):
                self.Owner.Sprite.Visible = False
                self.Start = True
                self.Start2 = False

Zero.RegisterComponent("SedrickSymbol", SedrickSymbol)