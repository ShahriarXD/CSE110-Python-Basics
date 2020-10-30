#xxxargs 
# so xxxargs muloto dictonary er moton kaj korbe.

def student(**details):
    print(details)

student(id=101 , name="KS MAHIR", section="A" )    


def sex_worker(**details):
    print(details["name"])

sex_worker(id=101 , name="KS MAHIR", section="A" ) 



#OUTPUT============

#{'id': 101, 'name': 'KS MAHIR', 'section': 'A'}
#KS MAHIR 
