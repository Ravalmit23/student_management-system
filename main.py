class system:       
    details={
        "name":"",
        "roll-no":"",
        "marks":{}
        }

    def menu(self):
        while True:
            print('''
1:ADD STUDENT DETAILS
2:VIEW DETAILS
3:UPDATE DETAILS
4:DELETE DETAILS
5:EXIT
''')
            choice=int(input("ENTER YOUR CHOICE:"))
            if choice==1:
                self.add_details()
            elif choice==2:
                pass
            elif choice==3:
                pass
            elif choice==4:
                pass
            else:
                break
                exit()
    def add_details(self):
        name1=input("ENTER YOUR NAME:")
        self.details["name"]=name1
        roll=int(input("ENTER YOUR ROLL-NO:"))
        self.details["roll-no"]=roll
        subjects=int(input("ENTER YOUR NO OF SUBJECTS:"))
        for i in range(subjects):
            names=input(f"ENTER {i+1} SUBJECT NAME=")
            marks=int(input(f"ENTER {names} SUBJECT MARK="))
            self.details["marks"][names]=marks
        print(self.details)
            


s1=system()
s1.menu()