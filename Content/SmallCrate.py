import Zero
import Events
import Property
import VectorMath
import random

Vector3 = VectorMath.Vec3

class SmallCrate:
    
    def DefineProperties(self):
        self.MaxHealth = Property.Float(200)
        self.CurrentHealth = Property.Float(200)
        self.Start = Property.Bool(True)
        self.ParticleSize = Property.Float(1)
        self.RandomTexture = Property.Int(0)
        self.CrateSize = Property.Float(0)
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
            
            self.Owner.Name = "Crate"
            self.RandomTexture = random.randint(0, 2)
            if(self.RandomTexture is 0):
                self.Owner.Sprite.SpriteSource = "Crate"
                self.TextureNumber = 0
                
            elif(self.RandomTexture is 1):
                self.Owner.Sprite.SpriteSource = "CrateA"
                self.TextureNumber = 1
                
            else:
                self.Owner.Sprite.SpriteSource = "CrateB"
                self.TextureNumber = 2
            self.Start = False
            
        if(self.CrateSize == 0):
            if(self.TextureNumber is 0):
                if(self.CurrentHealth > 150 and self.CurrentHealth < 199 and self.Switch1 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateBreak1"
                    self.Switch1 = False
                    
                elif(self.CurrentHealth > 100 and self.CurrentHealth < 149 and self.Switch2 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateBreak2"
                    self.Switch2 = False
                    
                elif(self.CurrentHealth > 50 and self.CurrentHealth < 99 and self.Switch3 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateBreak3"
                    self.Switch3 = False
                    
                elif(self.CurrentHealth > 1 and self.CurrentHealth < 49 and self.Switch4 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateBreak4"
                    self.Switch4 = False
                
            elif(self.TextureNumber is 1):
                if(self.CurrentHealth > 150 and self.CurrentHealth < 199 and self.Switch1 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateABreak1"
                    self.Switch1 = False
                    
                elif(self.CurrentHealth > 100 and self.CurrentHealth < 149 and self.Switch2 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateABreak2"
                    self.Switch2 = False
                    
                elif(self.CurrentHealth > 50 and self.CurrentHealth < 99 and self.Switch3 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateABreak3"
                    self.Switch3 = False
                    
                elif(self.CurrentHealth > 1 and self.CurrentHealth < 49 and self.Switch4 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateABreak4"
                    self.Switch4 = False
                    
            elif(self.TextureNumber is 2):
                if(self.CurrentHealth > 150 and self.CurrentHealth < 199 and self.Switch1 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateBBreak1"
                    self.Switch1 = False
                    
                elif(self.CurrentHealth > 100 and self.CurrentHealth < 149 and self.Switch2 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateBBreak2"
                    self.Switch2 = False
                    
                elif(self.CurrentHealth > 50 and self.CurrentHealth < 99 and self.Switch3 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateBBreak3"
                    self.Switch3 = False
                    
                elif(self.CurrentHealth > 1 and self.CurrentHealth < 49 and self.Switch4 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateBBreak4"
                    self.Switch4 = False
                    
                    
                    
        elif(self.CrateSize == 1):
            if(self.TextureNumber is 0):
                if(self.CurrentHealth > 225 and self.CurrentHealth < 299 and self.Switch1 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateBreak1"
                    self.Switch1 = False
                    
                elif(self.CurrentHealth > 150 and self.CurrentHealth < 224 and self.Switch2 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateBreak2"
                    self.Switch2 = False
                    
                elif(self.CurrentHealth > 75 and self.CurrentHealth < 149 and self.Switch3 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateBreak3"
                    self.Switch3 = False
                    
                elif(self.CurrentHealth > 1 and self.CurrentHealth < 74 and self.Switch4 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateBreak4"
                    self.Switch4 = False
                
            elif(self.TextureNumber is 1):
                if(self.CurrentHealth > 225 and self.CurrentHealth < 299 and self.Switch1 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateABreak1"
                    self.Switch1 = False
                    
                elif(self.CurrentHealth > 150 and self.CurrentHealth < 224 and self.Switch2 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateABreak2"
                    self.Switch2 = False
                    
                elif(self.CurrentHealth > 75 and self.CurrentHealth < 149 and self.Switch3 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateABreak3"
                    self.Switch3 = False
                    
                elif(self.CurrentHealth > 1 and self.CurrentHealth < 74 and self.Switch4 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateABreak4"
                    self.Switch4 = False
                    
            elif(self.TextureNumber is 2):
                if(self.CurrentHealth > 225 and self.CurrentHealth < 299 and self.Switch1 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateBBreak1"
                    self.Switch1 = False
                    
                elif(self.CurrentHealth > 150 and self.CurrentHealth < 224 and self.Switch2 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateBBreak2"
                    self.Switch2 = False
                    
                elif(self.CurrentHealth > 75 and self.CurrentHealth < 149 and self.Switch3 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateBBreak3"
                    self.Switch3 = False
                    
                elif(self.CurrentHealth > 1 and self.CurrentHealth < 74 and self.Switch4 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateBBreak4"
                    self.Switch4 = False
                    
                    
                    
        elif(self.CrateSize == 2):
            if(self.TextureNumber is 0):
                if(self.CurrentHealth > 300 and self.CurrentHealth < 399 and self.Switch1 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateBreak1"
                    self.Switch1 = False
                    
                elif(self.CurrentHealth > 200 and self.CurrentHealth < 299 and self.Switch2 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateBreak2"
                    self.Switch2 = False
                    
                elif(self.CurrentHealth > 100 and self.CurrentHealth < 199 and self.Switch3 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateBreak3"
                    self.Switch3 = False
                    
                elif(self.CurrentHealth > 1 and self.CurrentHealth < 99 and self.Switch4 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateBreak4"
                    self.Switch4 = False
                
            elif(self.TextureNumber is 1):
                if(self.CurrentHealth > 300 and self.CurrentHealth < 399 and self.Switch1 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateABreak1"
                    self.Switch1 = False
                    
                elif(self.CurrentHealth > 200 and self.CurrentHealth < 299 and self.Switch2 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateABreak2"
                    self.Switch2 = False
                    
                elif(self.CurrentHealth > 100 and self.CurrentHealth < 199 and self.Switch3 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateABreak3"
                    self.Switch3 = False
                    
                elif(self.CurrentHealth > 1 and self.CurrentHealth < 99 and self.Switch4 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateABreak4"
                    self.Switch4 = False
                    
            elif(self.TextureNumber is 2):
                if(self.CurrentHealth > 300 and self.CurrentHealth < 399 and self.Switch1 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateBBreak1"
                    self.Switch1 = False
                    
                elif(self.CurrentHealth > 200 and self.CurrentHealth < 299 and self.Switch2 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateBBreak2"
                    self.Switch2 = False
                    
                elif(self.CurrentHealth > 100 and self.CurrentHealth < 199 and self.Switch3 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateBBreak3"
                    self.Switch3 = False
                    
                elif(self.CurrentHealth > 1 and self.CurrentHealth < 99 and self.Switch4 is True):
                    
                    self.Owner.Sprite.SpriteSource = "CrateBBreak4"
                    self.Switch4 = False
            
            
        if(GetCurrentHealth <= 0):
            Position = self.Owner.Transform.WorldTranslation
            PlayerBlasterProjectile1 = self.Space.CreateAtPosition("WoodParticle", Vector3(Position.x, Position.y + 0.5, 4))
            PlayerBlasterProjectile1.Transform.Scale = Vector3(self.ParticleSize, self.ParticleSize, 1)
            
            PlayerBlasterProjectile2 = self.Space.CreateAtPosition("WoodParticle", Vector3(Position.x, Position.y + 0.5, 4))
            PlayerBlasterProjectile2.Transform.Scale = Vector3(self.ParticleSize, self.ParticleSize, 1)
            
            PlayerBlasterProjectile3 = self.Space.CreateAtPosition("WoodParticle", Vector3(Position.x, Position.y + 0.5, 4))
            PlayerBlasterProjectile3.Transform.Scale = Vector3(self.ParticleSize, self.ParticleSize, 1)
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

Zero.RegisterComponent("SmallCrate", SmallCrate)