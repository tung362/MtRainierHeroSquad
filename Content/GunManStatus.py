import Zero
import Events
import Property
import VectorMath

class GunManStatus:
    def DefineProperties(self):
        self.CanShoot = Property.Bool(False)
        
        self.RayCast1 = Property.Bool(False)
        self.RayCast2 = Property.Bool(False)
        self.RayCast3 = Property.Bool(False)
        self.RayCast4 = Property.Bool(False)
        self.RayCast5 = Property.Bool(False)
        self.RayCast6 = Property.Bool(False)
        self.RayCast7 = Property.Bool(False)
        self.RayCast8 = Property.Bool(False)
        self.RayCast9 = Property.Bool(False)

    def Initialize(self, initializer):
        #Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        pass

    def OnLogicUpdate(self, UpdateEvent):
        pass

Zero.RegisterComponent("GunManStatus", GunManStatus)