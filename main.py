# QAP 4 Program forthe  ONE STOP INSURANCE COMPANY
# Author: Khoa Pham
# Written: July 26, 2024

# Import Statements
import datetime
import time

# Constants Read from Const.dat file
f = open('Const.dat', 'r')
POLICY_NUM = int(f.readline())
BASIC_PREM_RATE = float(f.readline())
ADD_DISCOUNT_RATE = float(f.readline())
EXTRA_LIABILITY_RATE = float(f.readline())
GLASS_COV_RATE = float(f.readline())
LOANER_RATE = float(f.readline())
HST_RATE = float(f.readline())
MON_PRO_FEE = float(f.readline())
f.close()

# Begin function with time library
def begin():
    print("Welcome to ONE STOP INSURANCE COMPANY POLICY SYSTEM")
    time.sleep(1.5)
    print("Please wait as files load and system's initalize")
    time.sleep(1.5)
    print(".")
    time.sleep(1.5)
    print("..")
    time.sleep(1.5)
    print("...")
    time.sleep(1)
    print("System's Ready!")
    time.sleep(1)

# Closing function with time library
def close():
    print("Thank you for using ONE STOP INSURANCE COMPANY POLICY SYSTEM")
    time.sleep(1.5)
    print("Please wait as files save and system's shuts down")
    time.sleep(1.5)
    print(".")
    time.sleep(1.5)
    print("..")
    time.sleep(1.5)
    print("...")
    time.sleep(1)
    print("Shutting Down...GOODBYE :)")
    time.sleep(1)
    exit()

