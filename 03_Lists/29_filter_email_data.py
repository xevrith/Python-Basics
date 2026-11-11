# Data quality filter

emails = [
    "aman@gmail.com",
    "sara@gmail",
    "rahul@yahoo.com",
    "priya@outlook.com",
    "invalid"
]

check_email = [email for email in emails if email.endswith(".com")]
print(check_email)