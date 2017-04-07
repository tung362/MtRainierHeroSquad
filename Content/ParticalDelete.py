import Zero
import Events
import Property
import VectorMath
import Action

class ParticalDelete:
    
    def DefineProperties(self):
        self.timer = Property.Float()

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)

    def OnLogicUpdate(self, UpdateEvent):
        
        #Timer
        DeltaTime = UpdateEvent.Dt
        self.timer += DeltaTime
        
        if(self.timer > 0.3):
            self.Owner.SphericalParticleEmitter.EmitRate = 0
            
        if(self.timer > 2.0):
            self.Owner.Destroy()

Zero.RegisterComponent("ParticalDelete", ParticalDelete)