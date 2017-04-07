import Zero
import Events
import Property
import VectorMath
import math

Vector3 = VectorMath.Vec3
Quaternion = VectorMath.Quaternion

class TreyBody:
    def DefineProperties(self):
        self.IsRight = Property.Bool(False)
        self.IsLeft = Property.Bool(False)
        self.LeftRight = Property.Bool(False)
        
        self.Start = Property.Bool(True)
        
        self.BodyX = Property.Float(0)
        self.BodyX = Property.Float(0)
        self.BodyZ = Property.Float(0)

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)

    def OnLogicUpdate(self, UpdateEvent):
        Parent = self.Owner.Parent
        Position = self.Owner.Transform.Translation
        
        MouseScreenPosition = Zero.Mouse.ScreenPosition
        WorldMousePosition = self.LevelSettings.CameraViewport.ScreenToWorldZPlane(MouseScreenPosition, 0)
        Distance = WorldMousePosition - self.Owner.Transform.WorldTranslation
        
        RotationAngles = Quaternion(0, 0, 0)
        
        if(self.Start is True):
            self.BodyX = Position.x
            self.BodyY = Position.y
            self.BodyZ = Position.z
            self.Start = False
        
        if(Parent.TreyPlayerController.Side is True):
            
            self.Owner.Orientation.LookAtPoint(Vector3(WorldMousePosition.x, WorldMousePosition.y, 0))
            
        if(Parent.TreyPlayerController.Side2 is True):
            self.Owner.Orientation.LookAtPoint(Vector3(WorldMousePosition.x, WorldMousePosition.y, 0))
            
        #print(self.Owner.Orientation.AbsoluteAngle)
        #print(self.Owner.Orientation.Rotation)
        
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
                    
        if(Zero.Keyboard.KeyIsDown(Zero.Keys.S) and not Zero.Keyboard.KeyIsDown(Zero.Keys.A) and not Zero.Keyboard.KeyIsDown(Zero.Keys.D)):
            self.Owner.Transform.Translation = Vector3(self.BodyX, self.BodyY - 0.09, self.BodyZ)
            Parent.BoxCollider.Offset = Vector3(0.02, 0.07, 0)
            Parent.BoxCollider.Size = Vector3(0.1, 0.3, 10)
            
        elif(Zero.Keyboard.KeyIsDown(Zero.Keys.Space) or Parent.TreyPlayerController.OnGround is False):
            self.Owner.Transform.Translation = Vector3(self.BodyX, self.BodyY - 0.02, self.BodyZ)
            
        else:
            self.Owner.Transform.Translation = Vector3(self.BodyX, self.BodyY, self.BodyZ)
            Parent.BoxCollider.Offset = Vector3(0.02, 0.15, 0)
            Parent.BoxCollider.Size = Vector3(0.1, 0.5, 10)

Zero.RegisterComponent("TreyBody", TreyBody)