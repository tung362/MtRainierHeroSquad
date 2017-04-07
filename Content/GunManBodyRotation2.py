import Zero
import Events
import Property
import VectorMath
import math

Vector3 = VectorMath.Vec3
Quaternion = VectorMath.Quaternion

class GunManBodyRotation2:
    def DefineProperties(self):
        self.IsRight = Property.Bool(False)
        self.IsLeft = Property.Bool(False)
        self.LeftRight = Property.Bool(False)
        
        self.Start = Property.Bool(True)
        
        self.BodyX = Property.Float(0)
        self.BodyX = Property.Float(0)
        self.BodyZ = Property.Float(0)
        
        self.IsNormal = Property.Bool(True)
        

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)

    def OnLogicUpdate(self, UpdateEvent):
        Parent = self.Owner.Parent
        Position = self.Owner.Transform.Translation
        
        Tung = self.Space.FindObjectByName("Tung")
        Austin = self.Space.FindObjectByName("Austin")
        Trey = self.Space.FindObjectByName("Trey")
        Peyton = self.Space.FindObjectByName("Peyton")
        Sedrick = self.Space.FindObjectByName("Sedrick")
        Julio = self.Space.FindObjectByName("Julio")
        
        MouseScreenPosition = Zero.Mouse.ScreenPosition
        WorldMousePosition = self.LevelSettings.CameraViewport.ScreenToWorldZPlane(MouseScreenPosition, 0)
        Distance = WorldMousePosition - self.Owner.Transform.WorldTranslation
        
        RotationAngles = Quaternion(0, 0, 0)
        
        if(self.Start is True):
            self.BodyX = Position.x
            self.BodyY = Position.y
            self.BodyZ = Position.z
            self.Start = False
            
        Distance = Vector3(0, 0, 0)
        
        if(Tung):
            GetTungPos = Tung.Transform.Translation
            Distance = GetTungPos - self.Owner.Transform.WorldTranslation
            
        elif(Austin):
            GetAustinPos = Austin.Transform.Translation
            Distance = GetAustinPos - self.Owner.Transform.WorldTranslation
            
        elif(Trey):
            GetTreyPos = Trey.Transform.Translation
            Distance = GetTreyPos - self.Owner.Transform.WorldTranslation
            
        elif(Peyton):
            GetPeytonPos = Peyton.Transform.Translation
            Distance = GetPeytonPos - self.Owner.Transform.WorldTranslation
            
        elif(Sedrick):
            GetSedrickPos = Sedrick.Transform.Translation
            Distance = GetSedrickPos - self.Owner.Transform.WorldTranslation
            
        elif(Julio):
            GetJulioPos = Julio.Transform.Translation
            Distance = GetJulioPos - self.Owner.Transform.WorldTranslation
        
        
        if(self.Owner.GunManStatus.CanShoot is True):
            self.IsNormal = False
                
            if(Distance.x < 0):
                self.IsLeft = True
                self.IsRight = False
                if(self.IsLeft is True):
                    if(self.LeftRight is True):
                        #print("Right")
                        RotationAngles.y = 1
                        self.Owner.Transform.Rotation = RotationAngles
                        self.LeftRight = False
                
            if(Distance.x > 0):
                self.IsLeft = False
                self.IsRight = True
                if(self.IsRight is True):
                    if(self.LeftRight is False):
                        #print("Left")
                        RotationAngles.y = 0
                        self.Owner.Transform.Rotation = RotationAngles
                        self.LeftRight = True
        else:
            self.IsNormal = True
            
            
            
        if(self.IsNormal is True):
            if(Parent.GunManBody.IsLeftRR is True):
                self.IsLeft = True
                self.IsRight = False
                if(self.IsLeft is True):
                    if(self.LeftRight is True):
                        RotationAngles.y = -1
                        self.Owner.Transform.Rotation = RotationAngles
                        self.LeftRight = False
                        
            if(Parent.GunManBody.IsRightRR is True):
                self.IsLeft = False
                self.IsRight = True
                if(self.IsRight is True):
                    if(self.LeftRight is False):
                        RotationAngles.y = 0
                        self.Owner.Transform.Rotation = RotationAngles
                        self.LeftRight = True

Zero.RegisterComponent("GunManBodyRotation2", GunManBodyRotation2)