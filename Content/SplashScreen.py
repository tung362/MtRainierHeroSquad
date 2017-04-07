import Zero
import Events
import Property
import VectorMath

class SplashScreen:
    
    def DefineProperties(self):
        self.Timer = Property.Float()

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)

    def OnLogicUpdate(self, UpdateEvent):
        
        DeltaTime = UpdateEvent.Dt
        self.Timer += DeltaTime
        if(self.Timer > 8.0):
            self.Space.LoadLevel("MainMenu")

Zero.RegisterComponent("SplashScreen", SplashScreen)