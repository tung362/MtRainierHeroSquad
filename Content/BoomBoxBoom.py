import Zero
import Events
import Property
import VectorMath
import Action
import math

Vector3 = VectorMath.Vec3

class BoomBoxBoom:
    
    def DefineProperties(self):
        self.Start = Property.Bool(True)
        self.CanExplode = Property.Bool(True)

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        Zero.Connect(self.Owner, Events.CollisionStarted, self.OnCollisionStarted)

    def OnLogicUpdate(self, UpdateEvent):
        sequence = Action.Sequence(self.Owner.Actions)
        
        if(self.Start == True):
            
            self.Owner.Name = "BoomBoxBoom"
            self.Start = False
            
            
        if(self.CanExplode is True):
            StatusTracker = self.Space.FindObjectByName("PlayerTracker")
            StatusTracker.PlayerTracker.Explode = True
            self.Owner.RigidBody.DynamicState = 2
            self.Owner.AddComponentByName("SphereCollider")
            self.Owner.SphereCollider.CollisionGroup = "PlayerProjectile"
            self.Owner.SphereCollider.Radius = 2.5
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
            
    def OnCollisionStarted(self, CollisionEvent):
        
        other = CollisionEvent.OtherObject
        sequence = Action.Sequence(self.Owner.Actions)
        ObjectPosition = self.Owner.Transform.WorldTranslation
            
        if(other.Name == "Grass1" and self.CanExplode is True):
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.Grass.CurrentHealth -= Damage * 20
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "Dirt1" and self.CanExplode is True):
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.Dirt.CurrentHealth -= Damage * 20
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "WallBackGround" and self.CanExplode is True):
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.WallBackGround.CurrentHealth -= Damage * 20
            #print(Damage * 100)
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "Wall1" and self.CanExplode is True):
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.Wall1.CurrentHealth -= Damage * 20
            #print(Damage * 100)
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "Crate" and self.CanExplode is True):
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.SmallCrate.CurrentHealth -= Damage * 20
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "Barrel" and self.CanExplode is True):
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.Barrel.CurrentHealth -= Damage * 20
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "FireBarrel" and self.CanExplode is True):
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.FireBarrel.CurrentHealth -= Damage * 20
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "BridgeBottom" and self.CanExplode is True):
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.Bridge.CurrentHealth -= Damage * 20
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "GunMan" and self.CanExplode is True):
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.GunManHealth.CurrentHealth -= Damage * 20
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
            
    def OnDeath(self):
        self.Owner.Destroy()

Zero.RegisterComponent("BoomBoxBoom", BoomBoxBoom)