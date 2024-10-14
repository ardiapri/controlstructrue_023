# fungsi untuk mengevaluasi kinerja siswa
def evaluate_performance(percentage):
    if percentage >= 90:
        print ("Excellent performance")
    elif percentage >= 80:
        print ("Very Good performance")
    elif percentage >= 70:
        print ("Good performance")
    elif percentage >= 60:
        print ("Average performance")
    else:
        print ("Below average performance")

# panggil fungsi untuk evaluasi dan tampilkan hasil
percentage = float(input("Enter the percentage: "))
print(evaluate_performance(percentage))