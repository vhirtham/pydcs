from .unit import Unit


class Vehicle(Unit):
    def __init__(self, id=None, name=None, _type="Sandbox"):
        super(Vehicle, self).__init__(id, name, _type)
        self.player_can_drive = False
        self.transportable = {"randomTransportable": False}

    def dict(self):
        d = super(Vehicle, self).dict()
        d["playerCanDrive"] = self.player_can_drive
        d["transportable"] = self.transportable
        return d
