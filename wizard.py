# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 10:01:37 2021

@author: jmyou
"""

import xlrd
import os 
import pandas as pd
import sys
import openpyxl
import win32com.client as win32
import math
from parser_lib import Parser_Lib


def open_files(files):
    for file in files:
        file = '/'.join([data_dir,file])
        ext = file.split('.')[len(file.split('.'))-1]
        
        if ext == 'xlsx':
            #for xlsx files
            workbook = pd.read_excel(file)
        elif ext == 'xls':
            # for xls files
            workbook = xlrd.open_workbook(file)
        else:
            file = file.split('/')[-1]
            print('Error: {1} has a {0} extension'.format(ext,file))
        


def get_usd_share_multiplier(header):
    
    
    header2 = header[0]
    header = header.name
    
    m_headers = p_lib.mult_header_lib

    if header in m_headers.no_mult_headers:
        try:
            if math.isnan(float(header2)):
                usd_mult = 1
                sh_mult = 1
                
                
        except ValueError:
            if header2 == '':
                header = header.name
            
            elif header2 in m_headers.no_mult_headers:
                usd_mult = 1
                sh_mult = 1
            
            elif header2 in m_headers.mil_thous_headers:
                usd_mult = 1000000
                sh_mult = 1000
                
            elif header2 in m_headers.thous_zero_headers:
                usd_mult = 1000
                sh_mult = 1
            
            elif header2 in m_headers.mil_zero_headers:
                usd_mult = 1000000
                sh_mult = 1
            elif header2 in m_headers.bil_zero_headers:
                usd_mult = 1000000000
                sh_mult = 1
            else:
                print('hloop1','new usd / share multiplier header found:',header2)
                
                usd_mult = 1
                sh_mult = 1
            
            
        


    elif header in m_headers.mil_thous_headers:
        usd_mult = 1000000
        sh_mult = 1000
        
    elif header in m_headers.thous_zero_headers:
        usd_mult = 1000
        sh_mult = 1
    
    elif header in m_headers.mil_zero_headers:
        usd_mult = 1000000
        sh_mult = 1
    elif header in m_headers.bil_zero_headers:
        usd_mult = 1000000000
        sh_mult = 1
    else:
        print('new usd / share multiplier header found')
        print(header)
        usd_mult = 1
        sh_mult = 1


    return usd_mult,sh_mult



def get_ssnd_iss(b_info):
    
    #relevant keyword library
    s_words = p_lib.basic_info_lib.ss_iss
    
    #checks key word list for the correct key word needed to access
    #the relevant data row
    for word in s_words:
        try:
            ssnd_iss = b_info.loc[word,:]
            break
        except KeyError:
            continue

        
    #grabs data from the accessed row
    try:
        ssnd_iss = ssnd_iss.iloc[0,0] 
    except pd.core.indexing.IndexingError:
        ssnd_iss = ssnd_iss[0]
    

        
        
        
    return ssnd_iss

def get_vltry_flr(b_info):
    
    #relevant keyword library
    v_words = p_lib.basic_info_lib.vltry_flr
    
    #checks key word list for the correct key word needed to access
    #the relevant data row
    for word in v_words:
        try:
            vltry_flr = b_info.loc[word,:]
            break
        except KeyError:
            continue
            
    #grabs data from the accessed row
    try:
        vltry_flr = vltry_flr.iloc[0,0]
    except pd.core.indexing.IndexingError:
        vltry_flr = vltry_flr[0]    
    
    
    
    return vltry_flr

def get_cm_out_shares(b_info):
    
    
    cm_words = p_lib.basic_info_lib.cmn_out_shares
    
    for word in cm_words:
        try:
            cm_out_shares = b_info.loc[word,:]
            break
        except KeyError:
            continue
    
    
    
    try:
        c_out_shares = cm_out_shares.iloc[0,1]
    except pd.core.indexing.IndexingError:
        try:
            c_out_shares = cm_out_shares[1]
        except IndexError:
            c_out_shares = cm_out_shares[0]
    
    if c_out_shares == "'":
    
        try:
            i = 0
            while c_out_shares == "'":
                c_out_shares = cm_out_shares.iloc[0,i]
                i += 1
        
        except IndexError:
            i = 0
            while c_out_shares == "'":
                c_out_shares = cm_out_shares.iloc[i]
                i += 1
            
        except pd.core.indexing.IndexingError:
             i = 0
             while c_out_shares == "'":
                c_out_shares = cm_out_shares.iloc[i]
                i += 1           
            


    return c_out_shares

def get_flr_cat(b_info):
    
    
    flr_words = p_lib.basic_info_lib.filer_cat
    
    for word in flr_words:
        try:
            flr_cat = b_info.loc[word,:]
            break
        except KeyError:
            continue
    
    

    try:
        flr_cat = flr_cat.iloc[0,0]
    except pd.core.indexing.IndexingError:
        flr_cat = flr_cat[0]
        
    
    return flr_cat

def get_pub_flt(b_info):
    
    
    
    pf_words = p_lib.basic_info_lib.publ_flt
    
    for word in pf_words:
        try:
            pub_flt = b_info.loc[word,:]
            break
        except KeyError:
            continue
    
    
    
    try:
        pub_fl = pub_flt.iloc[0,2]
    except IndexError:
        pub_fl = pub_flt[2]
    except pd.core.indexing.IndexingError:
        try:
            pub_fl = pub_flt.iloc[0,1]
        except pd.core.indexing.IndexingError:
            try:
                pub_fl = pub_flt.iloc[0,0]
            except pd.core.indexing.IndexingError:
                try:
                    pub_fl = pub_flt[2]
                except IndexError:
                    try:
                        pub_fl = pub_flt[1]
                    except IndexError:
                        pub_fl = pub_flt[0]
        
    
    if pub_fl == "'":
        try:
            pub_fl = pub_flt.iloc[0,1]
        except pd.core.indexing.IndexingError:
            pub_fl = pub_flt[1]
        
        
    if type(pub_fl) == str:
        if ',' in pub_fl:
            pub_fl = pub_fl.replace(',','')
        if '$' in pub_fl:
            pub_fl = pub_fl.replace('$','')
        if ' ' in pub_fl:
            pub_fl = pub_fl.replace(' ','')
        pub_fl = float(pub_fl)
    
    return pub_fl


def get_basic_info(file,ext,data_dir):

    if ext == 'xlsx':
        #for xlsx files
        ticker = data_dir.split('/')[-1]

        b_info = pd.read_excel(file,sheet_name=0)
        b_info.index = b_info.iloc[:,0]
        b_info = b_info.iloc[:,1:]    
        usd_mult,sh_mult = get_usd_share_multiplier(b_info.index)
        date = b_info.iloc[0,:][0]
        ssnd_iss = get_ssnd_iss(b_info)
        vltry_flr = get_vltry_flr(b_info)
        flr_cat = get_flr_cat(b_info)
        cm_out_shares = get_cm_out_shares(b_info)
        pub_flt = get_pub_flt(b_info)
        
        pub_flt *= usd_mult
        cm_out_shares *= sh_mult
        
        data = [ticker,date,ssnd_iss,vltry_flr,flr_cat,pub_flt,
                cm_out_shares]
        
    elif ext == 'xls':
        # for xls files
        ticker = data_dir.split('/')[-1]
        b_info = pd.read_excel(file,sheet_name=0)
        b_info.index = b_info.iloc[:,0]
        b_info = b_info.iloc[:,1:]   
        usd_mult,sh_mult = get_usd_share_multiplier(b_info.index)
        date = b_info.iloc[0,:][0]
        ssnd_iss = get_ssnd_iss(b_info)
        vltry_flr = get_vltry_flr(b_info)
        flr_cat = get_flr_cat(b_info)
        cm_out_shares = get_cm_out_shares(b_info)
        pub_flt = get_pub_flt(b_info)
        
        pub_flt *= usd_mult
        cm_out_shares *= sh_mult
        
        data = [ticker,date,ssnd_iss,vltry_flr,flr_cat,pub_flt,
                cm_out_shares]
    else:
        file = file.split('/')[-1]
        print('Error: {1} has a {0} extension'.format(ext,file))
        
        data = [float('nan') for i in range(7)]



    return data

def get_ttl_liab(st_op_info):
    
    liab_words = p_lib.cons_bal_sheet_lib.ttl_lb
    liab_eq_words = p_lib.cons_bal_sheet_lib.ttl_liab_and_eq
    eq_words = p_lib.cons_bal_sheet_lib.ttl_eq
    
        
    ttl_liab = None
    for word in liab_words:
        try:
            ttl_liab = st_op_info.loc[word]
            ttl_lib = ttl_liab[0]
            break
        except KeyError:
            continue
        

    if type(ttl_liab) is not pd.core.series.Series:
        if ttl_liab == None:
            for word in liab_eq_words:
                try:
                    ttl_liab_eqty = st_op_info.loc[word]
                    break
                except KeyError:
                    continue
            
            
            try:
                ttl_lb_eq = ttl_liab_eqty.iloc[0,0]
            except pd.core.indexing.IndexingError:
                ttl_lb_eq = ttl_liab_eqty[0]
            
            
            
            for word in eq_words:
                try:
                    ttl_eq = st_op_info.loc[word]
                    break
                except KeyError:
                    continue
            try:
                ttl_e = ttl_eq.iloc[0,0]    
            except pd.core.indexing.IndexingError:
                ttl_e = ttl_eq.iloc[0] 
            
            
            ttl_lib = float(ttl_lb_eq) - float(ttl_e)  
        
        
    if type(ttl_lib) == str:
        if '[' in ttl_lib:
            ttl_lib = ttl_liab[1]    
  

    
    return ttl_lib

def get_ttl_asst(st_op_info):
    
    ass_words = p_lib.cons_bal_sheet_lib.ttl_ass
    
    for word in ass_words:
        try:
            ttl_asst = st_op_info.loc[word]
            break
        except KeyError:
            continue
        
    
    
    try:
        ttl_ast = ttl_asst[0]
    except KeyError:
        ttl_ast = ttl_asst.iloc[0,0]
    
    
    
    if type(ttl_ast) == str:
        if '[' in ttl_ast:
            ttl_ast = ttl_asst[1]
        
    if math.isnan(ttl_ast):
        ttl_ast = ttl_asst[1]

    
    return ttl_ast

def get_ttl_eq(st_op_info):
    
    eq_words = p_lib.cons_bal_sheet_lib.ttl_eq
    
    for word in eq_words:
        try:
            ttl_eq = st_op_info.loc[word]
    

            break
        except KeyError:
            continue
    
    try:
        ttl_e = ttl_eq[0]
    except KeyError:
        ttl_e = ttl_eq.iloc[0,0]
        
        
        
    if type(ttl_e) == str:
        if '[' in ttl_e:
            ttl_e = ttl_eq[1]
    
    if math.isnan(ttl_e):
        ttl_e = ttl_eq[1]
    
    return ttl_e
    
def open_cons_bal_sheet(file):
    
    s_names = p_lib.sheet_lib.con_bal_sheet
    
    for name in s_names:
        try:
            st_op_info = pd.read_excel(file,sheet_name=name)
            break
        except xlrd.XLRDError:
            continue
        
        except KeyError:
            continue
        
    
    
    
    
    st_op_info.index = st_op_info.iloc[:,0]
    st_op_info = st_op_info.iloc[:,1:]
    
    return st_op_info


def get_balance_sheet_info(file):
    st_op_info = open_cons_bal_sheet(file)

    
    ttl_liab = get_ttl_liab(st_op_info)
    usd_mult,sh_mult = get_usd_share_multiplier(st_op_info.index)
    
    ttl_asst = get_ttl_asst(st_op_info)
    ttl_eq = get_ttl_eq(st_op_info)
    
    ttl_liab *= usd_mult
    ttl_asst *= usd_mult
    ttl_eq *= usd_mult
    
    
    
    return ttl_asst, ttl_eq, ttl_liab



def single_dir_loop_test(files,xmls,data_dir,non_s):
    
    complete_flag = True
    count = 0
    ticker = data_dir.split('/')[2]
    dir_num = data_dirs.index(ticker)
    
    
    for file in files:
        file = '/'.join([data_dir,file])
        ext = file.split('.')[len(file.split('.'))-1]
        try:
            if ext == 'xlsx':
                data = get_basic_info(file,ext,data_dir)
                ttl_asst, ttl_eq, ttl_liab = get_balance_sheet_info(file)
                
                data.insert(len(data),ttl_asst)
                data.insert(len(data),ttl_eq)
                data.insert(len(data),ttl_liab)
                
                db.append(data)
                
            elif ext == 'xls':
                data = get_basic_info(file,ext,data_dir)
                ttl_asst, ttl_eq, ttl_liab = get_balance_sheet_info(file)
                
                data.insert(len(data),ttl_asst)
                data.insert(len(data),ttl_eq)
                data.insert(len(data),ttl_liab)
            
                db.append(data)
            
            print(file,'Success',dir_num,count)
            count += 1
            
        except ValueError:
            print(file,"XML file",dir_num,count)
            count += 1
            xmls.append(file)
            continue
        
        except KeyError:
            print(file,': non-standard format',dir_num,count)
            count += 1
            non_s.append(file)
            complete_flag = False
        
        except UnboundLocalError:
            print(file,': non-standard format',dir_num,count)
            count += 1
            non_s.append(file)
            complete_flag = False
            
    
    if complete_flag:
        complete_dirs.append(ticker)
            
    return xmls, non_s


def mult_dir_loop_test(data_dirs,non_s):
    global complete_flag
    
    for data_dir in data_dirs:
        #if data_dir not in complete_dirs:
        #specific security directory
         
        print('------- {0} -------'.format(data_dir))
        data_dir = '/'.join([dbase_dir,data_dir])
        
        
        #files in current directory
        files = os.listdir(data_dir)
        files = [file for file in files if '10_K_A' not in file]
        
        
        #Tests current parsing script on a whole directory of files if loop_flag=True
        loop_flag = True
        if loop_flag:

           bad_files, non_s = single_dir_loop_test(files,xmls,data_dir,non_s)
           
           
           print('---------END---------')
        
        
        # else:
        #     print('{0} has already been completed ---'.format(data_dir))
    
    
    return bad_files, non_s

#^^^^ Script functions ^^^^
# Make this its own script***
















#------Actual script ------
# Move this to its own notebook or something***

#Global variables
global p_lib
global db
global dir_count
global data_dirs
global complete_dirs 



#Parser Keyword / Keyphrase library
p_lib = Parser_Lib()

#Parsed Database
db = []


#completed directory filepath
comp_dir_path = './logs/completed_directories2.csv'

#Complete directories
if os.path.exists(comp_dir_path):
    complete_dirs = list(pd.read_csv(comp_dir_path).iloc[:,1])
else:
    complete_dirs = []



#bad files
xmls = []
non_s = []

dir_count = 0

#All security directories
dbase_dir = './data'
data_dirs = os.listdir(dbase_dir)
data_dirs = [d for d in data_dirs if '.' not in d]


m_flag = True


#Multiple directory testing
if m_flag:
    try:
        bad_files, non_s = mult_dir_loop_test(data_dirs,non_s)
        db = pd.DataFrame(db)
    except KeyboardInterrupt:
        print('------Early Termination-------')
        db = pd.DataFrame(db)
        complete_dirs = pd.DataFrame(complete_dirs)
        complete_dirs.to_csv(comp_dir_path)
    
#Single directory test
else:
    data_dir = data_dirs[128]
    
    print('------- {0} -------'.format(data_dir))
    data_dir = '/'.join([dbase_dir,data_dir])
    
    
    
    
    
    #files in current directory
    files = os.listdir(data_dir)
    files = [file for file in files if '10_K_A' not in file]
    
    
    #Tests current parsing script on a whole directory of files if loop_flag=True
    s_loop_flag = True
    if s_loop_flag:
       print('------- {0} -------'.format(data_dir))
       bad_files, non_s = single_dir_loop_test(files,xmls,data_dir,non_s)
       print('---------END---------')
    
    
    #Single File Test
    else:
        file = files[4]
        ext = file.split('.')[len(file.split('.'))-1]
        data = []
        file = '/'.join([data_dir,file])
        xl = pd.ExcelFile(file)
        
        names = xl.sheet_names
        if ext == 'xlsx':
            data = get_basic_info(file,ext,data_dir)
            ttl_asst, ttl_eq, ttl_liab = get_balance_sheet_info(file)
            
        elif ext == 'xls':
            data = get_basic_info(file,ext,data_dir)
            ttl_asst, ttl_eq, ttl_liab = get_balance_sheet_info(file)
    
            
    
        
        else:
            print('yo')
        
        # except ValueError:
        #     #XML FILE
        #     print(file,"XML file, we'll write a parser eventually")
        #     # with open(file,'r') as f:
        #     #     contents2 = f.readlines()
        #     #     for c in contents2:
        #     #         if 'Document' in c:
        #     #             print(c)
        #     xmls.append(file)
        
        
        # except KeyError:
        #     print('Weird format')
        #     non_s.append(file)
            
            
            
    # print('---------END---------')
