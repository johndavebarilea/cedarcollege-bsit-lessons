# input: q1, q2, q3, q4, sem1, sem2, fin
# process: 
#   sem1 = (q1+q2) / 2
#   sem2 = (q3+q4) / 2
#   fin = (sem1+sem2) / 2
# output: fin

q1 = int(input("Enter first quarter: "))
q2 = int(input("Enter second quarter: "))
q3 = int(input("Enter third quarter: "))
q4 = int(input("Enter fourth quarter: "))

sem1 = (q1+q2) / 2
sem2 = (q3+q4) / 2

fin = (sem1+sem2) / 2

print("---SEMESTER GRADES---")
print("First semester grade: "+str(sem1))
print("Second semester grade: "+str(sem2))

print("Final grade: "+str(fin))