import Zero
import Events
import Property
import VectorMath
import random

Vector3 = VectorMath.Vec3

class CloudSpawner:
    def DefineProperties(self):
        self.Timer = Property.Float()
        self.Delay = Property.Float(3)
        self.CollisionGroupName = Property.String()
        self.CloudSpeed = Property.Float(10)
        
        self.Start = Property.Bool(True)
        self.Chance = Property.Int(0)
        self.IsLeft = Property.Bool(True)

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)

    def OnLogicUpdate(self, UpdateEvent):
        
        DeltaTime = UpdateEvent.Dt
        self.Timer += DeltaTime
        
        Position = self.Owner.Transform.Translation
        
        
        if(self.Start == True):
            
            self.Delay = random.uniform(3.0, 5.0)
            self.Chance = random.randint(1, 6)
            if(self.IsLeft is True):
                
                self.CloudSpeed = random.uniform(8.1, 15.2)
            else:
                self.CloudSpeed = random.uniform(-8.1, -15.2)
            self.Start = False
        
        
        if(self.Timer > self.Delay):
            
            if(self.Chance == 1):
                RockSpawn1 = self.Space.CreateAtPosition("Cloud1", Vector3(Position.x, Position.y, -9))
                RockSpawn1.BoxCollider.CollisionGroup = self.CollisionGroupName
                RockSpawn1.CloudBehavior.Speed = self.CloudSpeed
                
            elif(self.Chance == 2):
                RockSpawn2 = self.Space.CreateAtPosition("Cloud2", Vector3(Position.x, Position.y, -10))
                RockSpawn2.BoxCollider.CollisionGroup = self.CollisionGroupName
                RockSpawn2.CloudBehavior.Speed = self.CloudSpeed
                
            elif(self.Chance == 3):
                RockSpawn3 = self.Space.CreateAtPosition("Cloud3", Vector3(Position.x, Position.y, -8))
                RockSpawn3.BoxCollider.CollisionGroup = self.CollisionGroupName
                RockSpawn3.CloudBehavior.Speed = self.CloudSpeed
                
            elif(self.Chance == 4):
                RockSpawn4 = self.Space.CreateAtPosition("BackCloud", Vector3(Position.x, Position.y, -12))
                RockSpawn4.BoxCollider.CollisionGroup = self.CollisionGroupName
                RockSpawn4.CloudBehavior.Speed = self.CloudSpeed
                
            self.Start = True
            self.Timer = 0

Zero.RegisterComponent("CloudSpawner", CloudSpawner)