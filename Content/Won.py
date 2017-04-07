import Zero
import Events
import Property
import VectorMath

class Won:
    def DefineProperties(self):
        #self.Lives = Property.Int(9)
        pass

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)

    def OnLogicUpdate(self, UpdateEvent):
        AirBalloon = self.Space.FindObjectByName("AirBalloonBasket")
        
        if(AirBalloon.AirBalloonBasket.HasCollided is True):
            self.Owner.SpriteText.Visible = True
        else:
            self.Owner.SpriteText.Visible = False

Zero.RegisterComponent("Won", Won)