import Zero
import Events
import Property
import VectorMath
import Action

Vector3 = VectorMath.Vec3
Quaternion = VectorMath.Quaternion

class TungHealth:

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
                Body = self.Owner.FindChildByName("TungBody")
                Weapon1 = self.Owner.FindChildByName("MachineGun1")
                Weapon2 = self.Owner.FindChildByName("MachineGun2")
                Weapon3 = self.Owner.FindChildByName("MachineGun3")
                Weapon4 = self.Owner.FindChildByName("MachineGun4")
                Weapon5 = self.Owner.FindChildByName("MachineGun5")
                Weapon6 = self.Owner.FindChildByName("MachineGun6")
                Weapon7 = self.Owner.FindChildByName("MachineGun7")
                Weapon8 = self.Owner.FindChildByName("MachineGun8")
                Weapon9 = self.Owner.FindChildByName("MachineGun9")
                Weapon10 = self.Owner.FindChildByName("MachineGun10")
                
                PivotBody.RemoveComponentByName("TungBody")
                Body.RemoveComponentByName("TungBodyShoot")
                Weapon1.RemoveComponentByName("MachineGun1")
                Weapon2.RemoveComponentByName("MachineGun1")
                Weapon3.RemoveComponentByName("MachineGun1")
                Weapon4.RemoveComponentByName("MachineGun1")
                Weapon5.RemoveComponentByName("MachineGun1")
                Weapon6.RemoveComponentByName("MachineGun1")
                Weapon7.RemoveComponentByName("MachineGun1")
                Weapon8.RemoveComponentByName("MachineGun1")
                Weapon9.RemoveComponentByName("MachineGun1")
                Weapon10.RemoveComponentByName("MachineGun1")
                
                self.Owner.RemoveComponentByName("PlayerController")
                
                self.Owner.Sprite.SpriteSource = "TungIdle"
                Body.Sprite.SpriteSource = "TungBody"
                
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


Zero.RegisterComponent("TungHealth", TungHealth)