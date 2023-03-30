#Empty List
AWS = []

#Services
AWS.append('EC2')
AWS.append('RDS')
AWS.append('IAM')
AWS.append('EBS')

#Printing List/Length
length = len (AWS)
print ("This is a list of AWS services", AWS)
print ("The length of the list is",length)

#Remove 2 Services
AWS.remove('RDS')
AWS.remove('IAM')

#Printing List/Length
length = len (AWS)
print ("This is the new list of AWS services",AWS)
print ("The length of the new list is",length)