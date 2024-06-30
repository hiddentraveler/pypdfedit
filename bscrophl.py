from PIL import Image
import os 
import sys

pdfname=sys.argv[1]
firstpage=int(sys.argv[2])
lastpage= int(sys.argv[3])


#clearn final_img folder
try:
    os.system("cd final_img/ && rm *.png")
except:
    print("noting to clear in final_img folder")
#clean medium folder
try:
    os.system("cd medium && rm *")
except:
    print("noting to clear in final_img folder")
# convert pdf to image
cp_cmd = "cp init_pdf/%s.pdf medium/%s.pdf" % (pdfname,pdfname)
os.system(cp_cmd)
cmd = "cd medium/ && pdftoppm %s.pdf -f %d -l %d img -png" % (pdfname,firstpage,lastpage)
os.system(cmd)
print("finished covertingpdf to img")
for x in range(firstpage,lastpage,2):
    first_img_loc = "medium/img-%02d.png" % x
    first_img= Image.open(first_img_loc)
    second_img_loc = "medium/img-%02d.png" % (x+1)
    second_img= Image.open(second_img_loc)
    # third_half_img = Image.open("medium/img-03.png")


    first_img_copy = first_img.copy()
    # co-ord for first half
    # left = 73
    # top = 142
    # right = 618
    # bottom = 1640
 
    left = 630
    top = 142
    right = 1164
    bottom = 1640
 
  
    first_part = first_img.crop((left, top, right, bottom)) 
    second_part = second_img.crop((left, top, right, bottom)) 

    first_part_copy = first_part.copy()

    first_img_copy.paste(first_part_copy,(73,142))
    first_img_copy.paste(second_part,(630,142))

    final_img = "final_img/img-%02d.png" % x
    first_img_copy.save(final_img)
 

if ((lastpage-firstpage)+1)%2 == 0:
    print("finished noramally")
else:
    first_img_loc = "medium/img-%02d.png" % lastpage
    first_img= Image.open(first_img_loc)
    lastpg = "final_img/img-%02d.png" % lastpage
    first_img.save(lastpg)
    print("finished adding one last page")

# converting img to pdf
last_cmd = "cd final_img/ && convert *.png  ../pdfs/%s.pdf" % pdfname
os.system(last_cmd)
