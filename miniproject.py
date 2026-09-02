import os
import re
from docx import Document
folder_path = r"C:\Users\victus\Desktop\python2\Resumes"
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-z0-9.-]+\.[a-zA-z]{2,}"
with open("emails3jul","w") as output_file:
    for filename in os.listdir(folder_path):
        if filename.startswith("~$"):
            continue
        if filename.endswith(".docx"):
            file_path = os.path.join(folder_path,filename)
            try:
                doc = Document(file_path)

                text = ""
                for para in doc.paragraphs:
                    text += para.text + "\n"

                emails = re.findall(pattern,text)

                output_file.write(f"\nFile: {filename}\n")

                if emails:
                    for email in emails:
                        print(filename, ":", email)
                        output_file.write(email + "\n")
                else:
                    output_file.write("No Email Found\n")
            
            except Exception as e:
                print(f"Error reading {filename} : {e}")

print("Completed")                



                    
                
