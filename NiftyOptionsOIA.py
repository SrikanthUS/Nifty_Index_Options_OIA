#!/usr/bin/env python
# coding: utf-8

# Project Title: Nifty Index Options Trading:  
#                Profiting from Open Interest Analysis of Options Chain

# In[1]:


#STEPS to execute the code
#1.) Install the required library. 
#2.) Restart and Run All or Run Step by Step
#3.) Provide User Input
#    to select the No of Strikes aroung ATM to be considered for Analysis.
#4.) Provide User Input
#    to select the No of Levels Of "Open Interest" around the Close Price
#    to be shown on the Chart.
#5.) Provide User Input
#    to select the No of Levels Of "Change in Open Interest" 
#    around the Close Price to be shown on the Chart.


# In[ ]:





# # Load Library

# In[2]:


# Import Libraries for usage in project
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from datetime import datetime
import plotly.graph_objects as go
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:





# In[ ]:





# # Functions 

# LoadFiles(): There are two excel files that are used in the project. CapstoneNiftyData.xlsx and CapstoneNiftyOptionsData. These two files are loaded to the data frame, and the records are displayed.

# In[3]:


def LoadFiles():
    
    # Read the excel file containing Nifty 50 Index Data
    dataset1 = pd.read_excel('./NiftyData.xlsx')
    nifty = pd.DataFrame(dataset1) 

    # Read the Base Data
    # Data about Nifty Index is stored in the excel file NiftyData.xlsx
    # Data about Nifty Index Options is stored in the excel file NiftyOptionsData.xlsx

    # Read the file into Pandas DataFrame
    dataset2 = pd.read_excel('./NiftyOptionsData.xlsx')
    nifty_options = pd.DataFrame(dataset2)
     

    return  nifty,nifty_options


# In[ ]:





# GetUserInput() is going to capture the user input, select any number from 1-7 and press enter, as to how many strikes around the ATM price needs to be considered for analysis.
# Nifty Index Options has each strike of 50 points apart. So selecting 5 strikes means 250 points on either side of the ATM or spot price is considered for analysis. So ATM = 15000, then the strikes selected are 14750  - 15250.
# 

# In[4]:


def GetUserInput():

    # Obtain user Input

    # The user can choose how many strikes on either side of the ATM Strike he wants the data to be analysed

    print ('How many Strike to Consider for NIFTY50 Index Options from ATM? Enter 1-7:')
    print ('1. 05 Strikes = 250 points')
    print ('2. 10 Strikes = 500 points')
    print ('3. 15 Strikes = 750 points')
    print ('4. 20 Strikes = 1000 points')
    print ('5. 25 Strikes = 1250 points')
    print ('6. 30 Strikes = 1500 points')
    print ('7. ALL Strikes')

    ip = input('> ')

    if ip == '1':
        ip1 = 250
        ip11 = 'You have selected 1. 05 Strikes = 250 points'
    elif ip == '2':
        ip1 = 500
        ip11 = 'You have selected 2. 10 Strikes = 500 points'
    elif ip == '3':
        ip1 = 750
        ip11 = 'You have selected 3. 15 Strikes = 750 points'
    elif ip == '4':
        ip1 = 1000
        ip11 = 'You have selected 4. 20 Strikes = 1000 pointss'
    elif ip == '5':
        ip1 = 1250
        ip11 = 'You have selected 5. 25 Strikes = 1250 points'
    elif ip == '6':
        ip1 = 1500
        ip11 = 'You have selected 6. 30 Strikes = 1500 points'
    elif ip == '7':
        ip1 = 10000
        ip11 = 'You have selected 7. ALL Strikes'
    else:
        pass
    
    #print(ip11)   
    return ip1, ip11


# In[ ]:





# GetUserInput_Charts() is going to capture the user input, select any number from 1-7 and press enter. This considers the first highest Open Interest or first highest Change in Open Interest to the next four levels below. Select 1 if you want to analyse the first highest OI or COI level wrt the Close price of the underlying.

# In[5]:


def GetUserInput_IOCharts():

    # Obtain user Input

    # The user can choose how many Levels of Depth he wants the data to be analysed

    print ('How many Levels of "NIFTY50 Index Options OI" do you want to View in the Chart? Enter 1-6:')
    print ('1. High1 OI Level')
    print ('2. High2 OI Level')
    print ('3. High3 OI Level')
    print ('4. High4 OI Level')
    print ('5. High5 OI Level')
    print ('6. ALL 1-5 OI Levels')
    print ('7. High1, and High 2 OI Level')
 

    ip = input('> ')

    if ip == '1':
        ip2 = 1
        ip21 = 'You have selected 1. Highest OI Level'
    elif ip == '2':
        ip2 = 2
        ip21 = 'You have selected 2. Higher OI Level'
    elif ip == '3':
        ip2 = 3
        ip21 = 'You have selected 3. High3 OI Level'
    elif ip == '4':
        ip2 = 4
        ip21 = 'You have selected 4. High4 OI Level'
    elif ip == '5':
        ip2 = 5
        ip21 = 'You have selected 5. High5 OI Level'
    elif ip == '6':
        ip2 = 6
        ip21 = 'You have selected 6. ALL 1-5 OI Level'
    elif ip == '7':
        ip2 = 7
        ip21 = 'You have selected 7. High1, High2 OI Level'

    #print(ip11)   
    return ip2, ip21


# In[6]:


def GetUserInput_COICharts():

    # Obtain user Input

    # The user can choose how many Levels of Depth he wants the data to be analysed

    print ('How many Levels of "NIFTY50 Index Options COI" do you want to View in the Chart? Enter 1-6:')
    print ('1. High1 COI Level')
    print ('2. High2 COI Level')
    print ('3. High3 COI Level')
    print ('4. High4 COI Level')
    print ('5. High5 COI Level')
    print ('6. ALL 1-5 OI Levels')
    print ('7. High1, and High 2 COI Level')
 

    ip = input('> ')

    if ip == '1':
        ip2 = 1
        ip21 = 'You have selected 1. Highest COI Level'
    elif ip == '2':
        ip2 = 2
        ip21 = 'You have selected 2. Higher COI Level'
    elif ip == '3':
        ip2 = 3
        ip21 = 'You have selected 3. High3 COI Level'
    elif ip == '4':
        ip2 = 4
        ip21 = 'You have selected 4. High4 COI Level'
    elif ip == '5':
        ip2 = 5
        ip21 = 'You have selected 5. High5 COI Level'
    elif ip == '6':
        ip2 = 6
        ip21 = 'You have selected 6. ALL 1-5 COI Level'
    elif ip == '7':
        ip2 = 7
        ip21 = 'You have selected 7. High1, High2 COI Level'

    #print(ip11)   
    return ip2, ip21


# In[7]:



#   MaxPain() function , captures the Max Pain details and displayed.
def MaxPain(nifty_options):
    # extrace the MaxPain data from the base file
    mxpn = nifty_options[['Date','ITM_OTM','Close','Strike', 'CALL_OI','PUT_OI']]
    mxpn['MaxPain'] = mxpn['CALL_OI'] + mxpn['PUT_OI']  
 
    
    return mxpn


# In[8]:


#   DailyRange() captures the Daily Range and other details and are displayed.
def DailyRange(nifty):
    # extrace the MaxPain data from the base file
    DailyRange = nifty[['Date' , 'Volume\n(x1000)','Daily Return','Daily Range','Gap Open','Daily Body']]
    
         
    return DailyRange


# In[9]:


#   MaxPain_Top1() captures the one Top Max Pain considering all the strikes for a day.
def MaxPain_Top1(mxpn, ui):

    # Make calculations for Open Interest
    # Shortlist Open Interest Data for CALL ITM and CALL OTM Options

    data = mxpn#.set_index(['Close','Strike', 'CALL_OI','PUT_OI']).groupby(['Date'])['MaxPain'].nlargest(10000).reset_index()   
     


    # Shortlist the data based on user input
    # Open Interest Data for CALL ITM and PUT OTM Options on either side of the ATM, 
    # based on the number of strikes the user has selected

    #select_color = df.loc[df['Color'] == 'Green']
    data = data.loc[data['Strike'] < data['Close']+ui]
    data = data.loc[data['Strike'] > data['Close']-ui]

    # Shortlist the data based on Top 5, Highest OpenInterest  Values
    # Shortlist Top 5, Highest OpenInterest  Values for CALL ITM and CALL OTM Options on either side of the ATM,

    mxpn = data.set_index(['Close','Strike', 'CALL_OI','PUT_OI']).groupby(['Date'])['MaxPain'].nlargest(1).reset_index()   



    # Change the Column Header for Column = 'Strike'
    mxpn.rename(columns = {'Strike':'MaxPain_Strike'}, inplace = True)
     

 
 

    return mxpn


# In[10]:


#   MaxPain_IOTM_Top1() captures the one Top Max Pain considering all the strikes for a day separated by ITM and OTM.
def MaxPain_IOTM_Top1(mxpn, ui):

    # Make calculations for Open Interest
    # Shortlist Open Interest Data for CALL ITM and CALL OTM Options

    data = mxpn#.set_index(['Close','Strike', 'CALL_OI','PUT_OI']).groupby(['Date','ITM_OTM'])['MaxPain'].nlargest(10000).reset_index()   
     


    # Shortlist the data based on user input
    # Open Interest Data for CALL ITM and PUT OTM Options on either side of the ATM, 
    # based on the number of strikes the user has selected

    #select_color = df.loc[df['Color'] == 'Green']
    data = data.loc[data['Strike'] < data['Close']+ui]
    data = data.loc[data['Strike'] > data['Close']-ui]

    # Shortlist the data based on Top 5, Highest OpenInterest  Values
    # Shortlist Top 5, Highest OpenInterest  Values for CALL ITM and CALL OTM Options on either side of the ATM,

    mxpn = data.set_index([ 'Close','Strike', 'CALL_OI','PUT_OI']).groupby(['Date','ITM_OTM'])['MaxPain'].nlargest(1).reset_index()   



    # Change the Column Header for Column = 'Strike'
    mxpn.rename(columns = {'Strike':'MaxPain_Strike'}, inplace = True)
     

 
 

    return mxpn


# In[11]:


#   MaxPain_Top5() captures the five Top Max Pain considering all the strikes for a day separated by ITM and OTM.
def MaxPain_Top5(mxpn, ui):

    # Make calculations for Open Interest
    # Shortlist Open Interest Data for CALL ITM and CALL OTM Options

    data = mxpn#.set_index(['Close','Strike', 'CALL_OI','PUT_OI']).groupby(['Date','ITM_OTM'])['MaxPain'].nlargest(10000).reset_index()   
     


    # Shortlist the data based on user input
    # Open Interest Data for CALL ITM and PUT OTM Options on either side of the ATM, 
    # based on the number of strikes the user has selected

    #select_color = df.loc[df['Color'] == 'Green']
    data = data.loc[data['Strike'] < data['Close']+ui]
    data = data.loc[data['Strike'] > data['Close']-ui]

    # Shortlist the data based on Top 5, Highest OpenInterest  Values
    # Shortlist Top 5, Highest OpenInterest  Values for CALL ITM and CALL OTM Options on either side of the ATM,

    mxpn = data.set_index(['Close','Strike', 'CALL_OI','PUT_OI']).groupby(['Date','ITM_OTM'])['MaxPain'].nlargest(5).reset_index()   



    # Change the Column Header for Column = 'Strike'
    mxpn.rename(columns = {'Strike':'MaxPain_Strike'}, inplace = True)
     

 
 

    return mxpn


# In[ ]:





# In[ ]:





# In[ ]:





# In[12]:


#   Call_OI_Top5() captures the top five Open Interest strikes for Call and Put options.
def Call_OI_Top5(nifty_options, ui):

    # Make calculations for Open Interest
    # Shortlist Open Interest Data for CALL ITM and CALL OTM Options

    test_coi_sample = nifty_options#.set_index(['Open', 'High', 'Low', 'Close','Strike']).groupby(['Date','ITM_OTM'])['CALL_OI'].nlargest(10000).reset_index()   
    #test_coi_sample.head(10)


    # Shortlist the data based on user input
    # Open Interest Data for CALL ITM and PUT OTM Options on either side of the ATM, 
    # based on the number of strikes the user has selected

    #select_color = df.loc[df['Color'] == 'Green']
    test_coi_sample = test_coi_sample.loc[test_coi_sample['Strike'] < test_coi_sample['Close']+ui]
    test_coi_sample = test_coi_sample.loc[test_coi_sample['Strike'] > test_coi_sample['Close']-ui]

    # Shortlist the data based on Top 5, Highest OpenInterest  Values
    # Shortlist Top 5, Highest OpenInterest  Values for CALL ITM and CALL OTM Options on either side of the ATM,

    test_coi = test_coi_sample.set_index(['Open', 'High', 'Low', 'Close','Strike']).groupby(['Date','ITM_OTM'])['CALL_OI'].nlargest(5).reset_index()   



    # Change the Column Header for Column = 'Strike'
    test_coi.rename(columns = {'Strike':'Call_OI_Strike'}, inplace = True)
     

 
 

    return test_coi


# In[13]:


#   Put_OI_Top5() captures the top five Open Interest strikes for Call and Put options.
def Put_OI_Top5(nifty_options,ui):
    
    # Make calculations for Open Interest
    # Shortlist Open Interest Data for PUT OTM and PUT ITM Options


    test_poi_sample = nifty_options#.set_index(['Open', 'High', 'Low', 'Close','Strike']).groupby(['Date','ITM_OTM'])['PUT_OI'].nlargest(10000).reset_index()   

    # Shortlist the data based on user input
    # Open Interest Data for PUT OTM and PUT ITM Options on either side of the ATM, 
    # based on the number of strikes the user has selected
 
    test_poi_sample = test_poi_sample.loc[test_poi_sample['Strike'] < test_poi_sample['Close']+ui]
    test_poi_sample = test_poi_sample.loc[test_poi_sample['Strike'] > test_poi_sample['Close']-ui]
    
    # Shortlist the data based on Top 5, Highest OpenInterest  Values
    # Shortlist Top 5, Highest OpenInterest  Values for PUT OTM and PUT IM Options on either side of the ATM,

    test_poi = test_poi_sample.set_index(['Open', 'High', 'Low', 'Close','Strike']).groupby(['Date','ITM_OTM'])['PUT_OI'].nlargest(5).reset_index()   
     

    # Change the Column Header for Column = 'Strike'
    test_poi.rename(columns = {'Strike':'Put_OI_Strike'}, inplace = True)
 
    
    return test_poi


# In[ ]:





# In[ ]:





# In[14]:


