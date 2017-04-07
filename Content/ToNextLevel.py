import Zero
import Events
import Property
import VectorMath

class ToNextLevel:
    def DefineProperties(self):
        self.NextLevelName = Property.String()

    def Initialize(self, initializer):
        #Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        Zero.Connect(self.Owner, Events.CollisionStarted, self.OnCollisionStarted)

    def OnLogicUpdate(self, UpdateEvent):
        pass
        
    def OnCollisionStarted(self, CollisionEvent):
        other = CollisionEvent.OtherObject
        
        if(other.Name == "AirBalloonBasket"):
            self.Space.LoadLevel(self.NextLevelName)

Zero.RegisterComponent("ToNextLevel", ToNextLevel)