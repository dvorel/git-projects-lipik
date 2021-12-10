import numpy as np


#prvi
arr = np.zeros((3,4,2), dtype=np.float64)

print("Broj osi: ", arr.ndim)
print("Dimenzije polja: ", arr.ndim)
print("Ukupni broj elemenata: ", arr.size)
print("Tip elemenata: ", arr.dtype)

#drugi
arr.dtype = np.int16
print("Novi tip elemenata: ", arr.dtype)

#treci
arr_9 = np.full((2,7,3), 9, dtype=np.int32)
print(arr_9)

#cetvrti
arr_3_15 = np.arange(3, 15, 3)
print(arr_3_15)

#peti
arr_2_19 = np.linspace(2, 19, 12)
print(arr_2_19)

#sesti
arr_jed = np.eye(4,4)
arr_44 = np.full((4,4), 9)
print("Zbroj: \n", arr_jed+arr_44)
print("Razlika: \n", arr_jed-arr_44)
print("Umnozak: \n", arr_jed*arr_44)
print("Kolicnik: \n", arr_jed/arr_44)

#sedmi
arr_10 = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr_10)
arr_10[2:7:2] = 99
print(arr_10)

#osmi
arr_5_6 = np.ones((5,6))
a, b, c = arr_5_6[:, ::2].T
print("Svaki drugi", a, b, c)

#deveti
arr = [np.full((16), j) for j in range(16)]
arr_16_16 = np.array(arr)
print(arr_16_16)

arr4_8_8 = arr_16_16.reshape((4,8,8))
print(arr4_8_8)

#deseti
arr_10 = np.full((3,576,720), 2)
arr_10_1 = (arr_10.swapaxes(0, 2)).swapaxes(0, 1)
print(arr_10_1.shape)

#jedanaesti
arr_11 = np.array([[0,1,5],[8,5,6]])
if arr_11.mean() > 10:
    print("SUM: ", arr_11.sum())
else:
    print("MAX: ", arr_11.max())