while True:
    begin()
    # Gather customer information 
    while True:
        first_name = input("Please Enter Customer's First Name: ").strip().title()
        if first_name == "":
            print("Data entry error - First name cannot be empty, Please try again")
        elif first_name.isalpha() == False:
            print("Data entry error - First name must me letter, Please try again")
        else:
            break
    while True:
        last_name = input("Enter Customer Last Name: ").strip().title()
        if last_name == "":
            print("Data entry error - Last name cannot be empty, Please try again")
        elif last_name.isalpha() == False:
            print("Data entry error - Last name must be lette, Please try again")
        else:
            break
    while True:
        street_address = input("Enter Street Address: ").strip().title()
        if street_address == "":
            print("Data entry error - Street address cannot be empty, Please try again")
        else:
            break
    while True:
        city = input("Enter Customer City: ").strip().title()
        if city == "":
            print("Data entry error - City cannot be empty, Please try again")
        elif city.isalnum() == True:
            print("Data entry error - City must be letter, Please try again")
        else:
            break
    valid_province = ['ON', 'QC', 'BC', 'AB', 'MB', 'SK', 'NS', 'NB', 'NL', 'PE', 'NT', 'YT', 'NU']
    while True:
        province = input("Enter Province (XX): ").upper()
        if len(province) != 2:
            print("Data entry error - Please re-enter province as (XX)")
        elif province == "":
            print("Data entry error - Province field cannot be empty, Please try againr")
        elif not province in valid_province:
            print("Data entry error - Please enter a valid province of Canada")
        else:
            break
    while True:
        postal_code = input("Enter Postal Code (A0A 0A0): ").strip().upper()
        if postal_code[3] != " ":
            print("Data entry error - Please include a space between postal code")
        elif len(postal_code) != 7:
            print("Data entry error - Please enter postal code as: A0A 0A0")
        else:
            break
    while True:
        phone_num = input("Enter Phone number (Without Spaces):").strip()
        if len(phone_num) != 10:
            print("Data entry error - Please format phone number as 10 digits without spaces")
        elif not phone_num.isdigit():
            print("Data entry error - Please enter a valid phone number")
        else:
            formatted_phone_num = phone_num[:3] + "-" + phone_num[3:6] + "-" + phone_num[6:]
            break
    while True:
        try:
            number_cars = int(input("Number of cars customer want's to insure: "))
        except:
            print("Data entry error - Please enter a valid number.")
        else:
            if number_cars < 1:
                print("Data entry error - Please enter a number greater than 1.")
            else:
                break
    while True:
        extra_insurance = input("Would customer like to purchase extra insurance (Y/N): ").strip().upper()
        if extra_insurance == "Y" or extra_insurance == "N":
            break
        else:
            print("Data entry error - Please select Y for yes, or N for no")
    while True:
        glass_coverage = input("Would customer like to purchase additional glass coverage (Y/N): ").strip().upper()
        if glass_coverage == "Y" or glass_coverage == "N":
            break
        else:
            print("Data entry error - Please select Y for yes, or N for no")
    while True:
        loaner_car = input("Would customer like to purchase additional loaner car coverage (Y/N): ").strip().upper()
        if loaner_car == "Y" or loaner_car == "N":
            break
        else:
            print("Data entry error - Please select Y for yes, or N for no")
    while True:
        pay_method = input("Would the customer like to pay in full or monthly installments (F/M) ").strip().upper()
        if pay_method == "F" or pay_method == "M":
            break
        else:
            print("Data entry error - Please select F for Full, M for Monthly")
    if pay_method == "F":
        payment_text = "Full"
    if pay_method == "M":
        payment_text = "Monthly"
        while True:
            try:
                down_payment = float(input("Enter the down payment amount if applicable: "))
            except:
                print("Data entry error - Please enter a valid number.")
            else:
                break
    while True:
        try:
            num_claims = int(input("Enter number of previous claims: "))
        except:
             print("Data entry error - Please enter a valid number.")
        else:
            break
    previous_claim = []
    for i in range(num_claims):
        while True:
            claim_number = input(f"Enter claim #{i + 1} number (XXXX): ").strip()
            if claim_number.isalpha == True:
                print("Data entry error - Please enter a valid number")
            elif len(claim_number) != 4:
                print("Data entry error - Please enter correct form (XXXX)")
            else:
                break
        while True:
            claim_date = input(f"Enter claim #{i + 1} date (YYYY-MM-DD): ").strip()
            if len(claim_date) != 10:
                print("Data entry error - Please enter correct form (YYYY-MM-DD)")
            else:
                break
        while True:
            try:
                claim_amount = float(input(f"Enter claim #{i + 1} amount: "))
            except:
                print("Data entry error - Please enter a valid number: ")
            else:
                break
        previous_claim.append((claim_number, claim_date, claim_amount))

    # Perform calculation for the output
    today = datetime.date.today()
    first_day_next_month = datetime.date(today.year + (today.month // 12), (today.month % 12) + 1, 1)
    basic_premium = BASIC_PREM_RATE
    if number_cars > 1:
        add_car = (number_cars - 1) * BASIC_PREM_RATE * (1 - ADD_DISCOUNT_RATE)
        basic_premium += add_car
    if extra_insurance == "Y":
        extra_insurance_cost = number_cars * EXTRA_LIABILITY_RATE
    if glass_coverage == "Y":
        glass_coverage_cost = number_cars * GLASS_COV_RATE
    if loaner_car == "Y":
        loaner_car_cost = number_cars * LOANER_RATE
    total_extra_costs = extra_insurance_cost + glass_coverage_cost + loaner_car_cost
    total_premium = total_extra_costs + basic_premium
    hst = total_premium * HST_RATE
    total_cost = total_premium + hst 
    if pay_method == "M":
        if down_payment > 0:
            total_cost -= down_payment
        total_cost += MON_PRO_FEE
        monthly_payment = total_cost / 8
    elif pay_method == "F":
        monthly_payment = 0

    # formatting variables for output
    full_name = (f"{first_name} {last_name}")
    dsp_first_car_cost = "${:,.2f}".format(BASIC_PREM_RATE)
    dsp_add_car_cost = "${:,.2f}".format(add_car)
    dsp_basic_premium = "${:,.2f}".format(basic_premium)
    dsp_extra_insurance_cost = "${:,.2f}".format(extra_insurance_cost)
    dsp_glass_coverage_cost = "${:,.2f}".format(glass_coverage_cost)
    dsp_loaner_car_cost = "${:,.2f}".format(loaner_car_cost)
    dsp_hst = "${:,.2f}".format(hst)
    dsp_total_cost = "${:,.2f}".format(total_cost)
    dsp_total_extra_costs = "${:,.2f}".format(total_extra_costs)
    dsp_MON_PRO_FEE = "${:,.2f}".format(MON_PRO_FEE)
    dsp_monthly_payment = "${:,.2f}".format(monthly_payment)
    dsp_total_premium = "${:,.2f}".format(total_premium)

    # Display the recepit of the ONE STOP INSURANCE COMPANY
    print()
    print()
    print("-" * 75)
    print("One Stop Insurance Company".center(75))
    print("Insurance Policy Receipt Record".center(75))
    print()
    time.sleep(0.5)
    print(f"Policy Number: {POLICY_NUM}")
    print("-------------------")
    print()
    print(f"Date Created:         {today}")
    print(f"Client Name:          {full_name}")
    print(f"Phone Number:         {formatted_phone_num}")
    print(f"Address:              {street_address}, {city}, {province} ")
    print(f"                      {postal_code}")
    print("-" * 75)
    time.sleep(0.5)
    print("            Basic Premium")
    print(f"Number of Cars Insured: {number_cars:>2d}")
    print(f"Payment Frequency:       {payment_text:<7s}")
    print("---------------------------------")
    print(f"First Car Cost:           {dsp_first_car_cost:>7s} ")
    print(f"Additional Car Cost:    {dsp_add_car_cost:>9}")
    print(f"Basic Premium Total:   {dsp_basic_premium:>10}")
    print(f"---------------------------------")
    print("            Extra Fees")
    print(f"Extra Liability:       {dsp_extra_insurance_cost:>10}")
    print(f"Glass Coverage:        {dsp_glass_coverage_cost:>10}")
    print(f"Loaner Car:            {dsp_loaner_car_cost:>10}")
    print(f"Total Extra Costs:     {dsp_total_extra_costs:>10}")
    print(f"Total Premium Costs:     {dsp_total_premium:>10}")
    print(f"---------------------------------")
    time.sleep(0.5)
    print("            Totals")
    print(f"HST:                   {dsp_hst:>10}")
    if pay_method == "M":
        print(f"Processing Fee:            {dsp_MON_PRO_FEE:>6}")
    print(f"Total Cost:            {dsp_total_cost:>10}")
    print()
    print(f"---------------------------------")
    if pay_method == "M":
        print(f"Monthly Payment:       {dsp_monthly_payment:>10}")
    else:
        print(f"Full Payment:          {dsp_total_cost:>10}")
    print(f"---------------------------------")
    print(f"Next Payment date:     {first_day_next_month}")
    print(f"---------------------------------")
    print("          Previous Claims")
    print("Claim #   Claim Date       Amount")
    print(f"---------------------------------")
    for claim in previous_claim:
        claim_number, claim_date, claim_amount = claim
        dsp_claim_amount = f"${claim_amount:,.2f}"
        print(f"{claim_number}      {claim_date}    {dsp_claim_amount}")
    # Opening Policies.dat file to store information from user input
    f = open("Policies.dat", "a")
    # Writing to file with information below
    f.write("{}, ".format(str(POLICY_NUM)))
    f.write("{}, ".format(first_name))
    f.write("{}, ".format(last_name))
    f.write("{}, ".format(street_address))
    f.write("{}, ".format(city))
    f.write("{}, ".format(province))
    f.write("{}, ".format(postal_code))
    f.write("{}, ".format(formatted_phone_num))
    f.write("{}, ".format(str(number_cars)))
    f.write("{}, ".format(extra_insurance))
    f.write("{}, ".format(glass_coverage))
    f.write("{}, ".format(loaner_car))
    f.write("{}, ".format(pay_method))
    f.write("{}\n".format(str(total_premium)))
    f.write("{}, ".format(claim))
    f.close()
    print()
    print("Policy information processed and saved.")
    print()
    POLICY_NUM += 1
    # Close the Const.dat files
    f = open("Const.dat", 'w')
    f.write("{}\n".format(str(POLICY_NUM)))
    f.write("{}\n".format(str(BASIC_PREM_RATE)))
    f.write("{}\n".format(str(ADD_DISCOUNT_RATE)))
    f.write("{}\n".format(str(EXTRA_LIABILITY_RATE)))
    f.write("{}\n".format(str(GLASS_COV_RATE)))
    f.write("{}\n".format(str(LOANER_RATE)))
    f.write("{}\n".format(str(HST_RATE)))
    f.write("{}\n".format(str(MON_PRO_FEE)))
    f.close()
    continue_question = input("Would you like to start another Invoice (Y/N):  ").upper()
    if continue_question == "Y":
        print("Starting new Policy Application...")
        time.sleep(2)
        continue
    else:
        close()


            
    


    

