import Zero
import Events
import Property
import VectorMath

class HeavyGunManBodyShoot:
    def DefineProperties(self):
        self.CanAnimate = Property.Bool(True)
        self.CanAnimateIdle = Property.Bool(False)
        self.CanShoot = Property.Bool(False)
        self.CanIdle = Property.Bool(False)
        self.timer2 = Property.Float()

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)

    def OnLogicUpdate(self, UpdateEvent):
        
        DeltaTime = UpdateEvent.Dt
        
        if(self.Owner.GunManStatus.CanShoot is True):
            self.timer2 += DeltaTime
            
            if(self.timer2 > 0.6):
                self.CanAnimateIdle = True
                
                if(self.CanAnimate is True):
                    self.CanShoot = True
                    self.CanAnimate = False
            else:
                if(self.CanAnimateIdle is True):
                    self.CanIdle = True
                self.CanAnimate = True
                self.CanAnimateIdle = False

        else:
            self.timer2 = 0
            
            if(self.CanAnimateIdle is True):
                    self.CanIdle = True
                    self.CanAnimate = True
                    self.CanAnimateIdle = False
            
        
        if(self.CanShoot is True):
            self.Owner.Sprite.SpriteSource = "HeavyGunManBodyShoot"
            self.CanShoot = False
        elif(self.CanIdle is True):
            self.Owner.Sprite.SpriteSource = "HeavyGunManBody"
            self.CanIdle = False

Zero.RegisterComponent("HeavyGunManBodyShoot", HeavyGunManBodyShoot)