#   Merge_CallPutOI() merges Call_OI_Top5 and Put_OI_Top5() , so that all details are available in one dataframe.
def Merge_Call_Put_OI(Call_OI_Top5, Put_OI_Top5):
    
    
    #Drop the unwanted Columns that are not necessary for further processing
    Call_OI_Top5.drop('ITM_OTM', inplace=True, axis=1)
    Call_OI_Top5.drop('CALL_OI', inplace=True, axis=1)
 

    #Drop the unwanted Columns that are not necessary for further processing
    Put_OI_Top5.drop('Date', inplace=True, axis=1)
    Put_OI_Top5.drop('ITM_OTM', inplace=True, axis=1)
    Put_OI_Top5.drop('Open', inplace=True, axis=1)
    Put_OI_Top5.drop('High', inplace=True, axis=1)
    Put_OI_Top5.drop('Low', inplace=True, axis=1)
    Put_OI_Top5.drop('Close', inplace=True, axis=1)
    Put_OI_Top5.drop('PUT_OI', inplace=True, axis=1)
 
    
    #Calculate the size of the table for CALL OI
    #print(Call_OI_Top5.shape)
    #print(Call_OI_Top5.shape[0])
    a = Call_OI_Top5.shape[0]/10
    a= int(a) 
    #print(a)

    #print(Call_OI_Top5.shape[1])
    b = Call_OI_Top5.shape[1] 
    b= int(b) 
    #print(b)
    
    
    #Calculate the size of the table for PUT OI

    #print(Put_OI_Top5.shape)
    c = Put_OI_Top5.shape[0]/10
    c= int(c) 
    #print(c)

    #print(Put_OI_Top5.shape[1])
    d = Put_OI_Top5.shape[1] 
    d= int(d) 
    #print(d)

    
    # Rebuild the table
    # transform the ranking of Strikes from vertical columns to horizontal rows for CALL OI

    Call_OI_Top5 = pd.DataFrame(Call_OI_Top5.values.reshape(a,b*10), 
                       columns=['Date_COTM1', 'Open_COTM1', 'High_COTM1', 'Low_COTM1', 'Close_COTM1', 'OI_COTM_Strike1', 
                                'Date_COTM2', 'Open_COTM2', 'High_COTM2', 'Low_COTM2', 'Close_COTM2', 'OI_COTM_Strike2', 
                                'Date_COTM3', 'Open_COTM3', 'High_COTM3', 'Low_COTM3', 'Close_COTM3', 'OI_COTM_Strike3', 
                                'Date_COTM4', 'Open_COTM4', 'High_COTM4', 'Low_COTM4', 'Close_COTM4', 'OI_COTM_Strike4' ,
                                'Date_COTM5', 'Open_COTM5', 'High_COTM5', 'Low_COTM5', 'Close_COTM5', 'OI_COTM_Strike5' ,
                                'Date_CITM1', 'Open_CITM1', 'High_CITM1', 'Low_CITM1', 'Close_CITM1', 'OI_CITM_Strike1', 
                                'Date_CITM2', 'Open_CITM2', 'High_CITM2', 'Low_CITM2', 'Close_CITM2', 'OI_CITM_Strike2' ,
                                'Date_CITM3', 'Open_CITM3', 'High_CITM3', 'Low_CITM3', 'Close_CITM3', 'OI_CITM_Strike3' ,
                                'Date_CITM4', 'Open_CITM4', 'High_CITM4', 'Low_CITM4', 'Close_CITM4', 'OI_CITM_Strike4' ,
                                'Date_CITM5', 'Open_CITM5', 'High_CITM5', 'Low_CITM5', 'Close_CITM5', 'OI_CITM_Strike5'])


    
    # Rebuild the table
    # transform the ranking of Strikes from vertical columns to horizontal rows for PUT OI

    Put_OI_Top5 = pd.DataFrame(Put_OI_Top5.values.reshape(c,d*10), 
                       columns=['OI_PITM_Strike1', 
                                'OI_PITM_Strike2', 
                                'OI_PITM_Strike3', 
                                'OI_PITM_Strike4' ,
                                'OI_PITM_Strike5' ,
                                'OI_POTM_Strike1', 
                                'OI_POTM_Strike2' ,
                                'OI_POTM_Strike3' ,
                                'OI_POTM_Strike4' ,
                                'OI_POTM_Strike5'])

    
    
    # Merge the PUT OI data to the CALL OI main table
    #result = pd.concat([df1, df3], axis=1, join='inner')
    #display(result)
    #test_option = pd.concat([test_coi, test_poi], axis=1, join='inner')
    CallPut_OI_Top5 = pd.concat([Call_OI_Top5, Put_OI_Top5], axis=1, join='inner')
     

    # Remove the dulplicate columns

    CallPut_OI_Top5=CallPut_OI_Top5[[  'Date_CITM1',     'Open_CITM1',      'High_CITM1',      'Low_CITM1',         'Close_CITM1',
                                       'OI_COTM_Strike1','OI_COTM_Strike2', 'OI_COTM_Strike3', 'OI_COTM_Strike4' ,  'OI_COTM_Strike5' ,
                                       'OI_CITM_Strike1','OI_CITM_Strike2', 'OI_CITM_Strike3', 'OI_CITM_Strike4' ,  'OI_CITM_Strike5' ,
                                       'OI_PITM_Strike1','OI_PITM_Strike2', 'OI_PITM_Strike3', 'OI_PITM_Strike4' ,  'OI_PITM_Strike5' ,
                                       'OI_POTM_Strike1','OI_POTM_Strike2', 'OI_POTM_Strike3', 'OI_POTM_Strike4' ,  'OI_POTM_Strike5'
                                  ]]

    
    CallPut_OI_Top5.rename(columns = {'Date_CITM1':'Date'}, inplace = True)
    CallPut_OI_Top5.rename(columns = {'Open_CITM1':'Open'}, inplace = True)
    CallPut_OI_Top5.rename(columns = {'High_CITM1':'High'}, inplace = True)
    CallPut_OI_Top5.rename(columns = {'Low_CITM1':'Low'}, inplace = True)
    CallPut_OI_Top5.rename(columns = {'Close_CITM1':'Close'}, inplace = True)

        
    return CallPut_OI_Top5


# In[15]:


#   Merge_CallPutOI_MaxPain() merges Merge_CallPut_OI and MaxPain_Top5, so that all details are available in one dataframe.
def Merge_CallPutOI_MaxPain(Merge_Call_Put_OI, MaxPain_Top5, Daily_Range):
    
    
    #Drop the unwanted Columns that are not necessary for further processing
    MaxPain_Top5.drop('Date', inplace=True, axis=1)
    MaxPain_Top5.drop('ITM_OTM', inplace=True, axis=1)
    MaxPain_Top5.drop('Close', inplace=True, axis=1)
    MaxPain_Top5.drop('CALL_OI', inplace=True, axis=1)
    MaxPain_Top5.drop('PUT_OI', inplace=True, axis=1)
    MaxPain_Top5.drop('MaxPain', inplace=True, axis=1)
    
        
    #Calculate the size of the table for CALL OI
    #print(Call_OI_Top5.shape)
    #print(Call_OI_Top5.shape[0])
    a = MaxPain_Top5.shape[0]/10
    a= int(a) 
    #print(a)

    #print(Call_OI_Top5.shape[1])
    b = MaxPain_Top5.shape[1] 
    b= int(b) 
    #print(b)
    
    
    # Rebuild the table
    # transform the ranking of Strikes from vertical columns to horizontal rows for PUT OI

    MaxPain_Top5 = pd.DataFrame(MaxPain_Top5.values.reshape(a,b*10), 
                       columns=['MaxPain_OTM_Strike1', 
                                'MaxPain_OTM_Strike2', 
                                'MaxPain_OTM_Strike3', 
                                'MaxPain_OTM_Strike4' ,
                                'MaxPain_OTM_Strike5' ,
                                'MaxPain_ITM_Strike1', 
                                'MaxPain_ITM_Strike2' ,
                                'MaxPain_ITM_Strike3' ,
                                'MaxPain_ITM_Strike4' ,
                                'MaxPain_ITM_Strike5'])

    
    
    # Merge the PUT OI data to the CALL OI main table
    #result = pd.concat([df1, df3], axis=1, join='inner')
    #display(result)
    #test_option = pd.concat([test_coi, test_poi], axis=1, join='inner')
    CallPutOI_MaxPain_Top5 = pd.concat([Merge_Call_Put_OI, MaxPain_Top5], axis=1, join='inner')
     
     
    #Drop the unwanted Columns that are not necessary for further processing
    Daily_Range.drop('Date', inplace=True, axis=1)
    CallPutOI_MaxPain_Top5 = pd.concat([CallPutOI_MaxPain_Top5, Daily_Range], axis=1, join='inner')
        
    return CallPutOI_MaxPain_Top5


# In[16]:



def COTM_PITM(nifty_options):
    # Capture data of CALL and  PUT Open Interest, and Change of Open Interest, both ITM and OTM
    
    
    COTM_PITM = nifty_options.set_index(['Close' , 'CALL_OI', 'PUT_OI' ,'CALL_COI', 'PUT_COI']).groupby(['Date','ITM_OTM'])['Strike'].nsmallest(10000).reset_index()   
    #aa.head(10)
   

    # Capture data of CALL and  PUT Open Interest, and Change of Open Interest, 
    # this is data for CALL OTM and PUT ITM
    #aa2=COTM_PITM

    COTM_PITM.drop(COTM_PITM.loc[COTM_PITM['ITM_OTM']==1].index, inplace=True) # 0=OTM, 1=ITM
     
    #Rename the columns    
    COTM_PITM.rename(columns = {'CALL_OI':'OI_CALL_OTM'}, inplace = True)
    COTM_PITM.rename(columns = {'CALL_COI':'COI_CALL_OTM'}, inplace = True)
    COTM_PITM.rename(columns = {'PUT_OI':'OI_PUT_ITM'}, inplace = True)
    COTM_PITM.rename(columns = {'PUT_COI':'COI_PUT_ITM'}, inplace = True)

    # obtain the total of the values for each column
    #COTM_PITM=COTM_PITM.groupby(['Date']).sum().reset_index()
    
    # drop unwanted columns
    #COTM_PITM.drop('Date', inplace=True, axis=1)
    #COTM_PITM.drop('Strike', inplace=True, axis=1)
    COTM_PITM.drop('ITM_OTM', inplace=True, axis=1)
    #COTM_PITM.drop('Close', inplace=True, axis=1)
    
    
    return COTM_PITM


# In[ ]:





# In[17]:


def CITM_POTM(nifty_options):
    
    # Capture data of CALL and  PUT Open Interest, and Change of Open Interest, 
    # this is data for CALL ITM and PUT OTM

    CITM_POTM = nifty_options.set_index(['Close' , 'CALL_OI', 'PUT_OI' ,'CALL_COI', 'PUT_COI']).groupby(['Date','ITM_OTM'])['Strike'].nlargest(10000).reset_index()   
    
    # get CALL OTM and PUT ITM Data
    CITM_POTM.drop(CITM_POTM.loc[CITM_POTM['ITM_OTM']==0].index, inplace=True) # 1 in file is ITM, 0 is OTM

    #Rename the Columns 
    CITM_POTM.rename(columns = {'CALL_OI':'OI_CALL_ITM'}, inplace = True)
    CITM_POTM.rename(columns = {'CALL_COI':'COI_CALL_ITM'}, inplace = True)
    CITM_POTM.rename(columns = {'PUT_OI':'OI_PUT_OTM'}, inplace = True)
    CITM_POTM.rename(columns = {'PUT_COI':'COI_PUT_OTM'}, inplace = True)

    #CITM_POTM.drop('Close', inplace=True, axis=1)
    #CITM_POTM.drop('Strike', inplace=True, axis=1)
    CITM_POTM.drop('ITM_OTM', inplace=True, axis=1)
    
    return CITM_POTM


# In[ ]:





# In[18]:


def CallPut_OI_COI(COTM_PITM,CITM_POTM):

    
    COTM_PITM.drop('Date', inplace=True, axis=1)
    COTM_PITM.drop('Strike', inplace=True, axis=1)
    #COTM_PITM.drop('ITM_OTM', inplace=True, axis=1)
    COTM_PITM.drop('Close', inplace=True, axis=1)
    
    
    #Combine the tables of CALL PUT ITM OTM top 5 
    #aa1 = pd.concat([aa1, aa2], axis=1, join='inner')
    CallPut_OI_COI = pd.concat([CITM_POTM, COTM_PITM], axis=1, join='inner')
     


    return CallPut_OI_COI


# In[ ]:





# In[19]:


