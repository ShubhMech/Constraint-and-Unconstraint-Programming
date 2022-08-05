from ortools.sat.python import cp_model

class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self):
        self.__solution_count += 1
        for v in self.__variables:
            print('%s=%i' % (v, self.Value(v)), end=' ')
        print()

    def solution_count(self):
        return self.__solution_count

model = cp_model.CpModel()

x = model.NewIntVar(0, 1000, 'x')
y = model.NewIntVar(0, 1000, 'y')
z = model.NewIntVar(0, 1000, 'z')

model.Add(2*x+7*y+3*z<=50)
model.Add(3*x-5*y+7*z<=45)
model.Add(5*x+2*y-6*z<=37)
model.Add(x+y+z>=10)

#model.Maximize(2*x+2*y+3*z)

solver = cp_model.CpSolver()
status = solver.Solve(model)

print('Status =', solver.StatusName(status))
print('FO =', solver.ObjectiveValue())
print('x =', solver.Value(x))
print('y =', solver.Value(y))
print('z =', solver.Value(z))

solution_printer = VarArraySolutionPrinter([x, y, z])
status = solver.SearchForAllSolutions(model, solution_printer)