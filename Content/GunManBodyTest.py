import Zero
import Events
import Property
import VectorMath
import math

Vector3 = VectorMath.Vec3
Quaternion = VectorMath.Quaternion

class GunManBodyTest:
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
        Child = self.Owner.FindChildByName("GunManBody")
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
        
        
        if(Child.GunManStatus.CanShoot is True):
            self.IsNormal = False
            
            if(Tung):
                GetTungPos = Tung.Transform.Translation
                self.Owner.Orientation.LookAtPoint(Vector3(GetTungPos.x, GetTungPos.y, 0))
                #print("Tung")
                
            elif(Austin):
                GetAustinPos = Austin.Transform.Translation
                self.Owner.Orientation.LookAtPoint(Vector3(GetAustinPos.x, GetAustinPos.y, 0))
                #print("Austin")
                
            elif(Trey):
                GetTreyPos = Trey.Transform.Translation
                self.Owner.Orientation.LookAtPoint(Vector3(GetTreyPos.x, GetTreyPos.y, 0))
                #print("Trey")
                
            elif(Peyton):
                GetPeytonPos = Peyton.Transform.Translation
                self.Owner.Orientation.LookAtPoint(Vector3(GetPeytonPos.x, GetPeytonPos.y, 0))
                #print("Peyton")
                
            elif(Sedrick):
                GetSedrickPos = Sedrick.Transform.Translation
                self.Owner.Orientation.LookAtPoint(Vector3(GetSedrickPos.x, GetSedrickPos.y, 0))
                #print("Sedrick")
                
            elif(Julio):
                GetJulioPos = Julio.Transform.Translation
                self.Owner.Orientation.LookAtPoint(Vector3(GetJulioPos.x, GetJulioPos.y, 0))
                
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
                #print("Julio")
            
            #if(Parent.GunManController.Side is True):
                
                #self.Owner.Orientation.LookAtPoint(Vector3(WorldMousePosition.x, WorldMousePosition.y, 0))
                
            #elif(Parent.GunManController.Side2 is True):
                #self.Owner.Orientation.LookAtPoint(Vector3(WorldMousePosition.x, WorldMousePosition.y, 0))
                
        if(self.IsNormal is True):
            if(Parent.GunManController.IsLeftR is True):
                self.IsLeft = True
                self.IsRight = False
                if(self.IsLeft is True):
                    if(self.LeftRight is True):
                        RotationAngles.y = 1
                        self.Owner.Transform.Rotation = RotationAngles
                        self.LeftRight = False
                        
            if(Parent.GunManController.IsRightR is True):
                self.IsLeft = False
                self.IsRight = True
                if(self.IsRight is True):
                    if(self.LeftRight is False):
                        RotationAngles.y = 0
                        self.Owner.Transform.Rotation = RotationAngles
                        self.LeftRight = True
                        
        #print(self.Owner.Transform.WorldRotation)
        if(Zero.Keyboard.KeyIsDown(Zero.Keys.S) and not Zero.Keyboard.KeyIsDown(Zero.Keys.A) and not Zero.Keyboard.KeyIsDown(Zero.Keys.D)):
            self.Owner.Transform.Translation = Vector3(self.BodyX, self.BodyY - 0.09, self.BodyZ)
            
        elif(Zero.Keyboard.KeyIsDown(Zero.Keys.Space) or Parent.GunManController.OnGround is False):
            self.Owner.Transform.Translation = Vector3(self.BodyX, self.BodyY - 0.02, self.BodyZ)
            
        else:
            self.Owner.Transform.Translation = Vector3(self.BodyX, self.BodyY, self.BodyZ)

Zero.RegisterComponent("GunManBodyTest", GunManBodyTest)