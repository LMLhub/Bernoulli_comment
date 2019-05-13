#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 19:01:56 2018

@author: Ole Peters
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime

x=np.arange(0.01,3,.01)
u=np.log(x)

####final equity vs. leverage#####
fig=plt.figure()
ax=plt.plot(x,u,linewidth=2,color='black')
plt.axvline(x=1,linestyle=':',color='red',linewidth=1.5)
plt.axvline(x=1+2*1.0403393028,linestyle=':',color='pink',linewidth=1.5)
plt.axvline(x=1-2*1.0403393028,linestyle=':',color='pink',linewidth=1.5)
plt.axhline(y=0,linestyle=':',color='grey',linewidth=.5)
frameon=False
plt.tick_params(top='off', bottom='off', left='off', right='off')
for spine in plt.gca().spines.values():
    spine.set_visible(False)

#ax.annotate('l=0',
#            xy=(0,final_equity_1.iloc[219]), xycoords='data',
#            xytext=(-60, 0), textcoords='offset points',
#            arrowprops=dict(color='brown',arrowstyle="->"))
#
#ax.annotate('l=1',
#            xy=(1,final_equity_1.iloc[244]), xycoords='data',
#            xytext=(-60, 0), textcoords='offset points',
#            arrowprops=dict(color='red',arrowstyle="->"))
#
#ax.annotate('l=2',
#            xy=(2,final_equity_1.iloc[270]), xycoords='data',
#            xytext=(-60, -30), textcoords='offset points',
#            arrowprops=dict(color='green',arrowstyle="->"))
#
#ax.annotate('l=3',
#            xy=(3,final_equity_1.iloc[295]), xycoords='data',
#            xytext=(40, 0), textcoords='offset points',
#            arrowprops=dict(color='magenta',arrowstyle="->"))
#
#ax.annotate('l=4',
#            xy=(4,final_equity_1.iloc[321]), xycoords='data',
#            xytext=(40, 20), textcoords='offset points',
#            arrowprops=dict(color='orange',arrowstyle="->"))
#
#ax.annotate('l=5',
#            xy=(5,final_equity_1.iloc[346]), xycoords='data',
#            xytext=(0, 30), textcoords='offset points',
#            arrowprops=dict(color='purple',arrowstyle="->"))
#

#plt.plot(final_equity_2, label='+ friction',linewidth=3)
#plt.plot(final_equity_3, label='+ borrowing premia',linewidth=1)
#ax.set_yscale('log')
plt.xlim([-2,6])
#plt.xlim([final_equity_1.index.min(),final_equity_1.index.max()])
#plt.ylim([-1.5,2.2])
#vals = ax.get_yticks()
#ax.set_yticklabels(['{:3.0f}% p.a.'.format(100*x) for x in vals])
#ax.set_aspect(1./(1.618*ax.get_data_ratio()))
#plt.title('some title')
plt.xlabel('Wealth x')
plt.ylabel('Utility u(x)')

#plt.axvline(x=1.68045,linestyle='--',color='grey',linewidth=1)
#plt.legend(loc=4, bbox_to_anchor=(.45,.7))
#ax.legend_.remove()
#plt.savefig("./EUT.pdf", bbox_inches='tight')
plt.show()