def Call_COI_P_Top5(nifty_options, ui,Merge_CallPutOI_MaxPain):
    # Make calculations for Change in Open Interest Positive
    # Shortlist Open Change of Interest Data for CALL ITM and CALL OTM Options
    
    test_ccoip_sample = nifty_options#.set_index(['Open', 'High', 'Low', 'Close','Strike']).groupby(['Date','ITM_OTM'])['CALL_COI'].nlargest(10000).reset_index()   

    # Shortlist the data based on user input
    # Open Interest Data for CALL ITM and PUT OTM Options on either side of the ATM, 
    # based on the number of strikes the user has selected

    #select_color = df.loc[df['Color'] == 'Green']
    test_ccoip_sample = test_ccoip_sample.loc[test_ccoip_sample['Strike'] < test_ccoip_sample['Close']+ui]
    test_ccoip_sample = test_ccoip_sample.loc[test_ccoip_sample['Strike'] > test_ccoip_sample['Close']-ui]
    # or test111['Strike'] < test111['Close']+500]
    
    # Shortlist the data based on Top 5, Highest 'Change in OpenInterest"  Values
    # Shortlist Top 5, Highest OpenInterest  Values for CALL ITM and CALL OTM Options on either side of the ATM,
    test_ccoip = test_ccoip_sample.set_index(['Open', 'High', 'Low', 'Close','Strike']).groupby(['Date','ITM_OTM'])['CALL_COI'].nlargest(5).reset_index()   
    

    # Change the Column Header for Column = 'Strike'
    test_ccoip.rename(columns = {'Strike':'CallP_COI_Strike'}, inplace = True)
    #test_ccoip1=test_ccoip
    
    #Drop the unwanted Columns that are not necessary for further processing
    test_ccoip.drop('Date', inplace=True, axis=1)
    test_ccoip.drop('ITM_OTM', inplace=True, axis=1)
    test_ccoip.drop('Open', inplace=True, axis=1)
    test_ccoip.drop('High', inplace=True, axis=1)
    test_ccoip.drop('Low', inplace=True, axis=1)
    test_ccoip.drop('Close', inplace=True, axis=1)
    test_ccoip.drop('CALL_COI', inplace=True, axis=1)
    

    #Calculate the size of the table for CALL OI
    #import numpy as np
    #print (np.reshape(test.values,(3,10)))
    #[['11' '12' '13' '14'   '15']
    #['21' '22' '23' '24' '25']]
    print(test_ccoip.shape)
    e = test_ccoip.shape[0]/10
    e= int(e) 
   # print(e)

    print(test_ccoip.shape[1])
    f = test_ccoip.shape[1] 
    f= int(f) 
    #print(f)
    
    # Rebuild the table
    # transform the ranking of Strikes from vertical columns to horizontal rows for CALL OI

    # Rebuild the table
    # transform the ranking of Strikes from vertical columns to horizontal rows for PUT OI

    test_ccoip = pd.DataFrame(test_ccoip.values.reshape(e,f*10), 
                       #columns=['Date','Date2','Date3','Date4','Date5','Date6','Date7','Date8','Date9','Date10',
                       columns=['COI_P_COTM_Strike1', 
                                'COI_P_COTM_Strike2', 
                                'COI_P_COTM_Strike3', 
                                'COI_P_COTM_Strike4',
                                'COI_P_COTM_Strike5',
                                'COI_P_CITM_Strike1', 
                                'COI_P_CITM_Strike2',
                                'COI_P_CITM_Strike3',
                                'COI_P_CITM_Strike4',
                                'COI_P_CITM_Strike5'])
    
    
    #test_ccoip2=test_ccoip
    #test_ccoip.drop('Date', inplace=True, axis=1)
    #test_ccoip.drop('Date2', inplace=True, axis=1)
    #test_ccoip.drop('Date3', inplace=True, axis=1)
    #test_ccoip.drop('Date4', inplace=True, axis=1)
    #test_ccoip.drop('Date5', inplace=True, axis=1)
    #test_ccoip.drop('Date6', inplace=True, axis=1)
    #test_ccoip.drop('Date7', inplace=True, axis=1)
    #test_ccoip.drop('Date8', inplace=True, axis=1)
    #test_ccoip.drop('Date9', inplace=True, axis=1)
    #test_ccoip.drop('Date10', inplace=True, axis=1)
    
    # Merge the CALL COI data to the main table
    #CallPut_OI_COI_MP
    Merge_CallPutOI_MaxPain  = pd.concat([Merge_CallPutOI_MaxPain, test_ccoip], axis=1, join='inner')
    #display(Merge_CallPutOI_MaxPain)


    #return test_ccoip, test_ccoip2, Merge_CallPutOI_MaxPain
    return Merge_CallPutOI_MaxPain


# In[ ]:





# In[20]:


def Put_COI_N_Top5(nifty_options, ui,Merge_CallPutOI_MaxPain):
  # Calculation for "Change in Open Interest" for PUT Options NEGATIVE VALUES

    # Shortlist Change in Open Interest Data for CALL ITM and CALL OTM Options
    test_pcoin_sample = nifty_options#.set_index(['Open', 'High', 'Low', 'Close','Strike']).groupby(['Date','ITM_OTM'])['PUT_COI'].nsmallest(5000).reset_index()   

    # Shortlist the data based on user input
    # Open Interest Data for CALL ITM and PUT OTM Options on either side of the ATM, 
    # based on the number of strikes the user has selected


    test_pcoin_sample = test_pcoin_sample.loc[test_pcoin_sample['Strike'] < test_pcoin_sample['Close']+ui]
    test_pcoin_sample = test_pcoin_sample.loc[test_pcoin_sample['Strike'] > test_pcoin_sample['Close']-ui]
    # or test111['Strike'] < test111['Close']+500]


    # Shortlist the data based on Top 5, Highest 'Change in OpenInterest"  Values
    # Shortlist Top 5, Highest OpenInterest  Values for CALL ITM and CALL OTM Options on either side of the ATM,

    test_pcoin = test_pcoin_sample.set_index(['Open', 'High', 'Low', 'Close','Strike']).groupby(['Date','ITM_OTM'])['PUT_COI'].nsmallest(5).reset_index()   
    
    # Change the Column Header for Column = 'Strike'

    test_pcoin.rename(columns = {'Strike':'PutN_COI_Strike'}, inplace = True)

    #Drop the unwanted Columns that are not necessary for further processing
    test_pcoin.drop('Date', inplace=True, axis=1)
    test_pcoin.drop('ITM_OTM', inplace=True, axis=1)
    test_pcoin.drop('Open', inplace=True, axis=1)
    test_pcoin.drop('High', inplace=True, axis=1)
    test_pcoin.drop('Low', inplace=True, axis=1)
    test_pcoin.drop('Close', inplace=True, axis=1)
    test_pcoin.drop('PUT_COI', inplace=True, axis=1)

    #Calculate the size of the table for CALL OI
    #import numpy as np
    #print (np.reshape(test.values,(3,10)))
    #[['11' '12' '13' '14'   '15']
    #['21' '22' '23' '24' '25']]
    #print(test_pcoin.shape)
    e = test_pcoin.shape[0]/10
    e= int(e) 
    #print(e)

    #print(test_pcoin.shape[1])
    f = test_pcoin.shape[1] 
    f= int(f) 
    #print(f)

    
    # Rebuild the table
    # transform the ranking of Strikes from vertical columns to horizontal rows for CALL OI

    # Rebuild the table
    # transform the ranking of Strikes from vertical columns to horizontal rows for PUT OI

    test_pcoin = pd.DataFrame(test_pcoin.values.reshape(e,f*10), 
                       columns=['COI_N_PITM_Strike1', 
                                'COI_N_PITM_Strike2', 
                                'COI_N_PITM_Strike3', 
                                'COI_N_PITM_Strike4',
                                'COI_N_PITM_Strike5',
                                'COI_N_POTM_Strike1', 
                                'COI_N_POTM_Strike2',
                                'COI_N_POTM_Strike3',
                                'COI_N_POTM_Strike4',
                                'COI_N_POTM_Strike5'])

    # Merge the PUT COI data to the main table
    Merge_CallPutOI_MaxPain = pd.concat([Merge_CallPutOI_MaxPain, test_pcoin], axis=1, join='inner')
    
    return Merge_CallPutOI_MaxPain


# In[ ]:





# In[21]:


def Put_COI_P_Top5(nifty_options, ui,Merge_CallPutOI_MaxPain):
    # Calculation for "Change in Open Interest" for PUT Options POSITIVE VALUES

    # Shortlist Change in Open Interest Data for CALL ITM and CALL OTM Options

    test_pcoip_sample = nifty_options#.set_index(['Open', 'High', 'Low', 'Close','Strike']).groupby(['Date','ITM_OTM'])['PUT_COI'].nlargest(10000).reset_index()   
 
    # Shortlist the data based on user input
    # Open Interest Data for CALL ITM and PUT OTM Options on either side of the ATM, 
    # based on the number of strikes the user has selected

    #select_color = df.loc[df['Color'] == 'Green']
    test_pcoip_sample = test_pcoip_sample.loc[test_pcoip_sample['Strike'] < test_pcoip_sample['Close']+ui]
    test_pcoip_sample = test_pcoip_sample.loc[test_pcoip_sample['Strike'] > test_pcoip_sample['Close']-ui]
    # or test111['Strike'] < test111['Close']+500]
    
    
    # Shortlist the data based on Top 5, Highest 'Change in OpenInterest"  Values
    # Shortlist Top 5, Highest OpenInterest  Values for PUT ITM and PUT OTM Options on either side of the ATM,

    test_pcoip = test_pcoip_sample.set_index(['Open', 'High', 'Low', 'Close','Strike']).groupby(['Date','ITM_OTM'])['PUT_COI'].nlargest(5).reset_index()   
    
    # Change the Column Header for Column = 'Strike'

    test_pcoip.rename(columns = {'Strike':'PUTP_COI_Strike'}, inplace = True)
    
    #Drop the unwanted Columns that are not necessary for further processing
    test_pcoip.drop('Date', inplace=True, axis=1)
    test_pcoip.drop('ITM_OTM', inplace=True, axis=1)
    test_pcoip.drop('Open', inplace=True, axis=1)
    test_pcoip.drop('High', inplace=True, axis=1)
    test_pcoip.drop('Low', inplace=True, axis=1)
    test_pcoip.drop('Close', inplace=True, axis=1)
    test_pcoip.drop('PUT_COI', inplace=True, axis=1)
    
    #Calculate the size of the table for PUT COI
    #import numpy as np
    #print (np.reshape(test.values,(3,10)))
    #[['11' '12' '13' '14'   '15']
    #['21' '22' '23' '24' '25']]
    #print(test_pcoip.shape)
    e = test_pcoip.shape[0]/10
    e= int(e) 
    #print(e)

    #print(test_pcoip.shape[1])
    f = test_pcoip.shape[1] 
    f= int(f) 
    #print(f)

    # Rebuild the table
    # transform the ranking of Strikes from vertical columns to horizontal rows for CALL OI

    # Rebuild the table
    # transform the ranking of Strikes from vertical columns to horizontal rows for PUT OI

    test_pcoip = pd.DataFrame(test_pcoip.values.reshape(e,f*10), 
                       columns=['COI_P_PITM_Strike1', 
                                'COI_P_PITM_Strike2', 
                                'COI_P_PITM_Strike3', 
                                'COI_P_PITM_Strike4',
                                'COI_P_PITM_Strike5',
                                'COI_P_POTM_Strike1', 
                                'COI_P_POTM_Strike2',
                                'COI_P_POTM_Strike3',
                                'COI_P_POTM_Strike4',
                                'COI_P_POTM_Strike5'])
    
    # Merge the CALL COI data to the main table
    Merge_CallPutOI_MaxPain = pd.concat([Merge_CallPutOI_MaxPain, test_pcoip], axis=1, join='inner')
    
    return Merge_CallPutOI_MaxPain


# In[ ]:





# In[22]:


def Call_COI_N_Top5(nifty_options, ui,Merge_CallPutOI_MaxPain):
   
   # Calculation for "Change in Open Interest" for CALL Options NEGATIVE VALUES
   # Shortlist Change in Open Interest Data for CALL ITM and CALL OTM Options

   test_ccoin_sample = nifty_options#.set_index(['Open', 'High', 'Low', 'Close','Strike']).groupby(['Date','ITM_OTM'])['CALL_COI'].nsmallest(10000).reset_index()   

   # Shortlist the data based on user input
   # Open Change of Interest Data for CALL ITM and PUT OTM Options on either side of the ATM, 
   # based on the number of strikes the user has selected

   #select_color = df.loc[df['Color'] == 'Green']
   test_ccoin_sample = test_ccoin_sample.loc[test_ccoin_sample['Strike'] < test_ccoin_sample['Close']+ui]
   test_ccoin_sample = test_ccoin_sample.loc[test_ccoin_sample['Strike'] > test_ccoin_sample['Close']-ui]
   # or test111['Strike'] < test111['Close']+500]

       # Shortlist the data based on Top 5, Highest 'Change in OpenInterest"  Values
   # Shortlist Top 5, Highest OpenInterest  Values for CALL ITM and CALL OTM Options on either side of the ATM,

   test_ccoin = test_ccoin_sample.set_index(['Open', 'High', 'Low', 'Close','Strike']).groupby(['Date','ITM_OTM'])['CALL_COI'].nsmallest(5).reset_index()   
   
   # Change the Column Header for Column = 'Strike'
   test_ccoin.rename(columns = {'Strike':'CallN_COI_Strike'}, inplace = True)

   #Drop the unwanted Columns that are not necessary for further processing
   test_ccoin.drop('Date', inplace=True, axis=1)
   test_ccoin.drop('ITM_OTM', inplace=True, axis=1)
   test_ccoin.drop('Open', inplace=True, axis=1)
   test_ccoin.drop('High', inplace=True, axis=1)
   test_ccoin.drop('Low', inplace=True, axis=1)
   test_ccoin.drop('Close', inplace=True, axis=1)
   test_ccoin.drop('CALL_COI', inplace=True, axis=1)
   
   #Calculate the size of the table for CALL OI
   #import numpy as np
   #print (np.reshape(test.values,(3,10)))
   #[['11' '12' '13' '14'   '15']
   #['21' '22' '23' '24' '25']]
   #print(test_ccoin.shape)
   e = test_ccoin.shape[0]/10
   e= int(e) 
   #print(e)

   #print(test_ccoin.shape[1])
   f = test_ccoin.shape[1] 
   f= int(f) 
   #print(f)

   # Rebuild the table
# transform the ranking of Strikes from vertical columns to horizontal rows for CALL OI

# Rebuild the table
# transform the ranking of Strikes from vertical columns to horizontal rows for PUT OI

   test_ccoin = pd.DataFrame(test_ccoin.values.reshape(e,f*10), 
                      columns=['COI_N_COTM_Strike1', 
                               'COI_N_COTM_Strike2', 
                               'COI_N_COTM_Strike3', 
                               'COI_N_COTM_Strike4',
                               'COI_N_COTM_Strike5',
                               'COI_N_CITM_Strike1', 
                               'COI_N_CITM_Strike2',
                               'COI_N_CITM_Strike3',
                               'COI_N_CITM_Strike4',
                               'COI_N_CITM_Strike5'])

   # Merge the CALL COI data to the main table

   Merge_CallPutOI_MaxPain = pd.concat([Merge_CallPutOI_MaxPain, test_ccoin], axis=1, join='inner')

   return Merge_CallPutOI_MaxPain


# In[ ]:





# In[23]:



def Call_OI_ITM_Chart(Merge_CallPutOI_MaxPain,no_levels):
    
    ip2=no_levels
    
    # Draw Candle Chart along with Call ITM
    fig2 = go.Figure(data=[go.Candlestick(x=Merge_CallPutOI_MaxPain['Date'],
                    open=Merge_CallPutOI_MaxPain['Open'],
                    high=Merge_CallPutOI_MaxPain['High'],
                    low=Merge_CallPutOI_MaxPain['Low'],
                    close=Merge_CallPutOI_MaxPain['Close'])])

    fig2.update_layout(legend_title_text = "CALL ITM Open Interest",autosize=True,width=1000, height=800)
    #fig2.update_layout(autosize=True,width=1000, height=800)
    #fig2.update_layout(width=1000, height=800)
    fig2.update_xaxes(title_text="Date")
    fig2.update_yaxes(title_text="NIFTY50 Index Strike Price")
    #fig2.Title( "CALL ITM Open Interest")
    #plotly.graph_objects.layout.Title
    #fig.data[0].marker.color = 'green'
    fig2.update_yaxes(automargin=True) 

    if ip2 == 1:
                 fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_CITM_Strike1"],mode='lines',
                        line = {'color' : 'red'}, name='Call ITM OI High1'))
    elif ip2 == 2:

                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_CITM_Strike2"],
                         line = {'color' : 'blue'},mode='lines',name='Call ITM OI High2'))
    elif ip2 == 3:

                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_CITM_Strike3"],
                                 line = {'color' : 'green'},mode='lines', name='Call ITM OI High3'))
    elif ip2 == 4:

                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_CITM_Strike4"],
                        mode='lines', name='Call ITM OI High2'))
    elif ip2 == 5:
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_CITM_Strike5"],
                        mode='lines', name='Call ITM OI High1'))

    elif ip2 == 6:
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_CITM_Strike1"],mode='lines',
                                name='Call ITM OI Highest'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_CITM_Strike2"],
                                mode='lines',name='Call ITM OI Higher'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_CITM_Strike3"],
                                mode='lines', name='Call ITM OI High1'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_CITM_Strike4"],
                                mode='lines', name='Call ITM OI High2'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_CITM_Strike5"],
                                mode='lines', name='Call ITM OI High3'))
    elif ip2 == 7:
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_CITM_Strike1"],mode='lines',
                         line = {'color' : 'red'},name='Call ITM OI High1'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_CITM_Strike2"],
                         line = {'color' : 'blue'},mode='lines',name='Call ITM OI High2'))




    fig2.show()
    return


