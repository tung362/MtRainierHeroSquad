import Zero
import Events
import Property
import VectorMath

Vector3 = VectorMath.Vec3

class HackFunction:
    def DefineProperties(self):
        self.GodMode = Property.Bool(False)
        self.Switch = Property.Bool(True)
        self.GodModeToggle = Property.Bool(True)
        self.GodModeToggle2 = Property.Bool(True)

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        Zero.Connect(self.GameSession, Events.GameRequestQuit, self.OnGameRequestQuit)
    
    
    def OnGameRequestQuit(self, gameEvent):
        gameEvent.Handled = True
        
    def OnLogicUpdate(self, UpdateEvent):
        
        Tracker = self.Space.FindObjectByName("PlayerTracker")
        Tung = self.Space.FindObjectByName("Tung")
        Austin = self.Space.FindObjectByName("Austin")
        Trey = self.Space.FindObjectByName("Trey")
        Peyton = self.Space.FindObjectByName("Peyton")
        Sedrick = self.Space.FindObjectByName("Sedrick")
        Julio = self.Space.FindObjectByName("Julio")
            
        if(Zero.Keyboard.KeyIsPressed(Zero.Keys.G)):
            if(self.Switch is True):
                if(self.GodMode is False):
                    self.GodModeToggle = True
                    self.GodModeToggle2 = True
                    self.GodMode = True
                    self.Switch = False
                elif(self.GodMode is True):
                    self.GodModeToggle = True
                    self.GodModeToggle2 = True
                    self.GodMode = False
                    self.Switch = False
            else: 
                self.Switch = True
            
        if(Zero.Keyboard.KeyIsPressed(Zero.Keys.Eight)):
            self.Space.LoadLevel("Level")
        
        if(Zero.Keyboard.KeyIsPressed(Zero.Keys.Nine)):
            self.Space.LoadLevel("Level2")
        
        if(Zero.Keyboard.KeyIsPressed(Zero.Keys.Zero)):
            self.Space.ReloadLevel()
        
        if(Zero.Keyboard.KeyIsPressed(Zero.Keys.Escape)):
            self.Space.LoadLevel("MainMenu")
            
        if(self.GodMode is True):
            
            if(self.GodModeToggle is True):
                if(Tung):
                    Tung.PlayerController.MaxNumberOfJumps = 300
                    
                elif(Austin):
                    Austin.AustinPlayerController.MaxNumberOfJumps = 300
                    
                elif(Trey):
                    Trey.TreyPlayerController.MaxNumberOfJumps = 300
                    
                elif(Peyton):
                    Peyton.PeytonPlayerController.MaxNumberOfJumps = 300
                    
                elif(Sedrick):
                    Sedrick.SedrickPlayerController.MaxNumberOfJumps = 300
                    
                elif(Julio):
                    Julio.JulioPlayerController.MaxNumberOfJumps = 300
                self.GodModeToggle = False
        else:
            if(self.GodModeToggle2 is True):
                if(Tung):
                    Tung.PlayerController.MaxNumberOfJumps = 2
                    
                elif(Austin):
                    Austin.AustinPlayerController.MaxNumberOfJumps = 2
                    
                elif(Trey):
                    Trey.TreyPlayerController.MaxNumberOfJumps = 2
                    
                elif(Peyton):
                    Peyton.PeytonPlayerController.MaxNumberOfJumps = 2
                    
                elif(Sedrick):
                    Sedrick.SedrickPlayerController.MaxNumberOfJumps = 2
                    
                elif(Julio):
                    Julio.JulioPlayerController.MaxNumberOfJumps = 2
                self.GodModeToggle2 = False

Zero.RegisterComponent("HackFunction", HackFunction)