d1={'teacher':'shikshak','book':'pustak','friend':'mitr'}
d2={'shikshak':'adhyapak','pustak':'kitab','mitr':'dost'}
for i in d1:
    for j in d2:
        if d1[i]==j:
            print(i,"in hindi means",j,"and in urdu means",d2[j])
