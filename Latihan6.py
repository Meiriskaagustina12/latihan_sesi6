print("===========Program Nilai===========")

nilai = int(input("masukan nilai anda : "))

if nilai >= 90 :
    grade = "A"
    predikat = "Dengan pujian"
elif nilai >= 80 :
    grade ="B"
    predikat = "Sangat Memuaskan"
elif nilai >= 70 :
    grade = "B"
    predikat = "Memuaskan"
elif nilai >= 60 :
    grade = "C"
    predikat = "Tidak Memuaskan"
else:
    grade = "E"
    predikat = "Tidak Lulus"

print("Grade: %s" %grade)
print("predikat: %s " %predikat)




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
