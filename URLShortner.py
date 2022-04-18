"""
Example input : https://github.com/MichaelOD766/Python/blob/main/House_Sales_in_King_Count_USA.ipynb
"""

import pyshorteners

link = input("\nEnter your link : ")

short = pyshorteners.Shortener()
x = short.tinyurl.short(link)

print("\nShorted link is : "+x)