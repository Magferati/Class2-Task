class Family:

    def __init__(self, fathername, mothername, brothername, sistername, familymember, myname):
        self.father_name = fathername
        self.mother_name = mothername
        self.brother_name = brothername
        self.sister_name = sistername
        self.family_member = familymember
        self.my_name = myname

family= Family('Aksh', 'Ava', 'Rana', 'Rimi', 5, 'Suva')
print(f'father name: {family.father_name},mother name: {family.mother_name}, brother name: {family.brother_name}, sister name: {family.sister_name}, family member: {family.family_member}, my name: {family.my_name}')