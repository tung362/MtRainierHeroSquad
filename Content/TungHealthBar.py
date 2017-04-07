import Zero
import Events
import Property
import VectorMath

Vector3 = VectorMath.Vec3

class TungHealthBar:
    
    def DefineProperties(self):
        self.ObjectX = Property.Float()
        self.FirstCameraSize = Property.Float()
        self.FirstScale = Property.Float()
        self.FirstPosition = Property.Float()
        self.Start = Property.Bool(True)
        self.Start2 = Property.Bool(True)

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)

    def OnLogicUpdate(self, UpdateEvent):
        
        Player = self.Space.FindObjectByName("Tung")
        GetCamera = self.Space.FindObjectByName("Camera")
        
        if(Player):
            ObjectPosition = self.Owner.Transform.Translation
            
            if(self.Start == True):
                self.Owner.Sprite.Visible = True
                self.ObjectX = ObjectPosition.x
                self.FirstCameraSize = GetCamera.Camera.Size
                self.FirstScale = self.Owner.Transform.Scale
                self.FirstPosition = self.Owner.Transform.Translation
                self.Start2 = True
                self.Start = False
                
            #Calculations for bar
            PlayerHealth = (Player.TungHealth.CurrentHealth / Player.TungHealth.MaxHealth)
            
            #More Bar Calculations
            ObjectAdjust = (1 - PlayerHealth) * 1.7
            
            AdjustedScaleX = self.FirstScale.x
                
            NewPosition = (self.ObjectX - ObjectAdjust)
                
            self.Owner.Transform.Scale = Vector3(PlayerHealth * AdjustedScaleX, 1.5, 1)
            self.Owner.Transform.Translation = Vector3(NewPosition, ObjectPosition.y, ObjectPosition.z)
        else:
            if(self.Start2 == True):
                self.Owner.Sprite.Visible = False
                self.Start = True
                self.Start2 = False

Zero.RegisterComponent("TungHealthBar", TungHealthBar)