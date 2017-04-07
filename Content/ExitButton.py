import Zero
import Events
import Property
import VectorMath

Vector3 = VectorMath.Vec3

class ExitButton:
    
    AllowQuit = Property.Bool(default = False)
    
    def DefineProperties(self):
        pass

    def Initialize(self, initializer):
        Zero.Connect(self.Owner, Events.MouseEnter, self.OnMouseEnter);
        Zero.Connect(self.Owner, Events.MouseExit, self.OnMouseExit);
        Zero.Connect(self.Owner, Events.MouseDown, self.OnMouseDown);
        Zero.Connect(self.Owner, Events.MouseUp, self.OnMouseUp);
        Zero.Connect(self.GameSession, Events.GameRequestQuit, self.OnGameRequestQuit)
        
    def OnGameRequestQuit(self, gameEvent):
        gameEvent.Handled = True
        
        #if(self.AllowQuit):
            #self.QuitGame()
        
        
    def OnMouseUp(self, ViewportMouseEvent):
        #Let Go Of Click
        
        self.GameSession.Quit()

    def OnMouseDown(self, ViewportMouseEvent):
        #Clicked
        
        self.Owner.Transform.Scale = Vector3(1.6, 1.6, 2)

    def OnMouseExit(self, ViewportMouseEvent):
        #Exiting Button
        
        self.Owner.Transform.Scale = Vector3(2, 2, 2)
        self.Owner.Sprite.SpriteSource = "ExitIdle"

    def OnMouseEnter(self, ViewportMouseEvent):
        #Entering Button
        
        self.Owner.Transform.Scale = Vector3(1.8, 1.8, 2)
        self.Owner.Sprite.SpriteSource = "ExitMoused"
    
    #def QuitGame(self):
        #self.GameSession.Quit()

Zero.RegisterComponent("ExitButton", ExitButton)