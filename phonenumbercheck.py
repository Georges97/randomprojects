import phonenumbers
from phonenumbers import timezone, geocoder, carrier

#orginal code from instagram post https://www.instagram.com/p/CUFNIG2g-Pg/
# phoneNumbers = phonenumbers.parse('+12488087821')

# timeZone = timezone.time_zones_for_number(phoneNumbers)

# Carrier = carrier.name_for_number(phoneNumbers, "en")

# Region = geocoder.description_for_number(phoneNumbers, "en")

# print(phoneNumbers)
# print(timeZone)
# print(Carrier)
# print(Region)


#My attempt to make it more automated and look nice.

def obtainphonenumber():
    phonenum_ok = False
    while not phonenum_ok:
        phonenum = input("Please enter your phonenumber plus country code (12487776544) in that format. ")
        phonenum_ok = isnumok(phonenum)

    return phonenum

def isnumok(passed_num):
    """valiadates the phonenumber is only numbers"""
    if passed_num.isdigit():
        return True
    else:
        print("Wasn't only numbers")


PhoneNum = phonenumbers.parse(f"+{obtainphonenumber()}")

TimeBelt = timezone.time_zones_for_number(PhoneNum)

PhoneBrand = carrier.name_for_number(PhoneNum, "en")

Region = geocoder.description_for_number(PhoneNum, "en")

print(f"\n{PhoneNum} \nTimezone: {TimeBelt} \nPhoneBrand: {PhoneBrand} \nRegion: {Region}")

