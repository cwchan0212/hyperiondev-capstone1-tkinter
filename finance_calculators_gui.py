# Task 12 - Capstone Project I - Variables and Control Structures
# Compulsory Task 1 (Modified)
# finance_calculators_gui.py
# Author: Eddy Chan, Chi-wai
# Date: 5 January 2023
#
#######################################################################################################################
# import math, tkinter libraries and their modules
#
import math, os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#
########################################################################################################################
# Set environment variables
# 
# Set the variable "window_width" to 640 as the width of the window
window_width  =  640
# Set the variable "window_height" to 480 as the height of the window
window_height  =  640
# Set the variable "window_margin_left" to 10 as the left margin of the window
window_margin_left = 10
# Set the variable "window_margin_top" to 10 as the top margin of the window
window_margin_top = 10
# Set the variable "window_margin_top" to 30 as the top padding of the window
window_padding_top = 30
# Set the variable "current_directory" to store the current directory path
# Replace the backslash of the variable "current_directory" to dash
current_directory = os.getcwd().replace("\\", "/")
#
########################################################################################################################
# Main
#
# Create an instance of the tkinter frame
window = Tk()
# Creating object "icon" of photoimage class Image should be in the same folder in which script is saved


icon = PhotoImage(file = f"{current_directory}/assets/github.png")
  # Setting icon of master window
