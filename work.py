#Task 1
amount = float(input(" amount is : "))
membership = input("Are you have a membership card? (yes/no): ").strip().lower() == "yes"
if amount >= 5000 and membership:
    discount =0.20
elif amount >= 3000:
    discount = 0.10
else:
    discount = 'no discount'
final_amount = amount - (amount * discount)
print("Total amount to pay: ₹", round(final_amount))


#Task 2
mark=75
attendance=80
if (mark >=70 and attendance>=75) or mark >=90:
   print('Eligible')
else:
   print('Not Eligible')
   
#Task3...
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
z = x
#if x is y:
print(x is y)
#if x is z:
print(x is z)
#if z exists in y
print(3 in y)