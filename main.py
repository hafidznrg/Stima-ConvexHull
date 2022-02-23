import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn import datasets 
import matplotlib.pyplot as plt


# Fungsi untuk menentukan apakah p3 berada di atas atau di bawah garis p1-p2
def location(p1, p2, p3):
	return p1[0]*p2[1] + p3[0]*p1[1] + p2[0]*p3[1] - p3[0]*p2[1] - p1[0]*p3[1] - p2[0]*p1[1]

def convexHullAtas(data):
	return []

def convexHullBawah(data):
	return []

def merge(arr1, arr2):
	return []

def myConvexHull(data):
	quickSort(data, 0, len(data)-1)
	if (len(data) == 2):
		return data
	else:
		atas = [data[0]]
		bawah = [data[0]]
		for i in range(1,len(data)-1):
			n = location(data[0], data[len(data)-1], data[i])
			if (n > 0):
				atas.append(data[i])
			elif (n < 0):
				bawah.append(data[i])
		
		atas.append(data[len(data)-1])
		bawah.append(data[len(data)-1])
		res  = merge(convexHullAtas(atas), convexHullBawah(bawah))
		return res

	
# Fungsi untuk mempartisi array
def partition(arr, low, high):
	i = (low-1)		 		# index elemen pertama
	pivot = arr[high]		# pivot

	for j in range(low, high):
		# penukaran elemen sesuai dengan urutan menaik
		if (arr[j][0] < pivot[0]):
			i += 1
			arr[i][0], arr[j][0] = arr[j][0], arr[i][0]
			arr[i][1], arr[j][1] = arr[j][1], arr[i][1]
		elif (arr[j][0] == pivot[0] and arr[j][1] < pivot[1]):
				i += 1
				arr[i][0], arr[j][0] = arr[j][0], arr[i][0]
				arr[i][1], arr[j][1] = arr[j][1], arr[i][1]

	arr[i+1][0], arr[high][0] = arr[high][0], arr[i+1][0]
	arr[i+1][1], arr[high][1] = arr[high][1], arr[i+1][1]
	return (i+1)

# Fungsi untuk mengurutkan array dengan algoritma QuickSort
def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:
		pi = partition(arr, low, high)

		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)

data = [[10,5],[7,4],[8,3],[9,2],[6,8],[1,1],[5,0],[6,6],[2,7],[3,8]]
data = np.array(data)
result = myConvexHull(data)