from engine.engine import Engine

class SternmanEngine(Engine):
    def __init__(self, warning_light):
        self.warning_light = warning_light

    def needs_service(self):
        if self.warning_light: 
            return True
        else: return False