import Zero
import Events
import Property
import VectorMath

class TungBodyShoot:
    def DefineProperties(self):
        self.CanAnimate = Property.Bool(True)
        self.CanAnimateIdle = Property.Bool(False)
        self.CanShoot = Property.Bool(False)
        self.CanIdle = Property.Bool(False)

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)

    def OnLogicUpdate(self, UpdateEvent):
        
        if(Zero.Mouse.IsButtonDown(Zero.MouseButtons.Left)):
            self.CanAnimateIdle = True
            
            if(self.CanAnimate is True):
                self.CanShoot = True
                self.CanAnimate = False
        else:
            if(self.CanAnimateIdle is True):
                self.CanIdle = True
            self.CanAnimate = True
            self.CanAnimateIdle = False
            
        
        if(self.CanShoot is True):
            self.Owner.Sprite.SpriteSource = "TungBodyShoot"
            self.CanShoot = False
        elif(self.CanIdle is True):
            self.Owner.Sprite.SpriteSource = "TungBody"
            self.CanIdle = False

Zero.RegisterComponent("TungBodyShoot", TungBodyShoot)