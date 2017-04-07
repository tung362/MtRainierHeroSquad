import Zero
import Events
import Property
import VectorMath

Vector3 = VectorMath.Vec3

class CloudBehavior:
    
    def DefineProperties(self):
        self.Speed = Property.Float(10)

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        Zero.Connect(self.Owner, Events.CollisionStarted, self.OnCollisionStarted)
        
    def OnLogicUpdate(self, UpdateEvent):
        
        self.Owner.RigidBody.Velocity = Vector3(self.Speed, 0, 0)
        
    def OnCollisionStarted(self, CollisionEvent):
        
        other = CollisionEvent.OtherObject
                
        if(other.Name == "CloudDestroyer"):
            
            self.Owner.Destroy()

Zero.RegisterComponent("CloudBehavior", CloudBehavior)