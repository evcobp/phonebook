import contacts
from os import system

main_message = """WELCOME TO PHONEBOOK
----------------------------------
Please choose:
1 - to add a new contact
2 - to find a contact
----------------------------------
"""

def prompt_add_contact():
	name = input("Please enter the contact's name: ")
	number = input("Please enter the contact's phone number: ")
	print(f"Adding {name} with {number}")
	contacts.add_contact(name, number)

def prompt_get_contact():
	name = input("Please enter the name to the find: ")
	number = contacts.get_contact(name)
	if number:
		print(f"{name}'s number is {number}")
	else:
		matches = contacts.search_contacts(name) 
		if matches: 
			for k in matches: 
				print(f"{k}'s number is {matches[k]}")
		else: 
			print(f"It looks like {name} does not exist")

def main():
	print(main_message)
	choice = input("Please make your choice: ").strip()
	if choice == "1":
		prompt_add_contact()
	elif choice == "2":
		prompt_get_contact()
	else:
		print("Invalid input. Please try again.")

while True:
	system("clear")
	main()
	input("Press enter to continue: ")
