numberLargest = int(input("Enter Largest number : "))
numberSmallest = int(input("Entwr Smallest number : "))

while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print("HCF is : ",numberLargest)