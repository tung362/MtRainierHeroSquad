import Zero
import Events
import Property
import VectorMath
import Action

Vector3 = VectorMath.Vec3

class EnemyGiantBullet:
    
    def DefineProperties(self):
        self.Start = Property.Bool(True)
        
        self.FireY = Property.Float(0)
        
        self.Speed = Property.Float(200)
        
        self.HasCollided = Property.Bool(False)


    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        Zero.Connect(self.Owner, Events.CollisionStarted, self.OnCollisionStarted)
        

    def OnLogicUpdate(self, UpdateEvent):
        
        RotationAngles = Vector3(0, 0, 0)
        Movement = Vector3(0, 0, 0)
        ForwardDirection = self.Owner.Orientation.WorldForward
        
        #Player = self.Space.FindObjectByName("BodyPivot")
        
        if(self.Start == True):
            
            #Name
            self.Owner.Name = "EnemyGiantBullet"
            #self.Owner.Transform.Rotation = Player.Transform.Rotation
            #self.Owner.Transform.RotateAnglesLocal(RotationAngles * UpdateEvent.Dt)
            #Movement = ForwardDirection * 100
            self.Start = False
            #print(self.Name)
        
        
        #Movement = ForwardDirection * 100
        if(self.HasCollided is False):
            Movement = ForwardDirection * self.Speed + Vector3(0, self.FireY, 0)
            Movement.normalized()
        
            self.Owner.RigidBody.Velocity += Movement * UpdateEvent.Dt
        
        
    def OnCollisionStarted(self, CollisionEvent):
        
        other = CollisionEvent.OtherObject
        
        sequence = Action.Sequence(self.Owner.Actions)
        
        if(other.Name == "Tung" or other.Name == "Austin" or other.Name == "Trey" or other.Name == "Peyton" or other.Name == "Sedrick" or other.Name == "Julio"):
            
            self.Owner.SoundEmitter.Volume = 0.4
            self.Owner.SoundEmitter.PlayCue("EnemyHitBullet")
            self.HasCollided = True
            self.Owner.Sprite.SpriteSource = "EnemyGiantBulletHit"
            self.Owner.RemoveComponentByName("RigidBody")
            Action.Delay(sequence, 0.4)
            Action.Call(sequence, self.OnDeath)
            
            
        elif(other.Name == "Grass1"):
            
            self.Owner.SoundEmitter.Volume = 0.2
            self.Owner.SoundEmitter.PlayCue("BulletHitBuilding")
            self.HasCollided = True
            self.Owner.Sprite.SpriteSource = "EnemyGiantBulletHit"
            self.Owner.RemoveComponentByName("RigidBody")
            Action.Delay(sequence, 0.4)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "Dirt1"):
            
            self.Owner.SoundEmitter.Volume = 0.2
            self.Owner.SoundEmitter.PlayCue("BulletHitBuilding")
            self.HasCollided = True
            self.Owner.Sprite.SpriteSource = "EnemyGiantBulletHit"
            self.Owner.RemoveComponentByName("RigidBody")
            Action.Delay(sequence, 0.4)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "BridgeBottom"):
            
            self.Owner.SoundEmitter.Volume = 0.2
            self.Owner.SoundEmitter.PlayCue("BulletHitBuilding")
            self.HasCollided = True
            self.Owner.Sprite.SpriteSource = "EnemyGiantBulletHit"
            self.Owner.RemoveComponentByName("RigidBody")
            Action.Delay(sequence, 0.4)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "Wall1"):
            
            self.Owner.SoundEmitter.Volume = 0.2
            self.Owner.SoundEmitter.PlayCue("BulletHitBuilding")
            self.HasCollided = True
            self.Owner.Sprite.SpriteSource = "EnemyGiantBulletHit"
            self.Owner.RemoveComponentByName("RigidBody")
            Action.Delay(sequence, 0.4)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "Barrel"):
            
            self.Owner.SoundEmitter.Volume = 0.2
            self.Owner.SoundEmitter.PlayCue("BulletHitBuilding")
            self.HasCollided = True
            self.Owner.Sprite.SpriteSource = "EnemyGiantBulletHit"
            self.Owner.RemoveComponentByName("RigidBody")
            Action.Delay(sequence, 0.4)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "Crate"):
            
            self.Owner.SoundEmitter.Volume = 0.2
            self.Owner.SoundEmitter.PlayCue("BulletHitBuilding")
            self.HasCollided = True
            self.Owner.Sprite.SpriteSource = "EnemyGiantBulletHit"
            self.Owner.RemoveComponentByName("RigidBody")
            Action.Delay(sequence, 0.4)
            Action.Call(sequence, self.OnDeath)
            
        elif(other.Name == "FireBarrel"):
            
            self.Owner.SoundEmitter.Volume = 0.2
            self.Owner.SoundEmitter.PlayCue("BulletHitBuilding")
            self.HasCollided = True
            self.Owner.Sprite.SpriteSource = "EnemyGiantBulletHit"
            self.Owner.RemoveComponentByName("RigidBody")
            Action.Delay(sequence, 0.4)
            Action.Call(sequence, self.OnDeath)
        
        
        
    def OnDeath(self):
        self.Owner.Destroy()

Zero.RegisterComponent("EnemyGiantBullet", EnemyGiantBullet)