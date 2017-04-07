import Zero
import Events
import Property
import VectorMath

Vector3 = VectorMath.Vec3

class AirBalloonBasket:
    def DefineProperties(self):
        self.HasCollided = Property.Bool(False)

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        Zero.Connect(self.Owner, Events.CollisionStarted, self.OnCollisionStarted)

    def OnLogicUpdate(self, UpdateEvent):
        if(self.HasCollided is True):
            Tung = self.Space.FindObjectByName("Tung")
            Austin = self.Space.FindObjectByName("Austin")
            Trey = self.Space.FindObjectByName("Trey")
            Peyton = self.Space.FindObjectByName("Peyton")
            Sedrick = self.Space.FindObjectByName("Sedrick")
            Julio = self.Space.FindObjectByName("Julio")
            
            Position = self.Owner.Transform.Translation
            
            Movement = Vector3(0, 0, 0)
            
            if(Tung):
                Tung.Transform.Translation = Vector3(Position.x, Position.y + 0.2, 0)
                
            elif(Austin):
                Austin.Transform.Translation = Vector3(Position.x, Position.y + 0.2, 0)
                
            elif(Trey):
                Trey.Transform.Translation = Vector3(Position.x, Position.y + 0.2, 0)
                
            elif(Peyton):
                Peyton.Transform.Translation = Vector3(Position.x, Position.y + 0.2, 0)
                
            elif(Sedrick):
                Sedrick.Transform.Translation = Vector3(Position.x, Position.y + 0.2, 0)
                
            elif(Julio):
                Julio.Transform.Translation = Vector3(Position.x, Position.y + 0.2, 0)
                
            Movement += Vector3(0, 1, 0)
            self.Owner.RigidBody.Velocity += Movement * UpdateEvent.Dt * 10.0
        
    def OnCollisionStarted(self, CollisionEvent):
        
        other = CollisionEvent.OtherObject
        
        if(other.Name == "Tung" or other.Name == "Austin" or other.Name == "Trey" or other.Name == "Peyton" or other.Name == "Sedrick" or other.Name == "Julio"):
            self.HasCollided = True

Zero.RegisterComponent("AirBalloonBasket", AirBalloonBasket)