import Zero
import Events
import Property
import VectorMath
import random

Vector3 = VectorMath.Vec3

class GiantMiniGun1:
    def DefineProperties(self):
        self.GlobalZ = Property.Float(0)
        self.timer = Property.Float()
        self.Delay = Property.Float(0.3)
        self.start = Property.Bool(True)
        self.RandomAngle = Property.Float(0)
        self.timer2 = Property.Float()
        
        self.CanAnimate = Property.Bool(True)
        self.CanAnimateIdle = Property.Bool(False)
        self.CanAnimateIdle2 = Property.Bool(False)
        self.CanShoot = Property.Bool(False)
        self.CanIdle = Property.Bool(False)

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        self.timer = 5

    def OnLogicUpdate(self, UpdateEvent):
        
        ObjectPostitionZ = self.GlobalZ
        DeltaTime = UpdateEvent.Dt
        self.timer += DeltaTime
        
        Parent = self.Owner.Parent
        
        if(self.start is True):
            self.RandomAngle = random.uniform(-5, 5)
            self.start = False
        
        if(Parent.GunManStatus.CanShoot is True):
            self.timer2 += DeltaTime
            
            WorldPosition = self.Owner.Transform.WorldTranslation
            
            if(self.timer2 > 0.6):
                
                if(self.timer > self.Delay):
                    
                    Bullet = self.Space.CreateAtPosition("EnemyGiantBullet", Vector3(WorldPosition.x, WorldPosition.y, ObjectPostitionZ))
                    Bullet.Transform.Rotation = Parent.Transform.WorldRotation
                    Bullet.EnemyGiantBullet.FireY = self.RandomAngle
                    
                    self.start = True
                    self.timer = 0
        else:
            self.timer2 = 0

Zero.RegisterComponent("GiantMiniGun1", GiantMiniGun1)