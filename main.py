from rb import *

database = "./databases/car.features"

read_data(database)

feat = {"buying":'med',
        "maint":'low',
        "doors":'4',
        "persons":'4',
        "lug_boot":'med',
        "safety":'high'
        }
print('oi\n')
x = ['vgood', 'good', 'acc', 'unacc']
for i in x:
    print(i, prob_classes(i, feat), "\n")
#for i in ['vgood', 'good', 'acc', 'unacc']:
#    print("{0} : {1}\n".format(i, prob_classes(i, feat))
