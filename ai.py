import os
import time
import openai
import json
import re
from tld import get_fld
import pandas
import requests

def getStatuscode(url):
    try:
        r = requests.head(url,verify=False,timeout=5) # it is faster to only request the header
        return (r.status_code)

    except:
        return -1



def countdown(t):
    while t: # while t > 0 for clarity
      mins = t // 60
      secs = t % 60
      timer = '{:02d}:{:02d}'.format(mins, secs)
      print(timer, end="\r") # overwrite previous line
      time.sleep(1)
      t -= 1
    print('Blast Off!!!')

def API():
    file_path = r'APIKey.txt'
    if os.path.exists(file_path):

        if os.path.getsize('APIKey.txt') == 0:
            print("\n API Key is not found")
            key = input('\n Enter your API key/Token: ')
            with open(file_path, 'w') as fp:
                fp.write(key)
                fp.close()
        else:
            myfile = open("APIKey.txt", "r")
            key = myfile.readline()
            #print(Key)
            myfile.close()

    else:
        # create a file
        print("\n API File is not found")
        key = input('\n Enter your API key/Token: ')
        with open(file_path, 'w') as fp:
            fp.write(key)
            fp.close()
    return key

def APIreq(Qline):
    openai.api_key = API()
    Qry = "show only the official website of" + Qline
    try:
        Res = openai.Completion.create(
            model="text-davinci-003",
            prompt=Qry,
            max_tokens=1000,
            temperature=0)
    except:
        print("\n The model is currently overloaded with other requests. Please wait for sometime")
        countdown(int(300))
        Res = openai.Completion.create(
            model="text-davinci-003",
            prompt=Qry,
            max_tokens=1000,
            temperature=0)

    json_data = json.loads(str(Res))
    raw_text = json_data['choices'][0]['text']
    if 'http' in raw_text:
        urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', raw_text)
        dom = urls[0]
        try:
            Tdomain = get_fld(dom)
        except:
            Tdomain='error'
        print("The official website of " + Qline + " : " + dom)
    elif 'www' in raw_text:
        urls = re.findall('www(?:[-\w.]|(?:%[\da-fA-F]{2}))+', raw_text)
        turl="http://"+urls[0]
        dom = urls[0]
        Tdomain = get_fld(turl)
        print("The official website of " + Qline + " : " + dom)
    else:
        dom = Tdomain = "No domain found"
        print("Website id not found")

    status_code=getStatuscode(dom)
    dct = {'Vendor': Qline.strip(), 'URL': dom.strip(), 'Domain': Tdomain.strip(), 'HTTP Status Code': status_code}

    dct_d.append(dct)



if __name__ == '__main__':

    API()
    os.system('cls' if os.name == 'nt' else 'clear')
    dct_d = []

    Query = input('Kindly provide the Input file path: ')

    QFile = open(Query, 'r', encoding="utf8")
    Qline = QFile.readline()
    i = 1
    t = 1
    k = 1
    while Qline:
        print("\n" + str(i) + " - Working on : " + Qline)
        APIreq(Qline)
        i = i + 1
        k = k + 1
        t = t + 1
        if t == 20:
            print("\n We're pausing the program for 60 seconds. Please wait")
            countdown(int(60))
            #time.sleep(60)
            t = 1
        if k == 26:
            # creating the dataframe
            dfEIP = pandas.json_normalize(dct_d)
            print(pandas.DataFrame(dfEIP))
            # saving the dataframe
            dfEIP.to_csv('Backup.csv')
            print("\n Backup file has been created")
            k = 1
        Qline = QFile.readline()
    QFile.close()

    # creating the dataframe
    dfEIP = pandas.json_normalize(dct_d)
    print(pandas.DataFrame(dfEIP))

    # saving the dataframe
    dfEIP.to_csv('FinalOutput.csv')
    os.remove('BackUp.csv')
