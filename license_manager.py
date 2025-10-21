import datetime

def check_license(company, licenses):
    today = datetime.date.today()
    if company in licenses and licenses[company] >= today:
        return True
    return False
