import Zero
import Events
import Property
import VectorMath

Vector3 = VectorMath.Vec3

class StartButton:
    def DefineProperties(self):
        pass

    def Initialize(self, initializer):
        Zero.Connect(self.Owner, Events.MouseEnter, self.OnMouseEnter);
        Zero.Connect(self.Owner, Events.MouseExit, self.OnMouseExit);
        Zero.Connect(self.Owner, Events.MouseDown, self.OnMouseDown);
        Zero.Connect(self.Owner, Events.MouseUp, self.OnMouseUp);

        
        
    def OnMouseUp(self, ViewportMouseEvent):
        #Let Go Of Click
        #print("Let Go Of Click")
        
        self.Space.LoadLevel("Level")

    def OnMouseDown(self, ViewportMouseEvent):
        #Clicked
        #print("Click")
        
        self.Owner.Transform.Scale = Vector3(1.6, 1.6, 2)

    def OnMouseExit(self, ViewportMouseEvent):
        #Exiting Button
        #print("Exit")
        
        self.Owner.Transform.Scale = Vector3(2, 2, 2)
        self.Owner.Sprite.SpriteSource = "PlayIdle"

    def OnMouseEnter(self, ViewportMouseEvent):
        #Entering Button
        #print("Enter")
        
        self.Owner.Transform.Scale = Vector3(1.8, 1.8, 2)
        self.Owner.Sprite.SpriteSource = "PlayMoused"

Zero.RegisterComponent("StartButton", StartButton)