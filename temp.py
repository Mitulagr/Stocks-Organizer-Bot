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


a = [1,2,3,4,5,6]
a = a[:4]
print(a)