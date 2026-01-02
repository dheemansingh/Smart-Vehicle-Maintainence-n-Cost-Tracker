class Vehicle:
    def __init__(self, vehicle_id, owner_name, vehicle_type, fuel_type):
        self.vehicle_id = vehicle_id
        self.owner_name = owner_name
        self.vehicle_type = vehicle_type   # car, bike, truck
        self.fuel_type = fuel_type         # petrol, diesel, ev
        self.service_records = []

    def add_service_record(self, service):
        self.service_records.append(service)

    def get_total_service_cost(self):
        total = 0
        for record in self.service_records:
            total += record["cost"]
        return total

    def display_vehicle_info(self):
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Owner: {self.owner_name}")
        print(f"Type: {self.vehicle_type}")
        print(f"Fuel: {self.fuel_type}")
        print(f"Total Services: {len(self.service_records)}")
