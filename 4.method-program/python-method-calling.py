def my_name_is():
    print("My name is Sanjida Islam Shammi")


def i_have_enrolled_course(course_name):
    print(f"I have enrolled in a course named {course_name}")


def i_have_learning(backend, frontend):
    return f"Learning {backend}, {frontend}"


course_and_learn = [
         
   {
       "course":"Python and web",
       "backend":"Java, HTML, CSS",
       "frontend": "Python"
   },
   {
       "course":"Java Spring Boot",
       "backend":"Java, HTML, CSS",
       "frontend": "Hibernet"
   },
   {
       "course": "C# & ASP.NET Core",
       "backend": "C#, Entity Framework",
       "frontend": "Razor"
   }
]


for item in course_and_learn:
    course_name=item["course"]
    backend=item["backend"]
    frontend=item["frontend"]



    my_name_is()
    i_have_enrolled_course(course_name)
    result = i_have_learning(backend, frontend)
    print(result)



