import codecs
def encrypt(orig_pass):
	try:
		orig_pass = str(orig_pass)
		sstring = ""
		for i in orig_pass:
		    temp = str(ord(i))
		    sstring += temp
		    if orig_pass.index(i) != len(orig_pass)-1:
			sstring+=','
		nums = sstring.split(',')
		nums = map(int,nums)
		some_math = lambda x: ((((x+1)*2)*12)-2**4)
		nums = map(some_math,nums)
		conv = codecs.getencoder('hex')
		converter = lambda x: conv(str(x))[0]
		encrypted_pass = map(converter,nums)
		return encrypted_pass
		#Old Feature, don't forget to remove log files
		#log = open(".log.txt","w") 
		#log.write(str(encrypted_pass)) 
		#log.close()
	except:
		print("Invalid input")
