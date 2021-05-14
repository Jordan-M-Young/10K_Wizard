# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 09:22:31 2021

@author: jmyou
"""


class Mult_Header_Lib():
    """Library containing all known 10-K document dollar / share multiplier
    headers. These phrases tell a viewer by what number the listed shares 
    and USD values should be multiplied by
    
    For example: 'Shares in thousands, $ USD in millions' tells the viewer
    to multiply all listed share-based figures by 1000 and all figures in 
    USD units by 1000000.
    """
    
    def __init__(self):
        super().__init__()
        

        
        """These headers let a viewer know that share / dollar value
        only needs to be multiplied by one"""
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
            'Document and Enitity Information - USD ($)',
            'Document and Entity Information Document and Entity Information - USD ($)',
            'Document and Entity Information Document and Entity Information (USD $)',
            'Consolidated Balance Sheets (USD $)', 
            'CONSOLIDATED BALANCE SHEETS (USD $)', 
            'CONSOLIDATED BALANCE SHEETS (USD $)', 
            'CONSOLIDATED BALANCE SHEETS (USD \xa0$)', 
            'CONSOLIDATED BALANCE SHEETS (USD  $)',
            'Current assets',
            'Current assets:',
            'CONSOLIDATED BALANCE SHEETS - USD ($)',
            'Consolidated Balance Sheets - USD ($)',
            'BALANCE SHEETS (USD $)',
            'Document and Entity Information (USD  $)',
            'Document and Entity Information (USD  $)',
            'Document and Entity Information Document - USD ($)',
            'Document and Entity Information Document (USD $)',
            'Document and Company Information (USD $)',
            'Assets',
            'ASSETS',
            'CURRENT ASSETS',
            'Current Assets:',
            'Cover Page - USD ($)',
            'Cover Page - USD ($)',
            'DEI Parenthetical (USD $)',
            'Cover - USD ($)',
            'Statement of Financial Position [Abstract]',
            'DEI Document - USD ($)',
            'DOCUMENT AND ENTITY INFORMATION DOCUMENT Document and Entity Information Document (USD $)',
            'Balance Sheets - USD ($)',
            'CONSOLIDATED STATEMENTS OF CONDITION - USD ($)',
            'Consolidated Statements of Condition (USD $)',
            'CONDENSED CONSOLIDATED BALANCE SHEETS (USD $)',
            'Equity Method Investments [Member]',
            'Balance Sheets (USD $)',
            'Current Assets',
            'Consolidated Balance Sheets(USD ($))',
            'BALANCE SHEETS - USD ($)',
            'Document - USD ($)',
            'Consolidated Balance Sheet (USD $)',
            'Consolidated Statements of Financial Position (USD $)',
            "Condensed Consolidated Balance Sheets - USD ($)",
            'Cover page - USD ($)',
            'Assets:',
            'Cash and Cash Equivalents',
            "Document Information",
            "CURRENT ASSETS:",
            "CONSOLIDATED BALANCE SHEET - USD ($)",
            "Balance Sheet",
            "COMBINED AND CONSOLIDATED BALANCE SHEETS - USD ($)",
            "Statement Of Income Alternative (USD $)",
            "Statement Of Cash Flows Indirect (USD $)",
            "CONDENSED BALANCE SHEETS (USD $)",
            "AUDITED CONDENSED CONSOLIDATED BALANCE SHEETS - USD ($)",
            "AUDITED CONDENSED CONSOLIDATED TRANSITION BALANCE SHEETS - USD ($)",
            "CONSOLIDATED BALANCE SHEET (Unaudited) (USD $)"]


        """These headers tell a viewer to multiply share figures by 1,000
        and dollar values by 1,000,000"""
        self.mil_thous_headers = [
            'Document and Entity Information - USD ($) shares in Thousands, $ in Millions',
            'Cover Page - USD ($) shares in Thousands, $ in Millions'
            ]

    
        """These hedaers tell a viewer to multiply dollar figures by 1,000
        and share figures by one"""
        self.thous_zero_headers = [
            'Document and Entity Information - USD ($) $ in Thousands',
            'Consolidated Balance Sheets - USD ($) $ in Thousands',
            'In Thousands, unless otherwise specified',
            'In Thousands, except Per Share',
            'In Thousands, except Per Share data',
            'In Thousands',
            'In Thousands, except Share data, unless otherwise specified',
            'CONSOLIDATED BALANCE SHEETS - USD ($) $ in Thousands',
            'BALANCE SHEETS - USD ($) $ in Thousands',
            'Document And Entity Information - USD ($) $ in Thousands',
            'CONSOLIDATED STATEMENTS OF CONDITION - USD ($) $ in Thousands',
            'Balance Sheets - USD ($) $ in Thousands',
            'CONSOLIIDATED BALANCE SHEETS - USD ($) $ in Thousands',
            'Consolidated Balance Sheets - Successor [Member] - USD ($) $ in Thousands',
            'Consolidated Balance Sheet - USD ($) $ in Thousands',
            'Consolidated Statements of Financial Position - USD ($) $ in Thousands',
            'CONSOLIDATED AND COMBINED BALANCE SHEETS - USD ($) $ in Thousands',
            'Condensed Consolidated Balance Sheets - USD ($) $ in Thousands',
            "Consolidated balance sheets - USD ($) $ in Thousands",
            "CONSOLIDATED BALANCE SHEET - USD ($) $ in Thousands",
            "CONDENSED CONSOLIDATED BALANCE SHEETS - USD ($) $ in Thousands",
            "CONSOLIDATED AND COMBINED BALANCE SHEET - USD ($) $ in Thousands",
            "CONSOLIDATED BALANCE SHEET (Unaudited) - USD ($) $ in Thousands"
            ]


        """These headers tell a viewer to multiply dollar values by
        1,000,000 and share values by 1"""
        self.mil_zero_headers = [
            'Document and Entity Information - USD ($) $ in Millions',
            'Document And Entity Information - USD ($) $ in Millions',
            'Cover Page - USD ($) $ in Millions',
            'CONSOLIDATED BALANCE SHEETS - USD ($) $ in Millions',
            'In Millions',
            'In Millions, unless otherwise specified',
            'In Millions, except Share data, unless otherwise specified',
            'Document and Entity Information Document and Entity Information - USD ($) $ in Millions',
            'Cover Page Cover Page - USD ($) $ in Millions',
            'Consolidated Balance Sheets - USD ($) $ in Millions',
            'In Millions, except Per Share data',
            'Cover - USD ($) $ in Millions',
            'Document Entity Information Document - USD ($) $ in Millions',
            'Document Entity Information - USD ($) $ in Millions',
            "Document and Entity Information Document - USD ($) $ in Millions",
            "Document and Entity Information - USD ($) $ / shares in Units, $ in Millions",
            "Consolidated Balance Sheets Consolidated Balance Sheets - USD ($) $ in Millions"
            ]
    
        """These headers tell a viewer to multiply dollar values by
        1,000,000,000 and share values by one."""
        self.bil_zero_headers = [
            'USD ($) $ in Billions',
            'Document and Entity Information - USD ($) $ in Billions',
            'Cover - USD ($) $ in Billions',
            'In Billions, except Share data, unless otherwise specified',
            'Document And Entity Information - USD ($) $ in Billions',
            'Cover Page - USD ($) $ in Billions',
            'Document and Entity Information - USD ($) $ / shares in Units, $ in Billions',
            'DOCUMENT AND ENTITY INFORMATION - USD ($) $ in Billions'
            ]
        

class Basic_Info_Lib():
    """Library for all the relevant keys used to access data stored in 
    pandas dataframe representations of each 10-K excel workbook's' 
    'Document and Entity Information' sheet
    """
    
    def __init__(self):
        super().__init__()
        
        self.pub_flt_keys = ['Entity Public Float',
                             'Entity public float',
                             "Public Float"]
        
        self.flr_cat = ['Entity Filer Category',
                        'Entity filer category']
        
        self.vltry_flr = ['Entity Voluntary Filers',
                          'Is Entity a Voluntary Filer?',
                          'Entity voluntary filers',
                          'Entity Voluntary Filer',
                          'Entity a Voluntary Filer',
                          'Is Entity a Voluntary Filer',
                          "Voluntary Status",
                          "Entity voluntary Filers",
                          "Entity Volunteer Filers"
                          ]
        
        self.ss_iss = ['Entity a Well-known Seasoned Issuer',
                         'Is Entity a Well-known Seasoned Issuer?',
                         'Is Entity a Well-known Seasoned Issuer',
                         'Entity well known seasoned issuer',
                         'Entity Well Known Seasoned Issuer',
                         'Entity Well-known Seasoned Issuer',
                         'Entity Well-known Season Issuer',
                         'Entity Well-Known Seasoned Issuer',
                         'Well Known Seasoned Issuer',
                         "Entity Well-known Seasoned Filer"
                         ]
        
        self.cmn_out_shares = ['Entity Common Stock, Shares Outstanding (in shares)',
                              'Entity Common Stock, Shares Outstanding',
                              'Entity common stock shares outstanding',
                              'Entity Common Stock Shares Outstanding',
                              'Entity Common Stock, Shares Outstanding',
                              'Entity Common Stock, Shares Outstanding (shares)',
                              "Entity Common Stock Shares Outstanding (actual number)",
                              "Entity Common Units Outstanding"
                              ]
        
        self.publ_flt = ['Entity Public Float',
                         'Entity public float',
                         'Entity Public float',
                         "Entity Public Float (actual number)",
                         "Public Float"]
        
        self.filer_cat = ['Entity Filer Category',
                          'Entity filer category']

class Cons_Bal_Sheet_Lib():
    
    def __init__(self):
        super().__init__()
        
        self.ttl_eq = ['Total equity',
                       "Total shareholders' equity",
                       'TOTAL EQUITY',
                       'Total Equity',
                       "Total shareholders’ equity",
                       "TOTAL STOCKHOLDERS' EQUITY",
                       "Total stockholders' equity",
                       "Total stockholders’ equity",
                       "Total stockholdersâ€™ equity",
                       'Total Stockholdersâ€™ Equity',
                       'Total stockholders’ (deficit) equity',
                       'Total stockholders’ deficit',
                       'TOTAL SHAREHOLDERS’ EQUITY',
                       'Total Stockholders’ Equity',
                       "Total stockholders' equity (deficit)",
                       "Total stockholders' equity (deficit)",
                       "Total stockholders’ equity (deficit)",
                       'Total Liabilities and Stockholders’ Deficit',
                       "Total Stockholders' Equity",
                       "Total Stockholders' (Deficit)",
                       "Total stockholders' / members' equity",
                       "Total Shareholdersâ€™ Equity",
                       "Total Shareholders’ Equity",
                       "Total Shareholders' Equity",
                       "Total Shareholders' equity (deficit)",
                       "Total stockholders' deficit",
                       "Total stockholders' (deficit)",
                       "TOTAL SHAREHOLDERS' EQUITY",
                       "TOTAL SHAREHOLDERSâ€™ EQUITY",
                       "Total stockholdersâ€™ equity (deficit)",
                       "Total stockholdersâ€™ deficit",
                       "Total Shareholders' equity",
                       "Total shareholdersâ€™ equity",
                       "Total Shareholdersâ€™ Equity (Deficiency)",
                       "TOTAL STOCKHOLDERS' (DEFICIENCY) EQUITY",
                       "TOTAL STOCKHOLDERS' EQUITY (DEFICIT)",
                       "Total shareholders equity/members (deficit)",
                       "Total liabilities and stockholders' (deficit)/equity",
                       "Total stockholders' (deficit) equity",
                       "Total (deficit) equity",
                       "TOTAL STOCKHOLDERS’ EQUITY",
                       "Total Stockholders’ Equity / (Deficit)",
                       "TOTAL STOCKHOLDERSâ€™ (DEFICIT) EQUITY",
                       "TOTAL STOCKHOLDERSâ€™ EQUITY (DEFICIT)",
                       "TOTAL STOCKHOLDERS’ EQUITY",
                       "TOTAL STOCKHOLDERS’ (DEFICIT) EQUITY",
                       "TOTAL STOCKHOLDERSâ€™ EQUITY",
                       "Total stockholders'/members’ equity",
                       "Total stockholders’/members’ equity",
                       "Total shareholders' equity (deficit)",
                       "Total shareholders' (deficit) equity",
                       "Total Stockholder's Deficit",
                       "Total shareholdersâ€™ equity (deficiency)",
                       "Total Stockholders' Equity/(Deficit)",
                       "Total Stockholders' Equity (Deficit)",
                       "Total Shareholder’s equity",
                       "Total Partners' Capital"]
        
        self.ttl_ass = ['Total assets',
                        'TOTAL ASSETS',
                        'Total Assets',
                        'total assets',
                        'total Assets',
                        'Total Assets'
                        ]
        
        
        self.ttl_lb = ['Total liabilities',
                         'TOTAL LIABILITIES',
                         'Total Liabilities',
                         'total liabilities',
                         'total Liabilities'
                         ]
        
        self.ttl_liab_and_eq = ["Total liabilities and stockholders' equity",
                                "Total liabilities and stockholders' equity",
                                "Total liabilities and stockholders’ equity",
                                "Total Liabilities and Stockholdersâ€™ Equity (Deficit)",
                                'Total Liabilities and Equity',
                                'Total liabilities and shareholders’ equity',
                                "Total liabilities and stockholders' / members' equity",
                                "Total liabilities and stockholders' (deficit) equity",
                                "Total liabilities and stockholders' deficit",
                                "Total liabilities and stockholders’ deficit",
                                "Total liabilities and shareholders' equity (deficit)",
                                "Total liabilities and stockholdersâ€™ equity",
                                'Total shareholdersâ€™ equity (deficiency)',
                                "Total shareholdersâ€™ equity (deficiency)",
                                'Total liabilities and equity',
                                "Total Liabilities and Stockholders’ Equity",
                                "Total Liabilities and Stockholdersâ€™ Equity",
                                "Total liabilities and stockholders' deficit",
                                "Total liabilities and stockholders' equity/(deficit)",
                                "Total liabilities and stockholders'(deficit)",
                                "Total liabilities and stockholders' equity (deficit)",
                                "Total liabilities and stockholders’ equity (deficit)",
                                "Total liabilities and stockholdersâ€™ deficit",
                                'Total stockholdersâ€™ deficit',
                                "Total Liabilities and Equity",
                                "TOTAL LIABILITIES & SHAREHOLDERSâ€™ EQUITY (DEFICIENCY)",
                                "Total liabilities and shareholdersâ€™ equity",
                                "TOTAL LIABILITIES AND STOCKHOLDERS' EQUITY",
                                "TOTAL LIABILITIES AND STOCKHOLDERSâ€™ (DEFICIT) EQUITY",
                                "TOTAL LIABILITIES AND STOCKHOLDERSâ€™ EQUITY (DEFICIT)",
                                "TOTAL LIABILITIES AND STOCKHOLDERS’ EQUITY",
                                "TOTAL LIABILITIES AND STOCKHOLDERS’ EQUITY",
                                "Total liabilities and shareholders' equity",
                                "Total liabilities, non-controlling interest and stockholders' equity",
                                "Total liabilities, non-controlling interest and stockholdersâ€™ equity",
                                "Total liabilities, non-controlling interest and stockholders’ equity",
                                "Total Liabilities and Stockholders' Equity",
                                "Total liabilities and stockholders’ (deficit) equity",
                                "Total liabilities, convertible preferred stock and stockholders’ deficit",
                                "TOTAL LIABILITIES AND STOCKHOLDERSâ€™ EQUITY",
                                "Total Liabilities and Stockholders' Equity/(Deficit)",
                                "TOTAL LIABILITIES AND SHAREHOLDERS' EQUITY",
                                "TOTAL LIABILITIES AND SHAREHOLDERS’ EQUITY",
                                "TOTAL LIABILITIES AND SHAREHOLDERS' EQUITY ",
                                "Total liabilities, preferred stock and stockholders’ equity",
                                "Total liabilities, convertible preferred stock and stockholders’ equity (deficit)",
                                "Total Liabilities and Stockholder's Deficit",
                                "Total Liabilities and Stockholders' Equity (Deficit)",
                                "Liabilities and Shareholders' Equity",
                                "Liabilities and stockholders' equity",
                                "TOTAL LIABILITIES AND PARTNERS' CAPITAL"]

class Sheet_Lib():
    
    
    def __init__(self):
        super().__init__()
        
        
        """Phrases used to access the 'Consolidated Balance Sheet' 
        sheet of a given 10-k document's excel file representation"""
        self.con_bal_sheet = ['CONSOLIDATED BALANCE SHEETS',
                              'Consolidated_Balance_Sheets',
                              'Consolidated_Balance_Sheet',
                              'CONSOLIDATED_BALANCE_SHEETS',
                              'CONSOLIDATED_BALANCE_SHEETS',
                              'CONSOLIIDATED BALANCE SHEETS',
                              'CONSOLIDATED_BALANCE_SHEETS',
                              'CONSOLIDATED_BALANCE_SHEETS',
                              'Statement Of Financial Position',
                              'Consolidated_Balance_Sheets',
                              "CONDENSED_BALANCE_SHEETS",
                              'Consolidated Balance Sheets',
                              'BALANCE_SHEETS',
                              'BALANCE SHEETS',
                              'CONSOLIDATED STATEMENTS OF COND',
                              'Balance Sheets',
                              'CONSOLIDATED AND COMBINED BALAN',
                              'Consolidated_Statements_of_Con',
                              'Balance_Sheets',
                              'CONDENSED_CONSOLIDATED_BALANCE',
                              'Consolidated Balance Sheet',
                              'Consolidated_Statements_of_Fin',
                              "Consolidated Statements of Fina",
                              "Condensed Consolidated Balance ",
                              "Condensed Consolidated Balance",
                              "Consolidated balance sheets",
                              "CONSOLIDATED BALANCE SHEET",
                              "Consolidated Balance Sheets Con",
                              "Balance Sheet",
                              "COMBINED AND CONSOLIDATED BALAN",
                              "Statement_of_Financial_Positio",
                              "CONDENSED CONSOLIDATED BALANCE ",
                              "CONDENSED CONSOLIDATED BALANCE",
                              "AUDITED CONDENSED CONSOLIDATED ",
                              "CONSOLIDATED_BALANCE_SHEET_Una",
                              "CONSOLIDATED BALANCE SHEET (Una"]
        

class Parser_Lib():
    """Contains all relevant keys and headers for accessing data stored within
    the parsed 10-k documents"""
    
    def __init__(self):
        super().__init__()
        
        self.sheet_lib = Sheet_Lib()
        
        self.mult_header_lib = Mult_Header_Lib()
        
        self.basic_info_lib = Basic_Info_Lib()
        
        self.cons_bal_sheet_lib = Cons_Bal_Sheet_Lib()
