
# coding: utf-8

#%matplotlib tk
#matplotlib notebook


# In[11]:

import os
import numpy as np
from matplotlib import pyplot as plt, font_manager

font_manager._rebuild()

font_dir = '/Users/pydata/Library/Fonts'
font_dir = font_manager.win32FontDirectory()
font_path = os.path.join(font_dir, 'SourceHanCodeJP-Regular.otf')
font=font_manager.FontProperties(fname=font_path, size=14)
print (font_dir)
np.random.seed(0)
x=range(5)

y=10+5*np.random.randn(5)
fig=plt.figure()
ax=fig.add_subplot(111)

ax.set_title('テストtest $X^2$', fontproperties=font)
ax.set_xlabel('X')
ax.set_xlabel('Y')

ax.bar(x,y)
plt.show()


# In[22]:

import os
import pandas as pd

base_url = 'https://raw.githubusercontent.com/practical-jupyter/sample-data/master/anime/'
anime_csv = os.path.join(base_url, 'anime.csv')

print(anime_csv)
pd.read_csv(anime_csv).head()

anime_master_csv = os.path.join(base_url, 'anime_master.csv')
pd.read_csv(anime_master_csv).head()


# 
# \begin{align}
# \sqrt{(2x-1)+(3+x)^3}
# \end{align}
# $$E=mc^2$$
# 
# Able | Bob
# --|--
# C | D
# E | F
