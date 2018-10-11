print "Enter the name of the directory"
d=raw_input()
n=[]
i=0
print "MENU\n1.Create File\n2.Delete File\n3.Display Files\n4.Search File\n5.Exit"
a=input()
while 1:
	if a==1:
		print "\nEnter the name of the file"
		s=raw_input()
		n.append(s)
		i+=1
	elif a==2:
		print "\nEnter the name of the file you want to delete"
		s=raw_input()
		try:
			n.remove(s)
			print "The file has been deleted"
		except ValueError:
			print "No such file exists"
		i-=1
	elif a==3:
		if(i!=0):
			print "\nThe files:"
			for j in range(0,i):
				print n[j]
		else:
			print "\nThe Directory is empty"
	elif a==4:
		print "\nEnter the name of the file you want to search for"
		s=raw_input()
		if n.count(s)==0:
			print "This file doesnt exist"
		else:
			print "The file has been found"
	else:
		print "\nExiting"
		break
	print "\n\nMENU\n1.Create File\n2.Delete File\n3.Display Files\n4.Search File\n5.Exit"
	a=input() 
