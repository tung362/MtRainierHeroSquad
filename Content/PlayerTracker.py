import Zero
import Events
import Property
import VectorMath

class PlayerTracker:
    def DefineProperties(self):
        self.Lives = Property.Int(6)
        
        self.TungIsAlive = Property.Bool(True)
        self.AustinIsAlive = Property.Bool(True)
        self.JulioIsAlive = Property.Bool(True)
        self.SedrickIsAlive = Property.Bool(True)
        self.TreyIsAlive = Property.Bool(True)
        self.PeytonIsAlive = Property.Bool(True)
        
        self.Explode = Property.Bool(False)
        
        self.DeathNumber = Property.Int(0)
        
        self.Timer = Property.Float()
        self.Timer2 = Property.Float()

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)

    def OnLogicUpdate(self, UpdateEvent):
        DeltaTime = UpdateEvent.Dt
        
        if(self.Lives < 0):
            self.Lives = 0
            
        if(self.Explode is True):
            self.Timer += DeltaTime
            
            if(self.Timer > 0.25):
                self.Explode = False
                self.Timer = 0
                
        if(self.TungIsAlive is False and self.AustinIsAlive is False and self.JulioIsAlive is False and self.SedrickIsAlive is False and self.TreyIsAlive is False and self.PeytonIsAlive is False and self.DeathNumber >= 6):
            self.Timer2 += DeltaTime
            
            if(self.Timer2 > 4):
                self.Space.LoadLevel("Lose")

Zero.RegisterComponent("PlayerTracker", PlayerTracker)