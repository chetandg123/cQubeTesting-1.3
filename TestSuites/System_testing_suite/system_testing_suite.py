import time
import unittest
from HTMLTestRunner import HTMLTestRunner

from CRC import crc_report_system_testing
from Diksha_Reports.Diksha_charts import diksha_chart_system_testing
from Diksha_Reports.Diksha_column_chart import column_system_testing
from Diksha_Reports.Diksha_table_report import diksha_table_system_testing
from Login import login_page
from SAR import student_attendance_system_testing
from SI.MAP import school_map_system_testing
from SI.Report import school_report_system_testing
from SR import semester_report_system_testing
from Semester_Exception import exception_system_testing
from Telemetry import telemetry_system_testing
from get_dir import pwd
from reuse_func import GetData


class MyTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(100)
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)


    def test_issue01(self):
        system_test = unittest.TestSuite()
        system_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(login_page.login),
        ])
        p = pwd()
        outfile = open(p.get_system_report_path(), "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='login to cQube system Test Report',
            verbosity=1,

        )
        runner1.run(system_test)
        outfile.close()

    def test_issue03(self):
        self.data.navigate_to_student_report()
        time.sleep(3)
        self.errMsg = self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the student attendance report page")
        else:
            system_test = unittest.TestSuite()
            system_test.addTests([
                # file name .class name
                unittest.defaultTestLoader.loadTestsFromTestCase(student_attendance_system_testing.cQube_Student_Attendance),
            ])
            p = pwd()
            outfile = open(p.get_system_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Student Attendance System Test Report',
                verbosity=1,

            )

            runner1.run(system_test)
            outfile.close()

    def test_issue04(self):
        self.data.navigate_to_crc_report()
        time.sleep(3)
        self.errMsg = self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the crc report page")
        else:
            system_test = unittest.TestSuite()
            system_test.addTests([
                # file name .class name
                unittest.defaultTestLoader.loadTestsFromTestCase(crc_report_system_testing.crc_System_Testing),
            ])
            p = pwd()
            outfile = open(p.get_system_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='CRC System Test Report',
                verbosity=1,

            )

            runner1.run(system_test)
            outfile.close()

    def test_issue05(self):
        self.data.navigate_to_semester_report()
        time.sleep(3)
        self.errMsg = self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the semester report page")
        else:
            system_test = unittest.TestSuite()
            system_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(semester_report_system_testing.cQube_Semester_Report),
            ])
            p = pwd()
            outfile = open(p.get_system_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Semester System Test Report',
                verbosity=1,

            )

            runner1.run(system_test)
            outfile.close()

    def test_issue06(self):
        self.data.navigate_to_school_infrastructure_map()
        time.sleep(3)
        self.errMsg = self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the school infra map report page")
        else:
            system_test = unittest.TestSuite()
            system_test.addTests([
                # file name .class name
                unittest.defaultTestLoader.loadTestsFromTestCase(school_map_system_testing.cQube_SI_Map_Report),

            ])
            p = pwd()
            outfile = open(p.get_system_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='School Infrastructure Map system Test Report',
                verbosity=1,

            )

            runner1.run(system_test)
            outfile.close()

    def test_issue07(self):
        self.data.navigate_to_school_infrastructure()
        time.sleep(3)
        self.errMsg = self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the school infra report page")
        else:
            system_test = unittest.TestSuite()
            system_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(school_report_system_testing.cQube_SI_Report)
            ])
            p = pwd()
            outfile = open(p.get_system_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='School Infrastructre scattor plot system Report',
                verbosity=1,

            )

            runner1.run(system_test)
            outfile.close()

    def test_issue08(self):

            system_test = unittest.TestSuite()
            system_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(diksha_chart_system_testing.cQube_diskha_chart)
            ])
            p = pwd()
            outfile = open(p.get_system_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Diksha chart system Test Report',
                verbosity=1,

            )

            runner1.run(system_test)
            outfile.close()

    def test_issue09(self):

            system_test = unittest.TestSuite()
            system_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(diksha_table_system_testing.cQube_diskha_regression)
            ])
            p = pwd()
            outfile = open(p.get_system_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Diksha Table system Test Report',
                verbosity=1,

            )

            runner1.run(system_test)
            outfile.close()

    def test_issue10(self):

            system_test = unittest.TestSuite()
            system_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(column_system_testing.cQube_diskha_column_report)
            ])
            p = pwd()
            outfile = open(p.get_system_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Diksha column system Test Report',
                verbosity=1,

            )

            runner1.run(system_test)
            outfile.close()

    def test_issue11(self):

            system_test = unittest.TestSuite()
            system_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(exception_system_testing.cQube_semester_exception_report)
            ])
            p = pwd()
            outfile = open(p.get_system_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Semester Exception system Test Report',
                verbosity=1,

            )

            runner1.run(system_test)
            outfile.close()

    def test_issue12(self):

            system_test = unittest.TestSuite()
            system_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    telemetry_system_testing.Test_Telemetry)
            ])
            p = pwd()
            outfile = open(p.get_system_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Telemetry system Test Report',
                verbosity=1,

            )

            runner1.run(system_test)
            outfile.close()

    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
