import Zero
import Events
import Property
import VectorMath

class DestroyOffScreen:
    def DefineProperties(self):
        self.timer = Property.Float()

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        Zero.Connect(self.Owner, Events.ExitView, self.OnExitView)
        
    def OnLogicUpdate(self, UpdateEvent):
        DeltaTime = UpdateEvent.Dt
        self.timer += DeltaTime
        
        if(self.timer > 2.0):
            self.Owner.Destroy()
        
    def OnExitView(self, GraphicalEvent):
        
        self.Owner.Destroy()

Zero.RegisterComponent("DestroyOffScreen", DestroyOffScreen)