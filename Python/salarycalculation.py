def grosssalary(basicsalary,allowances):
    return basicsalary + allowances
def netsalary(grosssalary,deductions):
    return grosssalary - deductions
def allowances(hra,da,ta):
    return hra + da + ta
def deductions(pf,insurance):
    if (basicsalary>8000):
        return 200 + pf + insurance
    else:
        return 150 + pf + insurance

basicsalary = float(input("enter basicsalary : "))
hra = basicsalary*0.22
da = basicsalary*0.18
ta = basicsalary*0.10
pf = basicsalary*0.12
insurance = basicsalary*0.08
print("the overall deductions are ",deductions(pf,insurance))
print("the overall allowances are ",allowances(hra,da,ta))
allowances = allowances(hra,da,ta)
deductions = deductions(pf,insurance)
print("the gross salary is ",grosssalary(basicsalary,allowances))
grosssalary = grosssalary(basicsalary,allowances)
print("the netsalary is ",netsalary(grosssalary,deductions))
