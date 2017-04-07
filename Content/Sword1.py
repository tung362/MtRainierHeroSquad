import Zero
import Events
import Property
import VectorMath
import random

#import DebugDraw
#import Color

Vector3 = VectorMath.Vec3

class Sword1:

    def DefineProperties(self):
        self.GlobalZ = Property.Float(0)
        self.timer = Property.Float()
        self.Delay = Property.Float(0.01)
        self.start = Property.Bool(True)
        self.RandomAngle = Property.Float(0)
        
        self.CanAnimate = Property.Bool(True)
        self.CanAnimateIdle = Property.Bool(False)
        self.CanAnimateIdle2 = Property.Bool(False)
        self.CanShoot = Property.Bool(False)
        self.CanIdle = Property.Bool(False)
        
        self.CanManSound = Property.Bool(False)
        self.timer2 = Property.Float()

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        self.timer = 5

    def OnLogicUpdate(self, UpdateEvent):
        
        ObjectPostitionZ = self.GlobalZ
        DeltaTime = UpdateEvent.Dt
        self.timer += DeltaTime
        
        Parent = self.Owner.Parent
        
        if(self.start is True):
            self.RandomAngle = random.uniform(-5, 5)
            self.start = False
        
        if(Zero.Mouse.IsButtonDown(Zero.MouseButtons.Left)):
            self.CanAnimateIdle = True
            
            WorldPosition = self.Owner.Transform.WorldTranslation
            
            
            if(self.timer > self.Delay):
                
                self.CanAnimateIdle2 = True
                self.timer2 += DeltaTime
                
                Position = self.Owner.Transform.WorldTranslation
                Child1 = self.Owner.FindChildByName("MeleeChild1")
                Child1Pos = Child1.Transform.WorldTranslation
                
                Ray = VectorMath.Ray()
                Ray.Start = Vector3(Position.x, Position.y, 0) #Start
                Ray.Direction = Vector3(Child1Pos.x - Position.x, Child1Pos.y - Position.y, Child1Pos.z - Position.z) #End
                MaxRayCastDistance = 1.0
                #RayColor = Color.Orange
                
                CastResultsRange = self.Space.PhysicsSpace.CastRayResults(Ray, 10) # Number Of Objects
                
                LastCastResult = None #Limit
                
                for CastResult in CastResultsRange:
                    if(CastResult.Distance >= MaxRayCastDistance):
                        break
                        
                    if(CastResult.ObjectHit.Name == "Grass1"):
                        
                        CastResult.ObjectHit.Grass.CurrentHealth -= 5
                    
                    elif(CastResult.ObjectHit.Name == "Dirt1"):
                        
                        CastResult.ObjectHit.Dirt.CurrentHealth -= 5
                        
                    elif(CastResult.ObjectHit.Name == "Wall1"):
                        
                        CastResult.ObjectHit.Wall1.CurrentHealth -= 5
                        
                    elif(CastResult.ObjectHit.Name == "Crate"):
                        
                        CastResult.ObjectHit.SmallCrate.CurrentHealth -= 5
                        
                    elif(CastResult.ObjectHit.Name == "Barrel"):
                        
                        CastResult.ObjectHit.Barrel.CurrentHealth -= 5
                        
                    elif(CastResult.ObjectHit.Name == "FireBarrel"):
                        
                        CastResult.ObjectHit.FireBarrel.CurrentHealth -= 5
                        
                    elif(CastResult.ObjectHit.Name == "BridgeBottom"):
                        
                        CastResult.ObjectHit.Bridge.CurrentHealth -= 5
                        
                    elif(CastResult.ObjectHit.Name == "GunMan"):
                        
                        CastResult.ObjectHit.GunManHealth.CurrentHealth -= 5
                        
                    elif(CastResult.ObjectHit.Name == "HeavyGunMan"):
                        
                        CastResult.ObjectHit.HeavyGunManHealth.CurrentHealth -= 5
                    
                    LastCastResult =  CastResult #Limit
            
                if(not LastCastResult): #Limit
                    EndPosition = Ray.Start + Ray.Direction * MaxRayCastDistance
                    #self.DrawArrow(Ray.Start, EndPosition, RayColor)
                else:
                    EndPosition = Ray.Start + Ray.Direction * LastCastResult.Distance
                    #self.DrawArrow(Ray.Start, EndPosition, RayColor)
                        
                if(self.CanAnimate is True):
                    self.CanShoot = True
                    self.CanAnimate = False
                
                if(self.timer2 > 0.2):
                    self.CanManSound = True
                    self.timer2 = 0
                
                self.start = True
                self.timer = 0
            else:
                if(self.CanAnimateIdle2 is True and Parent.Sprite.CurrentFrame >= 2):
                    self.CanIdle = True
                    self.CanManSound = True
                    self.CanAnimateIdle2 = False
                self.CanAnimate = True
        else:
            if(self.CanAnimateIdle is True):
                self.CanIdle = True
                self.CanAnimate = True
                self.CanAnimateIdle = False
                
        if(self.CanShoot is True):
            Parent.Sprite.SpriteSource = "JulioBodyShoot"
            self.CanShoot = False
        elif(self.CanIdle is True):
            Parent.Sprite.SpriteSource = "JulioBody"
            self.CanIdle = False
            
        if(self.CanManSound is True):
            self.Owner.SoundEmitter.PlayCue("JulioShoot")
            self.CanManSound = False
            
    #def DrawArrow(self, StartPos, EndPos, ArrowColor):
        #DebugDraw.DrawArrow(StartPos, EndPos, 0.25, ArrowColor)

Zero.RegisterComponent("Sword1", Sword1)