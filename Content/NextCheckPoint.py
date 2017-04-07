import Zero
import Events
import Property
import VectorMath

Vector3 = VectorMath.Vec3

class NextCheckPoint:
    def DefineProperties(self):
        self.CanFlagRise = Property.Bool(False)
        self.CanDoAnimation = Property.Bool(True)
        self.PlayerCollided = Property.Bool(False)
        
        self.CanSwitch = Property.Bool(True)

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        Zero.Connect(self.Owner, Events.CollisionStarted, self.OnCollisionStarted)
        
        
    def OnLogicUpdate(self, UpdateEvent):
        
        if(self.PlayerCollided is True):
            if(self.CanDoAnimation is True):
                
                self.CanFlagRise = True
                self.CanDoAnimation = False
        
        if(self.CanFlagRise is True):
            self.Owner.Sprite.SpriteSource = "FlagUp"
            self.CanFlagRise = False
            
        if(self.Owner.Sprite.CurrentFrame >= 2):
            self.Owner.Sprite.SpriteSource = "FlagUpIdle"
        
        
    def OnCollisionStarted(self, CollisionEvent):
        other = CollisionEvent.OtherObject
        
        if(other.Name == "Tung"):
            
            Position = self.Owner.Transform.Translation
            Tracker = self.Space.FindObjectByName("PlayerTracker")
            SpawnPoint = self.Space.FindObjectByName("SpawnPoint")
            
            SpawnPoint.Transform.Translation = Vector3(Position.x, Position.y, 0)
            
            if(self.CanSwitch is True):
                Tracker.PlayerTracker.TungIsAlive = True
                SpawnPoint.CheckPoint.Start = True
                other.Destroy()
                self.CanSwitch = False
                
            self.PlayerCollided = True
            
        elif(other.Name == "Austin"):
            
            Position = self.Owner.Transform.Translation
            Tracker = self.Space.FindObjectByName("PlayerTracker")
            SpawnPoint = self.Space.FindObjectByName("SpawnPoint")
            
            SpawnPoint.Transform.Translation = Vector3(Position.x, Position.y, 0)
            
            if(self.CanSwitch is True):
                Tracker.PlayerTracker.AustinIsAlive = True
                SpawnPoint.CheckPoint.Start = True
                other.Destroy()
                self.CanSwitch = False
                
            self.PlayerCollided = True
            
        elif(other.Name == "Trey"):
            
            Position = self.Owner.Transform.Translation
            Tracker = self.Space.FindObjectByName("PlayerTracker")
            SpawnPoint = self.Space.FindObjectByName("SpawnPoint")
            
            SpawnPoint.Transform.Translation = Vector3(Position.x, Position.y, 0)
            
            if(self.CanSwitch is True):
                Tracker.PlayerTracker.TreyIsAlive = True
                SpawnPoint.CheckPoint.Start = True
                other.Destroy()
                self.CanSwitch = False
                
            self.PlayerCollided = True
            
        elif(other.Name == "Peyton"):
            
            Position = self.Owner.Transform.Translation
            Tracker = self.Space.FindObjectByName("PlayerTracker")
            SpawnPoint = self.Space.FindObjectByName("SpawnPoint")
            
            SpawnPoint.Transform.Translation = Vector3(Position.x, Position.y, 0)
            
            if(self.CanSwitch is True):
                Tracker.PlayerTracker.PeytonIsAlive = True
                SpawnPoint.CheckPoint.Start = True
                other.Destroy()
                self.CanSwitch = False
                
            self.PlayerCollided = True
            
        elif(other.Name == "Sedrick"):
            
            Position = self.Owner.Transform.Translation
            Tracker = self.Space.FindObjectByName("PlayerTracker")
            SpawnPoint = self.Space.FindObjectByName("SpawnPoint")
            
            SpawnPoint.Transform.Translation = Vector3(Position.x, Position.y, 0)
            
            if(self.CanSwitch is True):
                Tracker.PlayerTracker.SedrickIsAlive = True
                SpawnPoint.CheckPoint.Start = True
                other.Destroy()
                self.CanSwitch = False
                
            self.PlayerCollided = True
            
        elif(other.Name == "Julio"):
            
            Position = self.Owner.Transform.Translation
            Tracker = self.Space.FindObjectByName("PlayerTracker")
            SpawnPoint = self.Space.FindObjectByName("SpawnPoint")
            
            SpawnPoint.Transform.Translation = Vector3(Position.x, Position.y, 0)
            
            if(self.CanSwitch is True):
                Tracker.PlayerTracker.JulioIsAlive = True
                SpawnPoint.CheckPoint.Start = True
                other.Destroy()
                self.CanSwitch = False
            
            self.PlayerCollided = True
        
        
        
        

Zero.RegisterComponent("NextCheckPoint", NextCheckPoint)