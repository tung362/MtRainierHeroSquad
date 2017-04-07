import Zero
import Events
import Property
import VectorMath

class MusicBox:
    
    CanNormal = Property.Bool(True)
    CanSedrickPlayOnce = Property.Bool(True)
    CanPlaySedrick1 = Property.Bool(True)
    CanPlaySedrick2 = Property.Bool(True)
    
    def DefineProperties(self):
        pass

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)

    def OnLogicUpdate(self, UpdateEvent):
        Sedrick = self.Space.FindObjectByName("Sedrick")
        Sedrick1 = self.Space.FindObjectByName("Sedrick1")
        Sedrick2 = self.Space.FindObjectByName("Sedrick2")
        LevelSong = self.Space.FindObjectByName("LevelSong")
        
        if(Sedrick):
            if(Zero.Mouse.IsButtonDown(Zero.MouseButtons.Left) and self.CanPlaySedrick1 is True):
                #print("Sedrick1")
                #Sedrick2.SoundEmitter.Stop()
                Sedrick2.SoundEmitter.Volume = 0
                LevelSong.SoundEmitter.Stop()
                Sedrick1.SoundEmitter.Play()
                self.CanPlaySedrick2 = True
                self.CanNormal = True
                self.CanPlaySedrick1 = False
            else:
                if(self.CanPlaySedrick2 is True and not Zero.Mouse.IsButtonDown(Zero.MouseButtons.Left)):
                    #print("Sedrick2")
                    Sedrick1.SoundEmitter.Stop()
                    LevelSong.SoundEmitter.Stop()
                    Sedrick2.SoundEmitter.Volume = 0.2
                    if(self.CanSedrickPlayOnce is True):
                        Sedrick2.SoundEmitter.Play()
                        self.CanSedrickPlayOnce = False
                    self.CanPlaySedrick1 = True
                    self.CanNormal = True
                    self.CanPlaySedrick2 = False
        else:
            
            if(self.CanNormal is True):
                #print("Normal")
                Sedrick1.SoundEmitter.Stop()
                Sedrick2.SoundEmitter.Stop()
                LevelSong.SoundEmitter.Play()
                self.CanPlaySedrick1 = True
                self.CanPlaySedrick2 = True
                self.CanNormal = False

Zero.RegisterComponent("MusicBox", MusicBox)