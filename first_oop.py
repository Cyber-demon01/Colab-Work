class data:
    '''Model of data provided by student. can edit if required more'''
    def __init__(self, student_data):
        self._student_data = student_data
        __university_code_tech = "techuniv02"
        __university_code_medical = "medic01"

class technical_Universities(data):
    '''Technical_universities recieve application from student and data from class data'''

    #check eligibility in all institute on the basis of required data
    def all_institute(self):
        avialable_choices = []
        if self.iit():
            avialable_choices.append("iit")
        if self.iilm():
            avialable_choices.append("iilm")
        if self.galgotia():
            avialable_choices.append("galgotia")
        return avialable_choices

    #each institute with their eligibility criteria
    #can be called saperately if student want to choose specific institute
    def iit(self):
        if int(self._student_data["Jee adv rank"]) < 6000:
            return True
        else:
            return False
    def iilm(self):
        if int(self._student_data["12 score"]) > 70:
            return True
        else:
            return False
    def galgotia(self):
        if int(self._student_data["Jee main rank"]) < 100000:
            return True
        else:
            return False

class medical_Universities(data):
    '''medical_universities recieve application from student and data from class data'''
    def all_institute(self):
        avialable_choices = []
        if self.aiims():
            avialable_choices.append("aiims")
        if self.sharda():
            avialable_choices.append("sharda")
        if self.Max():
            avialable_choices.append("Max")
        return avialable_choices

    #each institute with their eligibility criteria
    #can be called saperately if student want to choose specific institute   
    def aiims(self):
        if int(self._student_data["neet rank"]) < 6000:
            return True
        else:
            return False
    def sharda(self):
        if int(self._student_data["12 score"]) > 80:
            return True
        else:
            return False
    def Max(self):
        if int(self._student_data["neet rank"]) < 75000:
            return True
        else:
            return False


class iit(data):
    """Process data from student data class and provide info about branch"""

    def __init__(self, branch, student_data):
        super().__init__(student_data) #inherit the _student_data from data class
        self.branch = branch
        self.rank = int(self._student_data["Jee adv rank"]) #int require cause data is in str and comparing with int

    def selection(self):
        """select which branch student want to take"""
        if self.branch == "no":
            return self.all_branch()
        elif self.branch == "btech cse":
            if self.Btech_cse():
                print("congrats you got your desire CSE branch in iit")
            else:
                print("You didn't got your desire branch, better luck next time.")
        elif self.branch == "btech it":
            if self.Btech_it():
                print("congrats you got your desire IT branch in iit")
            else:
                print("You didn't got your desire branch, better luck next time.")
    def all_branch(self):
        """show all the available branch student is getting"""
        course = []
        if self.Btech_cse():
            course.append("CSE") 
        if self.Btech_it():
            course.append("IT")
        return course
    def Btech_cse(self):
        
        if self.rank < 100:
            return True
        else:
            return False
    def Btech_it(self):
        if self.rank < 200:
            return True
        else:
            return False

class aiims(data):
    """Process student data from data class and provide the branch they can get."""
    def __init__(self, branch, student_data):
        super().__init__(student_data)
        self.branch = branch
        self.rank = int(self._student_data["neet rank"])
    def selection(self):
        if self.branch == "no":
            return self.all_branch()
        elif self.branch == "medical science":
            if self.medical_science():
                print("congrats you got your desire medical science branch in aiims")
            else:
                print("You didn't got your desire branch, better luck next time.")
        elif self.branch == "cardio surgeon":
            if self.cardio_surgeon():
                print("congrats you got your desire cardio surgeon branch in iit")
            else:
                print("You didn't got your desire branch, better luck next time.")
    def all_branch(self):
        course = []
        if self.medical_science():
            course.append("medical science")
        if self.cardio_surgeon():
            course.append("cardio surgeon")
        return course
    def medical_science(self):
        
        if self.rank < 300:
            return True
        else:
            return False
    def cardio_surgeon(self):
        if self.rank < 100:
            return True
        else:
            return False


#data required by university to check eligibility
technical_student_data = {
    "name": "",
    "12 score": 0,
    "Jee main rank": 0,
    "Jee adv rank": 0,
}
medical_student_data = {
    "name": "",
    "12 score": 0,
    "neet rank": 0,
}

def request_by_student(request):
    """ask for data required for admission and return requested university"""
    if request == "technical":

        #loop through the required data mentioned in technical_student_data and medical_student_data
        for requested_data in technical_student_data:
            technical_student_data[requested_data] = input(f"{requested_data}: ")

        #send data to university
        apply = technical_Universities(technical_student_data)
        return apply
    elif request == "medical":
        for requested_data in medical_student_data: 
            medical_student_data[requested_data] = input(f"{requested_data}: ")
        apply = medical_Universities(medical_student_data)
        return apply
    else:
        #error check
        print("no such field available")
    

options = ""

#to keep running program until admission close
Admission = True

while Admission:
    #ask for field they want to choose tech or medical
    request = input("Which field you want to select (technical or medical): ").lower()
    #to close admission portal
    if request == "off":
        Admission = False
    else:
        apply = request_by_student(request)
        #call all_intitute to show all available choices.
        for i in range(0, len(apply.all_institute())):
            options += f"\n{i+1}. {apply.all_institute()[i]}"
        selected_institute = input(f"""you have qualified in the following institutes. Choose one to apply:{options}\n
        which one you want to choose: """).lower()
        branch = input("Any specific Branch you want if yes which one (hint: btech cse)if no write no: ").lower()

        if selected_institute == "iit":
            institute = iit(branch, technical_student_data)
        if selected_institute == "aiims":
            institute = aiims(branch, medical_student_data)
        return_value = institute.selection()
        if return_value != None:
            if len(return_value) > 1:
                course_got = ""
                for x in return_value:
                    course_got += f" {x}, "
                print(f"congrats you got {course_got} branches.")
            else:
                print(f"you got {return_value[0]} branch.")
    



    

