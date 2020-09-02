import configparser
import unittest
import pandas as pd
import glob
import json

from Queries.test_diksha_table import DikshaTableReport
from reuse_func import cqube
from get_dir import pwd

p = pwd()
config = configparser.ConfigParser()
config.read(p.get_json_data_ini_path())


class DikshaTable(unittest.TestCase):
    def setUp(self):
        con = cqube()
        self.connection = con.connect_to_postgres()

    def test_course(self):
        print("")
        course = DikshaTableReport()
        df1 = pd.read_sql_query(course.course_last_7_days, self.connection)
        df1=df1[['district_id', 'district_name', 'course', 'content_name',
       'total_content_plays', 'content_id', 'subject', 'grade', 'medium']]
        df1.sort_values(by=['district_id'], inplace=True)
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        path = config['jsondata']['table_reports_course_last_7_days']
        files = glob.glob(path)
        list = []
        for f1 in files:
            with open(f1, "r") as file:
                json_data = json.load(file)
                for x in json_data:
                    list.append(x)

        # print(list)
        df2 = pd.DataFrame(list)
        df2 = df2[['district_id', 'district_name', 'course', 'content_name',
                   'total_content_plays', 'content_id', 'subject', 'grade', 'medium']]
        df2.sort_values(by=['district_id'], inplace=True)
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        df_diff = pd.concat([df1, df2]).drop_duplicates(keep=False)
        assert df_diff.empty , "Found difference between s3 bucket metrics and the metrics generated outside cqube for diksha table "
        print("No Difference between s3 bucket metrics and the metrics generated outside cqube for diksha table")

    def tearDown(self):
        self.connection.close()
