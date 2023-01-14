from tkinter import *
import requests
import json
from tkinter import messagebox
root = Tk()
root.title("News")
root.geometry("750x750")
hl = Label(root, text="BBC News Update", font=("Arial", 20, "bold"))
hl.place(relx=0.5, rely=0.1, anchor=CENTER)
i = 0.15
ii = 0.03
news1 = Label(root,text="[NOT RETRIEVED]", font=(\
    "Calibri", 15, "bold"), fg="red", wraplength=500, justify="left")
news1.place(relx=0.15, rely=.15, anchor=W)
desc1 = Label(root, text="[NOT RETRIEVED]",fg="black",wraplength=500,justify="left")
desc1.place(relx=0.15,rely=.19,anchor=W)

news2 = Label(root, text="[NOT RETRIEVED]", font=(
    "Calibri", 15, "bold"), fg="red", wraplength=500, justify="left")
news2.place(relx=0.15,rely=.25,anchor=W)
desc2 = Label(root, text="[NOT RETRIEVED]", fg="black",
              wraplength=500, justify="left")
desc2.place(relx=0.15, rely=.29, anchor=W)

news3= Label(root, text="[NOT RETRIEVED]", font=(
    "Calibri", 15, "bold"), fg="red", wraplength=500, justify="left")
news3.place(relx=0.15, rely=.35, anchor=W)
desc3 = Label(root, text="[NOT RETRIEVED]", fg="black",
              wraplength=500, justify="left")
desc3.place(relx=0.15, rely=.39, anchor=W)

news4 = Label(root, text="[NOT RETRIEVED]", font=(
    "Calibri", 15, "bold"), fg="red", wraplength=500, justify="left")
news4.place(relx=0.15, rely=.45, anchor=W)
desc4 = Label(root, text="[NOT RETRIEVED]", fg="black",
              wraplength=500, justify="left")
desc4.place(relx=0.15, rely=.49, anchor=W)

news5 = Label(root, text="[NOT RETRIEVED]", font=(
    "Calibri", 15, "bold"), fg="red", wraplength=500, justify="left")
news5.place(relx=0.15, rely=.55, anchor=W)
desc5 = Label(root, text="[NOT RETRIEVED]", fg="black",
              wraplength=500, justify="left")
desc5.place(relx=0.15, rely=.59, anchor=W)

news6 = Label(root, text="[NOT RETRIEVED]", font=(
    "Calibri", 15, "bold"), fg="red", wraplength=500, justify="left")
news6.place(relx=0.15, rely=.65, anchor=W)
desc6 = Label(root, text="[NOT RETRIEVED]", fg="black",
              wraplength=500, justify="left")
desc6.place(relx=0.15, rely=.69, anchor=W)
def SendRequest():
    rqnv = 0
    try:
        req = requests.get(
            "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=[YOURAPIKEY]"
        )
    except requests.exceptions.ConnectionError:
        messagebox.showerror("Error","Failed To Make a Connection. \nPlease Check Your Internet Connection And Try Again")
        print("Failed To Make a Connection")
        rqnv = 1
    if rqnv==1:
        print("cannot access local variable 'req' where it is not associated with a value")
    else:
        print(req.status_code)
        if req.status_code == 200:
            con = json.loads(req.content)
            title1 = con["articles"][0]["title"]
            title2 = con["articles"][1]["title"]
            title3 = con["articles"][2]["title"]
            title4 = con["articles"][3]["title"]
            title5 = con["articles"][4]["title"]
            title6 = con["articles"][5]["title"]
            description1 = con["articles"][0]["description"]
            description2 = con["articles"][1]["description"]
            description3 = con["articles"][2]["description"]
            description4 = con["articles"][3]["description"]
            description5 = con["articles"][4]["description"]
            description6 = con["articles"][5]["description"]
            news1["text"] = title1
            news2["text"] = title2
            news3["text"] = title3
            news4["text"] = title4
            news5["text"] = title5
            news6["text"] = title6
            desc1["text"] = description1
            desc2["text"] = description2
            desc3["text"] = description3
            desc4["text"] = description4
            desc5["text"] = description5
            desc6["text"] = description6
        else:
            print("Unexpected Error :(")
SendRequest()
root.mainloop()
