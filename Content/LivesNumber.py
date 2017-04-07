import Zero
import Events
import Property
import VectorMath

class LivesNumber:
    
    
    def DefineProperties(self):
        pass

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)

    def OnLogicUpdate(self, UpdateEvent):
        
        Tracker = self.Space.FindObjectByName("PlayerTracker")
        Boss1Text = self.Space.FindObjectByName("Boss1Text")
        
        TungNum = 0
        AustinNum = 0
        TreyNum = 0
        PeytonNum = 0
        SedrickNum = 0
        JulioNum = 0
        
        if(Tracker.PlayerTracker.TungIsAlive is True):
            TungNum = 1
        else:
            TungNum = 0
            
        if(Tracker.PlayerTracker.AustinIsAlive is True):
            AustinNum = 1
        else:
            AustinNum = 0
            
        if(Tracker.PlayerTracker.TreyIsAlive is True):
            TreyNum = 1
        else:
            TreyNum = 0
            
        if(Tracker.PlayerTracker.PeytonIsAlive is True):
            PeytonNum = 1
        else:
            PeytonNum = 0
            
        if(Tracker.PlayerTracker.SedrickIsAlive is True):
            SedrickNum = 1
        else:
            SedrickNum = 0
            
        if(Tracker.PlayerTracker.JulioIsAlive is True):
            JulioNum = 1
        else:
            JulioNum = 0
        
        TotalNumber = TungNum + AustinNum + TreyNum + PeytonNum + SedrickNum + JulioNum
        
        if(TotalNumber < 0):
            TotalNumber = 0
        
        
        self.Owner.SpriteText.Text = str(TotalNumber)

Zero.RegisterComponent("LivesNumber", LivesNumber)