import Zero
import Events
import Property
import VectorMath

Vector3 = VectorMath.Vec3

class WallBackGround:
    def DefineProperties(self):
        self.MaxHealth = Property.Float(300)
        self.CurrentHealth = Property.Float(300)
        self.Start = Property.Bool(True)
        self.TextureNumber = Property.Int(0)
        
        self.Switch1 = Property.Bool(True)
        self.Switch2 = Property.Bool(True)
        self.Switch3 = Property.Bool(True)
        self.Switch4 = Property.Bool(True)
        
        self.SpawnParticle = Property.Bool(True)

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        
    def OnLogicUpdate(self, UpdateEvent):
        
        GetMaxHealth = self.MaxHealth;
        GetCurrentHealth = self.CurrentHealth;
        
        if(self.Start == True):
            
            self.Owner.Name = "WallBackGround"
            self.MaxHealth = 300
            self.CurrentHealth = 300
            self.Start = False
            
        if(self.TextureNumber is 0):
            if(self.CurrentHealth > 225 and self.CurrentHealth < 299 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftTopBackgroundBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 150 and self.CurrentHealth < 224 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftTopBackgroundBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 75 and self.CurrentHealth < 149 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftTopBackgroundBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 74 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftTopBackgroundBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 1):
            if(self.CurrentHealth > 225 and self.CurrentHealth < 299 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightTopBackgroundBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 150 and self.CurrentHealth < 224 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightTopBackgroundBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 75 and self.CurrentHealth < 149 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightTopBackgroundBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 74 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightTopBackgroundBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 2):
            if(self.CurrentHealth > 225 and self.CurrentHealth < 299 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleTopBackgroundBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 150 and self.CurrentHealth < 224 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleTopBackgroundBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 75 and self.CurrentHealth < 149 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleTopBackgroundBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 74 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleTopBackgroundBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 3):
            if(self.CurrentHealth > 225 and self.CurrentHealth < 299 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftBottomBackgroundBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 150 and self.CurrentHealth < 224 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftBottomBackgroundBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 75 and self.CurrentHealth < 149 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftBottomBackgroundBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 74 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftBottomBackgroundBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 4):
            if(self.CurrentHealth > 225 and self.CurrentHealth < 299 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftMiddleBackgroundBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 150 and self.CurrentHealth < 224 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftMiddleBackgroundBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 75 and self.CurrentHealth < 149 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftMiddleBackgroundBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 74 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftMiddleBackgroundBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 5):
            if(self.CurrentHealth > 225 and self.CurrentHealth < 299 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightBottomBackgroundBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 150 and self.CurrentHealth < 224 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightBottomBackgroundBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 75 and self.CurrentHealth < 149 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightBottomBackgroundBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 74 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightBottomBackgroundBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 6):
            if(self.CurrentHealth > 225 and self.CurrentHealth < 299 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightMiddleBackgroundBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 150 and self.CurrentHealth < 224 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightMiddleBackgroundBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 75 and self.CurrentHealth < 149 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightMiddleBackgroundBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 74 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightMiddleBackgroundBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 7):
            if(self.CurrentHealth > 225 and self.CurrentHealth < 299 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleBottomBackgroundBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 150 and self.CurrentHealth < 224 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleBottomBackgroundBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 75 and self.CurrentHealth < 149 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleBottomBackgroundBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 74 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleBottomBackgroundBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 8):
            if(self.CurrentHealth > 225 and self.CurrentHealth < 299 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleMiddleBackgroundBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 150 and self.CurrentHealth < 224 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleMiddleBackgroundBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 75 and self.CurrentHealth < 149 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleMiddleBackgroundBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 74 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleMiddleBackgroundBreak4"
                self.Switch4 = False
                
            
            
        if(GetCurrentHealth <= 0):
            Position = self.Owner.Transform.WorldTranslation
            
            if(self.SpawnParticle is True):
                PlayerBlasterProjectile = self.Space.CreateAtPosition("RubbleParticle", Vector3(Position.x, Position.y + 0.5, 4))
            self.SpawnParticle = False
            
            self.Owner.Destroy()

Zero.RegisterComponent("WallBackGround", WallBackGround)