# In[ ]:





# In[24]:


def Call_OI_OTM_Chart(Merge_CallPutOI_MaxPain,no_levels):
    
    ip2=no_levels
    
        # Draw Candle Chart along with Call OTM
    fig2 = go.Figure(data=[go.Candlestick(x=Merge_CallPutOI_MaxPain['Date'],
                    open=Merge_CallPutOI_MaxPain['Open'],
                    high=Merge_CallPutOI_MaxPain['High'],
                    low=Merge_CallPutOI_MaxPain['Low'],
                    close=Merge_CallPutOI_MaxPain['Close'])])


    fig2.update_layout(legend_title_text = "CALL OTM Open Interest",autosize=True,width=1000, height=800)
    #fig2.update_layout(autosize=True,width=1000, height=800)
    #fig2.update_layout(width=1000, height=800)
    fig2.update_xaxes(title_text="Date")
    fig2.update_yaxes(title_text="NIFTY50 Index Strike Price")
    #fig2.Title( "CALL ITM Open Interest")
    #plotly.graph_objects.layout.Title
    #fig.data[0].marker.color = 'green'
    fig2.update_yaxes(automargin=True) 


    if ip2 == 1:
                 fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_COTM_Strike1"],mode='lines',
                        name='Call OTM OI High1'))
    elif ip2 == 2:

                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_COTM_Strike2"],
                        mode='lines',name='Call OTM OI High2'))
    elif ip2 == 3:

                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_COTM_Strike3"],
                                mode='lines', name='Call OTM OI High3'))
    elif ip2 == 4:

                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_COTM_Strike4"],
                        mode='lines', name='Call OTM OI High2'))
    elif ip2 == 5:
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_COTM_Strike5"],
                        mode='lines', name='Call OTM OI High1'))

    elif ip2 == 6:
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_COTM_Strike1"],mode='lines',
                                name='Call OTM OI Highest'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_COTM_Strike2"],
                                mode='lines',name='Call OTM OI Higher'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_COTM_Strike3"],
                                mode='lines', name='Call OTM OI High1'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_COTM_Strike4"],
                                mode='lines', name='Call OTM OI High2'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_COTM_Strike5"],
                                mode='lines', name='Call OTM OI High3'))
    elif ip2 == 7:
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_COTM_Strike1"],mode='lines',
                        name='Call OTM OI High1'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_COTM_Strike2"],
                        mode='lines',name='Call OTM OI High2'))



    fig2.show()
    return
    
    


# In[ ]:





# In[25]:



def Put_OI_OTM_Chart(Merge_CallPutOI_MaxPain,no_levels):
        
    ip2=no_levels
        
        # Draw Candle Chart along with PUT OTM
    fig2 = go.Figure(data=[go.Candlestick(x=Merge_CallPutOI_MaxPain['Date'],
                    open=Merge_CallPutOI_MaxPain['Open'],
                    high=Merge_CallPutOI_MaxPain['High'],
                    low=Merge_CallPutOI_MaxPain['Low'],
                    close=Merge_CallPutOI_MaxPain['Close'])])


    fig2.update_layout(legend_title_text = "PUT OTM Open Interest",autosize=True,width=1000, height=800)
    #fig2.update_layout(autosize=True,width=1000, height=800)
    #fig2.update_layout(width=1000, height=800)
    fig2.update_xaxes(title_text="Date")
    fig2.update_yaxes(title_text="NIFTY50 Index Strike Price")
    #fig2.Title( "CALL ITM Open Interest")
    #plotly.graph_objects.layout.Title
    #fig.data[0].marker.color = 'green'
    fig2.update_yaxes(automargin=True) 


    if ip2 == 1:
                 fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_POTM_Strike1"],mode='lines',
                        name='Put OTM OI High1'))
    elif ip2 == 2:

                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_POTM_Strike2"],
                        mode='lines',name='Put OTM OI High2'))
    elif ip2 == 3:

                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_POTM_Strike3"],
                                mode='lines', name='Put OTM OI High3'))
    elif ip2 == 4:

                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_POTM_Strike4"],
                        mode='lines', name='Put OTM OI High2'))
    elif ip2 == 5:
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_POTM_Strike5"],
                        mode='lines', name='Put OTM OI High1'))

    elif ip2 == 6:
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_POTM_Strike1"],mode='lines',
                                name='Put OTM OI Highest'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_POTM_Strike2"],
                                mode='lines',name='Put OTM OI Higher'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_POTM_Strike3"],
                                mode='lines', name='Put OTM OI High1'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_POTM_Strike4"],
                                mode='lines', name='Put OTM OI High2'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_POTM_Strike5"],
                                mode='lines', name='Put OTM OI High3'))
    elif ip2 == 7:
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_POTM_Strike1"],mode='lines',
                                    name='Put OTM OI High1'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_POTM_Strike2"],
                        mode='lines',name='Put OTM OI High2'))


    fig2.show()
    return


# In[ ]:





# In[26]:


def Nifty_OHLC_Chart(Merge_CallPutOI_MaxPain):
         # Plot the OHLC graph

    #fig = px.line(test, x="Date_CITM1", y="Open_CITM1",  title='OHLC Chart',color='Open_CITM1')
    #fig = go.Figure(data=go.Scatter( x=test["Date_CITM1"], y=test["Open_CITM1"]))

    fig2 = go.Figure()

    fig2.update_layout(legend_title_text = "OHLC Graph for NIFTY 50 Index",autosize=True,width=1000, height=800)
    #fig2.update_layout(autosize=True,width=1000, height=800)
    #fig2.update_layout(width=1000, height=800)
    fig2.update_xaxes(title_text="Date")
    fig2.update_yaxes(title_text="NIFTY50 Index Strike Price")
    #fig2.Title( "CALL ITM Open Interest")
    #plotly.graph_objects.layout.Title
    #fig.data[0].marker.color = 'green'
    fig2.update_yaxes(automargin=True) 

    fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["Open"], mode='markers', name='Open'))
    fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["High"], mode='lines', name='High'))
    fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["Low"], mode='lines', name='Low'))
    fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["Close"], mode='markers', name='Close'))

    fig2.show()
    
    return


# In[ ]:





# In[27]:


def CallPut_OI_OTM_Chart(Merge_CallPutOI_MaxPain,no_levels):
    
    
        # Draw Candle Chart along with Call OTM and PUT OTM [COPO]
    fig2 = go.Figure(data=[go.Candlestick(x=Merge_CallPutOI_MaxPain['Date'],
                    open=Merge_CallPutOI_MaxPain['Open'],
                    high=Merge_CallPutOI_MaxPain['High'],
                    low=Merge_CallPutOI_MaxPain['Low'],
                    close=Merge_CallPutOI_MaxPain['Close'])])

    fig2.update_layout(legend_title_text = "CALL OTM, PUT OTM Open Interest",autosize=True,width=1000, height=800)
    #fig2.update_layout(autosize=True,width=1000, height=800)
    #fig2.update_layout(width=1000, height=800)
    fig2.update_xaxes(title_text="Date")
    fig2.update_yaxes(title_text="NIFTY50 Index Strike Price")
    #fig2.Title( "CALL ITM Open Interest")
    #plotly.graph_objects.layout.Title
    #fig.data[0].marker.color = 'green'
    fig2.update_yaxes(automargin=True) 

    #fig = go.Figure()
    fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_COTM_Strike5"],mode='lines',
                        name='Call OTM OI Highest'))
    #fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_COTM_Strike2"],
    #                    mode='lines',name='Call OTM OI Higher'))
    #fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date_CITM1"], y=Merge_CallPutOI_MaxPain["OI_CITM_Strike3"],
    #                    mode='markers', name='High1'))
    #fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date_CITM1"], y=Merge_CallPutOI_MaxPain["OI_CITM_Strike4"],
    #                    mode='markers', name='High2'))
    #fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date_CITM1"], y=Merge_CallPutOI_MaxPain["OI_CITM_Strike5"],
    #                    mode='markers', name='High3'))
    1
    fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_POTM_Strike5"],
                        mode='lines', name='Put OTM OI Highest'))
    #fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_POTM_Strike2"],
    #                    mode='lines',name='Put OTM OI Higher'))
    fig2.show()
    return


# In[ ]:





# In[28]:


def Put_OI_ITM_Chart(Merge_CallPutOI_MaxPain,no_levels):
    
    ip2=no_levels
    
    # Draw Candle Chart along with PUT ITM
    fig2 = go.Figure(data=[go.Candlestick(x=Merge_CallPutOI_MaxPain['Date'],
                    open=Merge_CallPutOI_MaxPain['Open'],
                    high=Merge_CallPutOI_MaxPain['High'],
                    low=Merge_CallPutOI_MaxPain['Low'],
                    close=Merge_CallPutOI_MaxPain['Close'])])


    fig2.update_layout(legend_title_text = "PUT ITM Open Interest",autosize=True,width=1000, height=800)
    #fig2.update_layout(autosize=True,width=1000, height=800)
    #fig2.update_layout(width=1000, height=800)
    fig2.update_xaxes(title_text="Date")
    fig2.update_yaxes(title_text="NIFTY50 Index Strike Price")
    #fig2.Title( "CALL ITM Open Interest")
    #plotly.graph_objects.layout.Title
    #fig.data[0].marker.color = 'green'
    fig2.update_yaxes(automargin=True) 


    if ip2 == 1:
                 fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_PITM_Strike1"],mode='lines',
                        name='Put ITM OI High1'))
    elif ip2 == 2:

                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_PITM_Strike2"],
                        mode='lines',name='Put ITM OI High2'))
    elif ip2 == 3:

                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_PITM_Strike3"],
                                mode='lines', name='Put ITM OI High3'))
    elif ip2 == 4:

                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_PITM_Strike4"],
                        mode='lines', name='Put ITM OI High2'))
    elif ip2 == 5:
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_PITM_Strike5"],
                        mode='lines', name='Put ITM OI High1'))

    elif ip2 == 6:
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_PITM_Strike1"],mode='lines',
                                name='Put ITM OI Highest'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_PITM_Strike2"],
                                mode='lines',name='Put ITM OI Higher'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_PITM_Strike3"],
                                mode='lines', name='Put ITM OI High1'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_PITM_Strike4"],
                                mode='lines', name='Put ITM OI High2'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_PITM_Strike5"],
                                mode='lines', name='Put ITM OI High3'))
    elif ip2 == 7:
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_PITM_Strike1"],mode='lines',
                                    name='Put ITM OI High1'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["OI_PITM_Strike2"],
                        mode='lines',name='Put ITM OI High2'))


    fig2.show()
    return


# In[ ]:





# In[29]:


def Call_OI_ITM_Scatter_Chart(Merge_CallPutOI_MaxPain):
        
        # Scatter Plot showing CALL ITM with respect to  close price

    #plt.scatter(nifty_options['Date'], nifty_options['CALL_OI'].astype(float)) #,  nifty_options['PUT COI'])
    plt.scatter(Merge_CallPutOI_MaxPain['Date'], Merge_CallPutOI_MaxPain['OI_CITM_Strike1'], color = 'red', label = "Call ITM OI Highest") #,  nifty_options['PUT COI'])
    plt.scatter(Merge_CallPutOI_MaxPain['Date'], Merge_CallPutOI_MaxPain['OI_CITM_Strike2'], color = 'blue', label = "Call ITM OI Higher") #,  nifty_options['PUT COI'])
    #plt.plot(test['Date_CITM1'], test['CALL_OI_ITM_Strike3'], color = 'green', label = "High 1") #,  nifty_options['PUT COI'])
    #plt.plot(test['Date_CITM1'], test['CALL_OI_ITM_Strike4'], color = 'yellow', label = "High 2") #,  nifty_options['PUT COI'])
    #plt.plot(test['Date_CITM1'], test['CALL_OI_ITM_Strike5'], color = 'cyan', label = "High 3") #,  nifty_options['PUT COI'])


    #plt.scatter(test['Date_CITM1'], test['Open_CITM1'], color = 'pink', label = "Highest") #,  nifty_options['PUT COI'])
    #plt.scatter(test['Date_CITM1'], test['High_CITM1'], color = 'red', label = "Highest") #,  nifty_options['PUT COI'])
    #plt.scatter(test['Date_CITM1'], test['Low_CITM1'], color = 'Green', label = "Highest") #,  nifty_options['PUT COI'])
    plt.scatter(Merge_CallPutOI_MaxPain['Date'], Merge_CallPutOI_MaxPain['Close'], color = 'black', label = "Close") #,  nifty_options['PUT COI'])

    #plt.scatter(test['Date_CITM1'], test['CALL_OI_OTM_Strike1'], color = 'blue', label = "Highest") #,  nifty_options['PUT COI'])

    #plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
    #         marker='o', markerfacecolor='blue', markersize=12)

    #plt.bar(left, height, tick_label = tick_label,
    #        width = 0.8, color = ['red', 'green'])

    #plt.hist(ages, bins, range, color = 'green',
    #        histtype = 'bar', rwidth = 0.8)

    plt.xlabel('Date')
    plt.ylabel('Strike Price')
    plt.title("CALL ITM OI Graph")
    plt.legend()


    plt.show()

    return


# In[ ]:





# In[30]:


