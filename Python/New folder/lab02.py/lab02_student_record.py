e=input("Enter Employee Name:")
print("Data type:",type(e))
id=int(input("Enter Employee ID:")) 
print("Data type:",type(id))
s=float(input("Enter Salary:"))
print("Data type:",type(s))
d=input("Enter Department:")
print("Data type:",type(d))
a=input("Is the employee active? (yes/no:)").lower() =="yes"
print("Data type:",type(a))

print("\n---Employee Details---")
print(f"NAME       : {e}")
print(f"ID         : {id}")
print(f"Salary     : {s:.2f}")
print(f"Department : {d}")
print(f"Active     : {a}")









