import os
import shutil

source_folder="Day_one/mix_documents"
destination_folder="Day_one/Photos"

if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)

for file in os.listdir(source_folder):
    if file.endswith(".jpg"):
        
        source_path=os.path.join(source_folder,file)
        destination_path=os.path.join(destination_folder,file)
        shutil.move(source_path,destination_path)
        
        print(file,"moved successfully")
print("all jpg files moved successfully")        