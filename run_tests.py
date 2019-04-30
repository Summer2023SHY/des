
'''
This runs all tests for the program.
'''
import unittest

# Import the test cases to use
import tests.product.product_test as product
import tests.union.union_test as union

# Initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Add the tests
suite.addTests(loader.loadTestsFromModule(product))
suite.addTests(loader.loadTestsFromModule(union))

# Initialize runner
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
