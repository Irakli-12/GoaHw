# 1) გაიხსენეთ და ახსენით წესები რომლებიც მუშაობს ყველა ლოგიკურ ოპერატორზე რაც დღეს ვისწავლეთ (and, or, not)
# თუ პრინტში 1 false მაინც არის , რამდენი true ც არ უნდა იყოს პასუხი იქნება false (and ოპერატორი)
# თუ პრინტში 0 false არის და სულ ყველა True არის პასუხი იქნება True (and ოპერატორი)
# თუ პრინტში ერთი True არის და დანარჩენი ყველა False არის, რამდენი False არ უნდა იყოს მაინც პასუხი იქნება True (or ოპერატორი)
# თუ პრინტში 0 True არის და ყველა False არის, პასუხი იქნება False (or ოპერატორი)
# 2) შექმენით and ოპერატორის მეშვეობით 5 სხვადასხვა 
print(False and False and False and True)
print(True and True and True)
print(True and False and True and True)
print(True and True and True)
print(False and False and False)

# 3) შექმენით or ოპერატორის მეშვეობით 5 სხვადასხვა მაგალითი
print(True and False)
print(False and False)
print(True and True)
print(False and True and True)
print(False and False and True)

# 4) შეურიეთ შედარების და ლოგიკური ოპერატორები და გააკეთეთ 5 მაგალითი

print(8 > 4 == False)
print(6 < 4 == False)
print(8 != 6 == True)
print(9 == 9 == True)
print(10 >= 11 == True)