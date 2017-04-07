import Zero
import Events
import Property
import VectorMath
import random

Vector3 = VectorMath.Vec3

class Ladder:
    
    def DefineProperties(self):
        self.Start = Property.Bool(True)
        
        self.RandomTexture = Property.Int(0)
        
        self.CanClimb = Property.Bool(False)

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        Zero.Connect(self.Owner, Events.CollisionStarted, self.OnCollisionStarted)
        Zero.Connect(self.Owner, Events.CollisionPersisted, self.OnCollisionPersisted)
        Zero.Connect(self.Owner, Events.CollisionEnded, self.OnCollisionEnded)

    def OnLogicUpdate(self, UpdateEvent):
        
        if(self.Start == True):
            
            self.Owner.Name = "Ladder"
            self.RandomTexture = random.randint(0, 2)
            if(self.RandomTexture is 0):
                self.Owner.Sprite.SpriteSource = "Ladder"
                
            elif(self.RandomTexture is 1):
                self.Owner.Sprite.SpriteSource = "LadderA"
                
            else:
                self.Owner.Sprite.SpriteSource = "LadderB"
            self.Start = False
            
            
            
    def OnCollisionStarted(self, CollisionEvent):
        
        other = CollisionEvent.OtherObject
                
        if(other.Name == "Tung" or other.Name == "Austin" or other.Name == "Trey" or other.Name == "Peyton" or other.Name == "Sedrick" or other.Name == "Julio"):
            
            self.CanClimb = True
            #print(self.CanClimb)
            
            
    def OnCollisionPersisted(self, CollisionEvent):
        
        other = CollisionEvent.OtherObject
                
        if(other.Name == "Tung"):
            
            self.CanClimb = True
            #print(self.CanClimb)
            
            if(self.CanClimb is True and Zero.Keyboard.KeyIsDown(Zero.Keys.W)):
                other.Sprite.SpriteSource = "TungIdle"
                other.RigidBody.Velocity = Vector3(0, 5, 0)
                
        elif(other.Name == "Austin"):
            
            self.CanClimb = True
            #print(self.CanClimb)
            
            if(self.CanClimb is True and Zero.Keyboard.KeyIsDown(Zero.Keys.W)):
                other.Sprite.SpriteSource = "AustinIdle"
                other.RigidBody.Velocity = Vector3(0, 5, 0)
                
        elif(other.Name == "Trey"):
            
            self.CanClimb = True
            #print(self.CanClimb)
            
            if(self.CanClimb is True and Zero.Keyboard.KeyIsDown(Zero.Keys.W)):
                other.Sprite.SpriteSource = "TreyIdle"
                
                other.RigidBody.Velocity = Vector3(0, 5, 0)
        elif(other.Name == "Peyton"):
            
            self.CanClimb = True
            #print(self.CanClimb)
            
            if(self.CanClimb is True and Zero.Keyboard.KeyIsDown(Zero.Keys.W)):
                other.Sprite.SpriteSource = "PeytonIdle"
                other.RigidBody.Velocity = Vector3(0, 5, 0)
                
        elif(other.Name == "Sedrick"):
            
            self.CanClimb = True
            #print(self.CanClimb)
            
            if(self.CanClimb is True and Zero.Keyboard.KeyIsDown(Zero.Keys.W)):
                other.Sprite.SpriteSource = "SedrickIdle"
                other.RigidBody.Velocity = Vector3(0, 5, 0)
                
        elif(other.Name == "Julio"):
            
            self.CanClimb = True
            #print(self.CanClimb)
            
            if(self.CanClimb is True and Zero.Keyboard.KeyIsDown(Zero.Keys.W)):
                other.Sprite.SpriteSource = "JulioIdle"
                other.RigidBody.Velocity = Vector3(0, 5, 0)
        
        
    def OnCollisionEnded(self, CollisionEvent):
        
        other = CollisionEvent.OtherObject
                
        if(other.Name == "Tung" or other.Name == "Austin" or other.Name == "Trey" or other.Name == "Peyton" or other.Name == "Sedrick" or other.Name == "Julio"):
            
            self.CanClimb = False
            #print(self.CanClimb)

Zero.RegisterComponent("Ladder", Ladder)