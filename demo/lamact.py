positive_negative_zero=lambda x: "positive" if x > 0 else "negative" if x <0 else "zero"
num=int(input("Enter a number:"))
print(positive_negative_zero(num))
