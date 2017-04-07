import Zero
import Events
import Property
import VectorMath
import random

Vector3 = VectorMath.Vec3

class Barrel:
    
    def DefineProperties(self):
        self.MaxHealth = Property.Float(450)
        self.CurrentHealth = Property.Float(450)
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
            
            self.Owner.Name = "Barrel"
            self.RandomTexture = random.randint(0, 2)
            if(self.RandomTexture is 0):
                self.Owner.Sprite.SpriteSource = "Barrel"
                self.TextureNumber = 0
                
            elif(self.RandomTexture is 1):
                self.Owner.Sprite.SpriteSource = "BarrelA"
                self.TextureNumber = 1
                
            else:
                self.Owner.Sprite.SpriteSource = "BarrelB"
                self.TextureNumber = 2
                
            self.MaxHealth = 450
            self.CurrentHealth = 450
            self.Start = False
            
        if(self.TextureNumber is 0):
            if(self.CurrentHealth > 337 and self.CurrentHealth < 449 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "BarrelBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 225 and self.CurrentHealth < 336 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "BarrelBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 112 and self.CurrentHealth < 224 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "BarrelBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 111 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "BarrelBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 1):
            if(self.CurrentHealth > 337 and self.CurrentHealth < 449 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "BarrelABreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 225 and self.CurrentHealth < 336 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "BarrelABreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 112 and self.CurrentHealth < 224 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "BarrelABreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 111 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "BarrelABreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 2):
            if(self.CurrentHealth > 337 and self.CurrentHealth < 449 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "BarrelBBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 225 and self.CurrentHealth < 336 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "BarrelBBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 112 and self.CurrentHealth < 224 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "BarrelBBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 111 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "BarrelBBreak4"
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

Zero.RegisterComponent("Barrel", Barrel)