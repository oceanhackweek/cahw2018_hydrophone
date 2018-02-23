# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Function made to retrieve the right mseed files and concatenate them into one file
"""

from datetime import datetime
import numpy as np
from obspy import read
import requests
from bs4 import BeautifulSoup
import sys

##### Parameters

list_file='filelist_RS01SBPS.txt'
root_dir='https://rawdata.oceanobservatories.org/files/RS01SBPS/PC01A/08-HYDBBA103/'
net='PC01A'
station='08-HYDBBA103'



####### FUNCTIONS


def build_path(root_dir,datetime_val):
    
    year=datetime_val.year
    month=datetime_val.month
    day=datetime_val.day
    
    fullpath=('%s/%04i/%02i/%02i/'%(root_dir,year,month,day))
    
    return fullpath


def list_files(url, ext='.mseed'):
    """
    List all files present in the url and whose extension is .mseed
    
    Parameters
    ---------
    
    url: str
        url to the mseed files
    ext: str
        extension of the file to be listed
    
    """
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href').lstrip('./') for node in soup.find_all('a') if node.get('href').endswith(ext)]

def parse_line(line,time_format='%Y-%m-%dT%H:%M:%S.%f'):
    """
    Function made to parse txt file into path and datetime
    
    line: str
        file line to parse
        
    Returns:
    -------
    
    path: str
    time_val: datetime
    """

    path=line.split(' ')[-1]
    date_str=path.split('/')[-1].split('.mseed')[0][-26:]
    
    date_time=datetime.strptime(date_str,time_format)
    
    return (path,date_time)

def file2time(file,time_format='%Y-%m-%dT%H:%M:%S.%f'):
    """
    """

    date_str=file.split('.mseed')[0][-26:]
    
    date_time=datetime.strptime(date_str,time_format)
    
    return date_time

def path2mseed(path):
    mseed_name=path.split('/')[-1]
    
    return mseed_name

###########################################"
    
####

start_date='2017-08-21T09:00:00'
end_date='2017-08-22T11:00:00'

format_date='%Y-%m-%dT%H:%M:%S'

### Transform to datetime

start_time=datetime.strptime(start_date,format_date)
end_time=datetime.strptime(end_date,format_date)

#### Make sure it's the same day

if start_time.date()!=end_time.date():
    raise ValueError('Please select the same day for start time and end time')
    
sys.exit()

#### Build daily URLs



### get path
    
url=build_path(root_dir,start_time)

#### List file

select_files=list_files(url, ext='.mseed')


kk=0
for mseed_file in select_files:

    
    file_time=file2time(path2mseed(mseed_file))
    
    if file_time>=start_time and file_time<=end_time:
        kk=kk+1
        print(path2mseed(mseed_file))
        st=read(mseed_file)
        st.write('temp_%03i.mseed'%(kk),format='MSEED')

    
    



#dir_list=np.loadtxt(list_file,dtype='str',usecols=3)