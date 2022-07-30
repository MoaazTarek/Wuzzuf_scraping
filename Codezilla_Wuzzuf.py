from unittest import result
import requests                   # to get link
from bs4 import BeautifulSoup     # to make html content 
import csv                        # to open csv file
from itertools import zip_longest   # to arrange data in rows 

job_titles = []               #here we provide the required data and make them into lists
job_skills = []
company_names = []
locations = []
links = []
salaries = []
resposiblities = []
posted_time = []
page_num = 0

while True: # this loop to apply function for all pages required
#2nd step use requests to fetch url
    result = requests.get(f'https://wuzzuf.net/search/jobs/?a=hpb&q=python&start={page_num}')

    #3rd step save page content/markup in bytes object
    src = result.content

    #4th step is to create soup object to parse content (lxml --> html format)
    soup = BeautifulSoup(src, 'lxml') #html content
    

    #5th step provide information you need "Accessing data from html content"
    #All return html content
    #job title, job skills, company name, location
    job_titles_html = soup.find_all('h2', {'class':'css-m604qf'})
    job_skills_html = soup.find_all('a', {'class':'css-5x9pm1'})
    company_names_html = soup.find_all('a', {'class':'css-17s97q8'})
    locations_html = soup.find_all('span', {'class':'css-5wys0k'})
    posted_new = soup.find_all('div', {'class':'css-4c4ojb'})
    posted_old = soup.find_all('div', {'class':'css-do6t5g'})
    posted = [*posted_new, *posted_old]
    no_jobs = int(soup.find('strong').text)

    #6th step extracting the text required from each item "html content" in lists acquired
    for i in range(len(job_titles_html)):
        job_titles.append(job_titles_html[i].text) #adding data to final lists
        url = "https://wuzzuf.net" + job_titles_html[i].find('a').attrs['href'] #this returns the value of "href" in "a" in html content 
        # print(url)
        links.append(url)
        job_skills.append(job_skills_html[i].text)
        company_names.append(company_names_html[i].text)
        locations.append(locations_html[i].text)
        posted_time.append(posted[i].text)
    if page_num > no_jobs // 15:
        break    
    page_num += 1 
    # no_jobs = no_jobs_html   
    # print(locations) 
# print(links)    

# for link in links:
#     # print(link)
#     result = requests.get(link)
#     src = result.content    
#     soup = BeautifulSoup(src, 'lxml')
#     # salaries_html = soup.find('div', {'class':'css-rcl8e5'})
#     # print(salaries_html)
#     # salaries.append(salaries_html.text)
#     res_html_sec = soup.find_all('h2', {'class':'css-fwj1k5'})
#     res_html_ul = soup.find_all('ul')
#     res_html_li = soup.find_all('li')
#     print(res_html_sec)
#     res_txt = ''
#     for li in res_html_li:
#         res_txt += li.text + '| '
#     resposiblities.append(res_txt)    
# # print(resposiblities)

#7th step create csv file with your collected data
file_list = [job_titles, job_skills, company_names, locations, links, posted_time] #all data i need 
file_rows = zip_longest(*file_list) #unpacking data and pairing - arranged in rows
with open('E:\Moaaz\Data Science\Web_Scraping\Wuzzuf.csv', 'w') as Wuz_data:
    wr = csv.writer(Wuz_data)
    wr.writerow(['Job Title', 'Job Skills', 'Company Name', 'Location', 'Link', 'posted'])
    wr.writerows(file_rows)

# my_dictionary = {'a':1}
# try:
#     my_dictionary['b']
# except KeyError as e:
#     raise KeyError('Bad key:' + str(e))