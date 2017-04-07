import Zero
import Events
import Property
import VectorMath
import Action

Vector3 = VectorMath.Vec3
Quaternion = VectorMath.Quaternion

class HeavyGunManHealth:
    
    def DefineProperties(self):
        self.MaxHealth = Property.Float(1000)
        self.CurrentHealth = Property.Float(1000)
        
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
        
        if(self.CurrentHealth <= 0):
            self.CurrentHealth = 0
            Position = self.Owner.Transform.WorldTranslation
            
            if(self.DeathSpawn == False):
                PivotBody = self.Owner.FindChildByName("BodyPivot")
                Body = self.Owner.FindChildByName("HeavyGunManBody")
                Weapon1 = self.Owner.FindChildByName("Look")
                Weapon2 = self.Owner.FindChildByName("GiantMiniGun1")
                Weapon3 = self.Owner.FindChildByName("GiantMiniGun2")
                Weapon4 = self.Owner.FindChildByName("GiantMiniGun3")
                
                PivotBody.RemoveComponentByName("HeavyGunManBody")
                Weapon1.RemoveComponentByName("Look")
                Weapon1.RemoveComponentByName("Look2")
                Weapon1.RemoveComponentByName("Look3")
                Weapon1.RemoveComponentByName("Look4")
                Weapon1.RemoveComponentByName("Look5")
                Weapon1.RemoveComponentByName("Look6")
                Weapon1.RemoveComponentByName("Look7")
                Weapon1.RemoveComponentByName("Look8")
                Weapon1.RemoveComponentByName("Look9")
                Weapon2.RemoveComponentByName("GiantMiniGun1")
                Weapon3.RemoveComponentByName("GiantMiniGun1")
                Weapon4.RemoveComponentByName("GiantMiniGun1")
                
                self.Owner.RemoveComponentByName("HeavyGunManController")
                
                self.Owner.Sprite.SpriteSource = "HeavyGunManIdle"
                Body.Sprite.SpriteSource = "HeavyGunManBody"
                
                if(self.LayDead is False):
                    self.Owner.RigidBody.RotationLocked = False
                    self.Owner.RigidBody.Velocity = Vector3(0, 0, 0)
                    self.Owner.Transform.Rotation = Quaternion(0, 0, 1.5)
                    PivotBody.Transform.WorldRotation = Quaternion(0, 0, 1.5)
                    self.LayDead = True
                self.DeathSpawn = True
                
            Action.Delay(sequence, 5.0)
            Action.Call(sequence, self.OnDeath)
    
    def OnCollisionStarted(self, CollisionEvent):
        
        other = CollisionEvent.OtherObject
        
        if(other.Name == "PlayerSmallBullet"):
            self.CurrentHealth -= 10
            
            
        elif(other.Name == "PlayerGiantBullet"):
            self.CurrentHealth -= 15
            
            
    def OnDeath(self):
        #Tracker = self.Space.FindObjectByName("PlayerTracker")
        
        if(self.CanTick is True):
            #Tracker.PlayerTracker.DeathNumber += 1
            self.CanTick = False
            
        self.Owner.Destroy()

Zero.RegisterComponent("HeavyGunManHealth", HeavyGunManHealth)