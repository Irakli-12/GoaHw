# 1) შექმენით list comprehension რომელიც შექმნის list'ს რიცხვებით 1'დან 100'მდე
list1 = [x for x in range(1, 100)]
print(list1)
# 2) შექმენით list comprehension რომელიც შექმნის list'ს რიცხვებით 1'დან 100'მდე, 2-2'ის გამოტოვებით. (ანუ: [1, 3, 5...])
# list2 = [x + 2 for x in range(1, 100)]
# print(list2)
list2 = [i for i in range(1, 101, 2)]
print(list2)
# 3) შექმენით რაიმე list'ი სახელებით და შემდეგ შექმენით list comprehension რომელიც შექმნის სახელების ახალ list'ს სადაც არ იქნება ასო "a" და ყველა string'ს თავში ექნება "#".
