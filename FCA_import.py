# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd

FCA_field_names =  [' Firm Ref ',' Registered Firm Name ',' Firm Legal Status Type code ', ' Firm Type code ', ' Authority To Hold Client  Money ', ' Principal Address Line 1', ' Principal Address Line 2', ' Principal Address Line 3', ' Principal Address Line 4', ' Principal Address Line 5', ' Principal Address Line 6', ' Post Code Out ', ' Post Code In ', ' Telephone No  Country Prefix ', ' Telephone No  Area Code ', ' Telephone No  Local Number ', ' Fax  Country Prefix ', ' Fax  Area Code ', 'Fax  Local Number', ' Current Authorisation Status code ', ' Date Status Last Changed ', ' Date first Authorised by Regulator ', ' Sort Key', ' Last Update Date ', 'Y']

dateparse = lambda x: pd.datetime.strptime(x, '%Y%m%d')
my_dat = pd.read_table(r'\\NDATA13\thomai$\My Documents\Temp FCA\firms20160107.ext', skiprows=1, header=None, delimiter='|', error_bad_lines = False, warn_bad_lines = True, skipfooter =1, names = FCA_field_names, parse_dates= [' Date Status Last Changed ', ' Date first Authorised by Regulator ', ' Last Update Date '], date_parser=dateparse )
