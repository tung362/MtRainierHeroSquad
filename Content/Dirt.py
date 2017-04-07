import Zero
import Events
import Property
import VectorMath
import random

Vector3 = VectorMath.Vec3

class Dirt:
    
    def DefineProperties(self):
        self.MaxHealth = Property.Float(200)
        self.CurrentHealth = Property.Float(200)
        self.RandomTexture = Property.Int(0)
        self.Start = Property.Bool(True)
        self.TextureNumber = Property.Int(0)
        
        self.Switch1 = Property.Bool(True)
        self.Switch2 = Property.Bool(True)
        self.Switch3 = Property.Bool(True)
        self.Switch4 = Property.Bool(True)
        
        self.SpawnParticle = Property.Bool(True)

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        Zero.Connect(self.Owner, Events.CollisionStarted, self.OnCollisionStarted)

    def OnLogicUpdate(self, UpdateEvent):
        
        GetMaxHealth = self.MaxHealth;
        GetCurrentHealth = self.CurrentHealth;
        
        if(self.Start == True):
            
            self.Owner.Name = "Dirt1"
            self.RandomTexture = random.randint(0, 11)
            
            if(self.RandomTexture is 0):
                self.Owner.Sprite.SpriteSource = "Dirt1"
                self.TextureNumber = 0
                
            elif(self.RandomTexture is 1):
                self.Owner.Sprite.SpriteSource = "Dirt1A"
                self.TextureNumber = 1
                
            elif(self.RandomTexture is 2):
                self.Owner.Sprite.SpriteSource = "Dirt2A"
                self.TextureNumber = 2
                
            elif(self.RandomTexture is 3):
                self.Owner.Sprite.SpriteSource = "Dirt1B"
                self.TextureNumber = 3
                
            elif(self.RandomTexture is 4):
                self.Owner.Sprite.SpriteSource = "Dirt2B"
                self.TextureNumber = 4
                
            elif(self.RandomTexture is 5):
                self.Owner.Sprite.SpriteSource = "Grass1A"
                self.TextureNumber = 5
                
            elif(self.RandomTexture is 6):
                self.Owner.Sprite.SpriteSource = "Grass2A"
                self.TextureNumber = 6
                
            elif(self.RandomTexture is 7):
                self.Owner.Sprite.SpriteSource = "Grass1B"
                self.TextureNumber = 7
                
            elif(self.RandomTexture is 8):
                self.Owner.Sprite.SpriteSource = "Grass2B"
                self.TextureNumber = 8
                
            elif(self.RandomTexture is 9):
                self.Owner.Sprite.SpriteSource = "Grass1"
                self.TextureNumber = 9
                
            elif(self.RandomTexture is 10):
                self.Owner.Sprite.SpriteSource = "Grass2"
                self.TextureNumber = 10
                
            else:
                self.Owner.Sprite.SpriteSource = "Dirt2"
                self.TextureNumber = 11
            self.Start = False
            
            
        if(self.TextureNumber is 0):
            if(self.CurrentHealth > 150 and self.CurrentHealth < 199 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Dirt1Break1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 100 and self.CurrentHealth < 149 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Dirt1Break2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 50 and self.CurrentHealth < 99 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Dirt1Break3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 49 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Dirt1Break4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 1):
            if(self.CurrentHealth > 150 and self.CurrentHealth < 199 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Dirt1ABreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 100 and self.CurrentHealth < 149 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Dirt1ABreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 50 and self.CurrentHealth < 99 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Dirt1ABreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 49 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Dirt1ABreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 2):
            if(self.CurrentHealth > 150 and self.CurrentHealth < 199 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Dirt2ABreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 100 and self.CurrentHealth < 149 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Dirt2ABreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 50 and self.CurrentHealth < 99 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Dirt2ABreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 49 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Dirt2ABreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 3):
            if(self.CurrentHealth > 150 and self.CurrentHealth < 199 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Dirt1BBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 100 and self.CurrentHealth < 149 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Dirt1BBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 50 and self.CurrentHealth < 99 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Dirt1BBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 49 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Dirt1BBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 4):
            if(self.CurrentHealth > 150 and self.CurrentHealth < 199 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Dirt2BBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 100 and self.CurrentHealth < 149 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Dirt2BBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 50 and self.CurrentHealth < 99 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Dirt2BBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 49 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Dirt2BBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 5):
            if(self.CurrentHealth > 150 and self.CurrentHealth < 199 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Grass1ABreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 100 and self.CurrentHealth < 149 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Grass1ABreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 50 and self.CurrentHealth < 99 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Grass1ABreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 49 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Grass1ABreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 6):
            if(self.CurrentHealth > 150 and self.CurrentHealth < 199 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Grass2ABreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 100 and self.CurrentHealth < 149 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Grass2ABreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 50 and self.CurrentHealth < 99 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Grass2ABreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 49 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Grass2ABreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 7):
            if(self.CurrentHealth > 150 and self.CurrentHealth < 199 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Grass1BBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 100 and self.CurrentHealth < 149 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Grass1BBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 50 and self.CurrentHealth < 99 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Grass1BBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 49 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Grass1BBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 8):
            if(self.CurrentHealth > 150 and self.CurrentHealth < 199 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Grass2BBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 100 and self.CurrentHealth < 149 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Grass2BBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 50 and self.CurrentHealth < 99 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Grass2BBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 49 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Grass2BBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 9):
            if(self.CurrentHealth > 150 and self.CurrentHealth < 199 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Grass1Break1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 100 and self.CurrentHealth < 149 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Grass1Break2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 50 and self.CurrentHealth < 99 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Grass1Break3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 49 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Grass1Break4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 10):
            if(self.CurrentHealth > 150 and self.CurrentHealth < 199 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Grass2Break1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 100 and self.CurrentHealth < 149 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Grass2Break2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 50 and self.CurrentHealth < 99 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Grass2Break3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 49 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Grass2Break4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 11):
            if(self.CurrentHealth > 150 and self.CurrentHealth < 199 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Dirt2Break1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 100 and self.CurrentHealth < 149 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Dirt2Break2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 50 and self.CurrentHealth < 99 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Dirt2Break3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 49 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Dirt2Break4"
                self.Switch4 = False
            
            
        if(GetCurrentHealth <= 0):
            Position = self.Owner.Transform.WorldTranslation
            
            if(self.SpawnParticle is True):
                PlayerBlasterProjectile = self.Space.CreateAtPosition("DirtParticle", Vector3(Position.x, Position.y + 0.5, 4))
            self.SpawnParticle = False
            
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

Zero.RegisterComponent("Dirt", Dirt)