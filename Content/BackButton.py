import Zero
import Events
import Property
import VectorMath

Vector3 = VectorMath.Vec3

class BackButton:
    def DefineProperties(self):
        pass

    def Initialize(self, initializer):
        Zero.Connect(self.Owner, Events.MouseEnter, self.OnMouseEnter);
        Zero.Connect(self.Owner, Events.MouseExit, self.OnMouseExit);
        Zero.Connect(self.Owner, Events.MouseDown, self.OnMouseDown);
        Zero.Connect(self.Owner, Events.MouseUp, self.OnMouseUp);

        
        
    def OnMouseUp(self, ViewportMouseEvent):
        #Let Go Of Click
        
        self.Space.LoadLevel("MainMenu")

    def OnMouseDown(self, ViewportMouseEvent):
        #Clicked
        
        self.Owner.Transform.Scale = Vector3(1.1, 1.1, 1)

    def OnMouseExit(self, ViewportMouseEvent):
        #Exiting Button
        
        self.Owner.Transform.Scale = Vector3(1.5, 1.5, 1)
        self.Owner.Sprite.SpriteSource = "BackIdle"

    def OnMouseEnter(self, ViewportMouseEvent):
        #Entering Button
        
        self.Owner.Transform.Scale = Vector3(1.3, 1.3, 1)
        self.Owner.Sprite.SpriteSource = "BackMoused"

Zero.RegisterComponent("BackButton", BackButton)