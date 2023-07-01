import pickle
import customtkinter
from tkinter import messagebox, StringVar
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

def num_digits(url):
    return sum(1 for c in url if c.isdigit())

def num_digits_in_domain(url):
    domain = extract_domain(url)
    return sum(1 for c in domain if c.isdigit())

def num_question_marks(url):
    return url.count('?')

def num_hyphen_in_domain(url):
    domain = extract_domain(url)
    return domain.count('-')

def tld_in_subdomain(url):
    extracted = tldextract.extract(url)
    subdomain = extracted.subdomain
    tld = extracted.suffix
    if tld in subdomain:
        return 1
    else:
        return 0

def num_at_symbols(url):
    return url.count('@')

def num_equals_symbols(url):
    return url.count('=')

def num_ampersand_symbols(url):
    return url.count('&')

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

def rfb_model(x):
    loaded_model = pickle.load(open("new_random_forest_model.sav", 'rb'))
    prediction = loaded_model.predict(x)
    return prediction

def logistic_model(x):
    loaded_model = pickle.load(open("new_logistic_regression_model", 'rb'))
    prediction = loaded_model.predict(x)
    return prediction

def svc_model(x):
    loaded_model = pickle.load(open("SVC_model.sav", 'rb'))
    prediction = loaded_model.predict(x)
    return prediction

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Phishing URL Detection")
root.geometry("500x350")

def check_url(choice):
    url = entry1.get()
    print(choice)

    domain = extract_domain(url)
    tld_subdomain = tld_in_subdomain(url)
    url_len = url_length(url)
    redirect = has_redirects(url)
    suspicious_chars = count_suspicious_chars(url)
    num_digits_url = num_digits(url)
    num_digits_domain = num_digits_in_domain(url)
    num_question_marks_url = num_question_marks(url)
    path_len = path_length(url)
    domain_age = get_domain_age(domain)
    num_hyphen = num_hyphen_in_domain(domain)
    num_at = num_at_symbols(url)
    num_equal = num_equals_symbols(url)
    num_and = num_ampersand_symbols(url)
    data = [{'url_length': url_len, 'num_digits': num_digits_url, 'domain_age': domain_age,
             'count_suspicious_chars': suspicious_chars, 'path_length': path_len,
             'num_digits_in_domain': num_digits_domain,
             'num_?': num_question_marks_url, 'has_redirects': redirect, 'num_hyphen_domain': num_hyphen,
             'tld_in_subdomain': tld_subdomain, 'num_@': num_at,
             'num_=': num_equal, 'num_&': num_and}]

    x = pd.DataFrame(data)


    if choice=="Random forest model":

        if rfb_model(x):
            messagebox.showinfo("URL Status", "The entered URL is real.")
        else:
            messagebox.showinfo("URL Status", "The entered URL is fake.")

    elif choice=="Logistic regression model":

        if logistic_model(x):
            messagebox.showinfo("URL Status", "The entered URL is real.")
        else:
            messagebox.showinfo("URL Status", "The entered URL is fake.")

    elif choice=="Support vector classifier":

        if svc_model(x):
            messagebox.showinfo("URL Status", "The entered URL is real.")
        else:
            messagebox.showinfo("URL Status", "The entered URL is fake.")



options = [
    "Random forest model",
    "Logistic regression model",
    "Support vector classifier"
]


frame = customtkinter.CTkFrame(master = root)
frame.pack(pady = 20 ,padx = 60,fill = "both",expand = True)

label = customtkinter.CTkLabel(master=frame,text=" URL Detection System",font=("Roboto",24))
label.pack(pady = 12 ,padx =10)

entry1 = customtkinter.CTkEntry(master = frame ,placeholder_text =" Enter URL")
entry1.pack(pady =12,padx =10)

combobox = customtkinter.CTkOptionMenu(master=frame,values=options,command=check_url).pack()


root.mainloop()

