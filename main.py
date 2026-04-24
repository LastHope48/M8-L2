import os
file_count=0
for root,dirs,files in os.walk(os.path.expanduser("~")):
    for file in files:
        print(os.path.join(root,file))
        file_count+=1
print(f"\n {file_count} dosya gezildi!!!!!!!!!!!!")
print("\n Kırkayaklar vadisi \n \a")