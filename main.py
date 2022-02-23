import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn import datasets 

# Fungsi untuk menentukan apakah p3 berada di atas atau di bawah garis p1-p2
def location(p1, p2, p3):
	return p1[0]*p2[1] + p3[0]*p1[1] + p2[0]*p3[1] - p3[0]*p2[1] - p1[0]*p3[1] - p2[0]*p1[1]

# Fungsi untuk menggabungkan 2 buah array dan menghapus duplikat (elemen terakhir arr 1 = elemen pertama arr2)
def merge(arr1, arr2):
	return arr1 + arr2[1:]

def convexHullAtas(data):
	if (len(data) == 2):
		return data
	else:
		# cari titik terjauh dari garis p1-p2
		max = 0
		idxmax = 0
		for i in range(1,len(data)-1):
			n = location(data[0], data[len(data)-1], data[i])
			if (n > max):
				max = n
				idxmax = i

		# sebelah kiri dari idxmax
		kiri = [data[0]]
		for i in range(1,idxmax):
			n = location(data[0], data[idxmax], data[i])
			if (n > 0):
				kiri.append(data[i])
		
		kiri.append(data[idxmax])

		# sebelah kanan dari idxmax
		kanan = [data[idxmax]]
		for i in range(idxmax+1,len(data)-1):
			n = location(data[idxmax], data[len(data)-1], data[i])
			if (n > 0):
				kanan.append(data[i])
		
		kanan.append(data[len(data)-1])
		return merge(convexHullAtas(kiri), convexHullAtas(kanan))

def convexHullBawah(data):
	if (len(data) == 2):
		return data
	else:
		# cari titik terjauh dari garis p1-p2
		min = 0
		idxmin = 0
		for i in range(1,len(data)-1):
			n = location(data[0], data[len(data)-1], data[i])
			if (n < min):
				min = n
				idxmin = i

		# sebelah kiri dari idxmin
		kiri = [data[0]]
		for i in range(1,idxmin):
			n = location(data[0], data[idxmin], data[i])
			if (n < 0):
				kiri.append(data[i])
		
		kiri.append(data[idxmin])

		# sebelah kanan dari idxmin
		kanan = [data[idxmin]]
		for i in range(idxmin+1,len(data)-1):
			n = location(data[idxmin], data[len(data)-1], data[i])
			if (n < 0):
				kanan.append(data[i])
		
		kanan.append(data[len(data)-1])
		return merge(convexHullBawah(kiri), convexHullBawah(kanan))

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
		return merge(convexHullAtas(atas), convexHullBawah(bawah)[::-1])
	
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

data = datasets.load_iris() 
#create a DataFrame 
df = pd.DataFrame(data.data, columns=data.feature_names) 
df['Target'] = pd.DataFrame(data.target) 
print(df.shape)
print(df)
df.head()

#visualisasi hasil ConvexHull
plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title('Petal Width vs Petal Length')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
for i in range(len(data.target_names)):
	bucket = df[df['Target'] == i]
	bucket = bucket.iloc[:,[0,1]].values
	hull = myConvexHull(bucket) #bagian ini diganti dengan hasil implementasi ConvexHull Divide & Conquer
	print("hasilnya : " + str(hull))
	plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
	hull = np.transpose(hull)
	plt.plot(hull[0], hull[1], color=colors[i])
plt.legend()
plt.waitforbuttonpress()