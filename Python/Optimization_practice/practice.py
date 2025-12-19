from pulp import *

# Elementary features

lp = LpProblem('Baker_Problem',LpMaximize)

# Define variables

x1 = LpVariable(name='log',lowBound=0,cat='Integer')
x2 = LpVariable(name='cake',lowBound=0,cat='Integer')

# Add the objecive function

lp += (10*x1) + (5*x2)
print("Objective funciton :",lp.objective)
print()

# Add the constraints

lp += (5*x1 + x2 <=90,'oven')
lp += (x1 + 10*x2 <=300,'food processor')
lp += (4*x1 + 6*x2 <=125,'boiler')

print('Constraints:')
for i in lp.constraints:
    print(i,":",lp.constraints[i])
print()

# Status the LP
status = lp.solve(PULP_CBC_CMD(msg=0))

status = lp.solve()
print('Status:', status)

# Print the solution

print("The optimum solution for above menitoned problem is")
for var in lp.variables():
    print(var,'=',value(var))
print('OPT =',value(lp.objective))


