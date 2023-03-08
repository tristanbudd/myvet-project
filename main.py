# MyVet Invoicing System
# Tristan Budd
# 08/03/2023
# Last Update: Mostly Finished Creating Items

from datetime import date
import time
import os
import math
import pandas as pd


def main():
    # This is the main menu selection system, Inputs a string, makes uppercase and goes to the target area.
    os.system('cls')
    print("""MYVET INVOICING SYSTEM\n\nToday's Date: """, date.today(), """\n\nChoose from the following:
    I - Create Invoice\n\tV - View Transaction\n\tX - To Exit""")
    while 1:
        main_menu_input = input("Input Option: ")
        main_menu_input = main_menu_input.upper()
        if main_menu_input == "I":
            create_invoice()
        elif main_menu_input == "V":
            view_transaction()
        elif main_menu_input == "X":
            exit()
        else:
            print("Error: Invalid Input, Please Try Again...")


def create_invoice():
    # This is the form for creating invoices, it collects all the details and puts in the correct format.
    os.system('cls')
    df = pd.DataFrame()
    print("CREATING CUSTOMER INVOICE")
    customer_name = "Not Set"
    pet_name = "Not Set"
    while 1:
        print("""\nChoose from the following, then save to continue:\n\tC - Customer Name (""", customer_name,
              """)\n\tP - Pet Name (""", pet_name, """)\n\tS - Save & Continue""")
        while 1:
            customer_detail_input = input("Input Option: ")
            customer_detail_input = customer_detail_input.upper()
            if customer_detail_input == "C":
                print("\nPlease input the customers name:")
                while 1:
                    customer_name_input = input("Input Name: ")
                    if len(customer_name_input) > 25:
                        print("""Error: The Customers Name Can Not Be Longer Than 25 Characters, Please Try Again...""",
                              """\nYou could try using a nickname or just their first name.""")
                    elif len(customer_name_input) < 1:
                        print("Error: The Customers Name Is Too Short, Please Try Again...")
                    else:
                        customer_name = customer_name_input
                        break
            if customer_detail_input == "P":
                print("\nPlease input the customers pet name:")
                while 1:
                    customer_pet_input = input("Input Pet Name: ")
                    if len(customer_pet_input) > 25:
                        print("""Error: The Customers Pet Name Can Not Be Longer Than 25 Characters,""",
                              """ Please Try Again...\nYou could try using a nickname.""")
                    elif len(customer_pet_input) < 1:
                        print("Error: The Customers Pet Name Is Too Short, Please Try Again...")
                    else:
                        pet_name = customer_pet_input
                        break
            if customer_detail_input == "S":
                if customer_name != "Not Set" and pet_name != "Not Set":
                    item_id = 1
                    item_amount = 0
                    data = {
                        "Customer Name": customer_name,
                        "Pet Name": pet_name,
                    }
                    customer_data = pd.DataFrame(data, index = [0])
                    df = pd.concat([df, customer_data], ignore_index=True, sort=False)
                    while 1:
                        os.system('cls')
                        print("""\nChoose from the following, then save to continue:\n\tA - Add Item (""", item_amount,
                              """Items )\n\tR - Remove Item\n\tS - Save & Continue""")
                        if item_amount > 0:
                            print("\n")
                            print("*" * 70)
                            print(df[["ITEM", "DESCRIPTION", "QUANTITY", "PRICE", "TOTAL"]].iloc[1:].to_string(index=False))
                            print("*" * 70)
                        while 1:
                            invoice_items_input = input("Input Option: ")
                            invoice_items_input = invoice_items_input.upper()
                            if invoice_items_input == "A":
                                print("\nPlease input a description of the item:")
                                while 1:
                                    item_description_input = input("Item Description: ")
                                    if len(item_description_input) > 30:
                                        print("""Error: The Item Description Can Not Be Longer Than 30 Characters,""",
                                              """ Please Try Again...\nYou could try using a abbreviation.""")
                                    elif len(item_description_input) < 1:
                                        print("Error: The Item Description Name Is Too Short, Please Try Again...")
                                    else:
                                        break
                                print("\nHow many of this item should be invoiced:")
                                while 1:
                                    item_quantity_input = input("Item Amount: ")
                                    if item_quantity_input.isnumeric():
                                        item_quantity_input = int(item_quantity_input)
                                        if item_quantity_input > 999999:
                                            print("""Error: You can not purchase more than 999999 items, Please Try""",
                                                  """ Again...\nYou could add more separately if you need more room""")
                                        elif item_quantity_input < 0:
                                            print("Error: Items Purchased Must Be Greater Than 0, Please Try Again...")
                                        else:
                                            break
                                    else:
                                        print("Error: The Quantity Must Be A Number Input, Please Try Again...")
                                print("\nWhat is the cost of this item (Per Unit):")
                                while 1:
                                    try:
                                        item_cost_input = input("Item Cost / Unit: ")
                                        item_cost_input = float(item_cost_input)
                                        if item_cost_input.is_integer():
                                            item_cost_input = int(item_cost_input)
                                        else:
                                            item_cost_input = round(item_cost_input, 2)
                                        break
                                    except ValueError:
                                        print("Error: Cost Per Unit Must Be A Float Input, Please Try Again...")
                                    if item_cost_input > 999999:
                                        print("""Error: Items can not cost more than 999999 per unit, Please Try""",
                                              """ Again...\nYou could add more separately if you need more room""")
                                    elif item_cost_input < 0:
                                        print("Error: Cost Per Unit Must Be Greater Than 0, Please Try Again...")
                                    else:
                                        break
                                # Saving Data to DataFrame
                                # Item & Quantity are converted to integers to prevent float formatting
                                data = {
                                    "ITEM": int(item_id),
                                    "DESCRIPTION": item_description_input,
                                    "QUANTITY": int(item_quantity_input),
                                    "PRICE": item_cost_input,
                                    "TOTAL": item_cost_input * int(item_quantity_input),
                                }
                                item_data = pd.DataFrame(data, index=[int(item_id)])
                                item_data["ITEM"] = item_data["ITEM"].astype(int)
                                item_data["ITEM"] = item_data["ITEM"].map("{:.0f}".format)
                                item_data["QUANTITY"] = item_data["QUANTITY"].astype(int)
                                item_data["QUANTITY"] = item_data["QUANTITY"].map("{:.0f}".format)
                                item_data["PRICE"] = item_data["PRICE"].map("£{:,.2f}".format)
                                item_data["TOTAL"] = item_data["TOTAL"].map("£{:,.2f}".format)
                                df = pd.concat([df, item_data], ignore_index=True)
                                item_id = item_id + 1
                                item_amount = item_amount + 1
                                break
                            elif invoice_items_input == "R":
                                print("\nEnter which item you would like to remove:")
                                while 1:
                                    item_remove_input = input("Item: ")
                            elif invoice_items_input == "S":
                                print("test")
                            else:
                                print("test")
                else:
                    print("\nError: Ensure you have set both a Customer Name & a Pet Name Before Continuing...")
                    print("Returning to the Basic Information Menu...")
                    time.sleep(3)
            break


def view_transaction():
    print("test")


if __name__ == "__main__":
    main()
