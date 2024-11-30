# Self-test 1.1:
# The number x satisfies the inequalities 2 < x <= 4 and |x| <= 3. Expressed as a single expression, what values cam x take?

from src.maths.standard import inequalities

if __name__=='__main__':
    # Initialise inequality with 2 < x (x > 2) and then add <= 4 bound
    inequality_under_test = inequalities.Inequality('>', 2)
    inequality_under_test.add_bound('<=', 4)

    # |x| <= 3 means if x > 0 then x <= 3 and if x < 0 then x >= -3
    inequality_under_test.add_bound('<=', 3)
    inequality_under_test.add_bound('>=', -3)

    inequality_under_test.combine_bounds()
    inequality_under_test.print_bounds()