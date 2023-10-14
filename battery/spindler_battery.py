from battery import Battery
from refactored.utilities import addYears

def SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        should_service_date = addYears(self.last_service_date, 3)
        if should_service_date <= self.current_date:
            return True
        else: return False