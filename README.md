# Domain-Lookup-Script-using-ChatGPT
Domain Lookup Script using ChatGPT API is a program that automates the process of identifying vendors from the Internet.

**Features:** 

The Python script uses natural language processing to understand the vendor name and extract relevant information from the internet. It then applies machine learning algorithms to identify the official websites of the vendor. The script is user-friendly and can be customized to suit specific needs.


**Benefits:** 

The script provides a time-saving solution for businesses to quickly identify the official websites of their vendors. It eliminates the need for manual research and helps businesses to make informed decisions about their vendor partnerships.

 
**Usage:**

To use the script, the user needs to provide the name of the vendor as input. The script will then utilize ChatGPT API to extract relevant information from the internet and provide a list of official websites associated with the vendor.
 

**How to use:**

We need an API key or token to run this script, that we can possibly generate from the URL below.

URL: https://platform.openai.com/account/api-keys 

Step 1: Execute the script & provide your API key / Token

![image-20230224-104628](https://github.com/rwashim/Domain-Lookup-Script-using-ChatGPT/assets/44086222/15d8019b-87c1-4cb1-bb3d-e5fad1cfa7f1)


Step 2: Enter your input file path

![image-20230224-104916](https://github.com/rwashim/Domain-Lookup-Script-using-ChatGPT/assets/44086222/93f143ee-956c-4ba6-93ac-c7472a904e2d)


Step 3: It produces the output as shown below and stores it in FinalOutput.csv:

![image-20230224-105356](https://github.com/rwashim/Domain-Lookup-Script-using-ChatGPT/assets/44086222/cc4bdf17-3abb-4d14-b30e-d0d0829bedf7)

**Source Code Overview:**

1. Package Installations:

   ![image-20230224-110128](https://github.com/rwashim/Domain-Lookup-Script-using-ChatGPT/assets/44086222/96a00587-b160-46ba-9751-734b851877b1)

To install any package, we just need to execute the below command on the Python terminal or command prompt:

pip3 install <"package name">

example: pip3 install os

2. Function getStatuscode():

This function's return value is the HTTP Status code for any URL that is sent as an argument. It makes it easier for us to tell whether the website is still active or not.

![image-20230224-110328](https://github.com/rwashim/Domain-Lookup-Script-using-ChatGPT/assets/44086222/6df3fa25-b364-4a05-b6d0-e0cf33216595)

HTTP Status Code:
Informational responses (100 – 199)
Successful responses (200 – 299)
Redirection messages (300 – 399)
Client error responses (400 – 499)
Server error responses (500 – 599)
For more information kindly go through the below URL:

HTTP Status Codes: https://www.restapitutorial.com/httpstatuscodes.html 

Note: If any form of error is encountered, it returns -1. such as SSL Error

3. Function countdown():

Time (only in seconds) is the only argument required for this function. then start a backward countdown, pausing the programme until it is done. 

![image-20230224-111456](https://github.com/rwashim/Domain-Lookup-Script-using-ChatGPT/assets/44086222/ec28685a-51dd-486e-834a-3c333e462d33)


4. Function API():

To avoid having to enter your API key each time this script is run, this method saves your API key or token into a text file called APIKey.txt

![image-20230224-112316](https://github.com/rwashim/Domain-Lookup-Script-using-ChatGPT/assets/44086222/f356c93f-f77f-4157-9e9b-bd49c66cb478)

5. Function APIreq():

With this method, we use the ChatGPT's API to submit requests and get responses in JSON format. The response is then assessed, and just the necessary information is extracted and stored in a dictionary. Also, we build a data frame with statistics.

Typically, we see errors when the ChatGPT model is overwhelmed with other requests. This feature eliminates this problem as well. When we meet such an error, our script pauses the entire programme for five minutes before re-executing the previous statement immediately. This will let the script operate smoothly and allow us to quickly resolve any runtime errors. 

![image-20230224-115146](https://github.com/rwashim/Domain-Lookup-Script-using-ChatGPT/assets/44086222/62806c5f-b228-4073-8e79-f075af1bb364)

6. Main function:

This is the main() function, which is where we control the other functions. 

![image-20230224-121021](https://github.com/rwashim/Domain-Lookup-Script-using-ChatGPT/assets/44086222/4f98c826-e2ad-48ed-87d4-32e5156d144c)

Since we are utilising the free ChatGPT API. So, we are restricted in certain ways. Thus, we halt the script for one minute per 20 requests. Also, this script creates an automatic backup in a Backup.csv file after getting every 25 results. When the script terminates itself for whatever reason—such as a power outage, a lost connection to the internet, a runtime problem, etc.—this capability comes in handy.

![image-20230224-121249](https://github.com/rwashim/Domain-Lookup-Script-using-ChatGPT/assets/44086222/4e49b533-c2b3-486a-8cae-3fe3a6b1be42)

**Conclusion:**

The Python script that uses ChatGPT API is an effective tool for businesses to identify the official websites of their vendors. It utilizes the latest technology to provide accurate results and can be customized to suit specific needs. This script is a valuable addition to any business looking to streamline its vendor identification process.


