import Zero
import Events
import Property
import VectorMath
import math
import random

Vector3 = VectorMath.Vec3
Quaternion = VectorMath.Quaternion

class AustinPlayerController:
    def DefineProperties(self):
        self.OnGround = Property.Bool(False)
        
        self.MoveSpeed = Property.Float(20.0)
        self.JumpSpeed = Property.Float(20.0)
        self.MaxNumberOfJumps = Property.Int(2)
        self.Start = Property.Bool(True)
        
        self.IsLeft = Property.Bool(False)
        self.IsRight = Property.Bool(True)
        
        self.CanFall = Property.Bool(False)
        self.CanWalk = Property.Bool(False)
        self.CanWalkBackward = Property.Bool(False)
        self.CanKneel = Property.Bool(False)
        
        self.CanMakeMove = Property.Bool(True)
        
        self.CanMakeMove2 = Property.Bool(True)
        
        self.TheKneel = Property.Bool(False)
        
        self.CanSwitchRightWalking = Property.Bool(False)
        self.CanSwitchRightFalling = Property.Bool(False)
        self.CanSwitchLeftWalking = Property.Bool(False)
        self.CanSwitchLeftFalling = Property.Bool(False)
        
        self.CanSwitchRightKneel = Property.Bool(False)
        self.CanSwitchLeftKneel = Property.Bool(False)
        self.KneelUsed = Property.Bool(False)
        
        self.Side = Property.Bool(False)
        self.Side2 = Property.Bool(False)
        self.Side3 = Property.Bool(False)
        
        self.Start = Property.Bool(True)
        
        self.ChaseSpeed = Property.Float(3.0)
        
        self.VerticleDistance = Property.Float(0)
        self.HorizontalDistance = Property.Float(0)
        
        self.CanMoveX = Property.Bool(False)
        self.CanMoveY = Property.Bool(False)
        
        self.IsOnAirShip = Property.Bool(False)

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
        
        if(self.Start is True):
            self.Start = False
        
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
        self.MoveRight = Zero.Keyboard.KeyIsDown(Zero.Keys.D)
        self.MoveLeft = Zero.Keyboard.KeyIsDown(Zero.Keys.A)
        self.Kneel = Zero.Keyboard.KeyIsDown(Zero.Keys.S)
        self.JumpIsPressed = Zero.Keyboard.KeyIsPressed(Zero.Keys.Space)
        
    def ApplyMovement(self, UpdateEvent):
        MoveDirection = Vector3(0, 0, 0)
        #RotationAngles = Quaternion(0, 0, 0)
        
        MouseScreenPosition = Zero.Mouse.ScreenPosition
        WorldMousePosition = self.LevelSettings.CameraViewport.ScreenToWorldZPlane(MouseScreenPosition, 0)
        Distance = WorldMousePosition - self.Owner.Transform.Translation
        
        TungBody = self.Space.FindObjectByName("AustinBody")
        
        StatusTracker = self.Space.FindObjectByName("PlayerTracker")
        
        if(self.Start is True):
            self.Start = False
        
        CameraPosition = self.Space.FindObjectByName("Camera")
        PlayPosition = self.Owner.Transform.Translation
        
        if(Zero.Keyboard.KeyIsDown(Zero.Keys.Equal) and CameraPosition.Camera.Size < 44):
            CameraPosition.Camera.Size += 1
            #print(CameraPosition.Camera.Size)
        
        if(Zero.Keyboard.KeyIsDown(Zero.Keys.Minus) and CameraPosition.Camera.Size > 7):
            CameraPosition.Camera.Size += -1
            #print(CameraPosition.Camera.Size)
        
        if(Zero.Keyboard.KeyIsDown(Zero.Keys.Back)):
            CameraPosition.Camera.Size = 20
        
        if((self.MoveRight or self.MoveLeft or self.JumpIsPressed or self.Kneel) and self.IsOnAirShip is False):
            
            if(self.Kneel):
                if(self.KneelUsed is False):
                    self.CanSwitchRightKneel = False
                    self.CanSwitchLeftKneel = False
                    self.KneelUsed = True
                    
                if(self.CanMakeMove is True):
                    if(self.OnGround is False):
                        self.CanFall = True
                    else:
                        self.CanKneel = True
                    self.CanMakeMove = False
                if((self.TheKneel is True and self.MoveRight) or (self.TheKneel is True and self.MoveLeft)):
                    if(Distance.x < 0 and self.MoveRight):
                        self.CanWalkBackward = True
                        self.TheKneel = False
                    elif(Distance.x < 0 and self.MoveLeft):
                        self.CanWalk = True
                        self.TheKneel = False
                        
                    if(Distance.x > 0 and self.MoveRight):
                        self.CanWalk = True
                        self.TheKneel = False
                    elif(Distance.x > 0 and self.MoveLeft):
                        self.CanWalkBackward = True
                        self.TheKneel = False
            else:
                self.KneelUsed = False
                    
            if(self.MoveRight and Distance.x > 0):
                #self.IsRight = True
                #self.IsLeft = False
                if(self.OnGround is False):
                    if(self.CanSwitchRightFalling is True):
                        self.CanFall = True
                        self.CanSwitchRightFalling = False
                else:
                    if(self.CanSwitchRightWalking is True):
                        self.CanWalk = True
                        self.CanSwitchRightWalking = False
                if(self.Kneel):
                    if(self.CanSwitchRightKneel is False):
                        self.TheKneel = True
                        self.CanSwitchRightKneel = True
                MoveDirection += Vector3(1, 0, 0)
                
            elif(self.MoveRight and Distance.x < 0):
                #self.IsRight = True
                #self.IsLeft = False
                if(self.OnGround is False):
                    if(self.CanSwitchRightFalling is True):
                        self.CanFall = True
                        self.CanSwitchRightFalling = False
                else:
                    if(self.CanSwitchRightWalking is True):
                        self.CanWalkBackward = True
                        self.CanSwitchRightWalking = False
                if(self.Kneel):
                    if(self.CanSwitchRightKneel is False):
                        self.TheKneel = True
                        self.CanSwitchRightKneel = True
                MoveDirection += Vector3(1, 0, 0)
            else:
                self.CanSwitchRightKneel = False
                if(self.Kneel and not self.MoveLeft):
                    self.TheKneel = True
                    self.CanKneel = True
                
            if(self.MoveLeft and Distance.x > 0):
                #self.IsRight = False
                #self.IsLeft = True
                if(self.OnGround is False):
                    if(self.CanSwitchLeftFalling is True):
                        self.CanFall = True
                        self.CanSwitchLeftFalling = False
                else:
                    if(self.CanSwitchLeftWalking is True):
                        self.CanWalkBackward = True
                        self.CanSwitchLeftWalking = False
                if(self.Kneel):
                    if(self.CanSwitchLeftKneel is False):
                        self.TheKneel = True
                        self.CanSwitchLeftKneel = True
                MoveDirection += Vector3(-1, 0, 0)
                
            elif(self.MoveLeft and Distance.x < 0):
                #self.IsRight = False
                #self.IsLeft = True
                if(self.OnGround is False):
                    if(self.CanSwitchLeftFalling is True):
                        self.CanFall = True
                        self.CanSwitchLeftFalling = False
                else:
                    if(self.CanSwitchLeftWalking is True):
                        self.CanWalk = True
                        self.CanSwitchLeftWalking = False
                if(self.Kneel):
                    if(self.CanSwitchLeftKneel is False):
                        self.TheKneel = True
                        self.CanSwitchLeftKneel = True
                MoveDirection += Vector3(-1, 0, 0)
            else:
                self.CanSwitchLeftKneel = False
                if(self.Kneel and not self.MoveRight):
                    self.TheKneel = True
                    self.CanKneel = True
                    
                
            if(self.CanJump() and self.JumpIsPressed):
                self.SubtractJumpsRemaining()
                if(self.CanMakeMove is True):
                    if(self.OnGround is False):
                        self.CanFall = True
                    else:
                        self.CanFall = True
                    self.CanMakeMove = False
                self.Owner.RigidBody.ApplyLinearImpulse(Vector3(0, 1, 0) * self.JumpSpeed)
        else:
            self.CanSwitchRightWalking = True
            self.CanSwitchLeftWalking = True
            if(self.OnGround is True):
                self.Owner.Sprite.SpriteSource = "AustinIdle"
            self.CanMakeMove = True
            
        if(self.OnGround is False and self.IsOnAirShip is False):
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
        
        #if(self.IsLeft is True):
            #RotationAngles.y = -1
        #if(self.IsLeft is True):
            #RotationAngles.y = 1
            
        if(CameraPosition.Transform.Translation.x < 7):
            CameraPosition.Transform.Translation = Vector3(7, 0, 40)
            self.CanMoveX = False
        elif(CameraPosition.Transform.Translation.y < -10):
            CameraPosition.Transform.Translation = Vector3(CameraPosition.Transform.Translation.x, -10, 40)
            self.CanMoveY = False
        else:
            self.CanMoveX = True
            self.CanMoveY = True
            
        if(Distance.x < 0):
            #print("Left")
            self.Owner.Sprite.FlipX = True
            self.CalculateChaseDirectionAndDistance()
            self.ChaseTarget(UpdateEvent)
            if(StatusTracker.PlayerTracker.Explode is False):
                if(Distance.y < 7 and Distance.y > 0 and self.CanMoveY is True):
                    self.VerticleDistance = Distance.y
                if(Distance.x < 0 and Distance.x > -16 and self.CanMoveX is True):
                    self.HorizontalDistance = Distance.x / 3
            else:
                if(Distance.y < 7 and Distance.y > 0 and self.CanMoveY is True):
                    self.VerticleDistance = Distance.y + random.randint(-6, 6)
                if(Distance.x < 0 and Distance.x > -16 and self.CanMoveX is True):
                    self.HorizontalDistance = Distance.x / 3 + random.randint(-6, 6)
                
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
            self.CalculateChaseDirectionAndDistance2()
            self.ChaseTarget(UpdateEvent)
            if(StatusTracker.PlayerTracker.Explode is False):
                if(Distance.y < 7 and Distance.y > 0 and self.CanMoveY is True):
                    self.VerticleDistance = Distance.y
                if(Distance.x > 0 and Distance.x < 16 and self.CanMoveX is True):
                    self.HorizontalDistance = Distance.x / 3
            else:
                if(Distance.y < 7 and Distance.y > 0 and self.CanMoveY is True):
                    self.VerticleDistance = Distance.y + random.randint(-6, 6)
                if(Distance.x > 0 and Distance.x < 16 and self.CanMoveX is True):
                    self.HorizontalDistance = Distance.x / 3 + random.randint(-6, 6)
                
            #RotationAngles.y = 0
            self.Side2 = True
            self.Side = False
            if(self.Side2 is True):
                if(self.Side3 is True):
                    self.CanSwitchRightWalking = True
                    self.CanSwitchLeftWalking = True
                    self.Side3 = False
        #print(Distance)
        #print(CameraPosition.Transform.Translation)
            
        if(self.CanWalk is True):
            self.Owner.Sprite.SpriteSource = "AustinWalk"
            self.CanWalk = False
            
        if(self.CanWalkBackward is True):
            self.Owner.Sprite.SpriteSource = "AustinWalkBack"
            self.CanWalkBackward = False
            
        elif(self.CanJump is True):
            self.Owner.Sprite.SpriteSource = "AustinFall"
            self.CanJump = False
            
        elif(self.CanFall is True):
            self.Owner.Sprite.SpriteSource = "AustinFall"
            self.CanFall = False
            
        elif(self.CanKneel is True):
            self.Owner.Sprite.SpriteSource = "AustinKneel"
            self.CanKneel = False
        
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
            
    def ChaseTarget(self, UpdateEvent):
        CameraPosition = self.Space.FindObjectByName("Camera")
        #PlayPosition = self.Owner.Transform.Translation
        #CamDistance = CameraPosition.Transform.Translation -  PlayPosition
        CameraPosition.Transform.Translation += Vector3(self.ChaseDirection.x, self.ChaseDirection.y, 0) * UpdateEvent.Dt * self.ChaseSpeed
        
    def CalculateChaseDirectionAndDistance(self):
        CameraPosition = self.Space.FindObjectByName("Camera")
        PlayPosition = self.Owner.Transform.Translation
        
        self.ChaseDirection = Vector3(PlayPosition.x - 2 + self.HorizontalDistance, PlayPosition.y + self.VerticleDistance, 40) - CameraPosition.Transform.Translation
        #self.DistanceFromTarget = self.ChaseDirection.length()
        #self.ChaseDirection.normalize()
        
    def CalculateChaseDirectionAndDistance2(self):
        CameraPosition = self.Space.FindObjectByName("Camera")
        PlayPosition = self.Owner.Transform.Translation
        
        self.ChaseDirection = Vector3(PlayPosition.x + 2 + self.HorizontalDistance, PlayPosition.y + self.VerticleDistance, 40) - CameraPosition.Transform.Translation

Zero.RegisterComponent("AustinPlayerController", AustinPlayerController)