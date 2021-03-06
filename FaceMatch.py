import face_recognition as fr
import os
import cv2
import face_recognition
import shutil
import glob
from tkinter import filedialog
from tkinter import *
import numpy as np
import PIL
from PIL import Image,ImageTk
import pytesseract
import tkinter as tk
from tkinter import ttk
import time
import sys
import threading

def imageSort_Thread():
	thead1=threading.Thread(target=imgsort)
	thead1.start()
def imgsort():
	global xx, name
	
	my_progress = ttk.Progressbar(frame2,orient=HORIZONTAL, length=225, mode= 'determinate',value= 50)
	my_progress.place(x = 130, y = 370)
	#text= Label(frame2,text="",bg="#E6E6E6",bd = 0,font="Times 8")
	#text.place(x = 210, y = 373)
	
	
	#my_progress['value']=100
	#text.config(text="Processing...",bg="#08AF24")
	try:
		if(xx.get()==""):
			print("error")
		elif(xx.get()=="Name"):
			print("error")
		else:
			sys.exit(0)
	except:
		s=xx.get()
		name=s
		root = Tk()
		root.withdraw()
		folder_selected = filedialog.askdirectory()
		
		
		
		def face_code():
			
			def get_encoded_faces():
				global f
							
				"""
				looks through the faces folder and encodes all
				the faces

				:return: dict of (name, image encoded)
				"""
				
				encoded = {}

				for dirpath, dnames, fnames in os.walk("./faces/" + name):
					for f in fnames:
						if f.endswith(".jpg") or f.endswith(".png"):
							face = fr.load_image_file("faces/"+ name +"/" + f)
							encoding = fr.face_encodings(face)[0]
							encoded[f.split(".")[0]] = encoding
										
							try:
								#make folder in copy dir
								os.mkdir("./copy/"+ f +"/")
								my_progress.start()					
							except OSError as e:
								pass
				return encoded
				
				
				


			def unknown_image_encoded(img):
				"""
				encode a face given the file name
				"""
				face = fr.load_image_file("faces/"+ name +"/" + img)
				encoding = fr.face_encodings(face)[0]

				return encoding


			def classify_face(b=[]):
				
				
				for x in range(len(b)):
					img = cv2.imread(b[x], 1)

				
					faces = get_encoded_faces()
					faces_encoded = list(faces.values())
					known_face_names = list(faces.keys())
					 
					
					#img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
					#img = img[:,:,::-1]
				 
					face_locations = face_recognition.face_locations(img)
					unknown_face_encodings = face_recognition.face_encodings(img, face_locations)

					face_names = []
					for face_encoding in unknown_face_encodings:
						# See if the face is a match for the known face(s)
						matches = face_recognition.compare_faces(faces_encoded, face_encoding)
						name = "Unknown"

						# use the known face with the smallest distance to the new face
						face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
						best_match_index = np.argmin(face_distances)
						if matches[best_match_index]:
							name = known_face_names[best_match_index]
							print("match " + b[x])
							shutil.copy(b[x],"./copy/"+ f +"/")
						#else:
							#print("not match " + b[x])

						face_names.append(name)

						for (top, right, bottom, left), name in zip(face_locations, face_names):
							# Draw a box around the face
							cv2.rectangle(img, (left-20, top-20), (right+20, bottom+20), (255, 0, 0), 2)

							# Draw a label with a name below the face
							cv2.rectangle(img, (left-20, bottom -15), (right+20, bottom+20), (255, 0, 0), cv2.FILLED)
							font = cv2.FONT_HERSHEY_DUPLEX
							cv2.putText(img,'Press Q to exit',(50, 50),font, 1,(0, 255, 255),2, cv2.LINE_4)
							cv2.putText(img, name, (left -20, bottom + 15), font, 1.0, (255, 255, 255), 2)


					# Display the resulting image
				while True:
				#	img_scale = cv2.resize(img, None, fx=0.25, fy=0.25)
					#cv2.imshow('Image Sorted, Press Q to Exit', img_scale)
				# 	if cv2.waitKey(1) & 0xFF == ord('q'):
					#my_progress.stop()
					#text.destroy()
					#my_progress['value']=0
					my_progress.destroy()
					return face_names 
					
					exit()

			#Reads the files with extintion .jpg in working dir
			#a = glob.glob('*.jpg')

			a = glob.glob(folder_selected + '/'+'*.jpg')
			#print(a - folder_selected)

			print(classify_face(a))
			print(f)

		face_code()


