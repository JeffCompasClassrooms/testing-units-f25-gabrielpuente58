import math
import unittest
from calc import Calc


class TestCalcAdd(unittest.TestCase):
    def setUp(self):
        self.c = Calc()

    # ---- Integers ----
    def test_add_two_positive_ints(self):
        self.assertEqual(self.c.add(2, 3), 5)

    def test_add_positive_and_negative_int(self):
        self.assertEqual(self.c.add(5, -2), 3)

    def test_add_two_negatives(self):
        self.assertEqual(self.c.add(-7, -8), -15)

    def test_add_with_zero_left(self):
        self.assertEqual(self.c.add(0, 9), 9)

    def test_add_with_zero_right(self):
        self.assertEqual(self.c.add(9, 0), 9)

    def test_add_large_ints(self):
        a = 10**12
        b = 10**12 + 5
        self.assertEqual(self.c.add(a, b), a + b)

    # ---- Floats ----
    def test_add_two_floats(self):
        self.assertAlmostEqual(self.c.add(2.5, 3.1), 5.6)

    def test_add_float_and_int(self):
        res = self.c.add(2.5, 2)
        self.assertIsInstance(res, float)
        self.assertAlmostEqual(res, 4.5, places=7)

    def test_add_negative_float(self):
        self.assertAlmostEqual(self.c.add(-2.75, 1.25), -1.5)

    def test_add_float_rounding_edge(self):
        self.assertAlmostEqual(self.c.add(0.1, 0.2), 0.3, places=7)

    # ---- Special numeric-like values ----
    def test_add_bools(self):
        # In Python, True == 1 and False == 0
        self.assertEqual(self.c.add(True, True), 2)
        self.assertEqual(self.c.add(True, False), 1)

    def test_add_infinities(self):
        self.assertTrue(math.isinf(self.c.add(float('inf'), 1.0)))

    def test_add_nan_propagates(self):
        res = self.c.add(float('nan'), 1.0)
        self.assertTrue(math.isnan(res))

    # ---- Non-numeric (valid Python + operator behavior) ----
    def test_add_strings_concatenates(self):
        self.assertEqual(self.c.add("foo", "bar"), "foobar")

    def test_add_lists_concatenates(self):
        self.assertEqual(self.c.add([1, 2], [3]), [1, 2, 3])

    def test_add_tuples_concatenates(self):
        self.assertEqual(self.c.add((1, 2), (3,)), (1, 2, 3))

    # ---- Type errors (invalid + combos) ----
    def test_add_string_and_int_raises(self):
        with self.assertRaises(TypeError):
            self.c.add("3", 4)

    def test_add_list_and_int_raises(self):
        with self.assertRaises(TypeError):
            self.c.add([1, 2], 3)


class TestCalcMul(unittest.TestCase):
    def setUp(self):
        self.c = Calc()

    # ---- Integers ----
    def test_mul_two_positive_ints(self):
        self.assertEqual(self.c.mul(4, 5), 20)

    def test_mul_positive_and_negative_int(self):
        self.assertEqual(self.c.mul(7, -3), -21)

    def test_mul_two_negatives(self):
        self.assertEqual(self.c.mul(-6, -2), 12)

    def test_mul_by_zero_left(self):
        self.assertEqual(self.c.mul(0, 999), 0)

    def test_mul_by_zero_right(self):
        self.assertEqual(self.c.mul(999, 0), 0)

    def test_mul_large_ints(self):
        a = 10**9
        b = 10**6
        self.assertEqual(self.c.mul(a, b), a * b)

    # ---- Floats ----
    def test_mul_two_floats(self):
        self.assertAlmostEqual(self.c.mul(2.5, 0.4), 1.0, places=7)

    def test_mul_float_and_int(self):
        self.assertAlmostEqual(self.c.mul(2.5, 2), 5.0, places=7)

    def test_mul_negative_float(self):
        self.assertAlmostEqual(self.c.mul(-1.5, 4.0), -6.0, places=7)

    def test_mul_float_rounding_edge(self):
        self.assertAlmostEqual(self.c.mul(0.1, 0.2), 0.02, places=7)

    # ---- Special numeric-like values ----
    def test_mul_bools(self):
        self.assertEqual(self.c.mul(True, 5), 5)
        self.assertEqual(self.c.mul(False, 5), 0)

    def test_mul_by_infinity(self):
        self.assertTrue(math.isinf(self.c.mul(float('inf'), 2.0)))

    def test_mul_nan_propagates(self):
        res = self.c.mul(float('nan'), 7.0)
        self.assertTrue(math.isnan(res))

    # ---- Non-numeric (valid Python * operator behavior) ----
    def test_mul_string_and_int_repeats(self):
        self.assertEqual(self.c.mul("ab", 3), "ababab")

    def test_mul_list_and_int_repeats(self):
        self.assertEqual(self.c.mul([1, 2], 2), [1, 2, 1, 2])

    # ---- Type errors (invalid * combos) ----
    def test_mul_two_strings_raises(self):
        with self.assertRaises(TypeError):
            self.c.mul("a", "b")

    def test_mul_dict_and_int_raises(self):
        with self.assertRaises(TypeError):
            self.c.mul({"x": 1}, 2)

    # ---- A few property-style checks ----
    def test_mul_distributes_over_add_simple(self):
        # (a+b)*c == a*c + b*c
        a, b, c = 2, 3, 4
        left = self.c.mul(self.c.add(a, b), c)
        right = self.c.add(self.c.mul(a, c), self.c.mul(b, c))
        self.assertEqual(left, right)

    def test_mul_commutative_for_numbers(self):
        a, b = 7.5, -2
        self.assertAlmostEqual(self.c.mul(a, b), self.c.mul(b, a), places=7)

    def test_add_commutative_for_numbers(self):
        a, b = -3.25, 9
        self.assertAlmostEqual(self.c.add(a, b), self.c.add(b, a), places=7)


if __name__ == "__main__":
    unittest.main()
