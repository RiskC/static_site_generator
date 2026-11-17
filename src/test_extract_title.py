import unittest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test(self):
        md = """
# Food

pizza
yum

""" 
        check = extract_title(md)
        output = "Food"
        self.assertEqual(check, output)
    
    def test_no_h1(self):
        md ="i like food"
        

        with self.assertRaises(ValueError) as cm:
            extract_title(md)
        self.assertEqual(str(cm.exception), "no h1 header")


    def test_h2(self):
        md = """
## My tummy hurts

"""
        with self.assertRaises(ValueError) as cm:
            extract_title(md)
        self.assertEqual(str(cm.exception), "no h1 header")


if __name__ == "__main__":
    unittest.main()
