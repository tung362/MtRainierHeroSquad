import Zero
import Events
import Property
import VectorMath

Vector3 = VectorMath.Vec3

class MT:
    def DefineProperties(self):
        self.Timer = Property.Float()
        self.Delay = Property.Float(1)
        self.CanMove = Property.Bool(True)
        self.X = Property.Float(0)
        self.Y = Property.Float(0)
        self.Z = Property.Float(0)
        self.Name = Property.String()
        
        self.CanPlaySound = Property.Bool(True)

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        Zero.Connect(self.Owner, Events.CollisionStarted, self.OnCollisionStarted)

    def OnLogicUpdate(self, UpdateEvent):
        DeltaTime = UpdateEvent.Dt
        self.Timer += DeltaTime
        
        if(self.Timer > self.Delay and self.CanMove is True):
            self.Owner.RigidBody.Velocity = Vector3(Vector3(-80, 0, 0))
            self.CanMove = False
            self.Timer = 0
        
    def OnCollisionStarted(self, CollisionEvent):
        
        other = CollisionEvent.OtherObject
                
        if(other.Name == self.Name):
            
            self.Owner.RigidBody.Velocity = Vector3(0, 0, 0)
            self.Owner.Transform.Translation = Vector3(self.X, self.Y, self.Z)
            Tracker = self.Space.FindObjectByName("SplashScreenTracker")
            Tracker.SplashScreenTracker.Explode = True
            if(self.CanPlaySound is True):
                self.Owner.SoundEmitter.Volume = 0.8
                self.Owner.SoundEmitter.PlayCue("Explode")

Zero.RegisterComponent("MT", MT)