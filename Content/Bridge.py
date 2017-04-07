import Zero
import Events
import Property
import VectorMath
import random

Vector3 = VectorMath.Vec3

class Bridge:
    
    def DefineProperties(self):
        self.MaxHealth = Property.Float(220)
        self.CurrentHealth = Property.Float(220)
        self.RandomTexture = Property.Int(0)
        self.Start = Property.Bool(True)
        self.TextureNumber = Property.Int(0)
        
        self.Switch1 = Property.Bool(True)
        self.Switch2 = Property.Bool(True)
        self.Switch3 = Property.Bool(True)
        self.Switch4 = Property.Bool(True)

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        Zero.Connect(self.Owner, Events.CollisionStarted, self.OnCollisionStarted)

    def OnLogicUpdate(self, UpdateEvent):
        
        GetMaxHealth = self.MaxHealth;
        GetCurrentHealth = self.CurrentHealth;
        
        if(self.Start == True):
            
            self.Owner.Name = "BridgeBottom"
            self.RandomTexture = random.randint(0, 2)
            if(self.RandomTexture is 0):
                self.Owner.Sprite.SpriteSource = "BridgeBottom"
                self.TextureNumber = 0
                
            elif(self.RandomTexture is 1):
                self.Owner.Sprite.SpriteSource = "BridgeBottomA"
                self.TextureNumber = 1
                
            else:
                self.Owner.Sprite.SpriteSource = "BridgeBottomB"
                self.TextureNumber = 2
            self.Start = False
            
        if(self.TextureNumber is 0):
            if(self.CurrentHealth > 165 and self.CurrentHealth < 219 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "BridgeBottomBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 110 and self.CurrentHealth < 164 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "BridgeBottomBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 55 and self.CurrentHealth < 109 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "BridgeBottomBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 54 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "BridgeBottomBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 1):
            if(self.CurrentHealth > 165 and self.CurrentHealth < 219 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "BridgeBottomABreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 110 and self.CurrentHealth < 164 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "BridgeBottomABreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 55 and self.CurrentHealth < 109 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "BridgeBottomABreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 54 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "BridgeBottomABreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 2):
            if(self.CurrentHealth > 165 and self.CurrentHealth < 219 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "BridgeBottomBBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 110 and self.CurrentHealth < 164 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "BridgeBottomBBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 55 and self.CurrentHealth < 109 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "BridgeBottomBBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 54 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "BridgeBottomBBreak4"
                self.Switch4 = False
            
            
        if(GetCurrentHealth <= 0):
            Position = self.Owner.Transform.WorldTranslation
            PlayerBlasterProjectile = self.Space.CreateAtPosition("WoodParticle", Vector3(Position.x, Position.y + 0.5, 4))
            PlayerBlasterProjectile = self.Space.CreateAtPosition("WoodParticle", Vector3(Position.x, Position.y + 0.5, 4))
            PlayerBlasterProjectile = self.Space.CreateAtPosition("WoodParticle", Vector3(Position.x, Position.y + 0.5, 4))
            self.Owner.Destroy()
            
            
    def OnCollisionStarted(self, CollisionEvent):
        
        other = CollisionEvent.OtherObject
                
                
                
        if(other.Name == "PlayerSmallBullet"):
            
            self.CurrentHealth -= 10
            
        elif(other.Name == "PlayerGiantBullet"):
            
            self.CurrentHealth -= 15
            
        elif(other.Name == "EnemySmallBullet"):
            
            self.CurrentHealth -= 10
            
        elif(other.Name == "EnemyGiantBullet"):
            
            self.CurrentHealth -= 15

Zero.RegisterComponent("Bridge", Bridge)