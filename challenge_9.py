import re
user_mail = input("Entar Your Maile :")

chek_mail = r"^[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-z]{2,}$"

if re.match(chek_mail, user_mail):
    print(f"'{user_mail}' એ માન્ય (valid) ઈમેલ છે.")
else:
    print(f"'{user_mail}' એ અમાન્ય એમીલ છે.")