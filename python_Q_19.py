"""
Q-19:Care hospital wants to know the medical speciality visited by the maximum number of patients.Assume that the patient id of the patient
along with the medical speciality visited by the patient is stored in a list.The details of the medical specialities are stored in a dictionary
as follows:
{"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
Write a function to find the medical speciality visited by the maximum number of patients and return the name of the speciality.
Note:1.Assume that there is always only one medical speciality which is visited by maximum number of patients.
2.Perform case sensitive string comparison whenever necessary.
sample input                                           expected output
[101,P,102,O,302,P,305,P]                              Pediatrics
[101,O,102,O,302,P,305,E,401,O,656,O]                  Orthopedics
[101,O,102,E,302,P,305,P,401,E,656,O,987,E]            ENT
"""
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    max_visit=0
    P=patient_medical_speciality_list.count('P')
    E=patient_medical_speciality_list.count('E')
    O=patient_medical_speciality_list.count('O')
    if P>E and P>O:
        speciality=medical_speciality['P']
    elif E>O:
        speciality=medical_speciality['O']
    else:
        speciality=medical_speciality['O']
    return speciality
patient_medical_speciality_list=[301,'P',302,'P',305,'P',401,'E',656,'E']
medical_speciality={'P':'Pediatrics','O':'Orthopedics','E':'ENT'}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