def OHLC_Chart_MaxPain(Merge_CallPutOI_MaxPain):
    # Plot the OHLC graph and MaxPain

    #fig = px.line(test, x="Date_CITM1", y="Open_CITM1",  title='OHLC Chart',color='Open_CITM1')
    #fig = go.Figure(data=go.Scatter( x=test["Date_CITM1"], y=test["Open_CITM1"]))

    fig2 = go.Figure()

    fig2.update_layout(legend_title_text = "ITM and OTM Max Pain Points",autosize=True,width=1000, height=800)
    #fig2.update_layout(autosize=True,width=1000, height=800)
    #fig2.update_layout(width=1000, height=800)
    fig2.update_xaxes(title_text="Date")
    fig2.update_yaxes(title_text="NIFTY50 Index Strike Price")
    #fig2.Title( "CALL ITM Open Interest")
    #plotly.graph_objects.layout.Title
    #fig.data[0].marker.color = 'green'
    fig2.update_yaxes(automargin=True) 


    #fig.add_trace(go.Scatter(x=MaxPain_IOTM_Top1["Date"], y=MaxPain_IOTM_Top1["Open"], mode='markers', name='Open'))
    #fig.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=MaxPain_IOTM_Top1["High"], mode='lines', name='High'))
    #fig.add_trace(go.Scatter(x=MaxPain_IOTM_Top1["Date"], y=MaxPain_IOTM_Top1["Low"], mode='lines', name='Low'))
    fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=MaxPain_IOTM_Top1["Close"], mode='lines', name='Close'))


    fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=MaxPain_IOTM_Top1["MaxPain_Strike"], mode='markers',name='ITM and OTM Max Pain Point '))
    #fig.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=MaxPain_IOTM_Top1["High"], mode='lines', name='High'))
    #fig.add_trace(go.Scatter(x=MaxPain_IOTM_Top1["Date"], y=MaxPain_IOTM_Top1["Low"], mode='lines', name='Low'))
    #fig.add_trace(go.Scatter(x=MaxPain_IOTM_Top1["Date"], y=MaxPain_IOTM_Top1["Close"], mode='markers', name='Close'))


    fig2.show()
    return


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[31]:


def Put_COI_N_OTM_Chart(Merge_CallPutOI_MaxPain,no_levels):
    
    ip2 = no_levels
    # Draw Candle Chart along with Chaneg of OI for Call OTM Positive Values 
    fig2 = go.Figure(data=[go.Candlestick(x=Merge_CallPutOI_MaxPain['Date'],
                    open=Merge_CallPutOI_MaxPain['Open'],
                    high=Merge_CallPutOI_MaxPain['High'],
                    low=Merge_CallPutOI_MaxPain['Low'],
                    close=Merge_CallPutOI_MaxPain['Close'])])

    fig2.update_layout(legend_title_text = "PUT OTM COI Negative",autosize=True,width=1000, height=800)
    #fig2.update_layout(autosize=True,width=1000, height=800)
    #fig2.update_layout(width=1000, height=800)
    fig2.update_xaxes(title_text="Date")
    fig2.update_yaxes(title_text="NIFTY50 Index Strike Price")
    #fig2.Title( "CALL ITM Open Interest")
    #plotly.graph_objects.layout.Title
    #fig.data[0].marker.color = 'green'
    fig2.update_yaxes(automargin=True)

    if ip2 == 1:
                 fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_COTM_Strike1"],mode='lines',
                        name='Put OTM COI- High1'))
    elif ip2 == 2:

                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_COTM_Strike2"],
                        mode='lines',name='Put OTM COI- High2'))
    elif ip2 == 3:

                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_COTM_Strike3"],
                                mode='lines', name='Put OTM COI- High3'))
    elif ip2 == 4:

                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_COTM_Strike4"],
                        mode='lines', name='Put OTM COI- High2'))
    elif ip2 == 5:
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_COTM_Strike5"],
                        mode='lines', name='Put OTM COI- High1'))

    elif ip2 == 6:
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_COTM_Strike1"],mode='lines',
                                name='Put OTM COI- High1'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_COTM_Strike2"],
                                mode='lines',name='Put OTM COI- High2'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_COTM_Strike3"],
                                mode='lines', name='Put OTM COI- High1'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_COTM_Strike4"],
                                mode='lines', name='Put OTM COI- High2'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_COTM_Strike5"],
                                mode='lines', name='Put OTM COI- High3'))
    elif ip2 == 7:
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_COTM_Strike1"],mode='lines',
                        name='Put OTM COI- High1'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_COTM_Strike2"],
                        mode='lines',name='Put OTM COI- High2'))




    fig2.show()
    
    return


# In[ ]:





# In[32]:



def Call_COI_P_OTM_Chart(Merge_CallPutOI_MaxPain,no_levels):
ip2 = no_levels

# Draw Candle Chart along with Chaneg of OI for Call OTM Positive Values 
fig2 = go.Figure(data=[go.Candlestick(x=Merge_CallPutOI_MaxPain['Date'],
                open=Merge_CallPutOI_MaxPain['Open'],
                high=Merge_CallPutOI_MaxPain['High'],
                low=Merge_CallPutOI_MaxPain['Low'],
                close=Merge_CallPutOI_MaxPain['Close'])])


fig2.update_layout(legend_title_text = "CALL OTM COI Positive",autosize=True,width=1000, height=800)
#fig2.update_layout(autosize=True,width=1000, height=800)
#fig2.update_layout(width=1000, height=800)
fig2.update_xaxes(title_text="Date")
fig2.update_yaxes(title_text="NIFTY50 Index Strike Price")
#fig2.Title( "CALL ITM Open Interest")
#plotly.graph_objects.layout.Title
#fig.data[0].marker.color = 'green'
fig2.update_yaxes(automargin=True) 


if ip2 == 1:
             fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_COTM_Strike1"],mode='lines',
                    name='Call OTM COI+ High1'))
elif ip2 == 2:

            fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_COTM_Strike2"],
                    mode='lines',name='Call OTM COI+ High2'))
elif ip2 == 3:

            fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_COTM_Strike3"],
                            mode='lines', name='Call OTM COI+ High3'))
elif ip2 == 4:

            fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_COTM_Strike4"],
                    mode='lines', name='Call OTM COI+ High2'))
elif ip2 == 5:
            fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_COTM_Strike5"],
                    mode='lines', name='Call OTM COI+ High1'))

elif ip2 == 6:
            fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_COTM_Strike1"],mode='lines',
                            name='Call OTM COI+ High1'))
            fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_COTM_Strike2"],
                            mode='lines',name='Call OTM COI+ High2'))
            fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_COTM_Strike3"],
                            mode='lines', name='Call OTM COI+ High1'))
            fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_COTM_Strike4"],
                            mode='lines', name='Call OTM COI+ High2'))
            fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_COTM_Strike5"],
                            mode='lines', name='Call OTM COI+ High3'))
elif ip2 == 7:
            fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_COTM_Strike1"],mode='lines',
                    name='Call OTM COI+ High1'))
            fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_COTM_Strike2"],
                    mode='lines',name='Call OTM COI+ High2'))




fig2.show()


return 


# In[ ]:





# In[33]:


def Call_COI_N_OTM_Chart(Merge_CallPutOI_MaxPain,no_levels):
    
    ip2 = no_levels
    
        # Draw Candle Chart along with Chaneg of OI for Call OTM NEGATIVE Values 
    fig2 = go.Figure(data=[go.Candlestick(x=Merge_CallPutOI_MaxPain['Date'],
                    open=Merge_CallPutOI_MaxPain['Open'],
                    high=Merge_CallPutOI_MaxPain['High'],
                    low=Merge_CallPutOI_MaxPain['Low'],
                    close=Merge_CallPutOI_MaxPain['Close'])])

    fig2.update_layout(legend_title_text = "CALL OTM COI Negative",autosize=True,width=1000, height=800)
    #fig2.update_layout(autosize=True,width=1000, height=800)
    #fig2.update_layout(width=1000, height=800)
    fig2.update_xaxes(title_text="Date")
    fig2.update_yaxes(title_text="NIFTY50 Index Strike Price")
    #fig2.Title( "CALL ITM Open Interest")
    #plotly.graph_objects.layout.Title
    #fig.data[0].marker.color = 'green'
    fig2.update_yaxes(automargin=True)

    if ip2 == 1:
                 fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_N_COTM_Strike1"],mode='lines',
                        name='Call OTM COI- High1'))
    elif ip2 == 2:

                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_N_COTM_Strike2"],
                        mode='lines',name='Call OTM COI- High2'))
    elif ip2 == 3:

                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_N_COTM_Strike3"],
                                mode='lines', name='Call OTM COI- High3'))
    elif ip2 == 4:

                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_N_COTM_Strike4"],
                        mode='lines', name='Call OTM COI- High2'))
    elif ip2 == 5:
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_N_COTM_Strike5"],
                        mode='lines', name='Call OTM COI- High1'))

    elif ip2 == 6:
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_N_COTM_Strike1"],mode='lines',
                                name='Call OTM COI- High1'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_N_COTM_Strike2"],
                                mode='lines',name='Call OTM COI- High2'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_N_COTM_Strike3"],
                                mode='lines', name='Call OTM COI- High1'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_N_COTM_Strike4"],
                                mode='lines', name='Call OTM COI- High2'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_N_COTM_Strike5"],
                                mode='lines', name='Call OTM COI- High3'))
    elif ip2 == 7:
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_N_COTM_Strike1"],mode='lines',
                        name='Call OTM COI- High1'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_N_COTM_Strike2"],
                        mode='lines',name='Call OTM COI- High2'))




    fig2.show()
    return


# In[ ]:





# In[34]:


def Put_COI_P_OTM_Chart(Merge_CallPutOI_MaxPain,no_levels):
    
    ip2 = no_levels
    
        # Draw Candle Chart along with Chaneg of OI for PUT OTM Positive Values 
    fig2 = go.Figure(data=[go.Candlestick(x=Merge_CallPutOI_MaxPain['Date'],
                    open=Merge_CallPutOI_MaxPain['Open'],
                    high=Merge_CallPutOI_MaxPain['High'],
                    low=Merge_CallPutOI_MaxPain['Low'],
                    close=Merge_CallPutOI_MaxPain['Close'])])

    fig2.update_layout(legend_title_text = "PUT OTM COI Positive",autosize=True,width=1000, height=800)
    #fig2.update_layout(autosize=True,width=1000, height=800)
    #fig2.update_layout(width=1000, height=800)
    fig2.update_xaxes(title_text="Date")
    fig2.update_yaxes(title_text="NIFTY50 Index Strike Price")
    #fig2.Title( "CALL ITM Open Interest")
    #plotly.graph_objects.layout.Title
    #fig.data[0].marker.color = 'green'
    fig2.update_yaxes(automargin=True)

    if ip2 == 1:
                 fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_POTM_Strike1"],mode='lines',
                        name='Put OTM COI+ High1'))
    elif ip2 == 2:

                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_POTM_Strike2"],
                        mode='lines',name='Put OTM COI+ High2'))
    elif ip2 == 3:

                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_POTM_Strike3"],
                                mode='lines', name='Put OTM COI+ High3'))
    elif ip2 == 4:

                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_POTM_Strike4"],
                        mode='lines', name='Put OTM COI+ High2'))
    elif ip2 == 5:
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_POTM_Strike5"],
                        mode='lines', name='Put OTM COI+ High1'))

    elif ip2 == 6:
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_POTM_Strike1"],mode='lines',
                                name='Put OTM COI+ High1'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_POTM_Strike2"],
                                mode='lines',name='Put OTM COI+ High2'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_POTM_Strike3"],
                                mode='lines', name='Put OTM COI+ High1'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_POTM_Strike4"],
                                mode='lines', name='Put OTM COI+ High2'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_POTM_Strike5"],
                                mode='lines', name='Put OTM COI+ High3'))
    elif ip2 == 7:
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_POTM_Strike1"],mode='lines',
                        name='Put OTM COI+ High1'))
                fig2.add_trace(go.Scatter(x=Merge_CallPutOI_MaxPain["Date"], y=Merge_CallPutOI_MaxPain["COI_P_POTM_Strike2"],
                        mode='lines',name='Put OTM COI+ High2'))




    fig2.show()
    
    return


# In[ ]:





# In[35]:


def Candle_Chart(Merge_CallPutOI_MaxPain):
    #Draw Candle Chart for the given period
    fig1 = go.Figure(data=[go.Candlestick(x=Merge_CallPutOI_MaxPain['Date'],
                    open=Merge_CallPutOI_MaxPain['Open'],
                    high=Merge_CallPutOI_MaxPain['High'],
                    low=Merge_CallPutOI_MaxPain['Low'],
                    close=Merge_CallPutOI_MaxPain['Close'])])
    #fig1.update_layout(legend_title_text = "NIFTY")

    fig1.update_layout(legend_title_text = "NIFTY 50 Index",autosize=True,width=1000, height=800)
    #fig2.update_layout(autosize=True,width=1000, height=800)
    #fig2.update_layout(width=1000, height=800)
    fig1.update_xaxes(title_text="Date")
    fig1.update_yaxes(title_text="NIFTY50 Index Strike Price")
    #fig2.Title( "CALL ITM Open Interest")
    #plotly.graph_objects.layout.Title
    #fig.data[0].marker.color = 'green'
    fig1.update_yaxes(automargin=True) 

    fig1.show()
    return


# In[ ]:





# In[ ]:





# Analyse_COI(Merge_CallPutOI_MaxPain): 
# The Change in Open Interest data will be analysed
# There are Six combinations of Call, Put, ITM,  OTM, Positive and Negative COI 
# values for the options Open Interest. 
# All these details are merged with Merge_CallPutOI_MaxPain dataframe.
# 

# In[36]:


