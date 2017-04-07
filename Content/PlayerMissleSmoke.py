import Zero
import Events
import Property
import VectorMath

class PlayerMissleSmoke:
    def DefineProperties(self):
        pass

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)

    def OnLogicUpdate(self, UpdateEvent):
        Parent = self.Owner.Parent
        
        if(Parent.PlayerMissle.HasCollided == True):
            self.Owner.SphericalParticleEmitter.EmitRate = 0

Zero.RegisterComponent("PlayerMissleSmoke", PlayerMissleSmoke)