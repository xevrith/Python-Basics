emails = [" Neha.Gupta@Gmail.COM ", "rohit@@yahoo.com", "amit.singh@company.co.in","sana.khan.gmail.com", " VIKRAM@Outlook.com"]

clean_email = [email.strip().lower() for email in emails]
print(clean_email)
print()

for email in clean_email:
    if "@" in email and email.count("@") == 1:
        print(f"{email} | Valid")
    else:
        print(f"{email} | Invalid")
