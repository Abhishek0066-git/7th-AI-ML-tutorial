# Project: User se name, email, aur city input lena.

# Program ko:

# Name ko clean karna (strip)
# Name ko proper format mein convert karna (title)
# Email check karna ki "@" present hai
# Email ka domain check karna
# City ko proper format mein print karna
# Final details ko f-string se display karna


name = input ("enter your name: ")
email = input ("enter your email id: ")
city = input ("enter your city: ")

name = name.strip().title()
email = email.strip()
city = city.strip().title()

if "@" in email:
    domain= email.split("@")[1]
    if domain in("gmail.com", "yahoo.com", "outlook.com"):
      print(f"Name: {name}\nEmail: {email}\ncity: {city}")
    else:
       print("invailid domain name\tplease enter valid domain name")
else:
   print("invailid email address\t please enter valid email address")      
    