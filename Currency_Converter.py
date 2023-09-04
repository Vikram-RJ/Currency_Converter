# Printing the Welcome Address
print("\n***** Welcome to Vikram's Currency Converter Application *****\n")

# Currency values of 72 countries in the form of dictionary type. ( The values are as of on 4th September, 2023 around 9 - 10 pm )
currencies_values = {'Algerian Dinar DZD' : 1.6525, 'Argentine Peso ARS' : 4.231, 'Australian Dollar AUD' : 0.0187, 
                     'Bahrain Dinar BHD' : 0.0046, 'Belarus Ruble BYN' : 0.0305, 'Brazilian Real BRL' : 0.0593, 
                     'Brunei Ringgit BND' : 0.0164, 'Bulgarian Lev BGN' : 0.0219, 'Cambodian Riel KHR' : 50.3667, 
                     'Canadian Dollar CAD' : 0.0164, 'Chilean Peso CLP' : 10.3582, 'Chinese Yuan CNY' : 0.0879, 
                     'Colombian Peso COP' : 48.9393, 'Costa Rican Colon CRC' : 6.4919, 'Czech Crown CZK' : 0.2699, 
                     'Danish Krone DKK' : 0.0834, 'Egyptian Pound EGP' : 0.3735, 'Euro EUR' : 0.0112, 
                     'Hong Kong Dollar HKD' : 0.0947, 'Hungarian Forint HUF' : 4.2835, 'Icelandic Krona ISK' : 1.6109, 
                     'Indian Rupee INR' : 1, 'Indonesia Rupiah IDR' : 183.1515, 'Iranian Rial IRR' : 503.6667, 
                     'Iraqi Dinar IQD' : 15.822, 'Israel New Shekel ILS' : 0.0461, 'Japanese Yen JPY' : 1.7704, 
                     'Jordanian Dinar JOD' : 0.0086, 'Kazakhstani Tenge KZT' : 5.5424, 'Kenya Shilling KES' : 1.7624, 
                     'Kuwaiti Dinar KWD' : 0.0037, 'Kyat MMK' : 25.395, 'Lao Kip LAK' : 237.0196, 
                     'Lebanese Pound LBP' : 180.4179, 'Macau Pataca MOP' : 0.0976, 'Malaysian Ringgit MYR' : 0.0563, 
                     'Mexican Peso MXN' : 0.2076, 'Moldovan Leu MDL' : 0.2158, 'Moroccan Dirham MAD' : 0.1229, 
                     'Naira NGN' : 9.1506, 'Nepalese Rupee NPR' : 1.6006, 'New Taiwan Dollar TWD' : 0.3857, 
                     'New Zealand Dollar NZD' : 0.0204, 'Norwegian Krone NOK' : 0.1289, 'Omani Rial OMR' : 0.0047, 
                     'Pakistani Rupee PKR' : 3.7046, 'Philippine Peso PHP' : 0.6843, 'Polish Zloty PLN' : 0.0501, 
                     'Pound Sterling GBP' : 0.0096, 'Qatari Riyal QAR' : 0.0441, 'Romanian Leu RON' : 0.0554, 
                     'Russian Ruble RUB' : 1.171, 'Saudi Riya SAR' : 0.0453, 'Singapore Dollar SGD' : 0.0164, 
                     'South African Rand ZAR' : 0.2299, 'Sri Lanka Rupee LKR' : 3.8768, 'Swedish Krona SEK' : 0.1332, 
                     'Swiss Franc CHF' : 0.0107, 'Syrian Poung SYP' : 156.987, 'Taka BDT' : 1.3291, 
                     'Tanzania Shilling TZS' : 30.2957, 'Thai Baht THB' : 0.4261, 'Tunisian Dinar TND' : 0.0377, 
                     'Turkish Lira TRY' : 0.3236, 'UAE Dirham AED' : 0.0444, 'Uganda Shilling UGX' : 44.9368, 
                     'Ukrainian Hryvnia UAH' : 0.4442, 'US Dollar USD' : 0.0121, 'Uzbekistani Som UZS' : 145.6386, 
                     'Vietnamese Dong VND' : 287.8095, 'Won KRW' : 15.9472, 'Zambian Kwacha ZMW' : 0.2457}

# options() function to show the list of all the options
def options():
    print("""
Enter - 1 for Currency Converter
2 for Exit Vikram's Currency Converter Application
          """)

# currency_converter() function to convert the currency values from one country's currency value to another
def currency_converter():
    keys = list(currencies_values.keys())
    values = list(currencies_values.values())
    print("Enter - ", end = '')
    for i in range(len(keys)):
        print(str(i+1),"for",keys[i])
    print()
	
	# get the amount to be converted
    amount = float(input("Enter the amount to be converted : "))

	# getting the 'From' and 'To' countrtes by their indices displayed
    _from_ = int(input('Currency "From" : '))
    _to_ = int(input('Currency "To" : '))

	# this one line code is the entire logic, where the currency will be converted from one to another
    converted_amount = (amount / values[_from_-1]) * values[_to_-1]
	
    print("The amount",amount,"from",keys[_from_-1],"to",keys[_to_-1],"is :",converted_amount)

while(True):
    options()
    option = int(input("Enter the option : "))
    if option == 1:
        currency_converter()

    elif option == 2:
        print("\n***** Thanks for interacted with Vikram's Currency Converter Application! Visit Again! *****\n")
        break

    else:
        print("*** You have entered a wrong option, kindly enter a correct option! ***")
