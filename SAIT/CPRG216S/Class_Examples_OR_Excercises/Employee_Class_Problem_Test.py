import Employee_Class_Problem

def main():
    # Test constructor
    Emp1 = Employee_Class_Problem.Employee()
    Emp2 = Employee_Class_Problem.Employee("Harvey", 0, 11.20)
    
    # Test setters
    Emp1.Set_Name("Sara")
    Emp1.Set_Hours_Worked(40)
    Emp1.Set_Rate_of_Pay(15)
    
    # Test getters
    print("Payroll Report for", Emp1.Get_Name())
    print("Hours =", Emp1.Get_Hours_Worked())
    print("Rate =", Emp1.Get_Rate_of_Pay())
    
    # Test calc_gross_pay() method
    print("Total Gross = $", Emp1.Calc_Gross_Pay(), sep='')
    print()
    
    # Test add_hours_worked()
    Emp2.Add_Hours_Worked(10)
    Emp2.Add_Hours_Worked(5)
    
    print("Payroll Report for " + Emp2.Get_Name())
    
    # Test of __str__()
    print(Emp2)

if __name__ == "__main__":
    main()

#Emp = Employee("Jon", 35, 19.50)
#print(Emp)