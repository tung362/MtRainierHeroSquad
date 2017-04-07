import Zero
import Events
import Property
import VectorMath
import random

Vector3 = VectorMath.Vec3

class SpawnPointLevel2:
    def DefineProperties(self):
        self.Chance = Property.Int()
        self.Start = Property.Bool(True)
        
        self.Switch1 = Property.Bool(True)
        self.Switch2 = Property.Bool(True)
        self.Switch3 = Property.Bool(True)
        self.Switch4 = Property.Bool(True)
        self.Switch5 = Property.Bool(True)
        self.Switch6 = Property.Bool(True)

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)

    def OnLogicUpdate(self, UpdateEvent):
        Position = self.Owner.Transform.WorldTranslation
        
        if(self.Start is True):
            self.Switch1 = True
            self.Switch2 = True
            self.Switch3 = True
            self.Switch4 = True
            self.Switch5 = True
            self.Switch6 = True
            self.Chance = random.randint(1, 6)
            self.Start = False
            
            
        if(self.Chance == 1):
            Tracker = self.Space.FindObjectByName("PlayerTracker")
            if(Tracker.PlayerTracker.TungIsAlive is True):
                Player = self.Space.CreateAtPosition("Tung", Vector3(Position.x, Position.y, 0))
                Player.PlayerController.IsOnAirShip = True
                Player.BoxCollider.Offset = Vector3(0, 0.05, 0)
                Player.BoxCollider.Size = Vector3(0.5, 0.5, 10)
                Tracker.PlayerTracker.TungIsAlive = False
                self.Switch1 = False
            else:
                if(self.Switch1 is True):
                    self.Start = True
                    self.Switch1 = False
            
        elif(self.Chance == 2):
            Tracker = self.Space.FindObjectByName("PlayerTracker")
            if(Tracker.PlayerTracker.AustinIsAlive is True):
                Player = self.Space.CreateAtPosition("Austin", Vector3(Position.x, Position.y, 0))
                Player.AustinPlayerController.IsOnAirShip = True
                Player.BoxCollider.Offset = Vector3(0, 0.05, 0)
                Player.BoxCollider.Size = Vector3(0.5, 0.5, 10)
                Tracker.PlayerTracker.AustinIsAlive = False
                self.Switch2 = False
            else:
                if(self.Switch2 is True):
                    self.Start = True
                self.Switch2 = False
            
        elif(self.Chance == 3):
            Tracker = self.Space.FindObjectByName("PlayerTracker")
            if(Tracker.PlayerTracker.TreyIsAlive is True):
                Player = self.Space.CreateAtPosition("Trey", Vector3(Position.x, Position.y, 0))
                Player.TreyPlayerController.IsOnAirShip = True
                Player.BoxCollider.Offset = Vector3(0, 0.05, 0)
                Player.BoxCollider.Size = Vector3(0.5, 0.5, 10)
                Tracker.PlayerTracker.TreyIsAlive = False
                self.Switch3 = False
            else:
                if(self.Switch3 is True):
                    self.Start = True
                    self.Switch3 = False
            
        elif(self.Chance == 4):
            Tracker = self.Space.FindObjectByName("PlayerTracker")
            if(Tracker.PlayerTracker.PeytonIsAlive is True):
                Player = self.Space.CreateAtPosition("Peyton", Vector3(Position.x, Position.y, 0))
                Player.PeytonPlayerController.IsOnAirShip = True
                Player.BoxCollider.Offset = Vector3(0, 0.05, 0)
                Player.BoxCollider.Size = Vector3(0.5, 0.5, 10)
                Tracker.PlayerTracker.PeytonIsAlive = False
                self.Switch4 = False
            else:
                if(self.Switch4 is True):
                    self.Start = True
                    self.Switch4 = False
            
        elif(self.Chance == 5):
            Tracker = self.Space.FindObjectByName("PlayerTracker")
            if(Tracker.PlayerTracker.SedrickIsAlive is True):
                Player = self.Space.CreateAtPosition("Sedrick", Vector3(Position.x, Position.y, 0))
                Player.SedrickPlayerController.IsOnAirShip = True
                Player.BoxCollider.Offset = Vector3(0, 0.05, 0)
                Player.BoxCollider.Size = Vector3(0.5, 0.5, 10)
                Tracker.PlayerTracker.SedrickIsAlive = False
                self.Switch5 = False
            else:
                if(self.Switch5 is True):
                    self.Start = True
                    self.Switch5 = False
            
        elif(self.Chance == 6):
            Tracker = self.Space.FindObjectByName("PlayerTracker")
            if(Tracker.PlayerTracker.JulioIsAlive is True):
                Player = self.Space.CreateAtPosition("Julio", Vector3(Position.x, Position.y, 0))
                Player.JulioPlayerController.IsOnAirShip = True
                Player.BoxCollider.Offset = Vector3(0, 0.05, 0)
                Player.BoxCollider.Size = Vector3(0.5, 0.5, 10)
                Tracker.PlayerTracker.JulioIsAlive = False
                self.Switch6 = False
            else:
                if(self.Switch6 is True):
                    self.Start = True
                    self.Switch6 = False
                    
        if(Zero.Keyboard.KeyIsPressed(Zero.Keys.O)):
            self.Start = True

Zero.RegisterComponent("SpawnPointLevel2", SpawnPointLevel2)