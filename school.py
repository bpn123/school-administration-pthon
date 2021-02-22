# Create class "Student" 
class Student: 
	 
	def __init__(self, name, rollno, m1, m2): 
		self.name = name 
		self.rollno = rollno 
		self.m1 = m1 
		self.m2 = m2 
		
	 
	def accept(self, Name, Rollno, marks1, marks2 ): 
		ob = Student(Name, Rollno, marks1, marks2 ) 
		ls.append(ob) 

	 
	def display(self, ob): 
			print("Name : ", ob.name) 
			print("RollNo : ", ob.rollno) 
			print("Marks1 : ", ob.m1) 
			print("Marks2 : ", ob.m2) 
			print("\n")	 
		
		 
	def search(self, rn): 
		for i in range(ls.__len__()): 
			if(ls[i].rollno == rn): 
				return i	 

									 
	def delete(self, rn): 
		i = obj.search(rn) 
		del ls[i] 

	 
	def update(self, rn, No): 
		i = obj.search(rn) 
		roll = No 
		ls[i].rollno = roll; 
		
# Create a list to add Students 
ls =[] 
# an object of Student class 
obj = Student('', 0, 0, 0) 

print("\nOperations used, ") 
print("\n1.Accept Student details\n2.Display Student Details\n" 
	  "3.Search Details of a Student\n4.Delete Details of Student" 
	  "\n5.Update Student Details\n6.Exit") 

# ch = int(input("Enter choice:")) 
# if(ch == 1): 
obj.accept("Asu", 1, 100, 98) 
obj.accept("Lkra", 2, 90, 90) 
obj.accept("Chinu", 3, 80, 75) 
		
# elif(ch == 2): 
print("\n") 
print("\nList of Students:\n") 
for i in range(ls.__len__()):	 
	obj.display(ls[i]) 
			
# elif(ch == 3): 
print("\n Student Found: ") 
s = obj.search(3) 
obj.display(ls[s]) 
		
# elif(ch == 4): 
obj.delete(2) 
print(ls.__len__()) 
print("List after deletion") 
for i in range(ls.__len__()):	 
	obj.display(ls[i]) 
			
# elif(ch == 5): 
obj.update(3, 2) 
print(ls.__len__()) 
print("List after updation:") 
for i in range(ls.__len__()):	 
	obj.display(ls[i]) 
			
# else: 
print("Thank You!") 
	
