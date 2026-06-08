class patient:
    hospital_name="City Hospital"
    def __init__(self,name,age):
      self.name=name
      self.age=age
    def display(self):
       return f"{self.name} of {self.age} from {self.hospital_name}"

patient_1=patient("siju",29)

print(patient_1.display())