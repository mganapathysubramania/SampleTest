
# python compare.py
# import the necessary packages
from skimage import metrics
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import sys
import csv

#list to store estimate percentages
Results = []

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar" the two images are
	return err

def compare_images(imageA, imageB):

	# compute the mean squared error and structural similarity index for the images
	
	#reshape image
	h,w = imageA.shape
	#print(imageA.shape)
	imageB=cv2.resize(imageB,(w,h))
	#print(imageB.shape)
	
	#Calculate MSE
	m = mse(imageA, imageB)
	
	#Calculate SSM
	s = metrics.structural_similarity(imageA, imageB)
	print("SSM is",s," & MSE is",m)
	
	#calculate estimate from MSE and SSM 
	if m>2000:
		if ((s*100)-(m/100.0))>0:
			E=(s*100)-(m/100.0)
		else:
			E=0
	else:
		E=s*100
		
	#print result
	print("Estimate is " ,E,"%")
	print("---------------------------------------------")
	
	#append to list
	Results.append(E)
	
def main():

	if len(sys.argv) < 2:
		errorInput()
		sys.exit()
			
	arg1 = sys.argv[1] # Picture 1
	print(os.path.isfile(arg1))

	file2path=os.getcwd()+"/images" #Path to images directory
	
	
	for arg2 in os.listdir(file2path):
		print(arg2)
		print(arg1)
		arg2_list = []
		arg2_list.append(arg2)
		
		#get image path 
		if arg2.split(".")[1] in accepted:
			path1=os.getcwd()+"/"+arg1
			path2=os.getcwd()+"/images/"+arg2
			
			#Check Image exists
			if (path.exists(path1) and path.exists(path2) == False):
				if (path.exists(path1) == False):
					print("Image " + arg1 +" not found")
				if (path.exists(path2) == False):
					print("Image " + arg2 +" not found")
				sys.exit()
				
				#Read input images
				orig = cv2.imread(path1)
				comp = cv2.imread(path2)
				
				#Black and white from color
				orig1 = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
				comp1 = cv2.cvtColor(comp, cv2.COLOR_BGR2GRAY)
				
				#Compare the images
				print("Comparison between ",str(arg1), " and ", str(arg2)
				compare_images(orig1, comp1)
				
	#print results
	print(arg2_list)
	print(Results)
	print ("Completed!")
	
	#Write to results.csv
	with open('results.csv', 'wb', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(arg2_list)
    writer.writerow(Results)
	
	#exit
	sys.exit()

main()
