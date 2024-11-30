# The following rules will be tested in this file
# (a) (a^x)(a^y) = a^(x+y)
# (b) a^0 = 1
# (c) a^-x = 1/(a^x)
# (d) (a^x)^y = a^(xy)
# (e) (a^x)(b^x) = (ab)^x

def rule_a_test(a, x, y):
    # Verify inputs
    if a == 0 and (x < 0 or y < 0):
        # Invalid test
        return True

    lhs = (a**x) * (a ** y)
    rhs = a**(x+y)

    if lhs == rhs:
        return True
    else:
        print("Rule (a) test failed\n")
        print(f"Expected {lhs} to be equal to {rhs}")

def rule_b_test(a):
    lhs = a**0
    rhs = 1

    if lhs == rhs:
        return True
    else:
        print("Rule (b) test failed\n")
        print(f"Expected {lhs} to be equal to {rhs}")

def rule_c_test(a, x):
    # Verify inputs
    if a == 0 and x != 0:
        # Invalid test
        return True

    lhs = a**(-1*x)
    rhs = 1/(a**x)

    if lhs == rhs:
        return True
    else:
        print("Rule (c) test failed\n")
        print(f"Expected {lhs} to be equal to {rhs}")

def rule_d_test(a, x, y):
    # Verify inputs
    if (a == 0 and x < 0) or (a == 0 and (y < 0 and x >= 0)):
        # Invalid test
        return True

    lhs = (a**x) ** y
    rhs = a**(x*y)

    if lhs == rhs:
        return True
    else:
        print("Rule (d) test failed\n")
        print(f"Expected {lhs} to be equal to {rhs}")

def rule_e_test(a, x, b):
    # Verify inputs
    if (a == 0 and x < 0) or (b == 0 and x < 0):
        # Invalid test
        return True

    lhs = (a**x) * (b ** x)
    rhs = (a*b)**x

    if lhs == rhs:
        return True
    else:
        print("Rule (e) test failed\n")
        print(f"Expected {lhs} to be equal to {rhs}")

if __name__=='__main__':
    all_tests_passed = True

    # Populate all combinations of values
    # Integers over 8 cause a float comparison failure
    positive_values = [8]
    negative_values = [-8]

    combination_array_size1 = []
    combination_array_size1.append(0)
    for value in positive_values:
        combination_array_size1.append(value)
    for value in negative_values:
        combination_array_size1.append(value)

    combination_array_size2 = []
    for value1 in combination_array_size1:
        for value2 in combination_array_size1:
            combination_array_size2.append([value1, value2])

    combination_array_size3 = []
    for size2_combination in combination_array_size2:
        for value3 in combination_array_size1:
            combination_array_size3.append([size2_combination[0], size2_combination[1], value3])

    # Run tests according to how many arguments they have
    for combination in combination_array_size1:
        all_tests_passed = (all_tests_passed and rule_b_test(combination))

    for combination in combination_array_size2:
        all_tests_passed = (all_tests_passed and rule_c_test(combination[0], combination[1]))

    for combination in combination_array_size3:
        all_tests_passed = (all_tests_passed and rule_a_test(combination[0], combination[1], combination[2]))
        all_tests_passed = (all_tests_passed and rule_d_test(combination[0], combination[1], combination[2]))
        all_tests_passed = (all_tests_passed and rule_e_test(combination[0], combination[1], combination[2]))

    if all_tests_passed:
        print("All tests passed\n")
    else:
        print("Tests failed\n")