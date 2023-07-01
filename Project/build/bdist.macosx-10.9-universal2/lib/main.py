import pickle

import customtkinter
from tkinter import messagebox
import pandas as pd

import tldextract
import urllib.parse
import requests
import re
import whois

from datetime import datetime



def extract_domain(url):
    return urllib.parse.urlparse(url).netloc

def url_length(url):
    return len(url)

def subdomain_count(url):
    domain_parts = extract_domain(url).split('.')
    return len(domain_parts[:-2])

def is_https(url):
    if urllib.parse.urlparse(url).scheme == 'https':
      return 1
    else:
      return 0

def has_redirects(url):
    try:
        response = requests.get(url, allow_redirects=False, timeout=3)
        if response.status_code in [301, 302, 303, 307, 308]:
            return 1
        else:
            return 0
    except:
        return -1

def count_suspicious_chars(url):
    return len(re.findall('[@!$#%^&*()_+|~=`{}[\]:/;<>?,.]', url))




def path_length(url):
    path = urllib.parse.urlparse(url).path
    return len(path)
def check_tld(url):
    extracted = tldextract.extract(url)
    tld = extracted.suffix

    # Add your condition here
    if tld == 'com':
        return 1
    else:
        return 0

def tld_in_subdomain(url):
    extracted = tldextract.extract(url)
    subdomain = extracted.subdomain
    tld = extracted.suffix

    if tld in subdomain:
        return 1
    else:
        return 0

def get_domain_age(domain):
    try:
        w = whois.whois(domain)
        creation_date = w.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        now = datetime.now()
        age = (now - creation_date).days
        return age
    except Exception as e:
        return -1


def model_prediction(x):
    loaded_model = pickle.load(open("/Users/mahmoud/Documents/college/6th semester/data mining/project/random_forest_model.sav", 'rb'))
    prediction= loaded_model.predict(x)
    return prediction


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def check_url():
    url = entry1.get()
    if is_real_url(url):
        messagebox.showinfo("URL Status", "The entered URL is real.")
    else:
        messagebox.showinfo("URL Status", "The entered URL is fake.")


def ip_address(domain):
    if bool(re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", domain))== True:
        return 1
    else:
        return 0



def is_real_url(url):
    print(url)
    domain = extract_domain(url)
    tld_in_path = check_tld(url)
    tld_subdomain = tld_in_subdomain(url)
    url_len = url_length(url)
    subdomain_counts = subdomain_count(url)
    https = is_https(url)
    redirect = has_redirects(url)
    suspicious_chars = count_suspicious_chars(url)
    ip_add = ip_address(domain)
    path_len = path_length(url)
    domain_age = get_domain_age(domain)
    data=[{'tld_in_path': tld_in_path,'tld_in_subdomain':tld_subdomain,'url_length':url_len,'subdomain_counts':subdomain_counts,'is_https':https,'has_redirects':redirect,
          'count_suspicious_chars':suspicious_chars,'is_ip_address':ip_add,'path_length':path_len,'domain_age':domain_age}]

    x = pd.DataFrame(data)
    prediction=model_prediction(x)
    return prediction




frame = customtkinter.CTkFrame(master = root)
frame.pack(pady = 20 ,padx = 60,fill = "both",expand = True)

label = customtkinter.CTkLabel(master=frame,text=" URL Detection System",font=("Roboto",24))
label.pack(pady = 12 ,padx =10)

entry1 = customtkinter.CTkEntry(master = frame ,placeholder_text =" Enter URL")
entry1.pack(pady =12,padx =10)

button = customtkinter.CTkButton(master=frame,text="Enter",command = check_url)
button.pack(pady =12,padx =10)

root.mainloop()

