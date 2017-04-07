import Zero
import Events
import Property
import VectorMath
import Action

class ExplodeBurst:
    
    def DefineProperties(self):
        self.timer = Property.Float()

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)

    def OnLogicUpdate(self, UpdateEvent):
        
        #Timer
        DeltaTime = UpdateEvent.Dt
        self.timer += DeltaTime
        
        if(self.timer > 0.8):
            self.Owner.SphericalParticleEmitter.EmitRate = 0
            
        if(self.timer > 1.8):
            self.Owner.Destroy()

Zero.RegisterComponent("ExplodeBurst", ExplodeBurst)