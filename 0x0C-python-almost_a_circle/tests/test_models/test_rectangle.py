#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
'''
    defining class TestRectangle
'''


class test_rectangle(unittest.TestCase):
    '''
        class to test rectangle
    '''

    def test_startup(self):
        '''
        intialize instance width and height
        '''
        self.rec = Rectangle(4, 5)

    def test_teardown(self):
        '''
            delete created instances
        '''
        self.rec = Rectangle(4, 5)
        del self.rec

    def test_width(self):
        '''
            testing rectangles width getter
        '''
        self.rec = Rectangle(4, 5)
        self.assertEqual(4, self.rec.width)

    def test_height(self):
        '''
            testing rectangles height getter
        '''
        self.rec = Rectangle(4, 5)
        self.assertEqual(5, self.rec.height)

    def test_x(self):
        '''
            testing rectangle x getter
        '''
        self.rec = Rectangle(4, 5, 32)
        self.assertEqual(32, self.rec.x)

    def test_y(self):
        '''
            testing rectangles y getter
        '''
        self.rec = Rectangle(4, 5, 32, 64)
        self.assertEqual(64, self.rec.y)

    def test_width_type(self):
        '''
            testing when string recived by width
        '''
        with self.assertRaises(TypeError):
            r = Rectangle("4", 5)

    def test_width_boo(self):
        '''
            let me test when bool passed to width
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(True, 5)

    def test_width_all(self):
        '''
            test when width over passed
        '''
        with self.assertRaises(TypeError):
            r = Rectangle((1, 2), 5)

    def test_height_type(self):
        '''
            test when string passed to height
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(4, "5")

    def test_height_boo(self):
        '''
            check for typeerror when boolean passed
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(4, True)

    def test_height_all(self):
        '''
            check when another over data passed
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(4, [1, 2])

    def test_x_type(self):
        '''
            test x when string passed
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(4, 5, "32")

    def test_x_boo(self):
        '''
            test when x passed as bool
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(4, 5, True)

    def test_x_all(self):
        '''
            test when over passed
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(4, 5, [1, 2])

    def test_y_type(self):
        '''
            test when string passed as y
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(4, 5, 32, "64")

    def test_y_boo(self):
        '''
            test when y passed as bool
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(4, 5, 32, True)

    def test_y_all(self):
        '''
            test when over passed
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(4, 5, 32, [64, 65])

    def test_width_val(self):
        '''
            test value of width
        '''
        with self.assertRaises(ValueError):
            r = Rectangle(-4, 5)

    def test_height_val(self):
        '''
            test value of height
        '''
        with self.assertRaises(ValueError):
            r = Rectangle(4, -5)

    def test_x_val(self):
        '''
            test value of x
        '''
        with self.assertRaises(ValueError):
            r = Rectangle(4, 5, -32)

    def test_y_val(self):
        '''
            test value of y
        '''
        with self.assertRaises(ValueError):
            r = Rectangle(4, 5, 32, -64)

    def test_width_zero_val(self):
        '''
            test when width is zero
        '''
        with self.assertRaises(ValueError):
            r = Rectangle(0, 5)

    def test_height_zero_val(self):
        '''
            test when height is zero
        '''
        with self.assertRaises(ValueError):
            r = Rectangle(4, 0)

    def test_x_zero_val(self):
        '''
            test when x is zero
        '''
        self.r = Rectangle(4, 5, 0)
        self.assertEqual(0, self.r.x)

    def test_y_zero_val(self):
        '''
            test when y is zero
        '''
        self.r = Rectangle(4, 5, 32, 0)
        self.assertEqual(0, self.r.y)

    def test_width_float(self):
        '''
            check when width is float
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(4.5, 5)

    def test_height_float(self):
        '''
            check when height is float
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(4, 5.05)

    def test_x_float(self):
        '''
            check when x is float
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(4, 5, 32.05)

    def test_y_float(self):
        '''
            check when y is float
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(4, 5, 32, 64.44)

    def test_area(self):
        '''
            testing area funtion
        '''
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.area(), 50)
        r = Rectangle(4, 5, 18, 18, 3)
        self.assertEqual(r.area(), 4 * 5)

    def test_str_load(self):
        r = Rectangle(4, 5, 32, 64, 89)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 32/64 - 4/5")

    def test_update_id(self):
        '''
            testing when id updated
        '''
        r = Rectangle(4, 5)
        r.update(44, 55)
        self.assertEqual(r.id, 44)

    def test_update_width(self):
        '''
            testing when width updated
        '''
        r = Rectangle(89, 4, 5)
        r.update(88, 6, 7)
        self.assertEqual(r.width, 6)

    def test_update_height(self):
        '''
            testing when height updated
        '''
        r = Rectangle(89, 4, 5, 67)
        r.update(88, 6, 7, 77)
        self.assertEqual(r.height, 7)

    def test_update_x(self):
        '''
            testing when x updated
        '''
        r = Rectangle(89, 4, 5, 67, 80)
        r.update(88, 6, 7, 77, 90)
        self.assertEqual(r.x, 77)

    def test_update_y(self):
        '''
            testing when y updated
        '''
        r = Rectangle(89, 4, 5, 67, 80)
        r.update(88, 6, 7, 77, 90)
        self.assertEqual(r.y, 90)

    def test_update_dict(self):
        '''
            testing update with **kwargs
        '''
        r = Rectangle(89, 4, 5, 32, 64)
        r.update(y=55, width=7, height=12, id=88)
        self.assertEqual(88, r.id)
        self.assertEqual(12, r.height)
        self.assertEqual(7, r.width)
        self.assertEqual(55, r.y)
        self.assertEqual(5, r.x)

    def test_to_dict(self):
        '''
            test type which returned from method to_dictionary
        '''
        r = Rectangle(5, 4)
        self.assertEqual(type(r.to_dictionary()), dict)

    def test_to_dict_val(self):
        '''
            test whether method is working propely
        '''
        r = Rectangle(4, 5, 0, 0, 400)
        to_be_tested_dict = r.to_dictionary()
        expected_dict = {'id': 400, 'width': 4, 'height': 5, 'x': 0, 'y': 0}
        self.assertEqual(to_be_tested_dict, expected_dict)

        def test_saving_file(self):
            '''
                test saving a file into json format
            '''
            try:
                os.remove("Rectangle.json")
            except:
                pass
            r = Rectangle(4, 5, 0, 0, 89)
            Rectangle.save_to_file([r])

            with open("Rectangle.json", "r") as file:
                c = file.read()
            ex = [{"x": 0, "y": 0, "id": 89, "height": 5, "width": 4}]
            self.assertEqual(ex, json.loads(c))

        def test_save_no_itera(self):
            '''
                test when non iterable to the function
            '''
            with self.assertRaises(TypeError):
                Rectangle.save_to_file(self.r)

        def test_display(self):
            '''
                test display function
            '''
            r = Rectangle(3, 2)
            ex = "###\n###\n"
            with patch('sys.stdout', new = stringIO()) as fake_out:
                r.display()
                self.assertEqual(fake_out.getvalue(), ex)
