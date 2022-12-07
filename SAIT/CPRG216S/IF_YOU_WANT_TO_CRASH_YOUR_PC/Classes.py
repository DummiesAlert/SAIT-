class Patient:
    def __init__(self, id, name, diagnosis, gender, age):
        self.id = id 
        self.name = name
        self.diagnosis = diagnosis
        self.gender = gender
        self.age = age
  
    def set_name(self,name):
        self.name = name
    def set_diagnosis(self,diagnosis):
        self.diagnosis = diagnosis
    def set_gender(self,gender):
        self.gender = gender
    def set_age(self,age):
        self.age = age 

    def get_id(self,id_user):
        if self.id==id_user:
            return True
        else :
            return False

    def __str__(self):
        return f"{self.id:>20s}{self.name:>20s}{self.diagnosis:>20s}{self.gender:>20s}{self.age:>20s}"
    
    def formatPatientInfo(self):
        return f"{self.id}_{self.name}_{self.diagnosis}_{self.gender}_{self.age}\n"

class Doctor:
    def __init__(self, id, name, specialty, schedule, qualification, room_number):
        self.id = id 
        self.name = name
        self.specialty = specialty
        self.schedule = schedule
        self.qualification = qualification
        self.room_number = room_number
    
    def set_name(self,name):
        self.name = name
    def set_specialty(self,specialty):
        self.specialty = specialty
    def set_schedule(self,schedule):
        self.schedule = schedule
    def set_qualification(self,qualification):
        self.qualification = qualification
    def set_age(self,age):
        self.age = age

    def get_id(self,id_user):
        if self.id==id_user:
            return True
        else :  
            return False
    def get_name(self,name_user):
        if self.name == name_user:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.id:>15s}{self.name:>15s}{self.specialty:>15s}{self.schedule:>15s}{self.qualification:>15s}{self.room_number:>15s}"
    
    def formatPatientInfo(self):
        return f"{self.id}_{self.name}_{self.specialty}_{self.schedule}_{self.qualification}{self.room_number}\n"
    
class Facilities: 
    
    def __init__(Self, Facilities_Name):
    
        Self.Facilities_Name = Facilities_Name 
    
    def Set_Facility_Name(Self, Facilities_Name):
        
        Self.Facilities_Name = Facilities_Name
        
    def __str__(Self): 
        
        a = "\n"
        return f'{Self.Facilities_Name} {a}'
    
    def formatFacilityInfo(Facilities_Name):
        
        return Facilities_Name