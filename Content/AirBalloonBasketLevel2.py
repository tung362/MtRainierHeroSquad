import Zero
import Events
import Property
import VectorMath

Vector3 = VectorMath.Vec3

class AirBalloonBasketLevel2:
    def DefineProperties(self):
        self.HasCollided = Property.Bool(False)
        self.HSpeed = Property.Float(10)
        #self.Movement = Property.Vector3()

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
                
            if(Zero.Keyboard.KeyIsDown(Zero.Keys.W)):
                Movement += Vector3(0, 4, 0) * self.HSpeed
            
            elif(Zero.Keyboard.KeyIsDown(Zero.Keys.S)):
                Movement += Vector3(0, -1, 0) * self.HSpeed
            
            elif(Zero.Keyboard.KeyIsDown(Zero.Keys.A)):
                Movement += Vector3(-6, 0, 0) * self.HSpeed
            
            elif(Zero.Keyboard.KeyIsDown(Zero.Keys.D)):
                Movement += Vector3(6, 0, 0) * self.HSpeed
            
            if(Zero.Keyboard.KeyIsDown(Zero.Keys.W) and Zero.Keyboard.KeyIsDown(Zero.Keys.A)):
                Movement += Vector3(-6, 4, 0) * self.HSpeed
            
            if(Zero.Keyboard.KeyIsDown(Zero.Keys.W) and Zero.Keyboard.KeyIsDown(Zero.Keys.D)):
                Movement += Vector3(6, 4, 0) * self.HSpeed
            
            if(Zero.Keyboard.KeyIsDown(Zero.Keys.S) and Zero.Keyboard.KeyIsDown(Zero.Keys.A)):
                Movement += Vector3(-6, -1, 0) * self.HSpeed
            
            if(Zero.Keyboard.KeyIsDown(Zero.Keys.S) and Zero.Keyboard.KeyIsDown(Zero.Keys.D)):
                Movement += Vector3(6, -1, 0) * self.HSpeed
                
            self.Owner.RigidBody.Velocity += Movement * UpdateEvent.Dt
        
    def OnCollisionStarted(self, CollisionEvent):
        
        other = CollisionEvent.OtherObject
        
        if(other.Name == "Tung" or other.Name == "Austin" or other.Name == "Trey" or other.Name == "Peyton" or other.Name == "Sedrick" or other.Name == "Julio"):
            self.HasCollided = True

Zero.RegisterComponent("AirBalloonBasketLevel2", AirBalloonBasketLevel2)