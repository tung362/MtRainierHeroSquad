import Zero
import Events
import Property
import VectorMath
import math
import random

Vector3 = VectorMath.Vec3
Quaternion = VectorMath.Quaternion

class GunManController:
    def DefineProperties(self):
        self.OnGround = Property.Bool(False)
        
        self.MoveSpeed = Property.Float(20.0)
        self.JumpSpeed = Property.Float(20.0)
        self.MaxNumberOfJumps = Property.Int(2)
        
        self.IsLeftR = Property.Bool(False)
        self.IsRightR = Property.Bool(True)
        
        self.CanFall = Property.Bool(False)
        self.CanWalk = Property.Bool(False)
        self.CanWalkBackward = Property.Bool(False)
        
        self.CanMakeMove = Property.Bool(True)
        
        self.CanMakeMove2 = Property.Bool(True)
        
        self.CanSwitchRightWalking = Property.Bool(False)
        self.CanSwitchRightFalling = Property.Bool(False)
        self.CanSwitchLeftWalking = Property.Bool(False)
        self.CanSwitchLeftFalling = Property.Bool(False)
        
        self.Side = Property.Bool(False)
        self.Side2 = Property.Bool(False)
        self.Side3 = Property.Bool(False)
        
        self.Start = Property.Bool(True)
        
        self.RandomAction = Property.Int(0)
        self.RandomTime = Property.Float(0)
        
        self.Timer = Property.Float(0)
        
        self.MLeft = Property.Bool(False)
        self.MRight = Property.Bool(False)
        
        self.AICanMove = Property.Bool(True)

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        
        self.OnGround = False
        self.JumpsRemaining = 0
        
        self.DistanceFromTarget = 0.0
        self.ChaseDirection = Vector3(0, 0, 0)

    def OnLogicUpdate(self, UpdateEvent):
        self.UpdatePlayerInput()
        self.UpdateGroundState()
        self.UpdateJumpState()
        self.ApplyMovement(UpdateEvent)
        
    def UpdateGroundState(self):
        self.OnGround = False
        for ContactHolder in self.Owner.Collider.Contacts:
            if(ContactHolder.IsGhost):
                continue
                
            ObjectHit = ContactHolder.OtherObject
            
            SurfaceNormal = -ContactHolder.FirstPoint.WorldNormalTowardsOther
            
            if(self.IsGround(SurfaceNormal)):
                self.OnGround = True
            return
            
    def CanJump(self):
        CanJump = (self.OnGround) or (self.JumpsRemaining > 1)
        return CanJump
        
    def UpdatePlayerInput(self):
        self.JumpIsPressed = Zero.Keyboard.KeyIsPressed(Zero.Keys.Space)
        
    def ApplyMovement(self, UpdateEvent):
        MoveDirection = Vector3(0, 0, 0)
        #RotationAngles = Quaternion(0, 0, 0)
        
        GunManBody = self.Owner.FindChildByName("GunManBody")
        StatusTracker = self.Space.FindObjectByName("PlayerTracker")
        
        CameraPosition = self.Space.FindObjectByName("Camera")
        PlayPosition = self.Owner.Transform.WorldTranslation
        
        Tung = self.Space.FindObjectByName("Tung")
        Austin = self.Space.FindObjectByName("Austin")
        Trey = self.Space.FindObjectByName("Trey")
        Peyton = self.Space.FindObjectByName("Peyton")
        Sedrick = self.Space.FindObjectByName("Sedrick")
        Julio = self.Space.FindObjectByName("Julio")
        
        DeltaTime = UpdateEvent.Dt
        Distance = Vector3(0, 0, 0)
        
        if(Tung):
            GetTungPos = Tung.Transform.Translation
            Distance = GetTungPos - self.Owner.Transform.WorldTranslation
            
        elif(Austin):
            GetAustinPos = Austin.Transform.Translation
            Distance = GetAustinPos - self.Owner.Transform.WorldTranslation
            
        elif(Trey):
            GetTreyPos = Trey.Transform.Translation
            Distance = GetTreyPos - self.Owner.Transform.WorldTranslation
            
        elif(Peyton):
            GetPeytonPos = Peyton.Transform.Translation
            Distance = GetPeytonPos - self.Owner.Transform.WorldTranslation
            
        elif(Sedrick):
            GetSedrickPos = Sedrick.Transform.Translation
            Distance = GetSedrickPos - self.Owner.Transform.WorldTranslation
            
        elif(Julio):
            GetJulioPos = Julio.Transform.Translation
            Distance = GetJulioPos - self.Owner.Transform.WorldTranslation
            
            
            
        if(self.Start is True):
            self.RandomAction = random.randint(1, 6)
            self.RandomTime = random.uniform(0.1, 0.5)
            self.Timer = 0
            self.Start = False
        
        if(self.RandomAction == 1):
            self.MLeft = True
            self.Timer += DeltaTime
        
            if(self.Timer > self.RandomTime):
                self.MRight = False
                self.MLeft = False
                self.Start = True
                self.Timer = 0
            
        elif(self.RandomAction == 2):
            self.MRight = True
            self.Timer += DeltaTime
            
            if(self.Timer > self.RandomTime):
                self.MLeft = False
                self.MRight = False
                self.Start = True
                self.Timer = 0
        else:
            self.MLeft = False
            self.MRight = False
            
            self.Timer += DeltaTime
            
            if(self.Timer > self.RandomTime):
                self.Start = True
                self.Timer = 0
        
        if(self.AICanMove is True and GunManBody.GunManStatus.CanShoot is False):
            
            if(self.MRight is True or self.MLeft is True):
                
                if(GunManBody.GunManStatus.CanShoot is True): #Unused if statement unless you want enemys to move while shooting
                    if(self.MRight is True and Distance.x > 0):
                        self.IsRightR = True
                        self.IsLeftR = False
                        if(self.OnGround is False):
                            if(self.CanSwitchRightFalling is True):
                                self.CanFall = True
                                self.CanSwitchRightFalling = False
                        else:
                            if(self.CanSwitchRightWalking is True):
                                self.CanWalk = True
                                self.CanSwitchRightWalking = False
                        MoveDirection += Vector3(1, 0, 0)
                        
                    elif(self.MRight is True and Distance.x < 0):
                        self.IsRightR = True
                        self.IsLeftR = False
                        if(self.OnGround is False):
                            if(self.CanSwitchRightFalling is True):
                                self.CanFall = True
                                self.CanSwitchRightFalling = False
                        else:
                            if(self.CanSwitchRightWalking is True):
                                self.CanWalkBackward = True
                                self.CanSwitchRightWalking = False
                        MoveDirection += Vector3(1, 0, 0)
                        
                    if(self.MLeft is True and Distance.x > 0):
                        self.IsRightR = False
                        self.IsLeftR = True
                        if(self.OnGround is False):
                            if(self.CanSwitchLeftFalling is True):
                                self.CanFall = True
                                self.CanSwitchLeftFalling = False
                        else:
                            if(self.CanSwitchLeftWalking is True):
                                self.CanWalkBackward = True
                                self.CanSwitchLeftWalking = False
                        MoveDirection += Vector3(-1, 0, 0)
                        
                    elif(self.MLeft is True and Distance.x < 0):
                        self.IsRightR = False
                        self.IsLeftR = True
                        if(self.OnGround is False):
                            if(self.CanSwitchLeftFalling is True):
                                self.CanFall = True
                                self.CanSwitchLeftFalling = False
                        else:
                            if(self.CanSwitchLeftWalking is True):
                                self.CanWalk = True
                                self.CanSwitchLeftWalking = False
                        MoveDirection += Vector3(-1, 0, 0)
                        
                        
                    '''if(self.CanJump() and self.JumpIsPressed):
                        self.SubtractJumpsRemaining()
                        if(self.CanMakeMove is True):
                            if(self.OnGround is False):
                                self.CanFall = True
                            else:
                                self.CanFall = True
                            self.CanMakeMove = False
                        self.Owner.RigidBody.ApplyLinearImpulse(Vector3(0, 1, 0) * self.JumpSpeed)'''
                        
                else:
                    if(self.MRight is True):
                        
                        self.IsRightR = True
                        self.IsLeftR = False
                        
                        if(self.CanSwitchRightWalking is True):
                            self.CanWalk = True
                            self.CanSwitchRightWalking = False
                        MoveDirection += Vector3(1, 0, 0)
                        
                    if(self.MLeft is True):
                        
                        self.IsRightR = False
                        self.IsLeftR = True
                        
                        if(self.CanSwitchLeftWalking is True):
                            self.CanWalk = True
                            self.CanSwitchLeftWalking = False
                        MoveDirection += Vector3(-1, 0, 0)
            else:
                self.CanSwitchRightWalking = True
                self.CanSwitchLeftWalking = True
                if(self.OnGround is True):
                    self.Owner.Sprite.SpriteSource = "GunManIdle"
                self.CanMakeMove = True
        else:
            if(self.OnGround is True):
                    self.Owner.Sprite.SpriteSource = "GunManIdle"
            
        if(self.OnGround is False):
            if(self.CanMakeMove2 is True):
                self.CanFall = True
                self.CanMakeMove2 = False
                self.CanSwitchRightWalking = True
                self.CanSwitchLeftWalking = True
        else:
            self.CanSwitchRightFalling = True
            self.CanSwitchLeftFalling = True
            self.CanMakeMove2 = True
            
        MoveDirection.normalize()
            
        if(GunManBody.GunManStatus.CanShoot is True):
            
            if(Distance.x < 0):
                #print("Left")
                self.Owner.Sprite.FlipX = True
                
                #RotationAngles.y = 1
                self.Side = True
                self.Side2 = False
                if(self.Side is True):
                    if(self.Side3 is False):
                        self.CanSwitchRightWalking = True
                        self.CanSwitchLeftWalking = True
                        self.Side3 = True
                        
            elif(Distance.x > 0):
                #print("Right")
                self.Owner.Sprite.FlipX = False
                
                #RotationAngles.y = 0
                self.Side2 = True
                self.Side = False
                if(self.Side2 is True):
                    if(self.Side3 is True):
                        self.CanSwitchRightWalking = True
                        self.CanSwitchLeftWalking = True
                        self.Side3 = False
        else:
            if(Distance.x < 0):
                #print("Left")
                if(self.IsLeftR is True):
                    self.Owner.Sprite.FlipX = True
                elif(self.IsRightR is True):
                    self.Owner.Sprite.FlipX = False
                    
                self.Side = True
                self.Side2 = False
                if(self.Side is True):
                    if(self.Side3 is False):
                        self.CanSwitchRightWalking = True
                        self.CanSwitchLeftWalking = True
                        self.Side3 = True
                        
            elif(Distance.x > 0):
                #print("Right")
                if(self.IsRightR is True):
                    self.Owner.Sprite.FlipX = False
                elif(self.IsLeftR is True):
                    self.Owner.Sprite.FlipX = True
                    
                self.Side2 = True
                self.Side = False
                if(self.Side2 is True):
                    if(self.Side3 is True):
                        self.CanSwitchRightWalking = True
                        self.CanSwitchLeftWalking = True
                        self.Side3 = False
            
        if(self.CanWalk is True):
            self.Owner.Sprite.SpriteSource = "GunManWalk"
            self.CanWalk = False
            
        if(self.CanWalkBackward is True):
            self.Owner.Sprite.SpriteSource = "GunManWalkBack"
            self.CanWalkBackward = False
            
        elif(self.CanJump is True):
            self.Owner.Sprite.SpriteSource = "GunManFall"
            self.CanJump = False
            
        elif(self.CanFall is True):
            self.Owner.Sprite.SpriteSource = "GunManFall"
            self.CanFall = False
        
        #self.Owner.Transform.Rotation = RotationAngles
        self.Owner.RigidBody.ApplyForce(MoveDirection * self.MoveSpeed)
        
    def GetDegreeDifference(self, SurfaceNormal):
        UpDirection = Vector3(0, 1, 0)
        CosTheta = SurfaceNormal.dot(UpDirection)
        CosTheta = min(max(CosTheta, -1.0), 1.0)
        Radians = math.acos(CosTheta)
        Degrees = math.degrees(Radians)
        return Degrees
        
    def IsGround(self, SurfaceNormal):
        
        Degrees = self.GetDegreeDifference(SurfaceNormal)
        return Degrees < 60.0
    
    def UpdateJumpState(self):
        if(self.OnGround):
            self.JumpsRemaining = self.MaxNumberOfJumps
    
    def SubtractJumpsRemaining(self):
        self.JumpsRemaining -= 1
        if(self.JumpsRemaining < 0):
            self.JumpsRemaining = 0
            
Zero.RegisterComponent("GunManController", GunManController)