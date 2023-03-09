# MyVet Invoicing System
# Tristan Budd
# 08/03/2023
# Last Update: Creating invoices done

from datetime import date
import time
import os
import pandas as pd


def main():
    while 1:
        # This is the main menu selection system, Inputs a string, makes uppercase and goes to the target area.
        os.system('cls')
        print("""MYVET INVOICING SYSTEM\n\nToday's Date: """, date.today(), """\n\nChoose from the following:
    I - Create Invoice\n    V - View Transaction\n    X - To Exit""")
        while 1:
            main_menu_input = input("Input Option: ")
            main_menu_input = main_menu_input.upper()
            if main_menu_input == "I":
                create_invoice()
                break
            elif main_menu_input == "V":
                view_transaction()
                break
            elif main_menu_input == "X":
                exit()
            else:
                print("Error: Invalid Input, Please Try Again...")


def create_invoice():
    # This is the form for creating invoices, it collects all the details and puts in the correct format.
    os.system('cls')
    return_method = 0
    df = pd.DataFrame()
    print("CREATING CUSTOMER INVOICE")
    customer_name = "Not Set"
    pet_name = "Not Set"
    while 1:
        if return_method == 1:
            break
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
                        "CUSTOMER NAME": customer_name,
                        "PET NAME": pet_name,
                        "DATE": date.today(),
                    }
                    customer_data = pd.DataFrame(data, index=[0])
                    df = pd.concat([df, customer_data], ignore_index=True, sort=False)
                    while 1:
                        if return_method == 1:
                            break
                        os.system('cls')
                        if item_amount > 0:
                            print("\n")
                            print("*" * 85)
                            print(df[["ITEM", "DESCRIPTION", "QUANTITY", "PRICE", "TOTAL"]].iloc[1:].to_string(
                                index=False))
                            print("*" * 85)
                        print("""\nChoose from the following, then save to continue:\n\tA - Add Item (""", item_amount,
                              """Items )\n\tR - Remove Item\n\tS - Save & Continue""")
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
                                        elif item_quantity_input <= 0:
                                            print("Error: Items Purchased Must Be Greater Than 0, Please Try Again...")
                                        else:
                                            break
                                    else:
                                        print("Error: The Quantity Must Be A Number Input, Please Try Again...")
                                print("\nWhat is the cost of this item (Per Unit):")
                                while True:
                                    item_cost_input = input("Item Cost / Unit: ")
                                    try:
                                        item_cost_input = float(item_cost_input)
                                        if item_cost_input > 999999:
                                            print(
                                                "Error: Items can not cost more than 999999 per unit, Please Try "
                                                "Again...\n You could add more separately if you need more room")
                                        elif item_cost_input <= 0:
                                            print("Error: Cost Per Unit Must Be Greater Than 0, Please Try Again...")
                                        else:
                                            break
                                    except ValueError:
                                        print("Error: Invalid Input, Please Enter A Valid Number Or Float, It Can Not "
                                              "Be More Than 999999 or Lower or Equal To 0")
                                # Saving Data to DataFrame
                                # Item & Quantity are converted to integers to prevent float formatting
                                data = {
                                    "ITEM": int(item_id),
                                    "DESCRIPTION": item_description_input,
                                    "QUANTITY": int(item_quantity_input),
                                    "PRICE": item_cost_input,
                                    "TOTAL": item_cost_input * int(item_quantity_input),
                                    "TOTALRAW": item_cost_input * int(item_quantity_input),
                                }
                                item_data = pd.DataFrame(data, index=[int(item_id)])
                                item_data["ITEM"] = item_data["ITEM"].astype(int)
                                item_data["ITEM"] = item_data["ITEM"].map("{:.0f}".format)
                                item_data["QUANTITY"] = item_data["QUANTITY"].astype(int)
                                item_data["QUANTITY"] = item_data["QUANTITY"].map("{:.0f}".format)
                                item_data["PRICE"] = item_data["PRICE"].astype(float)
                                item_data["PRICE"] = item_data["PRICE"].map("£{:,.2f}".format)
                                item_data["TOTAL"] = item_data["TOTAL"].astype(float)
                                item_data["TOTAL"] = item_data["TOTAL"].map("£{:,.2f}".format)
                                item_data["TOTALRAW"] = item_data["TOTALRAW"].astype(float)
                                df = pd.concat([df, item_data], ignore_index=True)
                                item_id = item_id + 1
                                item_amount = item_amount + 1
                                break
                            elif invoice_items_input == "R":
                                if item_amount == 0:
                                    print("Error: There are no items to remove, Returning to Item Menu...")
                                    time.sleep(2)
                                    break
                                print("\nEnter which item you would like to remove:")
                                while 1:
                                    while 1:
                                        item_remove_input = input("Item ID: ")
                                        if item_remove_input.isnumeric():
                                            item_remove_input = int(item_remove_input)
                                            if item_remove_input <= 0:
                                                print("Error: Number must be greater than 0, As there is no items "
                                                      "stored here, Please Try Again...")
                                            elif item_remove_input > item_amount:
                                                print(
                                                    "Error: There is not this many entries, "
                                                    "Please enter a lower number")
                                            print(df)
                                            item_remove_input = int(item_remove_input)
                                            df = df[df['ITEM'] != item_remove_input]
                                            print(df)
                                            item_id = item_id - 1
                                            item_amount = item_amount - 1
                                            print("Successfully removed item:", item_remove_input, ", Returning to "
                                                                                                   "Item Menu...")
                                            time.sleep(2)
                                            break
                                        else:
                                            print("Error: This must be a number, Please Try Again...")
                                    break
                                break
                            elif invoice_items_input == "S":
                                os.system('cls')
                                if item_amount == 0:
                                    print("Error: There are no items to show, Returning to Item Menu...")
                                    time.sleep(2)
                                    break
                                total_conversion = pd.Series(df['TOTALRAW'].iloc[1:].sum())
                                total_conversion = float(total_conversion)
                                print("*" * 85)
                                print("\n\nINVOICE\n")
                                print("*" * 85)
                                print("\nCustomer: ", df["CUSTOMER NAME"].loc[df.index[0]], "\n\nPet Name: ",
                                      df["PET NAME"].loc[df.index[0]], "\n")
                                print("*" * 85)
                                print(df[["ITEM", "DESCRIPTION", "QUANTITY", "PRICE", "TOTAL"]].iloc[1:].to_string(
                                    index=False))
                                print("*" * 85)
                                print("Subtotal: £{:.2f}\nVAT: £{:.2f}\nInvoice Total: £{:.2f}".format(total_conversion, total_conversion * 0.2, total_conversion * 1.2))
                                print("\nChoose from the following:\n\tS - Exit & Save\n\tC - Continue Editing Items")
                                while 1:
                                    invoice_complete_input = input("Input Option: ")
                                    invoice_complete_input = invoice_complete_input.upper()
                                    if invoice_complete_input == "S":
                                        # Saving data & Returning to Main Menu
                                        print("Saving Data & Returning To Main Menu...")
                                        data = {
                                            "SUBTOTAL": total_conversion,
                                            "VAT": total_conversion * 0.2,
                                            "INVOICE TOTAL": total_conversion * 1.2,
                                        }
                                        item_data = pd.DataFrame(data, index=[0])
                                        item_data["SUBTOTAL"] = item_data["SUBTOTAL"].astype(float)
                                        item_data["SUBTOTAL"] = item_data["SUBTOTAL"].map("£{:,.2f}".format)
                                        item_data["VAT"] = item_data["VAT"].astype(float)
                                        item_data["VAT"] = item_data["VAT"].map("£{:,.2f}".format)
                                        item_data["INVOICE TOTAL"] = item_data["INVOICE TOTAL"].astype(float)
                                        item_data["INVOICE TOTAL"] = item_data["INVOICE TOTAL"].map("£{:,.2f}".format)
                                        df = pd.concat([df.iloc[:4], item_data, df.iloc[4:].reset_index(drop=True)], axis=1)
                                        df = df.iloc[:, :12]
                                        if os.path.exists("data.csv") and os.stat("data.csv").st_size != 0:
                                            df_old = pd.read_csv("data.csv")
                                        else:
                                            df_old = pd.DataFrame()
                                        df = pd.concat([df_old, df], ignore_index=True)
                                        df.to_csv("data.csv", index=False)
                                        time.sleep(2)
                                        return_method = 1
                                        break
                                    elif invoice_complete_input == "C":
                                        break
                                    else:
                                        print("Error: Invalid Input, Please Try Again...")
                                break
                            else:
                                print("Error: Invalid Input, Please Try Again...")
                else:
                    print("\nError: Ensure you have set both a Customer Name & a Pet Name Before Continuing...")
                    print("Returning to the Basic Information Menu...")
                    time.sleep(2)
            break
    if return_method == 1:
        return


def view_transaction():
    print("*" * 85)
    df = pd.read_csv("data.csv")
    print(df[["DATE", "CUSTOMER NAME", "SUBTOTAL", "VAT", "INVOICE TOTAL"]].iloc[:1].to_string(index=False))
    print("*" * 85)
    input()
    print("Returning To Main Menu...")
    time.sleep(2)
    return


if __name__ == "__main__":
    main()
