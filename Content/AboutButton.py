import Zero
import Events
import Property
import VectorMath

Vector3 = VectorMath.Vec3

class AboutButton:
    def DefineProperties(self):
        pass

    def Initialize(self, initializer):
        Zero.Connect(self.Owner, Events.MouseEnter, self.OnMouseEnter);
        Zero.Connect(self.Owner, Events.MouseExit, self.OnMouseExit);
        Zero.Connect(self.Owner, Events.MouseDown, self.OnMouseDown);
        Zero.Connect(self.Owner, Events.MouseUp, self.OnMouseUp);

        
        
    def OnMouseUp(self, ViewportMouseEvent):
        #Let Go Of Click
        
        self.Space.LoadLevel("About")

    def OnMouseDown(self, ViewportMouseEvent):
        #Clicked
        
        self.Owner.Transform.Scale = Vector3(1.6, 1.6, 2)

    def OnMouseExit(self, ViewportMouseEvent):
        #Exiting Button
        
        self.Owner.Transform.Scale = Vector3(2, 2, 2)
        self.Owner.Sprite.SpriteSource = "AboutIdle"

    def OnMouseEnter(self, ViewportMouseEvent):
        #Entering Button
        
        self.Owner.Transform.Scale = Vector3(1.8, 1.8, 2)
        self.Owner.Sprite.SpriteSource = "AboutMoused"

Zero.RegisterComponent("AboutButton", AboutButton)