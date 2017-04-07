import Zero
import Events
import Property
import VectorMath
import random

Vector3 = VectorMath.Vec3
Vector4 = VectorMath.Vec4

class Wall1:
    
    def DefineProperties(self):
        self.MaxHealth = Property.Float(500)
        self.CurrentHealth = Property.Float(500)
        self.RandomColor = Property.Int(0)
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
            
            self.Owner.Name = "Wall1"
            self.RandomColor = random.randint(0, 2)
            if(self.RandomColor is 0):
                self.Owner.Sprite.Color = Vector4(38, 55, 89, 1.0) #HSL Color Type
                #F2E6D2
            elif(self.RandomColor is 1):
                self.Owner.Sprite.Color = Vector4(38, 65, 85, 1.0)
                
            else:
                self.Owner.Sprite.Color = Vector4(37, 60, 87, 1.0)
                
            self.MaxHealth = 500
            self.CurrentHealth = 500
            self.Start = False
            
            
        if(self.TextureNumber is 0):
            if(self.CurrentHealth > 375 and self.CurrentHealth < 499 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftTopBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 250 and self.CurrentHealth < 374 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftTopBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 125 and self.CurrentHealth < 249 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftTopBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 124 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftTopBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 1):
            if(self.CurrentHealth > 375 and self.CurrentHealth < 499 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightTopBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 250 and self.CurrentHealth < 374 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightTopBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 125 and self.CurrentHealth < 249 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightTopBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 124 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightTopBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 2):
            if(self.CurrentHealth > 375 and self.CurrentHealth < 499 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleTopBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 250 and self.CurrentHealth < 374 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleTopBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 125 and self.CurrentHealth < 249 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleTopBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 124 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleTopBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 3):
            if(self.CurrentHealth > 375 and self.CurrentHealth < 499 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftBottomBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 250 and self.CurrentHealth < 374 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftBottomBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 125 and self.CurrentHealth < 249 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftBottomBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 124 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftBottomBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 4):
            if(self.CurrentHealth > 375 and self.CurrentHealth < 499 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftMiddleBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 250 and self.CurrentHealth < 374 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftMiddleBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 125 and self.CurrentHealth < 249 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftMiddleBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 124 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftMiddleBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 5):
            if(self.CurrentHealth > 375 and self.CurrentHealth < 499 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightBottomBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 250 and self.CurrentHealth < 374 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightBottomBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 125 and self.CurrentHealth < 249 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightBottomBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 124 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightBottomBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 6):
            if(self.CurrentHealth > 375 and self.CurrentHealth < 499 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightMiddleBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 250 and self.CurrentHealth < 374 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightMiddleBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 125 and self.CurrentHealth < 249 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightMiddleBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 124 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightMiddleBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 7):
            if(self.CurrentHealth > 375 and self.CurrentHealth < 499 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleBottomBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 250 and self.CurrentHealth < 374 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleBottomBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 125 and self.CurrentHealth < 249 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleBottomBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 124 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleBottomBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 8):
            if(self.CurrentHealth > 375 and self.CurrentHealth < 499 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleTopTriBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 250 and self.CurrentHealth < 374 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleTopTriBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 125 and self.CurrentHealth < 249 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleTopTriBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 124 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleTopTriBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 9):
            if(self.CurrentHealth > 375 and self.CurrentHealth < 499 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftMiddleTriBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 250 and self.CurrentHealth < 374 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftMiddleTriBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 125 and self.CurrentHealth < 249 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftMiddleTriBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 124 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftMiddleTriBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 10):
            if(self.CurrentHealth > 375 and self.CurrentHealth < 499 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleTopEndLBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 250 and self.CurrentHealth < 374 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleTopEndLBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 125 and self.CurrentHealth < 249 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleTopEndLBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 124 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleTopEndLBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 11):
            if(self.CurrentHealth > 375 and self.CurrentHealth < 499 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleTopEndRBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 250 and self.CurrentHealth < 374 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleTopEndRBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 125 and self.CurrentHealth < 249 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleTopEndRBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 124 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleTopEndRBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 12):
            if(self.CurrentHealth > 375 and self.CurrentHealth < 499 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftMiddleEndLBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 250 and self.CurrentHealth < 374 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftMiddleEndLBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 125 and self.CurrentHealth < 249 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftMiddleEndLBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 124 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftMiddleEndLBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 13):
            if(self.CurrentHealth > 375 and self.CurrentHealth < 499 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftMiddleEndRBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 250 and self.CurrentHealth < 374 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftMiddleEndRBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 125 and self.CurrentHealth < 249 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftMiddleEndRBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 124 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1LeftMiddleEndRBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 14):
            if(self.CurrentHealth > 375 and self.CurrentHealth < 499 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightMiddleTriBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 250 and self.CurrentHealth < 374 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightMiddleTriBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 125 and self.CurrentHealth < 249 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightMiddleTriBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 124 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightMiddleTriBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 15):
            if(self.CurrentHealth > 375 and self.CurrentHealth < 499 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleBottomTriBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 250 and self.CurrentHealth < 374 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleBottomTriBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 125 and self.CurrentHealth < 249 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleBottomTriBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 124 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleBottomTriBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 16):
            if(self.CurrentHealth > 375 and self.CurrentHealth < 499 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightMiddleEndLBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 250 and self.CurrentHealth < 374 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightMiddleEndLBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 125 and self.CurrentHealth < 249 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightMiddleEndLBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 124 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightMiddleEndLBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 17):
            if(self.CurrentHealth > 375 and self.CurrentHealth < 499 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightMiddleEndRBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 250 and self.CurrentHealth < 374 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightMiddleEndRBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 125 and self.CurrentHealth < 249 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightMiddleEndRBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 124 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1RightMiddleEndRBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 18):
            if(self.CurrentHealth > 375 and self.CurrentHealth < 499 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleBottomEndLBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 250 and self.CurrentHealth < 374 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleBottomEndLBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 125 and self.CurrentHealth < 249 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleBottomEndLBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 124 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleBottomEndLBreak4"
                self.Switch4 = False
                
        elif(self.TextureNumber is 19):
            if(self.CurrentHealth > 375 and self.CurrentHealth < 499 and self.Switch1 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleBottomEndRBreak1"
                self.Switch1 = False
                
            elif(self.CurrentHealth > 250 and self.CurrentHealth < 374 and self.Switch2 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleBottomEndRBreak2"
                self.Switch2 = False
                
            elif(self.CurrentHealth > 125 and self.CurrentHealth < 249 and self.Switch3 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleBottomEndRBreak3"
                self.Switch3 = False
                
            elif(self.CurrentHealth > 1 and self.CurrentHealth < 124 and self.Switch4 is True):
                
                self.Owner.Sprite.SpriteSource = "Wall1MiddleBottomEndRBreak4"
                self.Switch4 = False
            
            
        if(GetCurrentHealth <= 0):
            Position = self.Owner.Transform.WorldTranslation
            
            if(self.SpawnParticle is True):
                PlayerBlasterProjectile = self.Space.CreateAtPosition("RubbleParticle", Vector3(Position.x, Position.y + 0.5, 4))
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

Zero.RegisterComponent("Wall1", Wall1)