import Zero
import Events
import Property
import VectorMath
import random

Vector3 = VectorMath.Vec3

class ShotGun1:

    def DefineProperties(self):
        self.GlobalZ = Property.Float(0)
        self.timer = Property.Float()
        self.Delay = Property.Float(1)
        self.start = Property.Bool(True)
        self.RandomAngle = Property.Float(0)
        
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
        
        if(Zero.Mouse.IsButtonDown(Zero.MouseButtons.Left)):
            self.CanAnimateIdle = True
            
            WorldPosition = self.Owner.Transform.WorldTranslation
            
            
            if(self.timer > self.Delay):
                
                self.CanAnimateIdle2 = True
                
                Bullet = self.Space.CreateAtPosition("PlayerSmallBullet", Vector3(WorldPosition.x, WorldPosition.y, ObjectPostitionZ))
                Bullet.Transform.Rotation = Parent.Transform.WorldRotation
                Bullet.PlayerSmallBullet.FireY = self.RandomAngle
                
                Bullet1 = self.Space.CreateAtPosition("PlayerSmallBullet", Vector3(WorldPosition.x, WorldPosition.y, ObjectPostitionZ))
                Bullet1.Transform.Rotation = Parent.Transform.WorldRotation
                Bullet1.PlayerSmallBullet.FireY = 5 + self.RandomAngle
                
                Bullet2 = self.Space.CreateAtPosition("PlayerSmallBullet", Vector3(WorldPosition.x, WorldPosition.y, ObjectPostitionZ))
                Bullet2.Transform.Rotation = Parent.Transform.WorldRotation
                Bullet2.PlayerSmallBullet.FireY = self.RandomAngle
                
                Bullet3 = self.Space.CreateAtPosition("PlayerSmallBullet", Vector3(WorldPosition.x, WorldPosition.y, ObjectPostitionZ))
                Bullet3.Transform.Rotation = Parent.Transform.WorldRotation
                Bullet3.PlayerSmallBullet.FireY = -5 + self.RandomAngle
                
                Bullet4 = self.Space.CreateAtPosition("PlayerSmallBullet", Vector3(WorldPosition.x, WorldPosition.y, ObjectPostitionZ))
                Bullet4.Transform.Rotation = Parent.Transform.WorldRotation
                Bullet4.PlayerSmallBullet.FireY = 10 + self.RandomAngle
                
                Bullet5 = self.Space.CreateAtPosition("PlayerSmallBullet", Vector3(WorldPosition.x, WorldPosition.y, ObjectPostitionZ))
                Bullet5.Transform.Rotation = Parent.Transform.WorldRotation
                Bullet5.PlayerSmallBullet.FireY = -10 + self.RandomAngle
                
                Bullet6 = self.Space.CreateAtPosition("PlayerSmallBullet", Vector3(WorldPosition.x, WorldPosition.y, ObjectPostitionZ))
                Bullet6.Transform.Rotation = Parent.Transform.WorldRotation
                Bullet6.PlayerSmallBullet.FireY = 15 + self.RandomAngle
                
                Bullet7 = self.Space.CreateAtPosition("PlayerSmallBullet", Vector3(WorldPosition.x, WorldPosition.y, ObjectPostitionZ))
                Bullet7.Transform.Rotation = Parent.Transform.WorldRotation
                Bullet7.PlayerSmallBullet.FireY = -15 + self.RandomAngle
                
                Bullet8 = self.Space.CreateAtPosition("PlayerSmallBullet", Vector3(WorldPosition.x, WorldPosition.y, ObjectPostitionZ))
                Bullet8.Transform.Rotation = Parent.Transform.WorldRotation
                Bullet8.PlayerSmallBullet.FireY = 20 + self.RandomAngle
                
                Bullet9 = self.Space.CreateAtPosition("PlayerSmallBullet", Vector3(WorldPosition.x, WorldPosition.y, ObjectPostitionZ))
                Bullet9.Transform.Rotation = Parent.Transform.WorldRotation
                Bullet9.PlayerSmallBullet.FireY = -20 + self.RandomAngle
                
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
                
        if(self.CanShoot is True):
            Parent.Sprite.SpriteSource = "AustinBodyShoot"
            self.CanShoot = False
        elif(self.CanIdle is True):
            Parent.Sprite.SpriteSource = "AustinBody"
            self.CanIdle = False

Zero.RegisterComponent("ShotGun1", ShotGun1)