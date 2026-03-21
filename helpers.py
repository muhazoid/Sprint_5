import random



def generate_unique_email():
    first_name = "alexey"
    last_name = "chikichev" 
    cohort = "42"
    random_digits = str(random.randint(100, 999))
    login = f"{first_name}_{last_name}_{cohort}_{random_digits}"
    domains = ["yandex.ru", "ya.ru", "gmail.com", "mail.ru"]
    domain = random.choice(domains)
    email = f"{login}@{domain}"
    return email

