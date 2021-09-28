import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
#add headers to avoid access denied
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
r= requests.get("https://www.analytixlabs.co.in/blog/nlp-interview-questions/", headers=headers)
c= r.content
#Use beatifulsoup to parse
soup = BeautifulSoup(c, "html.parser")
#content in dictinary
nlp={"Questions":[], "Answers":[]}
#search and append
#All the <p> after the questions (next siblings to Q)
for i in soup.find_all(id=re.compile("q")):
    if i.text !="":
            nlp["Questions"].append(i.text)
    for sib in i.next_siblings:
        if sib.name == 'p':
            if sib.text!="":
                nlp["Answers"].append(sib.text)
            break
#save dictionary to dataframe
df=pd.DataFrame(nlp)
#save dataframe to csv
df.to_csv("nlpqr.csv")
print("data saved to csv")
