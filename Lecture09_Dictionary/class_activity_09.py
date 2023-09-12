
student2 = {
    "ID" : 102,
    "First Name " : "Ali",
    "Last Name " : "Hassan",
    "Course" : "Maths",
    "Grades" : {"Maths" : 92 , "Science" : 88 , "History" : 90 }


}



for key,value in student2.items():
    print(f"{key},{value}")
    if key == "Grades":
     for i,j in value.items():
        print(f"{i},{j}")
