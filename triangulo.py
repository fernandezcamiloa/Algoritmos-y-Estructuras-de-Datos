ladoa = "5"
ladob = "5"
ladoc = "5"

if(ladoa==ladob) and (ladoa == ladoc): 
	print ("Es equilatero")
elif(ladoa != ladob) and (ladoa != ladoc) and (ladob != ladoc):
	print ("Es escaleno")
elif (ladoa==ladob) and (ladoa!=ladoc) and (ladob!=ladoc) or (ladoa!=ladob) and (ladoa==ladoc) and (ladob!=ladoc) or (ladoa!=ladob) and (ladoa!=ladoc) and (ladob==ladoc):
	print ("Es isoceles")
                 