window.iconphoto(False, icon)
# Set the variable "screen_width" to store the width of the screen
screen_width = window.winfo_screenwidth()
# Set the variable "screen_height" to store the height of the screen
screen_height = window.winfo_screenheight()
# Set the variable "x_cordinate" to the difference between the screen width and the window width
x_cordinate = int((screen_width/2) - (window_width/2))
# Set the variable "y_cordinate" to the difference between the screen height and the window height
y_cordinate = int((screen_height/2) - (window_height/2))
# Set the title of the window
window.title("Financial Calculator - Investment / Monthly Home Loan Repayment")
# Set the geometry of the frame
window.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
# Set the resizable property to False
window.resizable(False, False)
# Set the variable "font_setting_1" to the setting of the header 
font_setting_1 = ("Helvetica", 18)
# Set the variable "font_setting_2" to the setting of the paragraph 
font_setting_2 = ("Helvetica", 12)
# Create the list "investment_stringvar_name_list" to store the name of the StringVars() of the Entry of the Investment 
investment_stringvar_name_list = ["investment_deposit_amount","investment_interest_rate", "investment_year", "investment_interest_type", "investment_amount"]
# Create the list "investment_stringvar" to store the StringVar() of the Entry of the Investment
investment_stringvar =  [ StringVar(window, "1", investment_stringvar_name_list[i]) if i == 3 else StringVar(window, "", investment_stringvar_name_list[i])  for i in range(5)   ] 
# Set the variable "investment_count" to 0 
investment_count = 0
# Create the list "bond_stringvar_name_list" to store the name of the StringVars() of the Entry of the Bond of the Investment
bond_stringvar_name_list = ["bond_present_value_of_the_house","bond_interest_rate", "bond_months", "bond_amount"]
# Create the list "bond_stringvar" to store the StringVar() of the Entry of the Investment
bond_stringvar =  [ StringVar(window, "", bond_stringvar_name_list[i])  for i in range(4) ] 
# Set the variable "bond_count" to 0 
bond_count = 0
#
########################################################################################################################
# Create self-defined functions
########################################################################################################################
# Start: get_center_coords
#
# Create a function "get_center_coords" with the parameters "window" and "element" to calculate the left and top of the element
# to set the element as the centre
def get_center_coords(window, element):
    # Set the list "coords" to empty
    coords = []
    # If the parameters "window" and element are not empty, refresh and update the instance "window",
    # set the list to store the top and left of the elements 
    if window and element:
        window.update()
        coords = [(window_width - element.winfo_reqwidth()) // 2,
                  (window_height - element.winfo_reqheight()) // 2]
    # Return the list "coords"
    return coords
#
# End: get_center_coords
########################################################################################################################
# Start: clear_investment
#
# Create a function "clear_investment" to clear the entry fields
def clear_investment():
    # Use for-loop to clear all the entry fields in the list "investment_entry_list"
    for index, investment_entry in enumerate(investment_entry_list):
        # If the element "investment_entry" is not a "Button" object, it checks whether it is a "RadioButton" object
        if not isinstance(investment_entry, Button):
            # If the element "investment_entry" is not a "RadioButton" object, clear the entry field "investment_entry"
            if not isinstance(investment_entry, Radiobutton):
                investment_entry.delete(0, 'end')
                # If the attribute "text" of the element "investment_entry" is "investment_amount", set the entry field to "DISABLED"
                if "investment_amount" in investment_entry.config("text"):
                    investment_entry.config(state=DISABLED)
            # If the element "investment_entry" is a "RadioButton" object, set the radio button to the default value
            else:
                investment_entry.select()

#
# End: clear_investment
########################################################################################################################
# Start: compute_investment
#
# Create a function "compute_investment" to calculate the simple/compound interest with the initial deposit
def compute_investment():
    # Set the variables "deposit_amount", "interest_rate", "year", "interest_type", "amount" to initial values
    deposit_amount, interest_rate, year, interest_type, amount = 0, 0, 0, 1, 0 
    # Use for-loop to validate the StringVar() values of the list "investment_stringvar"
    for index, investment in enumerate(investment_stringvar):
        # If the variable "index" is less than or equal to 2, check the validity of the StringVar() values of the list "investment_stringvar"
        if index <= 2: 
            # If the variable "index" is 1, set the variable "field_name" to "DEPOSIT AMOUNT", 1 for "INTEREST RATE", 2 for "YEAR"
            field_name = "DEPOSIT AMOUNT" if index == 0 else "INTEREST RATE" if index == 1 else "YEAR"
            # If the element "investment_stringvar" is empty, print the message to notify the user
            if investment_stringvar[index].get() == "":
                messagebox.showerror("",  f"The field {field_name} is blank.")
                # Set focus to the field with the invalid value
                investment_entry_list[index].focus_set()
                # Use "return" to exit the function
                return
            # If the element "investment_stringvar" is not a number, print the message to notify the user
            # By calling the function "check_input_number" with the parameter "investment_stringvar"
            elif check_input_number(investment_stringvar[index].get())  ==  -1:
                messagebox.showerror("",  f"The field {field_name} is not a numberic.")
                # Set focus to the field with the invalid value
                investment_entry_list[index].focus_set()
                # Use "return" to exit the function
                return
            # If the element "investment_stringvar" is less than or equal to zero, print the message to notify the user
            # By calling the function "check_input_number" with the parameter "investment_stringvar"
            elif float(investment_stringvar[index].get()) <= 0:
                messagebox.showerror("",  f"The field {field_name} is not a positive number.")
                # Set focus to the field with the invalid value
                investment_entry_list[index].focus_set()
                # Use "return" to exit the function
                return
        # Use try-except block to test the overflow error of the calculation
        try: 
            # Set the variables "deposit_amount", "interest_rate", "year", "interest_type" to store the StringVar() values of the list "investment_stringvar" 
            deposit_amount, interest_rate, year, interest_type =  [float(investment_stringvar[index].get())  for index in range(len(investment_stringvar)) if index < len(investment_stringvar)-1 ]
            # If the variable "interest_type" is 1, calculate the amount by simple interest rate, 
            # otherwise calculate it by compound interest rate
            amount = round(deposit_amount * (1 + (interest_rate/100) * year),2) if int(interest_type) == 1 else round(deposit_amount * math.pow((1 + (interest_rate/100)), year),2) 
        # If it fails to calculate the amount, set the amount to the overflow value
        except OverflowError:
            amount = float('inf')
            
    # Use for-loop to enable the list "investment_entry_list" with the attribute "text" as "investment_amount"
    for index, investment_entry in enumerate(investment_entry_list):
        # If the attribute "text" of the element "investment_entry" is "investment_amount", set the entry field to "normal"
        if "investment_amount" in investment_entry.config("text"):
            investment_entry.configure(state = "normal")
            # Clear the entry of the element "investment_entry"
            investment_entry.delete(0, END)
            # Set the entry with a thousand separator
            investment_entry.insert(0, f"{amount: ,}")
#
# End: compute_investment    
########################################################################################################################    
# Start: clear_bond
#          
# Create a function "clear_bond" to clear the entry fields   
def clear_bond():
    # Use for-loop to clear all the entry fields in the list "bond_entry_list"
    for index, bond_entry in enumerate(bond_entry_list):
        # If the element "bond_entry" is not a "Button" object, it clears the entry of the element "bond_entry"
        if not isinstance(bond_entry, Button):
            bond_entry.delete(0, 'end')
            # If the attribute "text" of the element "bond_entry" is "bond_amount", set the entry field to "DISABLED"
            if "bond_amount" in bond_entry.config("text"):
                bond_entry.config(state=DISABLED)
#
# End: clear_bond
########################################################################################################################
# Start: compute_bond
#
# Create a function "compute_bond" to calculate the monthly repayment amount
def compute_bond():
    # Set the variables "present_value_of_the_house", "interest_rate", "number_of_months", "amount" to initial values
    present_value_of_the_house, interest_rate, number_of_months, amount = 0, 0, 0, 0 
    # Use for-loop to validate the StringVar() values of the list "bond_stringvar"
    for index, bond in enumerate(bond_stringvar):
        # If the variable "index" is less than or equal to 2, check the validity of the StringVar() values of the list "bond_stringvar"
        if index <= 2:
            # If the variable "index" is 1, set the variable "field_name" to "PRESENT VALUE OF THE HOUSE", 1 for "INTEREST RATE", 2 for "NUMBER OF MONTHS"
            field_name = "PRESENT VALUE OF THE HOUSE" if index == 0 else "INTEREST RATE" if index == 1 else "NUMBER OF MONTHS"
            # If the element "bond_stringvar" is empty, print the message to notify the user            
            if bond_stringvar[index].get() == "":
                messagebox.showerror("",  f"The field {field_name} is blank.")
                # Set focus to the field with the invalid value
                bond_entry_list[index].focus_set()
                # Use "return" to exit the function
                return
            # If the element "bond_stringvar" is not a number, print the message to notify the user
            # By calling the function "check_input_number" with the parameter "bond_stringvar"
            elif check_input_number(bond_stringvar[index].get())  ==  -1:
                messagebox.showerror("",  f"The field {field_name} is not a numberic.")
                # Set focus to the field with the invalid value
                bond_entry_list[index].focus_set()
                # Use "return" to exit the function
                return
            # If the element "bond_stringvar" is less than or equal to zero, print the message to notify the user
            # By calling the function "check_input_number" with the parameter "bond_stringvar"            
            elif float(bond_stringvar[index].get()) < 0:
                messagebox.showerror("",  f"The field {field_name} is not a positive number.")
                # Set focus to the field with the invalid value
                bond_entry_list[index].focus_set()
                # Use "return" to exit the function
                return
    
        # Use try-except block to test the overflow error of the calculation
        try: 
        # Set the variables "present_value_of_the_house", "interest_rate", "number_of_months" to store the StringVar() values of the list "bond_stringvar" 
            present_value_of_the_house, interest_rate, number_of_months =  [float(bond_stringvar[index].get())  for index in range(len(bond_stringvar)) if index < len(bond_stringvar)-1 ]
            amount = round(((interest_rate/100)/12) * present_value_of_the_house / (1 - math.pow((1 + ((interest_rate/100)/12)), (-number_of_months))),2)
        # If it fails to calculate the amount, set the amount to the overflow value
        except OverflowError:
            amount = float('inf')
    
    # Use for-loop to enable the list "bond_entry_list" with the attribute "text" as "bond_amount"
    for index, bond_entry in enumerate(bond_entry_list):
        # If the attribute "text" of the element "bond_entry" is "bond_amount", set the entry field to "normal"
        if "bond_amount" in bond_entry.config("text"):
            bond_entry.configure(state = "normal")
            # Clear the entry of the element "bond_entry"
            bond_entry.delete(0, END)
            # Set the entry with a thousand separator
            bond_entry.insert(0, f"{amount: ,}")
#
# End: compute_bond
########################################################################################################################
# Start: check_input_number
#
# Create a function "check_input_number" with the parameter "number_string" to check whether the input is a string or a number 
def check_input_number(number_string):
    # If the parameter "number_string" is an integer, return 1
    if str(number_string).isdigit():
        # Return 1 as it is an integer
        return 1
    # If the parameter "number_string" is not an integer, test it as a float or string
    else:
        # Use try-except block to test the parameter as float or string
        try:
            # try to convert the data type of the parameter "number_string"
            float(str(number_string))
            # Return 0 as it is a float
            return 0
        # If it is an exception, return -1 as it is a string
        except:
            # Return -1 as it is a string
            return -1
#
# End: # check_input_number
########################################################################################################################
# Start: Labels of the Investment 
#
# Set the variable "element_label_top_count" to 0
element_label_top_count = 0
# Set the list "investment_item_list" to store the text of the labels
investment_item_list = [
    "Investment Calculator", 
    "Investment - to calculate the amount of interest you'll earn on your investment",
    "Amount of deposit:",
    "Interest rate:",
    "Year:",
    "Interest type:",
    "Amount:"    
]

# Create a list "investment_label_list" to empty
investment_label_list = []
# Set a variable "element_entry_top_count" to 0
element_entry_top_count = 0
# Set the variables "left_margin" and "top_margin" to 0
left_margin, top_margin = 0, 0
# Set a variable "label_2_margin_top" to 0
label_2_margin_top = 0
# Use for-loop to store the Label objects in the list "investment_item_list"
for index, investment_item in enumerate(investment_item_list):
    # If the variable "index is 0, set the variable "font_set" to "font_setting_1", 
    # otherwise set it to "font_setting_2"
    font_set = font_setting_1 if index == 0 else font_setting_2
    # Use the list "investment_label_list" to store the "Label" object
    investment_label_list.append(Label(window, text = investment_item, font = font_set))
    # If the index is less than or equal to 1, set the variable "left_margin" to the left margin of the "Label" object
    # By calling the function get_center_coords with the parameters "window" and "investment_label_list"
    if index <= 1:
        left_margin = get_center_coords(window, investment_label_list[index])[0]
    # Set the variable "label_x" to the variable "left_margin"
    label_x = left_margin
    # Set the variable "label_y" to the sum of the variables "window_marin_top" and "window_padding_top" with adjustment
    label_y = window_margin_top + window_padding_top * element_label_top_count
    # If the variable "index" is 2, set the variable "label_2_margin_top" to the variable "label_y"
    if index == 2:
        label_2_margin_top = label_y
    # Place the Label object in the window
    investment_label_list[index].place(x = label_x, y = label_y)
    # The variable "element_label_top_count" is added by 1
    element_label_top_count += 1
    # Set the variable "top_margin" to the variable "label_y"
    top_margin = label_y
#
# End: Labels of the Investment 
########################################################################################################################
# Start: Entry/Button/RadioButton of the Investment 
#
# Create the list "investment_entry_list" to empty
investment_entry_list = []
# Set the variable "element_entry_top_count" to 0
element_entry_top_count = 0
# Set the variables "entry_x" and "entry_y" to 0
entry_x, entry_y = 0, 0
# Create the variable "element_total" to 
element_total = 8
# Create the variable "entry_index"
entry_index = 0
# Use while-loop to create the "Entry/Button/RadioButton" objects and store them in the list "investment_entry_list"
while entry_index < element_total:
    # If the variable "entry_index" is less than or equal to 2, store the "Entry" object to the list "investment_entry_list"
    if entry_index <= 2:
        investment_entry_list.append(Entry(window, width=20, textvariable = investment_stringvar[investment_count], font = font_setting_2, justify="right"))
        # Set the variable "entry_x" to the left margin of the "Entry" object
        entry_x = window_width - investment_entry_list[entry_index].winfo_reqwidth() - left_margin
        # Set the variable "entry_y" to the top margin of the "Entry" object with adjustment
        entry_y = label_2_margin_top +  window_padding_top * element_entry_top_count
        # Place the "Entry" object in the window
        investment_entry_list[entry_index].place(x = entry_x, y = entry_y)
        # The variable "investment_count" is added by 1
        investment_count += 1   
    # If the variable "entry_index" is 3, store the "Radiobutton" object in the list "investment_entry_list"
    if entry_index == 3:
        # Set the variable "count" to 1
        count = 1        
        # Set the variable "entry_y" to the top margin of the "Radiobutton" object with adjustment
        entry_y = label_2_margin_top +  window_padding_top * element_entry_top_count
        # Set the variable "radio_x" to the left margin of the "Radiobutton" object
        radio_x = window_width - left_margin - 105 * count
        # Set the variable "radio_y" to the variable "entry_y"
        radio_y = entry_y
        # Create the dictionary "interest_type_dictionary" to store the keys and values or the types of interest
        interest_type_dictionary = {"compound": 2, "simple": 1}
        # Us for-loop to store the "Radiobutton" object in the list "investment_entry_list"
        for key, value in interest_type_dictionary.items(): 
            investment_entry_list.append(Radiobutton(window, text = key, value = value, variable = investment_stringvar[investment_count]  , width = 10, font = font_setting_2))
            # Place the "Radiobutton" object in the window
            investment_entry_list[entry_index].place(x = window_width - left_margin - 105 * count  , y  = entry_y)
            # The variable "count" is added by 1
            count += 1
            # The variable "entry_index" is added by 1
            entry_index += 1
        # The variable "investment_count" is added by 1
        investment_count += 1
        # The variable "element_entry_top_count" is added by 1
        element_entry_top_count += 1
    # If the variable "entry_index" is 5, store the "Entry" object in the list "investment_entry_list"
    if entry_index == 5 :
        investment_entry_list.append(Entry(window, width=20, textvariable = investment_stringvar[investment_count], font=font_setting_2, justify = "right"))
        # Set the "Entry" object of the list "investment_entry_list" to disable
        investment_entry_list[-1].configure(state = DISABLED)
        # Set the variable "entry_x" to the left margin of the "Entry" object
        entry_x = window_width - investment_entry_list[entry_index].winfo_reqwidth() - left_margin
        # Set the variable "entry_y" to the top margin of the "Entry" object with adjustment
        entry_y = label_2_margin_top +  window_padding_top * element_entry_top_count
        # Place the "Entry" object in the window
        investment_entry_list[entry_index].place(x = entry_x, y = entry_y)
        # The variable "investment_count" is added by 1
        investment_count += 1
    # The variable "element_entry_top_count" is added by 1
    element_entry_top_count += 1
    # The variable "entry_index" is added by 1
    entry_index += 1
    # If the variable "entry_index" is 6, store the "Button" object in the list "investment_entry_list"
    if entry_index == 6:
        # Set the variable "count" to 1
        count = 1
        # Create the list "investment_button_list" to the text of the "Button" object
        investment_button_list = ["Clear", "Calculate"]
        # Use for-loop to store the "Button" object to the list "investment_entry_list"
        for button_index, button in enumerate(investment_button_list):
            # If the variable "count" is 1, store the [CLEAR] "Button" object to the list "investment_entry_list"
            if count == 1:
                investment_entry_list.append(Button(window, text = button,  width=9, font=font_setting_2, command = lambda: clear_investment()) )
            # If the variable "count" is not 1, store the [CALCULTE] "Button" object to the list "investment_entry_list"
            else:
                investment_entry_list.append(Button(window, text = button,  width=9, font=font_setting_2, command = lambda: compute_investment()))
            # Set the variable "entry_x" to the left margin of the "Entry" object
            entry_x = window_width - left_margin - investment_entry_list[entry_index].winfo_reqwidth() * count
            # Set the variable "entry_y" to the top margin of the "Entry" object with adjustment
            entry_y = label_2_margin_top +  window_padding_top * element_entry_top_count
            # Place the "Button" object in the window
            investment_entry_list[entry_index].place(x = entry_x, y = entry_y)
            # The variable "entry_index" is added by 1
            entry_index += 1
            # Set the variable "count" to 1
            count += 1
#
# End: Entry/Button/RadioButton of the Investment 
########################################################################################################################
# Start: Label of the Bond 
# Set the list "bond_item_list" to store the text of the labels
bond_item_list = [
    "Home Loan Repayment Calculator", 
    "bond - to calculate the amount you'll have to pay on a home loan",
    "Present value of the House",
    "Interest rate:",
    "Number of months:",
    "Amount:"    
]

# Set the list "bond_label_list" to empty
bond_label_list = []
 
# The variable "element_label_top_count" is added by 4 as a separator
element_label_top_count += 4
# Set the variable "bond_left_margin" to the variable "left_margin"
bond_left_margin = left_margin
# Use for loop to store the "Label" objects in the list "bond_label_list"
for index, bond_item in enumerate(bond_item_list):
    # If the variable "index is 0, set the variable "font_set" to "font_setting_1", 
    # otherwise set it to "font_setting_2"
    font_set = font_setting_1 if index == 0 else font_setting_2
    # Use the list "bond_label_list" to store the "Label" object
    bond_label_list.append(Label(window, text = bond_item, font = font_set))
    # If the index is 0, Set the variable "bond_left_margin" to the left margin of the [HEADER] Label object,
    # Otherwise set it to the left margin of the list of "investment_label_list"
    bond_left_margin = get_center_coords(window, bond_label_list[index])[0] if index == 0 else left_margin
    # Set the variable "label_x" to the variable "left_margin"
    label_x = bond_left_margin    
    # Set the variable "label_y" to the sum of the variables "window_marin_top" and "window_padding_top" with adjustment   
    label_y = window_margin_top + window_padding_top * element_label_top_count
    # If the variable "index" is 2, set the variable "label_2_margin_top" to the variable "label_y"
    if index == 2:
        label_2_margin_top = label_y
    # Place the Label object in the window
    bond_label_list[index].place(x = label_x, y = label_y)
    # The variable "element_label_top_count" is added by 1
    element_label_top_count += 1
    # Set the variable "top_margin" to the variable "label_y"
    top_margin = label_y
#    
# End: Label of the Bond 
########################################################################################################################
# Start: Entry/Button of the Bond 
#
# Create a list "bond_entry_list" to empty
bond_entry_list = []
# Set the variable "element_total" to 6
element_total = 6
# Set the variable "entry_index" to 0
entry_index = 0
# Set the variable "element_entry_top_count" to 0
element_entry_top_count = 0
# Use while-loop to create the "Entry/Button" objects and store them in the list "bond_entry_list"
while entry_index < element_total:
    # If the variable "entry_index" is less than or equal to 3, store the "Entry" object to the list "bond_entry_list"
    if entry_index <= 3:
        bond_entry_list.append(Entry(window, width=20, textvariable = bond_stringvar[bond_count], font=font_setting_2, justify = "right"))
        # If the variable "entry_index" is 3, set the "Entry" object of the list "bond_entry_list" to disable
        if entry_index == 3:
            bond_entry_list[-1].configure(state = DISABLED)
        # Set the variable "entry_x" to the left margin of the "Entry" object
        entry_x = window_width - bond_entry_list[entry_index].winfo_reqwidth() - left_margin
        # Set the variable "entry_y" to the top margin of the "Entry" object with adjustment
        entry_y = label_2_margin_top +  window_padding_top * element_entry_top_count
        # Place the "Button" object in the window
        bond_entry_list[entry_index].place(x = entry_x, y = entry_y)
        # The variable "bond_count" is added by 1
        bond_count += 1
    # The variable "element_entry_top_count" is added by 1
    element_entry_top_count += 1
    # The variable "entry_index" is added by 1
    entry_index += 1
    # Create the list "bond_entry_list" to the text of the "Button" object
    if entry_index == 4:
        # Set the variable "count" to 1
        count = 1
        # Create the list "bond_button_list" to the text of the "Button" object
        bond_button_list = ["Clear", "Calculate"]
        # Use for-loop to store the "Button" object to the list "bond_button_list"
        for button_index, button in enumerate(bond_button_list):
            # If the variable "count" is 1, store the [CLEAR] "Button" object in the list "bond_button_list"
            if count == 1:
                bond_entry_list.append(Button(window, text = button,  width=9, font=font_setting_2, command = lambda: clear_bond()) )
            # If the variable "count" is not 1, store the [CALCULATE] "Button" object in the list "bond_button_list"
            else:                
                bond_entry_list.append(Button(window, text = button,  width=9, font=font_setting_2, command = lambda: compute_bond() ))
            # Set the variable "entry_x" to the left margin of the "Entry" object
            entry_x = window_width - left_margin - bond_entry_list[entry_index].winfo_reqwidth() * count
            # Set the variable "entry_y" to the top margin of the "Entry" object with adjustment
            entry_y = label_2_margin_top +  window_padding_top * element_entry_top_count
            # Place the "Button" object in the window
            bond_entry_list [entry_index].place(x = entry_x, y = entry_y)
            # The variable "entry_index" is added by 1
            entry_index += 1
            # The variable "count" is added by 1
            count += 1
# End: Entry/Button of the Bond  
########################################################################################################################


# Nain function
def main():
    # run the Tkinter event loop
    mainloop()

# Set to call main function
if __name__ == "__main__":
    main()