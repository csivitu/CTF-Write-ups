def CheckingPasswd():
	UserWrote = input("Enter your *PASSWD*: ")
	if UserWrote[13:19] == "n6_c4n":
		if UserWrote[0:4] == "cbrh":
			if UserWrote[19:25] == "_b3_qu":
				if UserWrote[4:8] == "{r3v":
					if UserWrote[25:31] == "173_c0":
						if UserWrote[8:13] == "3r533":
							if UserWrote[31:36] == "0l_bu":
								if UserWrote[40:46] == "7_w17h":
									if UserWrote[50:54] == "h0n}":
										if UserWrote[46:50] == "_py7":
											if UserWrote[36:40] == "7_n0":
												return True	
	else:
		return False

				

def main():
	auth = CheckingPasswd()
	if auth == True:
		print("so... The flag can be the password.")
		print("You deserve it!Gj")
	else:
		print("Incorrect password!")
		print("F.O.C.U.S S.T.U.P.I.D H.U.M.A.N")
		AnotherMain()



def AnotherMain():
	auth = AnotherCheckingPasswd()
	if auth == True:
		print("The flag can be the password.")
		print("You deserve it!Gj")
		exit()
	else:
		print("Incorrect password!")
		print("NEXT ONE WILL BE THE GOOD ONE")
		AnotherMain()


def AnotherCheckingPasswd():
	UserWrote = input("Enter your *PASSWD*: ")
	if UserWrote[13:19] == "n6_c4n":
		if UserWrote[0:4] == "cbrh":
			if UserWrote[19:25] == "_b3_qu":
				if UserWrote[4:8] == "{r3v":
					if UserWrote[25:31] == "173_c0":
						if UserWrote[8:13] == "3r533":
							if UserWrote[31:36] == "0l_bu":
								if UserWrote[40:46] == "7_w17h":
									if UserWrote[50:54] == "h0n}":
										if UserWrote[46:50] == "_py7":
											if UserWrote[36:40] == "7_n0":
												return True
	else:
		return False

auth = False
main()
