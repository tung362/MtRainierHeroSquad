import Zero
import Events
import Property
import VectorMath
import random

class BridgeTop:
    def DefineProperties(self):
        self.RandomTexture = Property.Int(0)
        self.Start = Property.Bool(True)

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)

    def OnLogicUpdate(self, UpdateEvent):
        
        if(self.Start == True):
            
            self.RandomTexture = random.randint(0, 2)
            if(self.RandomTexture is 0):
                self.Owner.Sprite.SpriteSource = "BridgeTop"
                
            elif(self.RandomTexture is 1):
                self.Owner.Sprite.SpriteSource = "BridgeTopA"
                
            else:
                self.Owner.Sprite.SpriteSource = "BridgeTopB"
            self.Start = False

Zero.RegisterComponent("BridgeTop", BridgeTop)