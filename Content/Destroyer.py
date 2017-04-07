import Zero
import Events
import Property
import VectorMath

class Destroyer:
    def DefineProperties(self):
        pass

    def Initialize(self, initializer):
        #Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        Zero.Connect(self.Owner, Events.CollisionStarted, self.OnCollisionStarted)

    def OnLogicUpdate(self, UpdateEvent):
        pass
        
    def OnCollisionStarted(self, CollisionEvent):
        other = CollisionEvent.OtherObject
        
        if(other.Name == "Tung"):
            other.TungHealth.CurrentHealth -= 200
            
        if(other.Name == "Austin"):
            other.AustinHealth.CurrentHealth -= 200
            
        if(other.Name == "Trey"):
            other.TreyHealth.CurrentHealth -= 200
            
        if(other.Name == "Peyton"):
            other.PeytonHealth.CurrentHealth -= 200
            
        if(other.Name == "Sedrick"):
            other.SedrickHealth.CurrentHealth -= 200
            
        if(other.Name == "Julio"):
            other.JulioHealth.CurrentHealth -= 200
            
        if(other.Name == "GunMan"):
            other.Destroy()

Zero.RegisterComponent("Destroyer", Destroyer)