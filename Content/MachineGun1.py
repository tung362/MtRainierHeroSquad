import Zero
import Events
import Property
import VectorMath
import random

Vector3 = VectorMath.Vec3

class MachineGun1:

    def DefineProperties(self):
        self.GlobalZ = Property.Float(0)
        self.timer = Property.Float()
        self.Delay = Property.Float(0.3)
        self.start = Property.Bool(True)
        self.RandomAngle = Property.Float(0)

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)

    def OnLogicUpdate(self, UpdateEvent):
        
        ObjectPostitionZ = self.GlobalZ
        
        if(self.start is True):
            self.RandomAngle = random.uniform(-5, 5)
            self.start = False
        
        if(Zero.Mouse.IsButtonDown(Zero.MouseButtons.Left)):
            
            DeltaTime = UpdateEvent.Dt
            self.timer += DeltaTime
            
            WorldPosition = self.Owner.Transform.WorldTranslation
            
            Parent = self.Owner.Parent
            
            if(self.timer > self.Delay):
            
                Bullet = self.Space.CreateAtPosition("PlayerSmallBullet", Vector3(WorldPosition.x, WorldPosition.y, ObjectPostitionZ))
                Bullet.Transform.Rotation = Parent.Transform.WorldRotation
                Bullet.PlayerSmallBullet.FireY = self.RandomAngle
                self.start = True
                self.timer = 0

Zero.RegisterComponent("MachineGun1", MachineGun1)