import Zero
import Events
import Property
import VectorMath
import Action
import math

Vector3 = VectorMath.Vec3

class PlayerMissle:
    
    def DefineProperties(self):
        self.Start = Property.Bool(True)
        
        self.FireY = Property.Float(0)
        
        self.HasCollided = Property.Bool(False)
        
        self.Speed = Property.Float(20)
        
        self.CanExplode = Property.Bool(False)
        self.CanBlow = Property.Bool(True)
        
        self.CanPlaySound = Property.Bool(True)

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        Zero.Connect(self.Owner, Events.CollisionStarted, self.OnCollisionStarted)
        
        
        
    def OnLogicUpdate(self, UpdateEvent):
        
        RotationAngles = Vector3(0, 0, 0)
        Movement = Vector3(0, 0, 0)
        ForwardDirection = self.Owner.Orientation.WorldForward
        
        #Player = self.Space.FindObjectByName("Player")
        
        if(self.Start == True):
            
            #Name
            self.Owner.Name = "PlayerMissle"
            #self.Owner.Transform.Rotation = Player.Transform.Rotation
            #self.Owner.Transform.RotateAnglesLocal(RotationAngles * UpdateEvent.Dt)
            self.Start = False
            #print(self.Name)
        
        
        Movement = ForwardDirection * self.Speed + Vector3(0, self.FireY, 0)
        Movement.normalized()
        
        self.Owner.RigidBody.Velocity += Movement * UpdateEvent.Dt
        
        '''if(self.HasCollided is True):
            self.Owner.Sprite.Visible = False
            StatusTracker = self.Space.FindObjectByName("PlayerTracker")
            StatusTracker.PlayerTracker.Explode = True
            #self.Owner.RemoveComponentByName("MassOverride")
            #self.Owner.RemoveComponentByName("RigidBody")
            self.Owner.RigidBody.DynamicState = 2
            self.Owner.RemoveComponentByName("BoxCollider")
            self.CanExplode = True
            #self.Owner.Destroy()
            
        if(self.CanExplode is True):
            self.Owner.AddComponentByName("SphereCollider")
            self.Owner.SphereCollider.CollisionGroup = "Terrain"
            self.Owner.SphereCollider.Radius = 2.5'''
        
        
        
    def OnCollisionStarted(self, CollisionEvent):
        
        other = CollisionEvent.OtherObject
        sequence = Action.Sequence(self.Owner.Actions)
        ObjectPosition = self.Owner.Transform.WorldTranslation
        
        if(self.CanPlaySound is True):
            self.Owner.SoundEmitter.Volume = 0.4
            self.Owner.SoundEmitter.PlayCue("Explode")
            self.CanPlaySound = False
        
        if(other.Name == "GunMan"):
            
            #self.Owner.SoundEmitter.Volume = 0.2
            #self.Owner.SoundEmitter.PlayCue("PlayerMissleImpact")
            StatusTracker = self.Space.FindObjectByName("PlayerTracker")
            StatusTracker.PlayerTracker.Explode = True
            StatusTracker.PlayerTracker.Timer = 0
            self.Speed = 0
            self.Owner.Sprite.Visible = False
            self.HasCollided = True
            self.Owner.RigidBody.DynamicState = 2
            self.Owner.RemoveComponentByName("BoxCollider")
            self.Owner.AddComponentByName("SphereCollider")
            self.Owner.SphereCollider.CollisionGroup = "Terrain"
            self.Owner.SphereCollider.Radius = 1.5
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.GunManHealth.CurrentHealth -= Damage * 100
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        if(other.Name == "HeavyGunMan"):
            
            #self.Owner.SoundEmitter.Volume = 0.2
            #self.Owner.SoundEmitter.PlayCue("PlayerMissleImpact")
            StatusTracker = self.Space.FindObjectByName("PlayerTracker")
            StatusTracker.PlayerTracker.Explode = True
            StatusTracker.PlayerTracker.Timer = 0
            self.Speed = 0
            self.Owner.Sprite.Visible = False
            self.HasCollided = True
            self.Owner.RigidBody.DynamicState = 2
            self.Owner.RemoveComponentByName("BoxCollider")
            self.Owner.AddComponentByName("SphereCollider")
            self.Owner.SphereCollider.CollisionGroup = "Terrain"
            self.Owner.SphereCollider.Radius = 1.5
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.HeavyGunManHealth.CurrentHealth -= Damage * 100
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
            
        if(other.Name == "Grass1"):
            #self.Owner.SoundEmitter.Volume = 0.2
            #self.Owner.SoundEmitter.PlayCue("PlayerMissleImpact")
            StatusTracker = self.Space.FindObjectByName("PlayerTracker")
            StatusTracker.PlayerTracker.Explode = True
            StatusTracker.PlayerTracker.Timer = 0
            self.Speed = 0
            self.Owner.Sprite.Visible = False
            self.HasCollided = True
            self.Owner.RigidBody.DynamicState = 2
            self.Owner.RemoveComponentByName("BoxCollider")
            self.Owner.AddComponentByName("SphereCollider")
            self.Owner.SphereCollider.CollisionGroup = "Terrain"
            self.Owner.SphereCollider.Radius = 1.5
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.Grass.CurrentHealth -= Damage * 100
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "Dirt1"):
            #self.Owner.SoundEmitter.Volume = 0.2
            #self.Owner.SoundEmitter.PlayCue("PlayerMissleImpact")
            StatusTracker = self.Space.FindObjectByName("PlayerTracker")
            StatusTracker.PlayerTracker.Explode = True
            StatusTracker.PlayerTracker.Timer = 0
            self.Speed = 0
            self.Owner.Sprite.Visible = False
            self.HasCollided = True
            self.Owner.RigidBody.DynamicState = 2
            self.Owner.RemoveComponentByName("BoxCollider")
            self.Owner.AddComponentByName("SphereCollider")
            self.Owner.SphereCollider.CollisionGroup = "Terrain"
            self.Owner.SphereCollider.Radius = 1.5
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.Dirt.CurrentHealth -= Damage * 100
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "WallBackGround"):
            #self.Owner.SoundEmitter.Volume = 0.2
            #self.Owner.SoundEmitter.PlayCue("PlayerMissleImpact")
            StatusTracker = self.Space.FindObjectByName("PlayerTracker")
            StatusTracker.PlayerTracker.Explode = True
            StatusTracker.PlayerTracker.Timer = 0
            self.Speed = 0
            self.Owner.Sprite.Visible = False
            self.HasCollided = True
            self.Owner.RigidBody.DynamicState = 2
            self.Owner.RemoveComponentByName("BoxCollider")
            self.Owner.AddComponentByName("SphereCollider")
            self.Owner.SphereCollider.CollisionGroup = "Terrain"
            self.Owner.SphereCollider.Radius = 1.5
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.WallBackGround.CurrentHealth -= Damage * 100
            #print(Damage * 100)
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "Wall1"):
            #self.Owner.SoundEmitter.Volume = 0.2
            #self.Owner.SoundEmitter.PlayCue("PlayerMissleImpact")
            StatusTracker = self.Space.FindObjectByName("PlayerTracker")
            StatusTracker.PlayerTracker.Explode = True
            StatusTracker.PlayerTracker.Timer = 0
            self.Speed = 0
            self.Owner.Sprite.Visible = False
            self.HasCollided = True
            self.Owner.RigidBody.DynamicState = 2
            self.Owner.RemoveComponentByName("BoxCollider")
            self.Owner.AddComponentByName("SphereCollider")
            self.Owner.SphereCollider.CollisionGroup = "Terrain"
            self.Owner.SphereCollider.Radius = 1.5
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.Wall1.CurrentHealth -= Damage * 100
            #print(Damage * 100)
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "Crate"):
            #self.Owner.SoundEmitter.Volume = 0.2
            #self.Owner.SoundEmitter.PlayCue("PlayerMissleImpact")
            StatusTracker = self.Space.FindObjectByName("PlayerTracker")
            StatusTracker.PlayerTracker.Explode = True
            StatusTracker.PlayerTracker.Timer = 0
            self.Speed = 0
            self.Owner.Sprite.Visible = False
            self.HasCollided = True
            self.Owner.RigidBody.DynamicState = 2
            self.Owner.RemoveComponentByName("BoxCollider")
            self.Owner.AddComponentByName("SphereCollider")
            self.Owner.SphereCollider.CollisionGroup = "Terrain"
            self.Owner.SphereCollider.Radius = 1.5
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.SmallCrate.CurrentHealth -= Damage * 100
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "Barrel"):
            #self.Owner.SoundEmitter.Volume = 0.2
            #self.Owner.SoundEmitter.PlayCue("PlayerMissleImpact")
            StatusTracker = self.Space.FindObjectByName("PlayerTracker")
            StatusTracker.PlayerTracker.Explode = True
            StatusTracker.PlayerTracker.Timer = 0
            self.Speed = 0
            self.Owner.Sprite.Visible = False
            self.HasCollided = True
            self.Owner.RigidBody.DynamicState = 2
            self.Owner.RemoveComponentByName("BoxCollider")
            self.Owner.AddComponentByName("SphereCollider")
            self.Owner.SphereCollider.CollisionGroup = "Terrain"
            self.Owner.SphereCollider.Radius = 1.5
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.Barrel.CurrentHealth -= Damage * 100
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "FireBarrel"):
            #self.Owner.SoundEmitter.Volume = 0.2
            #self.Owner.SoundEmitter.PlayCue("PlayerMissleImpact")
            StatusTracker = self.Space.FindObjectByName("PlayerTracker")
            StatusTracker.PlayerTracker.Explode = True
            StatusTracker.PlayerTracker.Timer = 0
            self.Speed = 0
            self.Owner.Sprite.Visible = False
            self.HasCollided = True
            self.Owner.RigidBody.DynamicState = 2
            self.Owner.RemoveComponentByName("BoxCollider")
            self.Owner.AddComponentByName("SphereCollider")
            self.Owner.SphereCollider.CollisionGroup = "Terrain"
            self.Owner.SphereCollider.Radius = 1.5
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.FireBarrel.CurrentHealth -= Damage * 100
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "BridgeBottom"):
            #self.Owner.SoundEmitter.Volume = 0.2
            #self.Owner.SoundEmitter.PlayCue("PlayerMissleImpact")
            StatusTracker = self.Space.FindObjectByName("PlayerTracker")
            StatusTracker.PlayerTracker.Explode = True
            StatusTracker.PlayerTracker.Timer = 0
            self.Speed = 0
            self.Owner.Sprite.Visible = False
            self.HasCollided = True
            self.Owner.RigidBody.DynamicState = 2
            self.Owner.RemoveComponentByName("BoxCollider")
            self.Owner.AddComponentByName("SphereCollider")
            self.Owner.SphereCollider.CollisionGroup = "Terrain"
            self.Owner.SphereCollider.Radius = 1.5
            
            OtherObject = other.Transform.WorldTranslation
            Difference = Vector3(OtherObject.x - ObjectPosition.x, OtherObject.y - ObjectPosition.y, OtherObject.z - ObjectPosition.z)
            Distance = math.sqrt(math.pow(Difference.x, 2) + math.pow(Difference.y, 2) + math.pow(Difference.z, 2))
            Damage = 8 - Distance
            
            other.Bridge.CurrentHealth -= Damage * 100
            Action.Delay(sequence, 0.1)
            Action.Call(sequence, self.OnDeath)
            
            
            
            
            
            
    def OnDeath(self):
        Position = self.Owner.Transform.WorldTranslation
        if(self.CanBlow is True):
            
            PlayerBlasterProjectile = self.Space.CreateAtPosition("PlayerMissleExplodeParticle", Vector3(Position.x, Position.y + 0.5, 4))
            self.CanBlow = False
        self.Owner.Destroy()

Zero.RegisterComponent("PlayerMissle", PlayerMissle)