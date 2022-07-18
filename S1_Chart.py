import requests
from bs4 import BeautifulSoup
import datetime
import json
from openpyxl import load_workbook
from openpyxl.workbook import Workbook
from openpyxl.styles import Color, Fill, Font, colors, Alignment
from openpyxl.cell import Cell
import time
import pandas as pd
from matplotlib import pyplot as plt
from scipy.signal import butter,filtfilt
import numpy as np
from matplotlib.patches import PathPatch
import discord
from discord import colour
import requests
from discord.ext import commands, tasks
import math


def lpf(x,cutoff=0.1, order=2):
    normal_cutoff = cutoff
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    sb = sum(b)
    sa = sum(a)
    for i in range (len(b)) :  b[i] = b[i]/sb
    for i in range (len(a)) :  a[i] = a[i]/sa
    y = filtfilt(b, a, x)
    return y    

def day_chart(data,t,dt,d) :
    l = 13*(d-1) + t.index("03:30 PM")
    nd = len(data)//13
    if(t.index("03:30 PM")==0) : l = l + 13
    else : nd = nd + 1
    nd = min(nd,d)
    dc = d-1
    data = data[:l]
    t = t[:l] 
    ld = len(data)
    if(l!=ld) : dc = len(dt)-2   
    data = data[::-1]
    t = t[::-1]
    x = []
    interval = 1 + (d-1)//15
    for i in range(ld) :
        if(t[i]=="03:30 PM" or i==ld-1) :
            if(dc%interval==0) : x.append((datetime.datetime.strptime(dt[dc], '%Y-%m-%d %H:%M:%S')).strftime("%d %B"))
            dc = dc-1           
    n = range(ld)
    plt.figure(figsize=(12,4.5))
    plt.plot(n,data,color = (0.0, 0.5, 0.0, 0.7))
    for i in n :
        if(i%(13*interval)==13*((nd-1)%interval)) : plt.axvline(x=i, color=(0,0,0), linestyle='--',linewidth=0.5)
    yl = plt.gca().get_ylim()
    if(d==1) : plt.xticks(range(0,13,3),["9.30 AM","11.00 AM","12.30 PM","2.00 PM","3.30 PM"])
    else : plt.xticks(range(13*((nd-1)%interval),ld,13*interval),x)
    plt.title(f"{data[-1]}",fontdict={'fontsize': 15})
    step = 100
    for i in range (step) :
        uu = yl[0] + (yl[1]-yl[0])*i/step
        plt.fill_between(n, uu,data,where = data>uu, interpolate=True,facecolor=(0.0,1,0.5), alpha=0.01*(i/step)) 
    plt.ylim(yl)
    plt.xlim(0,13*d-1)
    plt.savefig(f'Stock Charts/Day{d}.png', bbox_inches='tight') 
    plt.cla()
    plt.close('all')

def lpf_day_chart(data,t,dt,d) :
    l = 13*(d-1)
    l1 = t.index("03:30 PM")
    if(t.index("03:30 PM")==0) : l1 = 13
    l = min(l,len(data)-l1)
    data = list(lpf(data[:l1])) + data[l1:]
    for i in range(l1,l+l1,13) :
        data = data[:i] + list(lpf(data[i:i+13])) + data[i+13:]
    day_chart(data,t,dt,d)    

def day(d) : 
    data = pd.read_excel('Stock_Chart.xlsx', sheet_name='Data',skiprows=[1])   
    t = list(data["Time"])
    data = list(data["Net Worth (Per 100000 Deposited)"])
    dt = pd.read_excel('Stock_Chart.xlsx', sheet_name='DayData',skiprows=[1]) 
    dt = list(dt["Date"])
    day_chart(data,t,dt,d)  

def lpf_day(d) : 
    data = pd.read_excel('Stock_Chart.xlsx', sheet_name='Data',skiprows=[1])   
    t = list(data["Time"])
    data = list(data["Net Worth (Per 100000 Deposited)"])
    dt = pd.read_excel('Stock_Chart.xlsx', sheet_name='DayData',skiprows=[1]) 
    dt = list(dt["Date"])
    day_chart(list(lpf(data)),t,dt,d) 

def max() :
    data = pd.read_excel('Stock_Chart.xlsx', sheet_name='Data',skiprows=[1])   
    data = list(data["Net Worth (Per 100000 Deposited)"])
    return math.ceil(len(data)/13)         