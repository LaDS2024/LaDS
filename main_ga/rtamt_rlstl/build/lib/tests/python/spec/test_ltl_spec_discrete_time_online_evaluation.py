import unittest
import rtamt

class TestLTLSpecDiscreteTimeOnlineEvaluation(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestLTLSpecDiscreteTimeOnlineEvaluation, self).__init__(*args, **kwargs)
        self.left1 = 100
        self.right1 = 20

        self.left2 = -1
        self.right2 = -2

        self.left3 = -2
        self.right3 = 10

        self.left4 = 5
        self.right4 = 4

        self.left5 = -1
        self.right5 = -1

    def test_constant(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('out', 'float')
        spec.spec = 'out = 5'

        spec.parse();
        out1 = spec.update(0, [])
        out2 = spec.update(1, [])

        self.assertEqual(out1, 5, "input 1")
        self.assertEqual(out2, 5, "input 2")

    def test_constant_2(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_const('c', 'int', 5)
        spec.declare_var('out', 'float')
        spec.spec = 'out = c'

        spec.parse();
        out1 = spec.update(0, [])
        out2 = spec.update(1, [])

        self.assertEqual(out1, 5, "input 1")
        self.assertEqual(out2, 5, "input 2")

    def test_addition(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req + gnt'

        spec.parse();

        out1 = spec.update(0, [('req', self.left1), ('gnt', self.right1)])
        out2 = spec.update(1, [('req', self.left2), ('gnt', self.right2)])
        out3 = spec.update(2, [('req', self.left3), ('gnt', self.right3)])
        out4 = spec.update(3, [('req', self.left4), ('gnt', self.right4)])
        out5 = spec.update(4, [('req', self.left5), ('gnt', self.right5)])

        self.assertEqual(out1, 120, "input 1")
        self.assertEqual(out2, -3, "input 2")
        self.assertEqual(out3, 8, "input 3")
        self.assertEqual(out4, 9, "input 4")
        self.assertEqual(out5, -2, "input 5")

    def test_subtraction(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req - gnt'

        spec.parse();

        out1 = spec.update(0, [('req', self.left1), ('gnt', self.right1)])
        out2 = spec.update(1, [('req', self.left2), ('gnt', self.right2)])
        out3 = spec.update(2, [('req', self.left3), ('gnt', self.right3)])
        out4 = spec.update(3, [('req', self.left4), ('gnt', self.right4)])
        out5 = spec.update(4, [('req', self.left5), ('gnt', self.right5)])

        self.assertEqual(out1, 80, "input 1")
        self.assertEqual(out2, 1, "input 2")
        self.assertEqual(out3, -12, "input 3")
        self.assertEqual(out4, 1, "input 4")
        self.assertEqual(out5, 0, "input 5")

    def test_multiplication(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req * gnt'

        spec.parse();

        out1 = spec.update(0, [('req', self.left1), ('gnt', self.right1)])
        out2 = spec.update(1, [('req', self.left2), ('gnt', self.right2)])
        out3 = spec.update(2, [('req', self.left3), ('gnt', self.right3)])
        out4 = spec.update(3, [('req', self.left4), ('gnt', self.right4)])
        out5 = spec.update(4, [('req', self.left5), ('gnt', self.right5)])

        self.assertEqual(out1, 2000, "input 1")
        self.assertEqual(out2, 2, "input 2")
        self.assertEqual(out3, -20, "input 3")
        self.assertEqual(out4, 20, "input 4")
        self.assertEqual(out5, 1, "input 5")

    def test_division(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req / gnt'

        spec.parse();

        out1 = spec.update(0, [('req', self.left1), ('gnt', self.right1)])
        out2 = spec.update(1, [('req', self.left2), ('gnt', self.right2)])
        out3 = spec.update(2, [('req', self.left3), ('gnt', self.right3)])
        out4 = spec.update(3, [('req', self.left4), ('gnt', self.right4)])
        out5 = spec.update(4, [('req', self.left5), ('gnt', self.right5)])

        self.assertEqual(out1, 100 / 20, "input 1")
        self.assertEqual(out2, -1 / -2, "input 2")
        self.assertEqual(out3, -2 / 10, "input 3")
        self.assertEqual(out4, 5 / 4, "input 4")
        self.assertEqual(out5, -1 / -1, "input 5")

    def test_abs(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = abs(req)'

        spec.parse();

        out1 = spec.update(0, [('req', self.left1)])
        out2 = spec.update(1, [('req', self.left2)])
        out3 = spec.update(2, [('req', self.left3)])
        out4 = spec.update(3, [('req', self.left4)])
        out5 = spec.update(4, [('req', self.left5)])

        self.assertEqual(out1, 100, "input 1")
        self.assertEqual(out2, 1, "input 2")
        self.assertEqual(out3, 2, "input 3")
        self.assertEqual(out4, 5, "input 4")
        self.assertEqual(out5, 1, "input 5")

    def test_previous(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = prev(req)'

        spec.parse();

        out1 = spec.update(0, [('req', self.left1)])
        out2 = spec.update(1, [('req', self.left2)])
        out3 = spec.update(2, [('req', self.left3)])
        out4 = spec.update(3, [('req', self.left4)])
        out5 = spec.update(4, [('req', self.left5)])

        self.assertEqual(out1, float("inf"), "input 1")
        self.assertEqual(out2, 100, "input 2")
        self.assertEqual(out3, -1, "input 3")
        self.assertEqual(out4, -2, "input 4")
        self.assertEqual(out5, 5, "input 5")

    def test_next_without_pastify(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = next(req)'

        spec.parse()

        self.assertRaises(rtamt.LTLNotImplementedException, spec.update, 0, [('req', self.left1)])

    def test_next_with_pastify(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = next(req)'

        spec.parse()
        spec.pastify()

        out1 = spec.update(0, [('req', self.left1)])
        out2 = spec.update(1, [('req', self.left2)])
        out3 = spec.update(2, [('req', self.left3)])
        out4 = spec.update(3, [('req', self.left4)])
        out5 = spec.update(4, [('req', self.left5)])

        self.assertEqual(out1, 100, "input 1")
        self.assertEqual(out2, -1, "input 2")
        self.assertEqual(out3, -2, "input 3")
        self.assertEqual(out4, 5, "input 4")
        self.assertEqual(out5, -1, "input 5")

    def test_and(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req and gnt'

        spec.parse();

        out1 = spec.update(0, [('req', self.left1), ('gnt', self.right1)])
        out2 = spec.update(1, [('req', self.left2), ('gnt', self.right2)])
        out3 = spec.update(2, [('req', self.left3), ('gnt', self.right3)])
        out4 = spec.update(3, [('req', self.left4), ('gnt', self.right4)])
        out5 = spec.update(4, [('req', self.left5), ('gnt', self.right5)])

        self.assertEqual(out1, 20, "input 1")
        self.assertEqual(out2, -2, "input 2")
        self.assertEqual(out3, -2, "input 3")
        self.assertEqual(out4, 4, "input 4")
        self.assertEqual(out5, -1, "input 5")

    def test_or(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req or gnt'

        spec.parse();

        out1 = spec.update(0, [('req', self.left1), ('gnt', self.right1)])
        out2 = spec.update(1, [('req', self.left2), ('gnt', self.right2)])
        out3 = spec.update(2, [('req', self.left3), ('gnt', self.right3)])
        out4 = spec.update(3, [('req', self.left4), ('gnt', self.right4)])
        out5 = spec.update(4, [('req', self.left5), ('gnt', self.right5)])

        self.assertEqual(out1, 100, "input 1")
        self.assertEqual(out2, -1, "input 2")
        self.assertEqual(out3, 10, "input 3")
        self.assertEqual(out4, 5, "input 4")
        self.assertEqual(out5, -1, "input 5")

    def test_iff(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req iff gnt'

        spec.parse();

        out1 = spec.update(0, [('req', self.left1), ('gnt', self.right1)])
        out2 = spec.update(1, [('req', self.left2), ('gnt', self.right2)])
        out3 = spec.update(2, [('req', self.left3), ('gnt', self.right3)])
        out4 = spec.update(3, [('req', self.left4), ('gnt', self.right4)])
        out5 = spec.update(4, [('req', self.left5), ('gnt', self.right5)])

        self.assertEqual(out1, -80, "input 1")
        self.assertEqual(out2, -1, "input 2")
        self.assertEqual(out3, -12, "input 3")
        self.assertEqual(out4, -1, "input 4")
        self.assertEqual(out5, 0, "input 5")

    def test_xor(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req xor gnt'

        spec.parse();

        out1 = spec.update(0, [('req', self.left1), ('gnt', self.right1)])
        out2 = spec.update(1, [('req', self.left2), ('gnt', self.right2)])
        out3 = spec.update(2, [('req', self.left3), ('gnt', self.right3)])
        out4 = spec.update(3, [('req', self.left4), ('gnt', self.right4)])
        out5 = spec.update(4, [('req', self.left5), ('gnt', self.right5)])

        self.assertEqual(out1, 80, "input 1")
        self.assertEqual(out2, 1, "input 2")
        self.assertEqual(out3, 12, "input 3")
        self.assertEqual(out4, 1, "input 4")
        self.assertEqual(out5, 0, "input 5")

    def test_implies(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req -> gnt'

        spec.parse();

        out1 = spec.update(0, [('req', self.left1), ('gnt', self.right1)])
        out2 = spec.update(1, [('req', self.left2), ('gnt', self.right2)])
        out3 = spec.update(2, [('req', self.left3), ('gnt', self.right3)])
        out4 = spec.update(3, [('req', self.left4), ('gnt', self.right4)])
        out5 = spec.update(4, [('req', self.left5), ('gnt', self.right5)])

        self.assertEqual(out1, 20, "input 1")
        self.assertEqual(out2, 1, "input 2")
        self.assertEqual(out3, 10, "input 3")
        self.assertEqual(out4, 4, "input 4")
        self.assertEqual(out5, 1, "input 5")

    def test_always_without_pastify(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = always(req)'

        spec.parse()

        self.assertRaises(rtamt.LTLNotImplementedException, spec.update, 0, [('req', self.left1)])

    def test_always_with_pastify(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = always(req)'

        spec.parse()

        self.assertRaises(rtamt.LTLPastifyException, spec.pastify)

    def test_eventually_without_pastify(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = eventually(req)'

        spec.parse()

        self.assertRaises(rtamt.LTLNotImplementedException, spec.update, 0, [('req', self.left1)])

    def test_eventually_with_pastify(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = eventually(req)'

        spec.parse()

        self.assertRaises(rtamt.LTLPastifyException, spec.pastify)

    def test_historically(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = historically(req)'

        spec.parse();

        out1 = spec.update(0, [('req', self.left1)])
        out2 = spec.update(1, [('req', self.left2)])
        out3 = spec.update(2, [('req', self.left3)])
        out4 = spec.update(3, [('req', self.left4)])
        out5 = spec.update(4, [('req', self.left5)])

        self.assertEqual(out1, 100, "input 1")
        self.assertEqual(out2, -1, "input 2")
        self.assertEqual(out3, -2, "input 3")
        self.assertEqual(out4, -2, "input 4")
        self.assertEqual(out5, -2, "input 5")

    def test_once(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = once(req)'

        spec.parse();

        out1 = spec.update(0, [('req', self.left1)])
        out2 = spec.update(1, [('req', self.left2)])
        out3 = spec.update(2, [('req', self.left3)])
        out4 = spec.update(3, [('req', self.left4)])
        out5 = spec.update(4, [('req', self.left5)])

        self.assertEqual(out1, 100, "input 1")
        self.assertEqual(out2, 100, "input 2")
        self.assertEqual(out3, 100, "input 3")
        self.assertEqual(out4, 100, "input 4")
        self.assertEqual(out5, 100, "input 5")

    def test_since(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req since gnt'

        spec.parse();

        out1 = spec.update(0, [('req', self.left1), ('gnt', self.right1)])
        out2 = spec.update(1, [('req', self.left2), ('gnt', self.right2)])
        out3 = spec.update(2, [('req', self.left3), ('gnt', self.right3)])
        out4 = spec.update(3, [('req', self.left4), ('gnt', self.right4)])
        out5 = spec.update(4, [('req', self.left5), ('gnt', self.right5)])

        self.assertEqual(out1, 20, "input 1")
        self.assertEqual(out2, -1, "input 2")
        self.assertEqual(out3, 10, "input 3")
        self.assertEqual(out4, 5, "input 4")
        self.assertEqual(out5, -1, "input 5")

    def test_until_without_pastify(self):
        spec = rtamt.LTLDiscreteTimeSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req until gnt'

        spec.parse()

        self.assertRaises(rtamt.LTLNotImplementedException, spec.update, 0, [('req', self.left1), ('gnt', self.right1)])

    def test_always_with_pastify(self):
        spec = rtamt.LTLDiscreteTimeSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req until gnt'

        spec.parse()

        self.assertRaises(rtamt.LTLPastifyException, spec.pastify)

    def test_not(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = not(req)'

        spec.parse();

        out1 = spec.update(0, [('req', self.left1)])
        out2 = spec.update(1, [('req', self.left2)])
        out3 = spec.update(2, [('req', self.left3)])
        out4 = spec.update(3, [('req', self.left4)])
        out5 = spec.update(4, [('req', self.left5)])

        self.assertEqual(out1, -100, "input 1")
        self.assertEqual(out2, 1, "input 2")
        self.assertEqual(out3, 2, "input 3")
        self.assertEqual(out4, -5, "input 4")
        self.assertEqual(out5, 1, "input 5")

    def test_rise(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = rise(req)'

        spec.parse();

        out1 = spec.update(0, [('req', self.left1)])
        out2 = spec.update(1, [('req', self.left2)])
        out3 = spec.update(2, [('req', self.left3)])
        out4 = spec.update(3, [('req', self.left4)])
        out5 = spec.update(4, [('req', self.left5)])

        self.assertEqual(out1, 100, "input 1")
        self.assertEqual(out2, -100, "input 2")
        self.assertEqual(out3, -2, "input 3")
        self.assertEqual(out4, 2, "input 4")
        self.assertEqual(out5, -5, "input 5")

    def test_fall(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = fall(req)'

        spec.parse();

        out1 = spec.update(0, [('req', self.left1)])
        out2 = spec.update(1, [('req', self.left2)])
        out3 = spec.update(2, [('req', self.left3)])
        out4 = spec.update(3, [('req', self.left4)])
        out5 = spec.update(4, [('req', self.left5)])

        self.assertEqual(out1, -100, "input 1")
        self.assertEqual(out2, 1, "input 2")
        self.assertEqual(out3, -1, "input 3")
        self.assertEqual(out4, -5, "input 4")
        self.assertEqual(out5, 1, "input 5")


    def test_predicate_leq(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req <= gnt'

        spec.parse();

        out1 = spec.update(0, [('req', self.left1), ('gnt', self.right1)])
        out2 = spec.update(1, [('req', self.left2), ('gnt', self.right2)])
        out3 = spec.update(2, [('req', self.left3), ('gnt', self.right3)])
        out4 = spec.update(3, [('req', self.left4), ('gnt', self.right4)])
        out5 = spec.update(4, [('req', self.left5), ('gnt', self.right5)])

        self.assertEqual(out1, -80, "input 1")
        self.assertEqual(out2, -1, "input 2")
        self.assertEqual(out3, 12, "input 3")
        self.assertEqual(out4, -1, "input 4")
        self.assertEqual(out5, 0, "input 5")

    def test_predicate_less(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req < gnt'

        spec.parse();

        out1 = spec.update(0, [('req', self.left1), ('gnt', self.right1)])
        out2 = spec.update(1, [('req', self.left2), ('gnt', self.right2)])
        out3 = spec.update(2, [('req', self.left3), ('gnt', self.right3)])
        out4 = spec.update(3, [('req', self.left4), ('gnt', self.right4)])
        out5 = spec.update(4, [('req', self.left5), ('gnt', self.right5)])

        self.assertEqual(out1, -80, "input 1")
        self.assertEqual(out2, -1, "input 2")
        self.assertEqual(out3, 12, "input 3")
        self.assertEqual(out4, -1, "input 4")
        self.assertEqual(out5, 0, "input 5")

    def test_predicate_geq(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req >= gnt'

        spec.parse();

        out1 = spec.update(0, [('req', self.left1), ('gnt', self.right1)])
        out2 = spec.update(1, [('req', self.left2), ('gnt', self.right2)])
        out3 = spec.update(2, [('req', self.left3), ('gnt', self.right3)])
        out4 = spec.update(3, [('req', self.left4), ('gnt', self.right4)])
        out5 = spec.update(4, [('req', self.left5), ('gnt', self.right5)])

        self.assertEqual(out1, 80, "input 1")
        self.assertEqual(out2, 1, "input 2")
        self.assertEqual(out3, -12, "input 3")
        self.assertEqual(out4, 1, "input 4")
        self.assertEqual(out5, 0, "input 5")

    def test_predicate_greater(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req > gnt'

        spec.parse();

        out1 = spec.update(0, [('req', self.left1), ('gnt', self.right1)])
        out2 = spec.update(1, [('req', self.left2), ('gnt', self.right2)])
        out3 = spec.update(2, [('req', self.left3), ('gnt', self.right3)])
        out4 = spec.update(3, [('req', self.left4), ('gnt', self.right4)])
        out5 = spec.update(4, [('req', self.left5), ('gnt', self.right5)])

        self.assertEqual(out1, 80, "input 1")
        self.assertEqual(out2, 1, "input 2")
        self.assertEqual(out3, -12, "input 3")
        self.assertEqual(out4, 1, "input 4")
        self.assertEqual(out5, 0, "input 5")

    def test_predicate_eq(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req == gnt'

        spec.parse();

        out1 = spec.update(0, [('req', self.left1), ('gnt', self.right1)])
        out2 = spec.update(1, [('req', self.left2), ('gnt', self.right2)])
        out3 = spec.update(2, [('req', self.left3), ('gnt', self.right3)])
        out4 = spec.update(3, [('req', self.left4), ('gnt', self.right4)])
        out5 = spec.update(4, [('req', self.left5), ('gnt', self.right5)])

        self.assertEqual(out1, -80, "input 1")
        self.assertEqual(out2, -1, "input 2")
        self.assertEqual(out3, -12, "input 3")
        self.assertEqual(out4, -1, "input 4")
        self.assertEqual(out5, 0, "input 5")

    def test_predicate_neq(self):
        spec = rtamt.LTLDiscreteTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req !== gnt'

        spec.parse();

        out1 = spec.update(0, [('req', self.left1), ('gnt', self.right1)])
        out2 = spec.update(1, [('req', self.left2), ('gnt', self.right2)])
        out3 = spec.update(2, [('req', self.left3), ('gnt', self.right3)])
        out4 = spec.update(3, [('req', self.left4), ('gnt', self.right4)])
        out5 = spec.update(4, [('req', self.left5), ('gnt', self.right5)])

        self.assertEqual(out1, 80, "input 1")
        self.assertEqual(out2, 1, "input 2")
        self.assertEqual(out3, 12, "input 3")
        self.assertEqual(out4, 1, "input 4")
        self.assertEqual(out5, 0, "input 5")

if __name__ == '__main__':
    unittest.main()