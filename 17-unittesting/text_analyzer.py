"""
Unit testing example: text analysis
- TODO:
    - write a simple text-analysis function, which takes file name as its only parameters
    - Calculate: 
        - the number of lines in the file
        - the number of characters in the file
- Note: TDD (Test Driven Development) is a form of software development where tests are written 
first i.e. before you write the actual functionality to be tested.
"""
import os
import unittest

def analyze_text():
    """
    Calculates the number of lines and characters in a file.
    """
    pass

class TextAnalysisTests(unittest.TestCase):
    """
    Test for the ``analyze_text()`` function
    """
    def setUp(self):
        """
        Fixture that creates a file for the text methods to use.
        """
        self.filename = "text_analysis_test_file.txt"
        with open(self.filename, 'w') as file_obj:
            file_obj.write("Hey\nI am learning python programming language")

    def test_function_runs(self):
        """
        Basic smoke test: does the function run.
        """
        analyze_text()
    
    def tearDown(self):
        """
        Fixture that deletes the files used by the test methods
        """
        try:
            os.remove(self.filename)
        except:
            pass
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()