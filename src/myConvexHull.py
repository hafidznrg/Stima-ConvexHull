# Fungsi untuk menghitung jarak titik p3 ke garis p1-p2
def location(p1, p2, p3):
	return p1[0]*p2[1] + p3[0]*p1[1] + p2[0]*p3[1] - p3[0]*p2[1] - p1[0]*p3[1] - p2[0]*p1[1]

# Fungsi untuk menggabungkan 2 buah array dan menghapus duplikat (elemen terakhir arr 1 = elemen pertama arr2)
def merge(arr1, arr2):
	return arr1 + arr2[1:]

# Fungsi bantuan untuk memproses algoritma convex hull
def convexHull(data, times):
	if (len(data) == 2):
		return data
	else:
		# cari titik terjauh dari garis p1-p2
		max = 0
		idxmax = 0
		for i in range(1,len(data)-1):
			n = location(data[0], data[len(data)-1], data[i])*times
			if (n > max):
				max = n
				idxmax = i

		# Filterisasi titik di sebelah kiri yang berada di luar garis
		kiri = [data[0]]
		for i in range(1,idxmax):
			n = location(data[0], data[idxmax], data[i])*times
			if (n > 0):
				kiri.append(data[i])
		kiri += [data[idxmax]]

		# Filterisasi titik di sebelah kanan yang berada di luar garis
		kanan = [data[idxmax]]
		for i in range(idxmax+1,len(data)-1):
			n = location(data[idxmax], data[len(data)-1], data[i])*times
			if (n > 0):
				kanan.append(data[i])
		
		kanan += [data[len(data)-1]]
		return merge(convexHull(kiri, times), convexHull(kanan, times))

# Fungsi awal dalam algoritma convex hull
def myConvexHull(data):
	# urutkan data dalam keadaan menaik
	quickSort(data, 0, len(data)-1)
	if (len(data) == 2):
		# base case
		return data
	else:
		atas = [data[0]]
		bawah = [data[0]]
		# pisahkan titik titik di atas dan bawah garis ujung kiri dan kanan
		for i in range(1,len(data)-1):
			n = location(data[0], data[len(data)-1], data[i])
			if (n > 0):
				atas.append(data[i])
			elif (n < 0):
				bawah.append(data[i])
		
		atas += [data[len(data)-1]]
		bawah += [data[len(data)-1]]
		# mengembalikan gabungan dari convex hull atas dan bawah
		return merge(convexHull(atas, 1), convexHull(bawah, -1)[::-1])
	
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