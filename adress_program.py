# Created by: Tochukwu Iroakazi
# Created on: Oct 2016
# Created for: ICS3U
# This program displays address


def information(first, street_address = ' ', city = ' ',province = ' ' ,postal_code = ' ', apt_number = ' ' ):
    if apt_number == ' ':
       print(street_address + ' ' + city + ' ' + ' ' + province + ' ' + postal_code )
    else:
       print(street_address, + ' ' + city, + ' ' +  province, +' '+ postal_code, +' '+ apt_number)
	
street_address = raw_input('Type in your street address : ')
city = raw_input('Type in your city : ')
province = raw_input('Type in your province : ')
postal_code = raw_input('Type in your postal code : ')
apt_number = raw_input('Do you have an apartment number (y/n) : ')
if apt_number == 'y':
    apt_number = raw_input('Type in your apartment number : ')
    print(street_address + ' ' + city + ' ' +  province +' '+ postal_code +' '+ apt_number)
else:
    print( street_address + ' ' + city + ' ' +  province + ' ' + postal_code  )