def Analyse_COI(Merge_CallPutOI_MaxPain):
    
    import numpy as np

    a_a = Merge_CallPutOI_MaxPain[['Date']]
    mt = Merge_CallPutOI_MaxPain


    a_a['Delta_Close']           = np.where((mt['Close']           > mt['Close'].shift(1))          ,1,np.where((mt['Close']           < mt['Close'].shift(1)),-1,0))
    a_a['Delta_COI_P_COTM_Strike1'] = np.where((mt['COI_P_COTM_Strike1'] > mt['COI_P_COTM_Strike1'].shift(1)),1,np.where((mt['COI_P_COTM_Strike1'] < mt['COI_P_COTM_Strike1'].shift(1)),-1,0))
    a_a['Delta_COI_P_COTM_Strike2'] = np.where((mt['COI_P_COTM_Strike2'] > mt['COI_P_COTM_Strike2'].shift(1)),1,np.where((mt['COI_P_COTM_Strike2'] < mt['COI_P_COTM_Strike2'].shift(1)),-1,0))
    a_a['Delta_COI_P_COTM_Strike3'] = np.where((mt['COI_P_COTM_Strike3'] > mt['COI_P_COTM_Strike3'].shift(1)),1,np.where((mt['COI_P_COTM_Strike3'] < mt['COI_P_COTM_Strike3'].shift(1)),-1,0))
    a_a['Delta_COI_P_COTM_Strike4'] = np.where((mt['COI_P_COTM_Strike4'] > mt['COI_P_COTM_Strike4'].shift(1)),1,np.where((mt['COI_P_COTM_Strike4'] < mt['COI_P_COTM_Strike4'].shift(1)),-1,0))
    a_a['Delta_COI_P_COTM_Strike5'] = np.where((mt['COI_P_COTM_Strike5'] > mt['COI_P_COTM_Strike5'].shift(1)),1,np.where((mt['COI_P_COTM_Strike5'] < mt['COI_P_COTM_Strike5'].shift(1)),-1,0))
    a_a['Delta_COI_N_COTM_Strike1'] = np.where((mt['COI_N_COTM_Strike1'] > mt['COI_N_COTM_Strike1'].shift(1)),1,np.where((mt['COI_N_COTM_Strike1'] < mt['COI_N_COTM_Strike1'].shift(1)),-1,0))
    a_a['Delta_COI_N_COTM_Strike2'] = np.where((mt['COI_N_COTM_Strike2'] > mt['COI_N_COTM_Strike2'].shift(1)),1,np.where((mt['COI_N_COTM_Strike2'] < mt['COI_N_COTM_Strike2'].shift(1)),-1,0))
    a_a['Delta_COI_N_COTM_Strike3'] = np.where((mt['COI_N_COTM_Strike3'] > mt['COI_N_COTM_Strike3'].shift(1)),1,np.where((mt['COI_N_COTM_Strike3'] < mt['COI_N_COTM_Strike3'].shift(1)),-1,0))
    a_a['Delta_COI_N_COTM_Strike4'] = np.where((mt['COI_N_COTM_Strike4'] > mt['COI_N_COTM_Strike4'].shift(1)),1,np.where((mt['COI_N_COTM_Strike4'] < mt['COI_N_COTM_Strike4'].shift(1)),-1,0))
    a_a['Delta_COI_N_COTM_Strike5'] = np.where((mt['COI_N_COTM_Strike5'] > mt['COI_N_COTM_Strike5'].shift(1)),1,np.where((mt['COI_N_COTM_Strike5'] < mt['COI_N_COTM_Strike5'].shift(1)),-1,0))
    a_a['Delta_COI_P_CITM_Strike1'] = np.where((mt['COI_P_CITM_Strike1'] > mt['COI_P_CITM_Strike1'].shift(1)),1,np.where((mt['COI_P_CITM_Strike1'] < mt['COI_P_CITM_Strike1'].shift(1)),-1,0))
    a_a['Delta_COI_P_CITM_Strike2'] = np.where((mt['COI_P_CITM_Strike2'] > mt['COI_P_CITM_Strike2'].shift(1)),1,np.where((mt['COI_P_CITM_Strike2'] < mt['COI_P_CITM_Strike2'].shift(1)),-1,0))
    a_a['Delta_COI_P_CITM_Strike3'] = np.where((mt['COI_P_CITM_Strike3'] > mt['COI_P_CITM_Strike3'].shift(1)),1,np.where((mt['COI_P_CITM_Strike3'] < mt['COI_P_CITM_Strike3'].shift(1)),-1,0))
    a_a['Delta_COI_P_CITM_Strike4'] = np.where((mt['COI_P_CITM_Strike4'] > mt['COI_P_CITM_Strike4'].shift(1)),1,np.where((mt['COI_P_CITM_Strike4'] < mt['COI_P_CITM_Strike4'].shift(1)),-1,0))
    a_a['Delta_COI_P_CITM_Strike5'] = np.where((mt['COI_P_CITM_Strike5'] > mt['COI_P_CITM_Strike5'].shift(1)),1,np.where((mt['COI_P_CITM_Strike5'] < mt['COI_P_CITM_Strike5'].shift(1)),-1,0))
    a_a['Delta_COI_N_CITM_Strike1'] = np.where((mt['COI_N_CITM_Strike1'] > mt['COI_N_CITM_Strike1'].shift(1)),1,np.where((mt['COI_N_CITM_Strike1'] < mt['COI_N_CITM_Strike1'].shift(1)),-1,0))
    a_a['Delta_COI_N_CITM_Strike2'] = np.where((mt['COI_N_CITM_Strike2'] > mt['COI_N_CITM_Strike2'].shift(1)),1,np.where((mt['COI_N_CITM_Strike2'] < mt['COI_N_CITM_Strike2'].shift(1)),-1,0))
    a_a['Delta_COI_N_CITM_Strike3'] = np.where((mt['COI_N_CITM_Strike3'] > mt['COI_N_CITM_Strike3'].shift(1)),1,np.where((mt['COI_N_CITM_Strike3'] < mt['COI_N_CITM_Strike3'].shift(1)),-1,0))
    a_a['Delta_COI_N_CITM_Strike4'] = np.where((mt['COI_N_CITM_Strike4'] > mt['COI_N_CITM_Strike4'].shift(1)),1,np.where((mt['COI_N_CITM_Strike4'] < mt['COI_N_CITM_Strike4'].shift(1)),-1,0))
    a_a['Delta_COI_N_CITM_Strike5'] = np.where((mt['COI_N_CITM_Strike5'] > mt['COI_N_CITM_Strike5'].shift(1)),1,np.where((mt['COI_N_CITM_Strike5'] < mt['COI_N_CITM_Strike5'].shift(1)),-1,0))
    a_a['Delta_COI_P_POTM_Strike1'] = np.where((mt['COI_P_POTM_Strike1'] > mt['COI_P_POTM_Strike1'].shift(1)),1,np.where((mt['COI_P_POTM_Strike1'] < mt['COI_P_POTM_Strike1'].shift(1)),-1,0))
    a_a['Delta_COI_P_POTM_Strike2'] = np.where((mt['COI_P_POTM_Strike2'] > mt['COI_P_POTM_Strike2'].shift(1)),1,np.where((mt['COI_P_POTM_Strike2'] < mt['COI_P_POTM_Strike2'].shift(1)),-1,0))
    a_a['Delta_COI_P_POTM_Strike3'] = np.where((mt['COI_P_POTM_Strike3'] > mt['COI_P_POTM_Strike3'].shift(1)),1,np.where((mt['COI_P_POTM_Strike3'] < mt['COI_P_POTM_Strike3'].shift(1)),-1,0))
    a_a['Delta_COI_P_POTM_Strike4'] = np.where((mt['COI_P_POTM_Strike4'] > mt['COI_P_POTM_Strike4'].shift(1)),1,np.where((mt['COI_P_POTM_Strike4'] < mt['COI_P_POTM_Strike4'].shift(1)),-1,0))
    a_a['Delta_COI_P_POTM_Strike5'] = np.where((mt['COI_P_POTM_Strike5'] > mt['COI_P_POTM_Strike5'].shift(1)),1,np.where((mt['COI_P_POTM_Strike5'] < mt['COI_P_POTM_Strike5'].shift(1)),-1,0))
    a_a['Delta_COI_N_POTM_Strike1'] = np.where((mt['COI_N_POTM_Strike1'] > mt['COI_N_POTM_Strike1'].shift(1)),1,np.where((mt['COI_N_POTM_Strike1'] < mt['COI_N_POTM_Strike1'].shift(1)),-1,0))
    a_a['Delta_COI_N_POTM_Strike2'] = np.where((mt['COI_N_POTM_Strike2'] > mt['COI_N_POTM_Strike2'].shift(1)),1,np.where((mt['COI_N_POTM_Strike2'] < mt['COI_N_POTM_Strike2'].shift(1)),-1,0))
    a_a['Delta_COI_N_POTM_Strike3'] = np.where((mt['COI_N_POTM_Strike3'] > mt['COI_N_POTM_Strike3'].shift(1)),1,np.where((mt['COI_N_POTM_Strike3'] < mt['COI_N_POTM_Strike3'].shift(1)),-1,0))
    a_a['Delta_COI_N_POTM_Strike4'] = np.where((mt['COI_N_POTM_Strike4'] > mt['COI_N_POTM_Strike4'].shift(1)),1,np.where((mt['COI_N_POTM_Strike4'] < mt['COI_N_POTM_Strike4'].shift(1)),-1,0))
    a_a['Delta_COI_N_POTM_Strike5'] = np.where((mt['COI_N_POTM_Strike5'] > mt['COI_N_POTM_Strike5'].shift(1)),1,np.where((mt['COI_N_POTM_Strike5'] < mt['COI_N_POTM_Strike5'].shift(1)),-1,0))
    a_a['Delta_COI_P_PITM_Strike1'] = np.where((mt['COI_P_PITM_Strike1'] > mt['COI_P_PITM_Strike1'].shift(1)),1,np.where((mt['COI_P_PITM_Strike1'] < mt['COI_P_PITM_Strike1'].shift(1)),-1,0))
    a_a['Delta_COI_P_PITM_Strike2'] = np.where((mt['COI_P_PITM_Strike2'] > mt['COI_P_PITM_Strike2'].shift(1)),1,np.where((mt['COI_P_PITM_Strike2'] < mt['COI_P_PITM_Strike2'].shift(1)),-1,0))
    a_a['Delta_COI_P_PITM_Strike3'] = np.where((mt['COI_P_PITM_Strike3'] > mt['COI_P_PITM_Strike3'].shift(1)),1,np.where((mt['COI_P_PITM_Strike3'] < mt['COI_P_PITM_Strike3'].shift(1)),-1,0))
    a_a['Delta_COI_P_PITM_Strike4'] = np.where((mt['COI_P_PITM_Strike4'] > mt['COI_P_PITM_Strike4'].shift(1)),1,np.where((mt['COI_P_PITM_Strike4'] < mt['COI_P_PITM_Strike4'].shift(1)),-1,0))
    a_a['Delta_COI_P_PITM_Strike5'] = np.where((mt['COI_P_PITM_Strike5'] > mt['COI_P_PITM_Strike5'].shift(1)),1,np.where((mt['COI_P_PITM_Strike5'] < mt['COI_P_PITM_Strike5'].shift(1)),-1,0))
    a_a['Delta_COI_N_PITM_Strike1'] = np.where((mt['COI_N_PITM_Strike1'] > mt['COI_N_PITM_Strike1'].shift(1)),1,np.where((mt['COI_N_PITM_Strike1'] < mt['COI_N_PITM_Strike1'].shift(1)),-1,0))
    a_a['Delta_COI_N_PITM_Strike2'] = np.where((mt['COI_N_PITM_Strike2'] > mt['COI_N_PITM_Strike2'].shift(1)),1,np.where((mt['COI_N_PITM_Strike2'] < mt['COI_N_PITM_Strike2'].shift(1)),-1,0))
    a_a['Delta_COI_N_PITM_Strike3'] = np.where((mt['COI_N_PITM_Strike3'] > mt['COI_N_PITM_Strike3'].shift(1)),1,np.where((mt['COI_N_PITM_Strike3'] < mt['COI_N_PITM_Strike3'].shift(1)),-1,0))
    a_a['Delta_COI_N_PITM_Strike4'] = np.where((mt['COI_N_PITM_Strike4'] > mt['COI_N_PITM_Strike4'].shift(1)),1,np.where((mt['COI_N_PITM_Strike4'] < mt['COI_N_PITM_Strike4'].shift(1)),-1,0))
    a_a['Delta_COI_N_PITM_Strike5'] = np.where((mt['COI_N_PITM_Strike5'] > mt['COI_N_PITM_Strike5'].shift(1)),1,np.where((mt['COI_N_PITM_Strike5'] < mt['COI_N_PITM_Strike5'].shift(1)),-1,0))


    a_a['Match_COI_P_COTM_Strike1'] = a_a.Delta_Close.eq(a_a.Delta_COI_P_COTM_Strike1.shift(1))
    a_a['Match_COI_P_COTM_Strike2'] = a_a.Delta_Close.eq(a_a.Delta_COI_P_COTM_Strike2.shift(1))
    a_a['Match_COI_P_COTM_Strike3'] = a_a.Delta_Close.eq(a_a.Delta_COI_P_COTM_Strike3.shift(1))
    a_a['Match_COI_P_COTM_Strike4'] = a_a.Delta_Close.eq(a_a.Delta_COI_P_COTM_Strike4.shift(1))
    a_a['Match_COI_P_COTM_Strike5'] = a_a.Delta_Close.eq(a_a.Delta_COI_P_COTM_Strike5.shift(1))
    a_a['Match_COI_N_COTM_Strike1'] = a_a.Delta_Close.eq(a_a.Delta_COI_N_COTM_Strike1.shift(1))
    a_a['Match_COI_N_COTM_Strike2'] = a_a.Delta_Close.eq(a_a.Delta_COI_N_COTM_Strike2.shift(1))
    a_a['Match_COI_N_COTM_Strike3'] = a_a.Delta_Close.eq(a_a.Delta_COI_N_COTM_Strike3.shift(1))
    a_a['Match_COI_N_COTM_Strike4'] = a_a.Delta_Close.eq(a_a.Delta_COI_N_COTM_Strike4.shift(1))
    a_a['Match_COI_N_COTM_Strike5'] = a_a.Delta_Close.eq(a_a.Delta_COI_N_COTM_Strike5.shift(1))
    a_a['Match_COI_P_CITM_Strike1'] = a_a.Delta_Close.eq(a_a.Delta_COI_P_CITM_Strike1.shift(1))
    a_a['Match_COI_P_CITM_Strike2'] = a_a.Delta_Close.eq(a_a.Delta_COI_P_CITM_Strike2.shift(1))
    a_a['Match_COI_P_CITM_Strike3'] = a_a.Delta_Close.eq(a_a.Delta_COI_P_CITM_Strike3.shift(1))
    a_a['Match_COI_P_CITM_Strike4'] = a_a.Delta_Close.eq(a_a.Delta_COI_P_CITM_Strike4.shift(1))
    a_a['Match_COI_P_CITM_Strike5'] = a_a.Delta_Close.eq(a_a.Delta_COI_P_CITM_Strike5.shift(1))
    a_a['Match_COI_N_CITM_Strike1'] = a_a.Delta_Close.eq(a_a.Delta_COI_N_CITM_Strike1.shift(1))
    a_a['Match_COI_N_CITM_Strike2'] = a_a.Delta_Close.eq(a_a.Delta_COI_N_CITM_Strike2.shift(1))
    a_a['Match_COI_N_CITM_Strike3'] = a_a.Delta_Close.eq(a_a.Delta_COI_N_CITM_Strike3.shift(1))
    a_a['Match_COI_N_CITM_Strike4'] = a_a.Delta_Close.eq(a_a.Delta_COI_N_CITM_Strike4.shift(1))
    a_a['Match_COI_N_CITM_Strike5'] = a_a.Delta_Close.eq(a_a.Delta_COI_N_CITM_Strike5.shift(1))
    a_a['Match_COI_P_POTM_Strike1'] = a_a.Delta_Close.eq(a_a.Delta_COI_P_POTM_Strike1.shift(1))
    a_a['Match_COI_P_POTM_Strike2'] = a_a.Delta_Close.eq(a_a.Delta_COI_P_POTM_Strike2.shift(1))
    a_a['Match_COI_P_POTM_Strike3'] = a_a.Delta_Close.eq(a_a.Delta_COI_P_POTM_Strike3.shift(1))
    a_a['Match_COI_P_POTM_Strike4'] = a_a.Delta_Close.eq(a_a.Delta_COI_P_POTM_Strike4.shift(1))
    a_a['Match_COI_P_POTM_Strike5'] = a_a.Delta_Close.eq(a_a.Delta_COI_P_POTM_Strike5.shift(1))
    a_a['Match_COI_N_POTM_Strike1'] = a_a.Delta_Close.eq(a_a.Delta_COI_N_POTM_Strike1.shift(1))
    a_a['Match_COI_N_POTM_Strike2'] = a_a.Delta_Close.eq(a_a.Delta_COI_N_POTM_Strike2.shift(1))
    a_a['Match_COI_N_POTM_Strike3'] = a_a.Delta_Close.eq(a_a.Delta_COI_N_POTM_Strike3.shift(1))
    a_a['Match_COI_N_POTM_Strike4'] = a_a.Delta_Close.eq(a_a.Delta_COI_N_POTM_Strike4.shift(1))
    a_a['Match_COI_N_POTM_Strike5'] = a_a.Delta_Close.eq(a_a.Delta_COI_N_POTM_Strike5.shift(1))
    a_a['Match_COI_P_PITM_Strike1'] = a_a.Delta_Close.eq(a_a.Delta_COI_P_PITM_Strike1.shift(1))
    a_a['Match_COI_P_PITM_Strike2'] = a_a.Delta_Close.eq(a_a.Delta_COI_P_PITM_Strike2.shift(1))
    a_a['Match_COI_P_PITM_Strike3'] = a_a.Delta_Close.eq(a_a.Delta_COI_P_PITM_Strike3.shift(1))
    a_a['Match_COI_P_PITM_Strike4'] = a_a.Delta_Close.eq(a_a.Delta_COI_P_PITM_Strike4.shift(1))
    a_a['Match_COI_P_PITM_Strike5'] = a_a.Delta_Close.eq(a_a.Delta_COI_P_PITM_Strike5.shift(1))
    a_a['Match_COI_N_PITM_Strike1'] = a_a.Delta_Close.eq(a_a.Delta_COI_N_PITM_Strike1.shift(1))
    a_a['Match_COI_N_PITM_Strike2'] = a_a.Delta_Close.eq(a_a.Delta_COI_N_PITM_Strike2.shift(1))
    a_a['Match_COI_N_PITM_Strike3'] = a_a.Delta_Close.eq(a_a.Delta_COI_N_PITM_Strike3.shift(1))
    a_a['Match_COI_N_PITM_Strike4'] = a_a.Delta_Close.eq(a_a.Delta_COI_N_PITM_Strike4.shift(1))
    a_a['Match_COI_N_PITM_Strike5'] = a_a.Delta_Close.eq(a_a.Delta_COI_N_PITM_Strike5.shift(1))

    a_a_coi = a_a

    a_a_coi1 = ["Match_COI_P_COTM_Strike1", "Match_COI_P_COTM_Strike2", "Match_COI_P_COTM_Strike3", "Match_COI_P_COTM_Strike4","Match_COI_P_COTM_Strike5",
         "Match_COI_P_CITM_Strike1", "Match_COI_P_CITM_Strike2", "Match_COI_P_CITM_Strike3", "Match_COI_P_CITM_Strike4","Match_COI_P_CITM_Strike5",
         "Match_COI_P_POTM_Strike1", "Match_COI_P_POTM_Strike2", "Match_COI_P_POTM_Strike3", "Match_COI_P_POTM_Strike4","Match_COI_P_POTM_Strike5",
         "Match_COI_P_PITM_Strike1", "Match_COI_P_PITM_Strike2", "Match_COI_P_PITM_Strike3", "Match_COI_P_PITM_Strike4","Match_COI_P_PITM_Strike5",
         "Match_COI_N_COTM_Strike1", "Match_COI_N_COTM_Strike2", "Match_COI_N_COTM_Strike3", "Match_COI_N_COTM_Strike4","Match_COI_N_COTM_Strike5",
         "Match_COI_N_CITM_Strike1", "Match_COI_N_CITM_Strike2", "Match_COI_N_CITM_Strike3", "Match_COI_N_CITM_Strike4","Match_COI_N_CITM_Strike5",
         "Match_COI_N_POTM_Strike1", "Match_COI_N_POTM_Strike2", "Match_COI_N_POTM_Strike3", "Match_COI_N_POTM_Strike4","Match_COI_N_POTM_Strike5",
         "Match_COI_N_PITM_Strike1", "Match_COI_N_PITM_Strike2", "Match_COI_N_PITM_Strike3", "Match_COI_N_PITM_Strike4","Match_COI_N_PITM_Strike5"]

    coi_analysis = (a_a_coi[a_a_coi1] == True).sum()

    return coi_analysis #, a_a_coi, a_a_coi1  
    


