import Zero
import Events
import Property
import VectorMath

#import DebugDraw
#import Color

Vector3 = VectorMath.Vec3

class Look4:
    
    def DefineProperties(self):
        pass

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)

    def OnLogicUpdate(self, UpdateEvent):
        
        Parent = self.Owner.Parent
        
        Position = self.Owner.Transform.WorldTranslation
        Child1 = self.Owner.FindChildByName("LookPoint4")
        Child1Pos = Child1.Transform.WorldTranslation
        
        Ray = VectorMath.Ray()
        Ray.Start = Vector3(Position.x, Position.y, 0) #Start
        Ray.Direction = Vector3(Child1Pos.x - Position.x, Child1Pos.y - Position.y, 0) #End
        MaxRayCastDistance = 1.0
        #RayColor = Color.Blue
        
        CastResultsRange = self.Space.PhysicsSpace.CastRayResults(Ray, 1) # Number Of Objects
        
        LastCastResult = None #Limit
        
        #print(Parent.GunManStatus.CanShoot)
        
        for CastResult in CastResultsRange:
            if(CastResult.Distance >= MaxRayCastDistance):
                break
                
            if(CastResult.ObjectHit.Name == "Tung" or CastResult.ObjectHit.Name == "Austin" or CastResult.ObjectHit.Name == "Trey" or CastResult.ObjectHit.Name == "Peyton" or CastResult.ObjectHit.Name == "Sedrick" or CastResult.ObjectHit.Name == "Julio"):
                Parent.GunManStatus.CanShoot = True
                Parent.GunManStatus.RayCast4 = True
            else:
                Parent.GunManStatus.RayCast4 = False
                
                if(Parent.GunManStatus.RayCast1 is False and Parent.GunManStatus.RayCast2 is False and Parent.GunManStatus.RayCast3 is False and Parent.GunManStatus.RayCast4 is False and Parent.GunManStatus.RayCast5 is False and Parent.GunManStatus.RayCast6 is False and Parent.GunManStatus.RayCast7 is False and Parent.GunManStatus.RayCast8 is False and Parent.GunManStatus.RayCast9 is False):
                    Parent.GunManStatus.CanShoot = False
            
            LastCastResult =  CastResult #Limit
            
        if(not LastCastResult): #Limit
            EndPosition = Ray.Start + Ray.Direction * MaxRayCastDistance
            #self.DrawArrow(Ray.Start, EndPosition, RayColor)
        else:
            EndPosition = Ray.Start + Ray.Direction * LastCastResult.Distance
            #self.DrawArrow(Ray.Start, EndPosition, RayColor)
                
            
    #def DrawArrow(self, StartPos, EndPos, ArrowColor):
        #DebugDraw.DrawArrow(StartPos, EndPos, 0.25, ArrowColor)

Zero.RegisterComponent("Look4", Look4)