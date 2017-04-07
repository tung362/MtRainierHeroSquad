import Zero
import Events
import Property
import VectorMath
import Action

Vector3 = VectorMath.Vec3
Quaternion = VectorMath.Quaternion

class SedrickHealth:
    
    def DefineProperties(self):
        self.MaxHealth = Property.Float(100)
        self.CurrentHealth = Property.Float(100)
        
        self.Start = Property.Bool(True)
        
        self.DeathSpawn = Property.Bool(False)
        
        self.CanTick = Property.Bool(True)
        self.LayDead = Property.Bool(False)

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        Zero.Connect(self.Owner, Events.CollisionStarted, self.OnCollisionStarted)

    def OnLogicUpdate(self, UpdateEvent):
        
        #if(self.Start == True):
            
            #self.Owner.SoundEmitter.Volume = 1
            #self.Owner.SoundEmitter.PlayCue("AllOnline")
            
            #self.Start = False
        
        sequence = Action.Sequence(self.Owner.Actions)
        
        if(Zero.Keyboard.KeyIsPressed(Zero.Keys.L)):
            self.CurrentHealth -= 25
        
        if(self.CurrentHealth <= 0):
            self.CurrentHealth = 0
            Position = self.Owner.Transform.Translation
            
            if(self.DeathSpawn == False):
                PivotBody = self.Owner.FindChildByName("BodyPivot")
                Body = self.Owner.FindChildByName("SedrickBody")
                Weapon1 = self.Owner.FindChildByName("BoomBox1")
                
                PivotBody.RemoveComponentByName("SedrickBody")
                Body.RemoveComponentByName("SedrickBodyShoot")
                Weapon1.RemoveComponentByName("BoomBox1")
                
                self.Owner.RemoveComponentByName("SedrickPlayerController")
                
                self.Owner.Sprite.SpriteSource = "SedrickIdle"
                Body.Sprite.SpriteSource = "SedrickBody"
                
                if(self.LayDead is False):
                    self.Owner.RigidBody.RotationLocked = False
                    self.Owner.RigidBody.Velocity = Vector3(0, 0, 0)
                    #self.Owner.RigidBody.ApplyAngularVelocity(Vector3(0, 0, 5))
                    #self.Owner.RigidBody.AngularVelocity = Vector3(0, 0, 10)
                    self.Owner.Transform.Rotation = Quaternion(0, 0, 1.5)
                    PivotBody.Transform.WorldRotation = Quaternion(0, 0, 1.5)
                    self.LayDead = True
                self.DeathSpawn = True
                
            Action.Delay(sequence, 5.0)
            Action.Call(sequence, self.OnDeath)
    
    def OnCollisionStarted(self, CollisionEvent):
        
        other = CollisionEvent.OtherObject
        
        if(other.Name == "EnemySmallBullet"):
            self.CurrentHealth -= 25
            
            
        elif(other.Name == "EnemyGiantBullet"):
            self.CurrentHealth -= 25
            
            
    def OnDeath(self):
        Tracker = self.Space.FindObjectByName("PlayerTracker")
        Spawn = self.Space.FindObjectByName("SpawnPoint")
        
        if(self.CanTick is True):
            Tracker.PlayerTracker.DeathNumber += 1
            Spawn.CheckPoint.Start = True
            self.CanTick = False
            
        self.Owner.Destroy()

Zero.RegisterComponent("SedrickHealth", SedrickHealth)