from validate_email import validate_email
with open('email_file','r') as f:
    email_list = f.readlines()
print("number of emails in the list : ",len(email_list))
valide_emails = []

for i,email in enumerate(email_list) :
    print("\rtraitement de l'email numero : {}-{}".format(i,email))
    if validate_email(email.strip(),verify=True):
         valide_emails.append(email.strip())
print("number of valide emails : ",len(valide_emails))
with open('email_file_output','w') as f:
    f.writelines(valide_emails)
