import Zero
import Events
import Property
import VectorMath
import random

Vector3 = VectorMath.Vec3

class SplashScreenCameraShake:
    def DefineProperties(self):
        pass

    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)

    def OnLogicUpdate(self, UpdateEvent):
        Tracker = self.Space.FindObjectByName("SplashScreenTracker")
        if(Tracker.SplashScreenTracker.Explode is True):
            self.Owner.Transform.Translation = Vector3(0.864878 + random.randint(-2, 2), -2.86364 + random.randint(-2, 2), 40)
            
        else:
            self.Owner.Transform.Translation = Vector3(0.864878, -2.86364, 40)

Zero.RegisterComponent("SplashScreenCameraShake", SplashScreenCameraShake)