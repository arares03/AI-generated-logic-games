import random
import argparse
import subprocess
from sympy import symbols, And, Or, Not, Implies, satisfiable, simplify

P, Q, R, S, T = symbols('P Q R S T')
variables = [P, Q, R, S, T]

def random_variable():
    """Return a random propositional variable."""
    return random.choice(variables)

def random_operator(expr1, expr2):
    """Return a random logical operator applied to two expressions."""
    operator = random.choice([And, Or, Implies])
    return operator(expr1, expr2)

def random_not(expr):
    """Randomly decide whether to apply a NOT operator."""
    return Not(expr) if random.choice([True, False]) else expr

def generate_random_statement():
    """Generate a random propositional logic statement."""
    var1 = random_variable()
    var2 = random_variable()
    expr1 = random_not(var1)
    expr2 = random_not(var2)
    return random_operator(expr1, expr2)

def generate_compatible_statements(num_statements=5):
    """Generate a list of logically compatible propositional logic statements."""
    statements = []

    while len(statements) < num_statements:
        new_statement = generate_random_statement()
        if satisfiable(And(*(statements + [new_statement]))):
            statements.append(new_statement)

    return statements

def generate_goal(statements, achievable=True):
    """Generate a goal that is a logical consequence of the statements if achievable is True, otherwise make it unachievable."""
    while True:
        potential_goal = generate_random_statement()
        implication = Implies(And(*statements), potential_goal)
        if achievable:
            if simplify(implication) == True:
                return potential_goal
        else:
            if not simplify(implication) == True:
                return potential_goal

def convert_to_prover9(expr):
    """Convert a sympy expression to Prover9 syntax."""
    if expr.func == And:
        return f"({convert_to_prover9(expr.args[0])} & {convert_to_prover9(expr.args[1])})"
    elif expr.func == Or:
        return f"({convert_to_prover9(expr.args[0])} | {convert_to_prover9(expr.args[1])})"
    elif expr.func == Implies:
        return f"({convert_to_prover9(expr.args[0])} -> {convert_to_prover9(expr.args[1])})"
    elif expr.func == Not:
        return f"-{convert_to_prover9(expr.args[0])}"
    else:
        return str(expr)

def write_prover9_input(statements, goal, filename="./myProver9.in"):
    """Write the statements and goal to a Prover9 input file."""
    with open(filename, "w") as f:
        f.write("formulas(assumptions).\n")
        for statement in statements:
            f.write(f"    {convert_to_prover9(statement)}.\n")
        f.write("end_of_list.\n\n")
        f.write("formulas(goals).\n")
        f.write(f"    {convert_to_prover9(goal)}.\n")
        f.write("end_of_list.\n")

def run_prover9(input_file="./myProver9.in"):
    """Run Prover9 with the given input file and return whether the goal is achievable."""
    prover9_path = "./prover9"
    result = subprocess.run([prover9_path, "-f", input_file], capture_output=True, text=True)
    output = result.stdout
    return "THEOREM PROVED" in output


def generatePropositionalLogic(achievable_flag):
    while True:
        statements = generate_compatible_statements(5)

        goal = generate_goal(statements, achievable_flag)

        write_prover9_input(statements, goal)

        goal_achieved = run_prover9()

        if goal_achieved == achievable_flag:
            prover9_statements = []
            for i, statement in enumerate(statements, 1):
                prover9_statement = convert_to_prover9(statement)
                prover9_statements.append(f"Statement {i}: {prover9_statement}")

            prover9_goal = convert_to_prover9(goal)

            return prover9_statements, prover9_goal

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a propositional logic problem with an achievable or unachievable goal.")
    parser.add_argument('--achievable', action='store_true', help="Set this flag if the goal should be achievable.")
    args = parser.parse_args()

    while True:
        statements = generate_compatible_statements(5)
        goal = generate_goal(statements, args.achievable)

        write_prover9_input(statements, goal)

        goal_achieved = run_prover9()

        if goal_achieved == args.achievable:
            for i, statement in enumerate(statements, 1):
                prover9_statement = convert_to_prover9(statement)
                print(f"Statement {i}: {prover9_statement}")
            prover9_goal = convert_to_prover9(goal)
            print(f"Goal: {prover9_goal}")
            break
