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
                self.view_details()
            elif choice==3:
                self.update()
            elif choice==4:
                self.dlt_details()
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
            marks01=int(input(f"ENTER {names} SUBJECT MARK="))
            self.details["marks"][names]=marks01
        print(self.details)


    def view_details(self):
        if self.details=="":
            # print(self.details)
            print("no data")
        else:
            print("THERE ARE NO DETAILS IN LIST")
            print(self.details)


    def update(self):
        if self.details=="":
            print("THERE ARE NO DETAILS IN LIST TO UPDATE")
        else:
            updates=input("what you update=")
            if updates=="name":
                upadte01=input(f"enter your new {updates}=")
                self.details["name"]=upadte01
            if updates=="roll-no":
                upadte01=input(f"enter your new {updates}=")
                self.details["roll-no"]=upadte01
            if updates=="marks":
                subjects=input("enter subject name to update=")
                for i in self.details["marks"]:
                    update_mark=int(input("ENTER UPDATED marks="))
                    self.details["marks"][subjects]=update_mark
                    print("marks updated successfully")
 
            

    def dlt_details(self):
        if self.details=="":
            print("there are no details to delete")
        else:
            dlt=input("what you delete=")
            if dlt=="name":
                self.details["name"]=""
                print("name deleted")
            if dlt=="roll-no":
                self.details["roll-no"]=""
            if dlt=="marks":
                subjects=input("enter subject name to delete marks=")
                for i in self.details["marks"]:
                    self.details["marks"][subjects]=""
                    print("marks deleted successfully")
 
            
            


s1=system()
s1.menu()