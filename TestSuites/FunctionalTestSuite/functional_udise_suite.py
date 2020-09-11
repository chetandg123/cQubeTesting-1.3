from UDISE.UDISE_map_report import  udise_regression_testing
from get_dir import pwd
import unittest
from HTMLTestRunner import HTMLTestRunner



class MyTestSuite(unittest.TestCase):


    def test_Issue(self):

            functional_test = unittest.TestSuite()
            functional_test.addTests([
                # file name .class name
                unittest.defaultTestLoader.loadTestsFromTestCase(udise_regression_testing.cQube_udise_Report),

            ])
            p= pwd()
            outfile = open(p.get_functional_report_path(), "w")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Admin console Regression Test Report',
                verbosity=1,
            )

            runner1.run(functional_test)
            outfile.close()


    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()