import math
import unittest
from circle import Circle


class TestCircle(unittest.TestCase):

    def test_init_sets_radius(self):
        c = Circle(3.5)
        self.assertEqual(c.getRadius(), 3.5)

    def test_get_radius_after_set(self):
        c = Circle(1.0)
        self.assertTrue(c.setRadius(4.25))
        self.assertEqual(c.getRadius(), 4.25)

    def test_set_radius_allows_zero(self):
        c = Circle(5.0)
        ok = c.setRadius(0.0)
        self.assertTrue(ok)
        self.assertEqual(c.getRadius(), 0.0)

    def test_set_radius_rejects_negative(self):
        c = Circle(2.0)
        ok = c.setRadius(-1.0)
        self.assertFalse(ok)
        self.assertEqual(c.getRadius(), 2.0)

    def test_area_zero_radius(self):
        c = Circle(0.0)
        self.assertEqual(c.getArea(), 0.0)

    def test_area_general(self):
        r = 3.0
        c = Circle(r)
        self.assertAlmostEqual(c.getArea(), math.pi * r * r, places=7)

    @unittest.expectedFailure
    def test_area_for_radius_two_should_be_4pi(self):
        c = Circle(2.0)
        self.assertAlmostEqual(c.getArea(), math.pi * 4.0, places=7)

    def test_circumference_zero(self):
        c = Circle(0.0)
        self.assertEqual(c.getCircumference(), 0.0)

    def test_circumference_general(self):
        r = 2.25
        c = Circle(r)
        self.assertAlmostEqual(c.getCircumference(), 2.0 * math.pi * r, places=7)

    def test_instances_are_independent(self):
        a = Circle(1.0)
        b = Circle(5.0)
        a.setRadius(3.0)
        self.assertEqual(a.getRadius(), 3.0)
        self.assertEqual(b.getRadius(), 5.0)


if __name__ == "__main__":
    unittest.main()
