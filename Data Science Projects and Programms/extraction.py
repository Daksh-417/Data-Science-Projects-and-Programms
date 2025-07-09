import pandas as pd
import requests as r
from bs4 import BeautifulSoup
m = r.get('https://www.rockstargames.com/VI').text
print(m)