p1= threading.Thread(target=imgsort)
p1.start()
p1.join()
########################################################################################################################
def show_frame(frame):
	frame.tkraise()
	
window = tk.Tk()
window.title('Face Match')
window.bind('<Escape>', lambda e: window.quit())
window.geometry('450x450')
window.resizable(width=False,height=False)
window.iconbitmap('./export/icnn.ico')
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1) 

frame1 = tk.Frame(window)
frame2 = tk.Frame(window) 
frame3 = tk.Frame(window)
frame4 = tk.Frame(window)
for frame in (frame1, frame2,frame3,frame4): 
	frame.grid(row = 0, column = 0,sticky='nwes')
########################################################################################################################
load = Image.open('./export/bg1.png')
render = ImageTk.PhotoImage(load)
img = Label(frame1,image = render)
img.place(x = 0,y = 0)

add_btn = PhotoImage(file = './export/Badd.png')
img_label = Label(image = add_btn)

add_btn2 = PhotoImage(file = './export/Bsort.png')
img_label = Label(image = add_btn2)

my_btn = Button(frame1, image = add_btn, border = 0,command=lambda:show_frame(frame3))
my_btn.place(x = 45, y = 300)

my_btn2 = Button(frame1, image = add_btn2, border = 0,command=lambda:show_frame(frame2))
my_btn2.place(x = 250, y = 300)
########################################################################################################################
frame4_title=tk.Label(frame4,text=' ')
frame4_title.pack()

load4 = Image.open('./export/bg4.png')
render4 = ImageTk.PhotoImage(load4)
img4 = Label(frame4,image = render4)
img4.place(x = 0,y = 0)

back4 = PhotoImage(file = './export/back.png')
img_label = Label(image = back4)
back_btn4=tk.Button(frame4, image = back4, border = 0,command=lambda:show_frame(frame3))
back_btn4.place(x = 15, y = 10)

#
cameraLable=LabelFrame(frame4,bg="red")
cameraLable.place(x = 50, y = 58)
cameraView=Label(cameraLable,bg="white",height="21",width="49")
cameraView.pack()
#

add_btnn4 = PhotoImage(file = './export/Bcap.png')
img_label = Label(image = add_btnn4)
frame4_btn=tk.Button(frame4, image = add_btnn4, border = 0,command=lambda:show_frame(frame1))
frame4_btn.place(x = 150, y = 390)

########################################################################################################################
########################################################################################################################
                  #S O R T - I M A G E
########################################################################################################################
frame2_title=tk.Label(frame2,text=' ')
frame2_title.pack()

load1 = Image.open('./export/bg2.png')
render1 = ImageTk.PhotoImage(load1)
img1 = Label(frame2,image = render1)
img1.place(x = 0,y = 0)

back2 = PhotoImage(file = './export/back.png')
img_labell = Label(image = back2)
back_btn=tk.Button(frame2, image = back2, border = 0,command=lambda:show_frame(frame1))
back_btn.place(x = 15, y = 10)

xx=StringVar()
entry = tk.Entry(frame2,width=20,font=("Segoe UI",15), bd=0, textvariable=xx)
entry.insert(0, 'Name')
entry.place(x = 132, y = 250)


add_btnn2 = PhotoImage(file = './export/Bsort.png')
img_label = Label(image = add_btnn2)

frame2_btn=tk.Button(frame2, image = add_btnn2, border = 0,command=imageSort_Thread)
frame2_btn.place(x = 150, y = 300)



########################################################################################################################
                 #A D D - F A C E
########################################################################################################################

frame3_title=tk.Label(frame3,text=' ')
frame3_title.pack()

load2 = Image.open('./export/bg2.png')
render2 = ImageTk.PhotoImage(load2)
img2 = Label(frame3,image = render2)
img2.place(x = 0,y = 0)

back = PhotoImage(file = './export/back.png')
img_labell = Label(image = back)
back_btn=tk.Button(frame3, image = back, border = 0,command=lambda:show_frame(frame1))
back_btn.place(x = 15, y = 10)

x=StringVar()
entry = Entry(frame3,width=20,font=("Segoe UI",15), bd=0, textvariable=x)
entry.insert(0, 'Name')
entry.place(x = 132, y = 250)


add_btnn3 = PhotoImage(file = './export/Badd.png')
img_label = Label(image = add_btnn3)
frame2_btn=tk.Button(frame3, image = add_btnn3, border = 0,command=lambda:show_frame(frame4))
frame2_btn.place(x = 150, y = 300)

########################################################################################################################
show_frame(frame1)
window.mainloop() 