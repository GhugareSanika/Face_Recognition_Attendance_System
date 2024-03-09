from tkinter import *  #Tkinter is a Python library,used to construct basic graphical user interface (GUI) applications.
from tkinter import ttk
from PIL import Image, ImageTk #PTL is the Python Template Language,allow to embed Python code within HTML for dynamic content generation in web applications.

class Face_recognise:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        #First Image
        img = Image.open(r"C:\Users\sanik\OneDrive\Desktop\face_recognition system\college_images\College_Full_view-1.jpg")
        img = img.resize((500,200))
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=200)

        #Second Image
        img1 = Image.open(r"C:\Users\sanik\OneDrive\Desktop\face_recognition system\college_images\RealNetworks.jpg")
        img1 = img1.resize((500, 200))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=200)

        #Third Image
        img2 = Image.open(r"C:\Users\sanik\OneDrive\Desktop\face_recognition system\college_images\download.jpeg")
        img2 = img2.resize((510, 200))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=530, height=200)

        #Bg Image
        img3 = Image.open(r"C:\Users\sanik\OneDrive\Desktop\face_recognition system\college_images\face-recognition-1024x630.jpg")
        img3 = img3.resize((1530,580))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=580)
        
        title = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 30, "bold"), bg="white", fg="black")
        title.place(x=0, y=0, width=1530 , height=45)

        #Student Button
        img4 = Image.open(r"C:\Users\sanik\OneDrive\Desktop\face_recognition system\college_images\istockphoto-1358014313-612x612 (1).jpg")
        img4 = img4.resize((300, 220))
        self.photoimg4 = ImageTk.PhotoImage(img4)
        btn1 = Button(bg_img, image=self.photoimg4, cursor="hand2")
        btn1.place(x=350, y=100, width=250, height=180)
        b1 = Button(bg_img, text="Student Details", cursor="hand2", font=("times new roman", 18, "bold"), bg="white", fg="black")
        b1.place(x=350, y=280, width=250, height=40)

        #Detect  face button
        img5 = Image.open(r"C:\Users\sanik\OneDrive\Desktop\face_recognition system\college_images\shutterstock_680761540-1.jpg")
        img5 = img5.resize((300, 220))
        self.photoimg5 = ImageTk.PhotoImage(img5)
        btn1 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        btn1.place(x=900, y=100, width=250, height=180)
        b1 = Button(bg_img, text="Face Detector", cursor="hand2", font=("times new roman", 18, "bold"), bg="white", fg="black")
        b1.place(x=900, y=280, width=250, height=40)

        #Attendance face button
        img6 = Image.open(r"C:\Users\sanik\OneDrive\Desktop\face_recognition system\college_images\MicrosoftTeams-image-246-1024x599.jpg")
        img6 = img6.resize((300, 220))
        self.photoimg6 = ImageTk.PhotoImage(img6)
        btn1 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        btn1.place(x=350, y=350, width=250, height=180)
        b1 = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman", 18, "bold"), bg="white", fg="black")
        b1.place(x=350, y=530, width=250, height=40)

        #Exit
        img7 = Image.open(r"C:\Users\sanik\OneDrive\Desktop\face_recognition system\college_images\depositphotos_59592641-stock-photo-exit-circular-icon-on-white.jpg")
        img7 = img7.resize((300, 220))
        self.photoimg7 = ImageTk.PhotoImage(img7)
        btn1 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        btn1.place(x=900, y=350, width=250, height=180)
        b1 = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 18, "bold"), bg="white", fg="black")
        b1.place(x=900, y=530, width=250, height=40)


if __name__ == "__main__":
    root = Tk()
    obj = Face_recognise(root)
    root.mainloop()
