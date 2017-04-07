import Zero
import Events
import Property
import VectorMath
import Action
import math

Vector3 = VectorMath.Vec3

class FireBarrel:
    
    def DefineProperties(self):
        self.MaxHealth = Property.Float(50)
        self.CurrentHealth = Property.Float(50)
        self.Start = Property.Bool(True)
        self.CanExplode = Property.Bool(False)
        self.CanBlow = Property.Bool(True)
        
        self.CanPlaySound = Property.Bool(True)

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        Zero.Connect(self.Owner, Events.CollisionStarted, self.OnCollisionStarted)

    def OnLogicUpdate(self, UpdateEvent):
        
        GetMaxHealth = self.MaxHealth
        GetCurrentHealth = self.CurrentHealth
        
        if(self.Start == True):
            
            self.Owner.Name = "FireBarrel"
            self.MaxHealth = 50
            self.CurrentHealth = 50
            self.Start = False
            
            
        if(GetCurrentHealth <= 0):
            self.Owner.Sprite.Visible = False
            StatusTracker = self.Space.FindObjectByName("PlayerTracker")
            StatusTracker.PlayerTracker.Explode = True
            #self.Owner.RemoveComponentByName("MassOverride")
            #self.Owner.RemoveComponentByName("RigidBody")
            self.Owner.RigidBody.DynamicState = 2
            self.Owner.RemoveComponentByName("BoxCollider")
            
            if(self.CanPlaySound is True):
                self.Owner.SoundEmitter.Volume = 0.6
                self.Owner.SoundEmitter.PlayCue("Explode")
                self.CanPlaySound = False
            
            self.CanExplode = True
            #self.Owner.Destroy()
            
        if(self.CanExplode is True):
            self.Owner.AddComponentByName("SphereCollider")
            self.Owner.SphereCollider.CollisionGroup = "Terrain"
            self.Owner.SphereCollider.Radius = 2.5
            
            
    def OnCollisionStarted(self, CollisionEvent):
        
        other = CollisionEvent.OtherObject
        sequence = Action.Sequence(self.Owner.Actions)
        ObjectPosition = self.Owner.Transform.WorldTranslation
            
            
        if(other.Name == "PlayerSmallBullet"):
            
            self.CurrentHealth -= 10
            
        elif(other.Name == "PlayerGiantBullet"):
            
            self.CurrentHealth -= 15
            
        elif(other.Name == "EnemySmallBullet"):
            
            self.CurrentHealth -= 10
            
        elif(other.Name == "EnemyGiantBullet"):
            
            self.CurrentHealth -= 15
            
        if(other.Name == "Grass1" and self.CanExplode is True):
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.Grass.CurrentHealth -= Damage * 100
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "Dirt1" and self.CanExplode is True):
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.Dirt.CurrentHealth -= Damage * 100
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "WallBackGround" and self.CanExplode is True):
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.WallBackGround.CurrentHealth -= Damage * 100
            #print(Damage * 100)
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "Wall1" and self.CanExplode is True):
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.Wall1.CurrentHealth -= Damage * 100
            #print(Damage * 100)
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "Crate" and self.CanExplode is True):
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.SmallCrate.CurrentHealth -= Damage * 100
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "Barrel" and self.CanExplode is True):
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.Barrel.CurrentHealth -= Damage * 100
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "FireBarrel" and self.CanExplode is True):
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.FireBarrel.CurrentHealth -= Damage * 100
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "BridgeBottom" and self.CanExplode is True):
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.Bridge.CurrentHealth -= Damage * 100
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "GunMan" and self.CanExplode is True):
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.GunManHealth.CurrentHealth -= Damage * 100
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "HeavyGunMan" and self.CanExplode is True):
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.HeavyGunManHealth.CurrentHealth -= Damage * 100
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "Tung" and self.CanExplode is True):
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.TungHealth.CurrentHealth -= Damage * 100
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "Austin" and self.CanExplode is True):
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.AustinHealth.CurrentHealth -= Damage * 100
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "Trey" and self.CanExplode is True):
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.TreyHealth.CurrentHealth -= Damage * 100
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "Peyton" and self.CanExplode is True):
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.PeytonHealth.CurrentHealth -= Damage * 100
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "Sedrick" and self.CanExplode is True):
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.SedrickHealth.CurrentHealth -= Damage * 100
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "Julio" and self.CanExplode is True):
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.JulioHealth.CurrentHealth -= Damage * 100
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
    def OnDeath(self):
        Position = self.Owner.Transform.WorldTranslation
        if(self.CanBlow is True):
            
            PlayerBlasterProjectile = self.Space.CreateAtPosition("PlayerMissleExplodeParticle", Vector3(Position.x, Position.y + 0.5, 4))
            self.CanBlow = False
        self.Owner.Destroy()

Zero.RegisterComponent("FireBarrel", FireBarrel)