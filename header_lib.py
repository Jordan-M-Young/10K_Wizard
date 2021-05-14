# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 09:22:31 2021

@author: jmyou
"""


class Header_Lib():
    """Library containing all known 10-K document headers that tell a viewer
    by what number the listed shares and USD values should be multiplied by
    
    For example: 'Shares in thousands, $ USD in millions' tells the viewer
    to multiply all share based figures by 1000 and all figures in USD units
    by 1000000.
    """
    
    def __init__(self):
        super().__init__()
        
        self.no_mult_headers = [
                       'Document and Entity Information (USD $)',
                       'Document and Entity Information (USD $)',
                       'Document and Entity Information (USD  $)',
                       'Document And Entity Information - USD ($)',
                       'Statement Of Financial Position Classified (USD $)',
                       'Statement Of Income (USD $)',
                       'Document and Entity Information (USD  $)',
                       'Document and Entity Information - USD ($)',
                       'Document And Entity Information (USD $)',
                       'Consolidated Balance Sheets (USD $)',
                       'CONSOLIDATED BALANCE SHEETS (USD $)']

        
        self.mil_thous_headers = [
               'Document and Entity Information - USD ($) shares in Thousands, $ in Millions',
               'Cover Page - USD ($) shares in Thousands, $ in Millions'
               ]

    
    
        self.thous_zero_headers = [
                          'Document and Entity Information - USD ($) $ in Thousands',
                          'Consolidated Balance Sheets - USD ($) $ in Thousands',
                          'In Thousands, unless otherwise specified',
                          'In Thousands, except Per Share',
                          'In Thousands, except Per Share data',
                          'In Thousands',
                          'CONSOLIDATED BALANCE SHEETS - USD ($) $ in Thousands']

    
        self.mil_zero_headers = [
                        'Document and Entity Information - USD ($) $ in Millions',
                        'Document And Entity Information - USD ($) $ in Millions',
                        'Cover Page - USD ($) $ in Millions'
                        ]
    
        self.bil_zero_headers = [
                        'USD ($) $ in Billions',
                        'Document and Entity Information - USD ($) $ in Billions',
                        'Cover - USD ($) $ in Billions'
                        ]
        

class Basic_Info_Lib():
    """Library for all the relevant keys used to access data stored in 
    pandas dataframe representations of each 10-K excel workbook's' 
    'Document and Entity Information' sheet
    """
    
    def _init__(self):
        super().__init__()
        
        self.pub_flt_keys = ['Entity Public Float',
                             'Entity public float']
        
        self.flr_cat = ['Entity Filer Category',
                        'Entity filer category']


class Parser_Lib():
    """Contains all relevant keys and headers for accessing data stored within
    the parsed 10-k documents"""
    
    def __init__(self):
        super().__init__()
        
        self.header_lib = Header_Lib()
        
        self.basic_info_lib = Basic_Info_Lib()