# In[ ]:





# Analyse_OI(Merge_CallPutOI_MaxPain): 
# The Change in Open Interest data will be analysed
# There are four combinations of Call, Put, ITM and OTM
# values for the options Open Interest. 
# All these details are merged with Merge_CallPutOI_MaxPain dataframe.

# In[37]:


def Analyse_OI(Merge_CallPutOI_MaxPain):
    import numpy as np
    
    

    a_a = Merge_CallPutOI_MaxPain[['Date']]
    mt = Merge_CallPutOI_MaxPain


    a_a['Delta_Close']           = np.where((mt['Close']           > mt['Close'].shift(1))          ,1,np.where((mt['Close']           < mt['Close'].shift(1)),-1,0))
    a_a['Delta_OI_COTM_Strike1'] = np.where((mt['OI_COTM_Strike1'] > mt['OI_COTM_Strike1'].shift(1)),1,np.where((mt['OI_COTM_Strike1'] < mt['OI_COTM_Strike1'].shift(1)),-1,0))
    a_a['Delta_OI_COTM_Strike2'] = np.where((mt['OI_COTM_Strike2'] > mt['OI_COTM_Strike2'].shift(1)),1,np.where((mt['OI_COTM_Strike2'] < mt['OI_COTM_Strike2'].shift(1)),-1,0))
    a_a['Delta_OI_COTM_Strike3'] = np.where((mt['OI_COTM_Strike3'] > mt['OI_COTM_Strike3'].shift(1)),1,np.where((mt['OI_COTM_Strike3'] < mt['OI_COTM_Strike3'].shift(1)),-1,0))
    a_a['Delta_OI_COTM_Strike4'] = np.where((mt['OI_COTM_Strike4'] > mt['OI_COTM_Strike4'].shift(1)),1,np.where((mt['OI_COTM_Strike4'] < mt['OI_COTM_Strike4'].shift(1)),-1,0))
    a_a['Delta_OI_COTM_Strike5'] = np.where((mt['OI_COTM_Strike5'] > mt['OI_COTM_Strike5'].shift(1)),1,np.where((mt['OI_COTM_Strike5'] < mt['OI_COTM_Strike5'].shift(1)),-1,0))
    a_a['Delta_OI_CITM_Strike1'] = np.where((mt['OI_CITM_Strike1'] > mt['OI_CITM_Strike1'].shift(1)),1,np.where((mt['OI_CITM_Strike1'] < mt['OI_CITM_Strike1'].shift(1)),-1,0))
    a_a['Delta_OI_CITM_Strike2'] = np.where((mt['OI_CITM_Strike2'] > mt['OI_CITM_Strike2'].shift(1)),1,np.where((mt['OI_CITM_Strike2'] < mt['OI_CITM_Strike2'].shift(1)),-1,0))
    a_a['Delta_OI_CITM_Strike3'] = np.where((mt['OI_CITM_Strike3'] > mt['OI_CITM_Strike3'].shift(1)),1,np.where((mt['OI_CITM_Strike3'] < mt['OI_CITM_Strike3'].shift(1)),-1,0))
    a_a['Delta_OI_CITM_Strike4'] = np.where((mt['OI_CITM_Strike4'] > mt['OI_CITM_Strike4'].shift(1)),1,np.where((mt['OI_CITM_Strike4'] < mt['OI_CITM_Strike4'].shift(1)),-1,0))
    a_a['Delta_OI_CITM_Strike5'] = np.where((mt['OI_CITM_Strike5'] > mt['OI_CITM_Strike5'].shift(1)),1,np.where((mt['OI_CITM_Strike5'] < mt['OI_CITM_Strike5'].shift(1)),-1,0))
    a_a['Delta_OI_POTM_Strike1'] = np.where((mt['OI_POTM_Strike1'] > mt['OI_POTM_Strike1'].shift(1)),1,np.where((mt['OI_POTM_Strike1'] < mt['OI_POTM_Strike1'].shift(1)),-1,0))
    a_a['Delta_OI_POTM_Strike2'] = np.where((mt['OI_POTM_Strike2'] > mt['OI_POTM_Strike2'].shift(1)),1,np.where((mt['OI_POTM_Strike2'] < mt['OI_POTM_Strike2'].shift(1)),-1,0))
    a_a['Delta_OI_POTM_Strike3'] = np.where((mt['OI_POTM_Strike3'] > mt['OI_POTM_Strike3'].shift(1)),1,np.where((mt['OI_POTM_Strike3'] < mt['OI_POTM_Strike3'].shift(1)),-1,0))
    a_a['Delta_OI_POTM_Strike4'] = np.where((mt['OI_POTM_Strike4'] > mt['OI_POTM_Strike4'].shift(1)),1,np.where((mt['OI_POTM_Strike4'] < mt['OI_POTM_Strike4'].shift(1)),-1,0))
    a_a['Delta_OI_POTM_Strike5'] = np.where((mt['OI_POTM_Strike5'] > mt['OI_POTM_Strike5'].shift(1)),1,np.where((mt['OI_POTM_Strike5'] < mt['OI_POTM_Strike5'].shift(1)),-1,0))
    a_a['Delta_OI_PITM_Strike1'] = np.where((mt['OI_PITM_Strike1'] > mt['OI_PITM_Strike1'].shift(1)),1,np.where((mt['OI_PITM_Strike1'] < mt['OI_PITM_Strike1'].shift(1)),-1,0))
    a_a['Delta_OI_PITM_Strike2'] = np.where((mt['OI_PITM_Strike2'] > mt['OI_PITM_Strike2'].shift(1)),1,np.where((mt['OI_PITM_Strike2'] < mt['OI_PITM_Strike2'].shift(1)),-1,0))
    a_a['Delta_OI_PITM_Strike3'] = np.where((mt['OI_PITM_Strike3'] > mt['OI_PITM_Strike3'].shift(1)),1,np.where((mt['OI_PITM_Strike3'] < mt['OI_PITM_Strike3'].shift(1)),-1,0))
    a_a['Delta_OI_PITM_Strike4'] = np.where((mt['OI_PITM_Strike4'] > mt['OI_PITM_Strike4'].shift(1)),1,np.where((mt['OI_PITM_Strike4'] < mt['OI_PITM_Strike4'].shift(1)),-1,0))
    a_a['Delta_OI_PITM_Strike5'] = np.where((mt['OI_PITM_Strike5'] > mt['OI_PITM_Strike5'].shift(1)),1,np.where((mt['OI_PITM_Strike5'] < mt['OI_PITM_Strike5'].shift(1)),-1,0))
    
    a_a['Match_OI_COTM_Strike1'] = a_a.Delta_Close.eq(a_a.Delta_OI_COTM_Strike1.shift(1))
    a_a['Match_OI_COTM_Strike2'] = a_a.Delta_Close.eq(a_a.Delta_OI_COTM_Strike2.shift(1))
    a_a['Match_OI_COTM_Strike3'] = a_a.Delta_Close.eq(a_a.Delta_OI_COTM_Strike3.shift(1))
    a_a['Match_OI_COTM_Strike4'] = a_a.Delta_Close.eq(a_a.Delta_OI_COTM_Strike4.shift(1))
    a_a['Match_OI_COTM_Strike5'] = a_a.Delta_Close.eq(a_a.Delta_OI_COTM_Strike5.shift(1))
    a_a['Match_OI_CITM_Strike1'] = a_a.Delta_Close.eq(a_a.Delta_OI_CITM_Strike1.shift(1))
    a_a['Match_OI_CITM_Strike2'] = a_a.Delta_Close.eq(a_a.Delta_OI_CITM_Strike2.shift(1))
    a_a['Match_OI_CITM_Strike3'] = a_a.Delta_Close.eq(a_a.Delta_OI_CITM_Strike3.shift(1))
    a_a['Match_OI_CITM_Strike4'] = a_a.Delta_Close.eq(a_a.Delta_OI_CITM_Strike4.shift(1))
    a_a['Match_OI_CITM_Strike5'] = a_a.Delta_Close.eq(a_a.Delta_OI_CITM_Strike5.shift(1))
    a_a['Match_OI_POTM_Strike1'] = a_a.Delta_Close.eq(a_a.Delta_OI_POTM_Strike1.shift(1))
    a_a['Match_OI_POTM_Strike2'] = a_a.Delta_Close.eq(a_a.Delta_OI_POTM_Strike2.shift(1))
    a_a['Match_OI_POTM_Strike3'] = a_a.Delta_Close.eq(a_a.Delta_OI_POTM_Strike3.shift(1))
    a_a['Match_OI_POTM_Strike4'] = a_a.Delta_Close.eq(a_a.Delta_OI_POTM_Strike4.shift(1))
    a_a['Match_OI_POTM_Strike5'] = a_a.Delta_Close.eq(a_a.Delta_OI_POTM_Strike5.shift(1))
    a_a['Match_OI_PITM_Strike1'] = a_a.Delta_Close.eq(a_a.Delta_OI_PITM_Strike1.shift(1))
    a_a['Match_OI_PITM_Strike2'] = a_a.Delta_Close.eq(a_a.Delta_OI_PITM_Strike2.shift(1))
    a_a['Match_OI_PITM_Strike3'] = a_a.Delta_Close.eq(a_a.Delta_OI_PITM_Strike3.shift(1))
    a_a['Match_OI_PITM_Strike4'] = a_a.Delta_Close.eq(a_a.Delta_OI_PITM_Strike4.shift(1))
    a_a['Match_OI_PITM_Strike5'] = a_a.Delta_Close.eq(a_a.Delta_OI_PITM_Strike5.shift(1))

    a_a_oi=a_a 
    
    a_a1 = ["Match_OI_COTM_Strike1", "Match_OI_COTM_Strike2", "Match_OI_COTM_Strike3", "Match_OI_COTM_Strike4","Match_OI_COTM_Strike5",
         "Match_OI_CITM_Strike1", "Match_OI_CITM_Strike2", "Match_OI_CITM_Strike3", "Match_OI_CITM_Strike4","Match_OI_CITM_Strike5",
         "Match_OI_POTM_Strike1", "Match_OI_POTM_Strike2", "Match_OI_POTM_Strike3", "Match_OI_POTM_Strike4","Match_OI_POTM_Strike5",
         "Match_OI_PITM_Strike1", "Match_OI_PITM_Strike2", "Match_OI_PITM_Strike3", "Match_OI_PITM_Strike4","Match_OI_PITM_Strike5"]

    oi_analysis = (a_a_oi[a_a1] == True).sum()

    return  oi_analysis , a_a_oi, a_a1   


