import requests 

URL = "http://realpython.github.io/fake-jobs/"
page = requests.get(URL)

print("page.text")

from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id="ResultsContainer")

print(results.prettify())

job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    print(job_element)
  
# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text.split())
#     print(company_element.text.split())
#     print(location_element.text.split())
#     print()   
    
# python_jobs = results.find_all(
#   "h2", string=lambda text: "python" in text.lower()
# )

# for job in python_jobs:
#   print(job.text)