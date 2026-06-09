class Patient:
    hospital_name="city_care_hospital"
    def __init__(self,patient_id,name,age,admitted_days,daily_charge):
        self.patient_id=patient_id
        self.name=name
        self.age=age
        self.admitted_days=admitted_days
        self.daily_charge=daily_charge
    def calculate_bill(self):
        total_bill = self.admitted_days * self.daily_charge
        return total_bill
    
    @classmethod
    def change_hospital_name(cls, new_name):
        Patient.hospital_name=new_name

    @staticmethod
    def is_senior(age):
        if age >= 60:
            return True
        else:
            return False
        
patient_1=Patient(101,"siju",5,100,100)

print(patient_1.is_senior(patient_1.age))

        
            