# In[ ]:





# In[ ]:





# In[ ]:





# # Main Program Starts

# In[38]:


# Load Data to Dataframes
# Read the Base Data
# Data about Nifty Index is stored in the excel file CapstoneNiftyData.xlsx 
# and loaded to the "nifty" DataFrame
# Data about Nifty Index Options is stored in the excel file CapstoneNiftyOptionsData.xlsx 
# and loaded to the "nifty_options" DataFrame

nifty, nifty_options=LoadFiles()
 


# In[39]:


# Display the Features and Observations of nifty df
nifty.head()


# In[40]:


# Confirm the number of Features and Observations in nifty df
nifty.shape


# In[41]:


# Confirm the Features in nifty df
nifty.dtypes


# In[ ]:





# In[42]:


# Display the Features and Observations of nifty_options df
nifty_options.head()


# In[43]:


# Confirm the number of Features and Observations in nifty_optiopns df
nifty_options.shape


# In[44]:


# Confirm the Features in nifty_options
nifty_options.dtypes


# In[ ]:





# This is going to capture the user input, select any number from 1-7 and press enter, as to how many strikes around the ATM price needs to be considered for analysis.
# 
# Nifty Index Options has each strike of 50 points apart. 
# 
# So selecting 5 strikes means 250 points on either side of the ATM or spot price is considered for analysis. 
# So ATM = 15000, then the strikes selected are 14750  - 15250.
# 

# In[45]:


# Obtain user Input
# The user can choose how many strikes on either side of the ATM Strike 
# he wants the data to be analysed

#('1. 05 Strikes = 250 points')
#('2. 10 Strikes = 500 points')
#('3. 15 Strikes = 750 points')
#('4. 20 Strikes = 1000 points')
#('5. 25 Strikes = 1250 points')
#('6. 30 Strikes = 1500 points')
#('7. ALL Strikes')
    
ui, uip = GetUserInput()
print(ui)
print(uip)


# In[46]:


# Calculate Max Pain data Point and display
mxpn = MaxPain(nifty_options)
mxpn.head() 


# In[47]:


mxpn.shape


# In[ ]:





# In[ ]:





# In[48]:


# Calculate Daily Range and other data Point and display
Daily_Range = DailyRange(nifty)
Daily_Range.head()


# In[49]:


Daily_Range.shape


# In[50]:


Daily_Range.dtypes


# In[ ]:





# In[51]:


# MaxPain_Top1() captures the one Top Max Pain considering all the strikes for a day.
MaxPain_Top1 = MaxPain_Top1(mxpn, ui)
MaxPain_Top1.head()


# In[52]:


MaxPain_Top1.tail()


# In[53]:


MaxPain_Top1.shape


# In[ ]:





# In[ ]:





# In[54]:


# MaxPain_IOTM_Top1() captures the one Top Max Pain considering all the strikes
# for a day separated by ITM and OTM.
MaxPain_IOTM_Top1 = MaxPain_IOTM_Top1(mxpn, ui)
MaxPain_IOTM_Top1.head()


# In[55]:


MaxPain_IOTM_Top1.shape


# In[ ]:





# In[ ]:





# In[56]:


#  MaxPain_Top5() captures the five Top Max Pain considering all the strikes 
# for a day separated by ITM and OTM.
MaxPain_Top5 = MaxPain_Top5(mxpn, ui)
MaxPain_Top5.head()


# In[57]:


MaxPain_Top5.shape


# In[ ]:





# In[ ]:





# In[58]:


# Call_OI_Top5() captures the top five Open Interest strikes for Call options.

Call_OI_Top5= Call_OI_Top5(nifty_options,ui)
Call_OI_Top5.head()


# In[59]:


Call_OI_Top5.shape


# In[ ]:





# In[60]:


# Put_OI_Top5() captures the top five Open Interest strikes for Put options.
Put_OI_Top5 = Put_OI_Top5(nifty_options,ui)
Put_OI_Top5.head()


# In[61]:


Put_OI_Top5.shape


# In[ ]:





# In[62]:


# •	CallPut_OI_Top5() captures the top five Open Interest strikes for Call and Put options.
Merge_Call_Put_OI = Merge_Call_Put_OI(Call_OI_Top5, Put_OI_Top5)
Merge_Call_Put_OI.head()


# In[63]:


Merge_Call_Put_OI.shape


# In[ ]:





# In[ ]:





# In[64]:


# Merge_CallPutOI_MaxPain() merges CallPut_OI_Top5 and MaxPain_Top5, 
# so that all details are available in one dataframe.
Merge_CallPutOI_MaxPain = Merge_CallPutOI_MaxPain(Merge_Call_Put_OI, MaxPain_Top5, Daily_Range)
Merge_CallPutOI_MaxPain.head()


# In[65]:


Merge_CallPutOI_MaxPain.shape


# In[66]:


Merge_CallPutOI_MaxPain.dtypes


# In[ ]:





# In[ ]:





# # Visualization of Open Interest Data

# In[ ]:





# In[67]:


# Visualise the Nifty Candle Chart for the given period
Candle_Chart(Merge_CallPutOI_MaxPain)


# In[ ]:





# This is going to capture the user input, 
# select any number from 1-7 and press enter. 
# This considers the first highest Open Interest to the next four levels below. 
# Select 1 if you want to Plot the first highest OI level wrt the Close price of the underlying.
# 
# Select 2 if you want to Plot the second highest OI level wrt the Close price of the underlying.
# 
# Select 7 if you want to Plot the First and second highest OI level wrt the Close price of the underlying.

# In[68]:


# Capture user Input to view the number of OI Levels in the chart
no_levels_oi,ip21 = GetUserInput_IOCharts()
print(ip21)


# In[ ]:





# In[69]:


# Draw Candle Chart along with Call ITM OI
Call_OI_ITM_Chart(Merge_CallPutOI_MaxPain,no_levels_oi)


# In[ ]:





# In[70]:


# Draw Candle Chart along with Call OTM OI
Call_OI_OTM_Chart(Merge_CallPutOI_MaxPain,no_levels_oi)


# In[ ]:





# In[71]:


# Draw Candle Chart along with Put OTM OI
Put_OI_OTM_Chart(Merge_CallPutOI_MaxPain,no_levels_oi)


# In[ ]:





# In[72]:


# Draw Candle Chart along with PUT ITM OI
Put_OI_ITM_Chart(Merge_CallPutOI_MaxPain,no_levels_oi)


# In[ ]:





# In[73]:


# Draw Candle Chart along with Call OTM PUT OTM OI
CallPut_OI_OTM_Chart(Merge_CallPutOI_MaxPain,no_levels_oi)


# In[ ]:





# In[74]:


# Plot the OHLC graph for Nifty
Nifty_OHLC_Chart(Merge_CallPutOI_MaxPain)


# In[ ]:





# In[75]:


# Plot the Scatter diagram for Call ITM OI
Call_OI_ITM_Scatter_Chart(Merge_CallPutOI_MaxPain)


# In[ ]:





# In[76]:


# Plot the OHLC graph and MaxPain

OHLC_Chart_MaxPain(Merge_CallPutOI_MaxPain)


# In[ ]:





# # CHANGE IN OPEN INTEREST 

# There are SIX combinations of Call, Put, ITM, OTM, Positive and Negative COI values, for the options Change in OT. 
# 
# All these details are merged with Merge_CallPutOI_MaxPain dataframe.

# In[ ]:





# In[77]:


# Gather data for Call Change of Open Interest values
Merge_CallPutOI_MaxPain = Call_COI_P_Top5(nifty_options,ui,Merge_CallPutOI_MaxPain)
Merge_CallPutOI_MaxPain.head(10)


# In[78]:


Merge_CallPutOI_MaxPain.dtypes


# In[79]:


Merge_CallPutOI_MaxPain.shape


# In[ ]:





# In[ ]:





# In[80]:



# Calculation for "Change in Open Interest" for CALL Options NEGATIVE VALUES

# Shortlist Change in Open Interest Data for CALL ITM and CALL OTM Options
Merge_CallPutOI_MaxPain = Call_COI_N_Top5(nifty_options, ui,Merge_CallPutOI_MaxPain)
Merge_CallPutOI_MaxPain.head()


# In[81]:



Merge_CallPutOI_MaxPain.shape


# In[ ]:





# In[ ]:





# In[82]:


# Calculation for "Change in Open Interest" for PUT Options POSITIVE VALUES

# Shortlist Change in Open Interest Data for CALL ITM and CALL OTM Options

Merge_CallPutOI_MaxPain = Put_COI_P_Top5(nifty_options, ui,Merge_CallPutOI_MaxPain)
Merge_CallPutOI_MaxPain.head()


# In[ ]:





# In[83]:


Merge_CallPutOI_MaxPain.shape


# In[ ]:





# In[84]:


# Calculation for "Change in Open Interest" for PUT Options NEGATIVE VALUES

# Shortlist Change in Open Interest Data for CALL ITM and CALL OTM Options

Merge_CallPutOI_MaxPain = Put_COI_N_Top5(nifty_options, ui,Merge_CallPutOI_MaxPain)
Merge_CallPutOI_MaxPain.head()


# In[85]:


Merge_CallPutOI_MaxPain.shape


# In[ ]:





# In[ ]:





# In[ ]:





# # Visualization of Change of OI Data

# In[86]:


no_levels_coi,ip21 = GetUserInput_COICharts()
print(ip21)


# In[ ]:





# In[87]:



Call_COI_P_OTM_Chart(Merge_CallPutOI_MaxPain,no_levels_coi)
 


# In[ ]:





# In[88]:


# Draw Candle Chart along with Chaneg of OI for Call OTM NEGATIVE Values 
Call_COI_N_OTM_Chart(Merge_CallPutOI_MaxPain,no_levels_coi)


# In[ ]:





# In[89]:


Put_COI_P_OTM_Chart(Merge_CallPutOI_MaxPain,no_levels_coi)


# In[ ]:





# In[90]:


Put_COI_N_OTM_Chart(Merge_CallPutOI_MaxPain,no_levels_coi)


# In[ ]:





# In[ ]:





# # Analysis and Results Prediction

# In[ ]:





# Analyse_OI() analyses the OI details of how it compares to the todays "Close" wrt previous days OI Strike.
# 
# For each level of OI strike for CALL , PUT, ITM and OTM are analysed wrt Close. 
# 
# If the OI predicts the next days Close level correctly, then OI is able to predict the trend for the next day. Each such True values are compared to the total transaction period and the percentage success rate is gathered. Higher the Percentage better is the predictable power of OI.
# 

# In[91]:


# Analyse the Open Interest Data for Call Put ITM and OTM
oi_analysis,a,b = Analyse_OI(Merge_CallPutOI_MaxPain)


# In[92]:


# Probability Number for the Open Interest for 82 Trading Days
oi_analysis


# In[93]:


oi_analysis.shape


# In[94]:


oi_analysis.dtypes


# In[95]:


oi_analysis


# In[96]:


a
a1=a
a1


# In[97]:


adf = pd.DataFrame(a, columns=['Match_OI_COTM_Strike1','Match_OI_COTM_Strike2','Match_OI_COTM_Strike3','Match_OI_COTM_Strike4','Match_OI_COTM_Strike5',
                              'Match_OI_POTM_Strike1','Match_OI_POTM_Strike2','Match_OI_POTM_Strike3','Match_OI_POTM_Strike4','Match_OI_POTM_Strike5',
                              'Match_OI_CITM_Strike1','Match_OI_CITM_Strike2','Match_OI_CITM_Strike3','Match_OI_CITM_Strike4','Match_OI_CITM_Strike5',
                              'Match_OI_PITM_Strike1','Match_OI_PITM_Strike2','Match_OI_PITM_Strike3','Match_OI_PITM_Strike4','Match_OI_PITM_Strike5'])
adf


# In[98]:


adf.shape


# In[99]:


adf1=adf.sum()
adf1


# In[100]:


adf['tool_sum'] = adf[['Match_OI_COTM_Strike1', 'Match_OI_COTM_Strike2', 'Match_OI_COTM_Strike3']].sum(1)
#adf2=adf[adf==True].count(axis=0) #   df[df==True].count(axis=0) #.value_counts()
adf


# In[101]:


adf1=pd.DataFrame(adf1,columns=['a'])
adf1


# In[ ]:





# In[ ]:





# In[ ]:





# In[102]:


# Plot the Results of Open Interest Analysis
#coi_analysis.plot.hist()
oi_analysis.plot.bar(stacked=True);


# Result Interpretation
# A value of 30 means that this Level has 30 times out of 82 transactions 
# got the correct prediction.
# 
# 82 is the number of trading days that we have considered here.
# 
# This translates to a Probability of Success = 30/82 = 36.58%

# In[ ]:





# In[ ]:





# In[103]:


coi_analysis = Analyse_COI(Merge_CallPutOI_MaxPain)


# In[104]:


# Probability Number for the Change of  Open Interest for 82 Trading Days
coi_analysis


# In[105]:


# Plot the Results of Change of Open Interest Analysis
#coi_analysis.plot.hist()
coi_analysis.plot.bar(stacked=True); 


# In[ ]:





# Result Interpretation
# A value of 45 means that this Level has 45 times out of 82 transactions 
# got the correct prediction.
# 
# 82 is the number of trading days that we have considered here.
# 
# This translates to a Probability of Success = 45/82 = 54.87%

# Result Interpretation
# 
# Any value above ZERO means that the TREND Prediction is not RANDOM.
# 
# So using "Open Intrest Data", it is possible to Predict the Trend of the Underlying.
# 
# So using "Change of Open Intrest Data", it is possible to Predict the Trend of the Underlying.
# 
# CONCLUSION: 
# Using "NIFTY 50 Index Options Open Intrest" Data, 
# it is possible to Predict the Trend of the Underlying.
# 
# 

#  
