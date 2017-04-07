import Zero
import Events
import Property
import VectorMath

class SplashScreenTracker:
    def DefineProperties(self):
        
        self.Explode = Property.Bool(False)
        
        self.Timer = Property.Float()

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)

    def OnLogicUpdate(self, UpdateEvent):
            
        if(self.Explode is True):
            DeltaTime = UpdateEvent.Dt
            self.Timer += DeltaTime
            
            if(self.Timer > 0.25):
                self.Explode = False
                self.Timer = 0

Zero.RegisterComponent("SplashScreenTracker", SplashScreenTracker)