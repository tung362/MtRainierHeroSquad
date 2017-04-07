import Zero
import Events
import Property
import VectorMath
import random

Vector3 = VectorMath.Vec3

class Pistol1:
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
            self.CanAnimateIdle = True
            
            WorldPosition = self.Owner.Transform.WorldTranslation
            
            if(self.timer2 > 0.6):
                
                if(self.timer > self.Delay):
                    
                    self.CanAnimateIdle2 = True
                    
                    Bullet = self.Space.CreateAtPosition("EnemySmallBullet", Vector3(WorldPosition.x, WorldPosition.y, ObjectPostitionZ))
                    Bullet.Transform.Rotation = Parent.Transform.WorldRotation
                    Bullet.EnemySmallBullet.FireY = self.RandomAngle
                    
                    if(self.CanAnimate is True):
                        self.CanShoot = True
                        self.CanAnimate = False
                    
                    self.start = True
                    self.timer = 0
                else:
                    if(self.CanAnimateIdle2 is True and Parent.Sprite.CurrentFrame >= 2):
                        self.CanIdle = True
                        self.CanAnimateIdle2 = False
                    self.CanAnimate = True
            else:
                if(self.CanAnimateIdle is True):
                    self.CanIdle = True
                    self.CanAnimate = True
                    self.CanAnimateIdle = False
        else:
            self.timer2 = 0
            
            if(self.CanAnimateIdle is True):
                    self.CanIdle = True
                    self.CanAnimate = True
                    self.CanAnimateIdle = False
            
        if(self.CanShoot is True):
            Parent.Sprite.SpriteSource = "GunManBodyShoot"
            self.CanShoot = False
        elif(self.CanIdle is True):
            Parent.Sprite.SpriteSource = "GunManBody"
            self.CanIdle = False

Zero.RegisterComponent("Pistol1", Pistol1)