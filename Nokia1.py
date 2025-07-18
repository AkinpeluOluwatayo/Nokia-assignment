print (""" WELCOME TO NOKIA
	
	MENU 
	
	1 phonebook
	2 Messages
	3 Chat
	4 Call registration
	5 Tones
	6 Settings
	7 Call divert
	8 Games
	9 Calculator
       10 Reminder
       11 Clock
       12 Profile
       13 Sim service """)
	
USERINPUT = int(input("Enter your Options:\n"))
match(USERINPUT):
	case  1 : 
		print ("""  
	   1 Search
  	   2 Service No
	   3 Add name
	   4 Erase
	   5 Edit
	   6 Assign tone
	   7 Send b'card
	   8 Options
	   9 Spread dials
	  10 Voice tags """)

		PHONEBOOK = int(input("press any key for options:\n"))
		match PHONEBOOK :
			case 1:
				print("Search")
			case 2:
				print("Service Nos")
			case 3:
				print("Add name")
			case 4: 
				print("Erase")
			case 5:
				print("Edit")
			case 6:
				print("Assign tone")
			case 7:
				print("Send b'card")
			case 8:
				print("options")
			case 9:
				print("Speed dails")
			case 10: 
				print("Voice tags")
			case _:
				print("Invalid")


	case 2:
  		
		print(""" 	
	1 Write message
	2 Inbox
	3 Output
	4 Picture message
	5 Templates
	6 Smileys
	7 Message settings
	8 Info service
 	9 Voice mailbox editor
       10 Service command editor """)
			
		MESSAGE = int(input("Enter any option:\n"))
		match MESSAGE :
				case 1:
					print("Write message")
				case 2:
					print("Inbox")
				case 3:
					print("Output")
				case 4:
					print("Picture message")
				case 5:
					print("Templates")
				case 6:
					print("Smileys")
				case 7:
					print(""""
					1 set
					2 common""")
				case 8:
					print("Info service")
				case 9:
					print("voice mailbox editor")
				case 10:
					print("Service command editor")
				case _:
					print("Invalid")

		
	
	case 3:
		print("""chat""")
	
	case 4:
		print("""
	1 Missed calls
	2 Received calls
	3 Dailed numbers
	4 Erase recent call list
	5 Show call duration
	6 Show call costs
	7 Call cost settings
	8 Prepaid credit""")
			
	
		call_register = int(input("Select an option:\n"))
		match call_register :
			case 1: 
				print("Missed calls")
			case 2:
				print("Recieved calls")
			case 3:
				print("Dailed numbers")
			case 4:
				print("Erase recent call list")
			case 5:
				print("Show call duration")
			case 6:
				print("Show call costs")
			case 7:
				print("call cost settings")
			case 8:
				print("prepaid credit")
			case _:
				print("invalid input")
	case 5:
		print("""
	1 Ringing tone
	2 Ringing volume
	3 Incoming call alert
	4 Composer
	5 Message alert tone
	6 Keypad tones
	7 Warning and games
	8 Vibrating alert
	9 Screensaver""")

		Tones = int(input("Pick one option:\n"))
		match Tones :
			case 1:
				print("Ringing tone")
			case 2:
				print("Ringing volume")
			case 3:
				print("Incoming call alert")
			case 4:
				print("Composer")
			case 5:
				print("Message alert tone")
			case 6:
				print("Keypad tones")
			case 7:
				print("Warning and game tone")
			case 8:
				print("Vibrating alert")
			case 9:
				print("Screensaver")
			case _:
				print("invalid key")
	case 6:
		print("""
		
	1 Call settings
	2 Phone settings
	3 Securing settings
	4 Restore factory settings""")
		
		Settings = int(input("select an option:\n"))
		match Settings :

			case 1: 
				print("""
				1 Automatic redial
				2 speed dailing
				3 call waiting options
				4 own number sending
				5 phone line in use
				6 Automatic answer""")
			case 2:
				print("""
				1 Language
				2 cell info display
				3 welcome note
				4 network selection
				5 lights
				6 confirm SIM service action""")
			case 3:
				print("""
				1 PIN code
				2 call barring service
				3 fixed dailing
				4 closed user group
				5 Phone security
				6 change access codes""")
			case 4:
				print("Restore factory")
				
	case 7:
		print("Call divert")
	case 8:
		print("Games")
	case 9:
		print("Calculate")
	case 10:
		print("Reminder")
	case 11:
		print("""
		1 Alarm clock
		2 clock settings
		3 date setting
		4 Stopwatch
		5 Countdown timer
		6 Auto update of date and time""")
	case 12:
		print("profiles")
	case 13:
		print("SIM services")