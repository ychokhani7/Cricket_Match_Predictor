import tkinter as tk
from tkinter import *
from tkinter import ttk

teamNames = ['Mumbai Indians','Kolkata Knight Riders','Royal Challengers Bangalore','Deccan Chargers','Chennai Super Kings','Rajasthan Royals','Delhi Daredevils','Gujarat Lions','Kings XI Punjab','Sunrisers Hyderabad','Rising Pune Supergiants','Kochi Tuskers Kerala','Pune Warriors']
imgAddressPrefix = r"C:\Users\pratd\Documents\COURSES\3-1\CS F407 AI\Cricket_Match_Predictor\assets"
imageTeams = [r"\mi.png",r"\kkr.png",r"\rcb.png",r"\dc.png",r"\csk.png",r"\rr.png",r"\dd.png",r"\gl.png",r"\kxip.png",r"\srh.png",r"\rps.png",r"\ktk.png",r"\pw.png"]

master = Tk() 
master.geometry('500x500')
master.title('IPL Cricket Match Predictor')
l1 = Label(master, text = "Team A", font=("Helvetica", 14, 'bold')) 
l2 = Label(master, text = "Team B", font=("Helvetica", 14, 'bold')) 
l3 = Label(master, text = "Venue") 
l4 = Label(master, text = "City") 
l5 = Label(master, text = "Match Date") 
l6 = Label(master, text = "Toss Winner") 
labelVS = Label(master, text = "VS", font=("Helvetica", 12, 'italic')) 
  
# grid method to arrange labels in respective 
# rows and columns as specified 
l1.grid(row = 3, column = 0, columnspan = 3, pady = 10) 
l2.grid(row = 3, column = 4, columnspan = 3, pady = 10) 
l3.grid(row = 5, column = 0, sticky = W, pady = 10, padx = 10) 
l4.grid(row = 6, column = 0, sticky = W, pady = 10, padx = 10) 
l5.grid(row = 7, column = 0, sticky = W, pady = 10, padx = 10) 
l6.grid(row = 8, column = 0, sticky = W, pady = 10, padx = 10) 
labelVS.grid(row = 1, column = 3) 
  
#list of Teams in IPL
tkvar = StringVar(master)
choices = { 'Mumbai Indians','Kolkata Knight Riders','Royal Challengers Bangalore','Deccan Chargers','Chennai Super Kings','Rajasthan Royals','Delhi Daredevils','Gujarat Lions','Kings XI Punjab','Sunrisers Hyderabad','Rising Pune Supergiants','Kochi Tuskers Kerala','Pune Warriors'}
tkvar2 = StringVar(master)
choices2 = { 'Mumbai Indians','Kolkata Knight Riders','Royal Challengers Bangalore','Deccan Chargers','Chennai Super Kings','Rajasthan Royals','Delhi Daredevils','Gujarat Lions','Kings XI Punjab','Sunrisers Hyderabad','Rising Pune Supergiants','Kochi Tuskers Kerala','Pune Warriors'}
tkvar.set('Mumbai Indians') # set the default option
tkvar2.set('Chennai Super Kings') # set the default option

#drop down menus for choosing 2 teams


imgA = PhotoImage(file = imgAddressPrefix+imageTeams[0]) 
img1A = imgA.subsample(2, 2) 
  
# setting image with the help of label 
teamAlogo = Label(master, image = img1A)
teamAlogo.grid(row = 0, column = 0, 
       columnspan = 3, rowspan = 3, padx = 5, pady = 20) 

imgB = PhotoImage(file = imgAddressPrefix+imageTeams[4])
img1B = imgB.subsample(2, 2) 
  
# setting image with the help of label 
teamBlogo = Label(master, image = img1B)
teamBlogo.grid(row = 0, column = 4, 
       columnspan = 3, rowspan = 3, padx = 5, pady = 20) 

def teamASelected(event):
    imgtemp =  PhotoImage(file = imgAddressPrefix+imageTeams[teamNames.index(event)])
    imgtemp = imgtemp.subsample(2, 2) 
    teamAlogo.configure(image = imgtemp)
    teamAlogo.image = imgtemp
    pass

def teamBSelected(event):
    imgtemp =  PhotoImage(file = imgAddressPrefix+imageTeams[teamNames.index(event)])
    imgtemp = imgtemp.subsample(2, 2) 
    teamBlogo.configure(image = imgtemp)
    teamBlogo.image = imgtemp
    pass

popupTeamA = OptionMenu(master, tkvar, *choices, command = teamASelected)
popupTeamA.bind
popupTeamB = OptionMenu(master, tkvar2, *choices2, command = teamBSelected)

# this will arrange entry widgets 
popupTeamA.config(width=24)
popupTeamA.grid(row = 4, column = 0, columnspan = 3, padx = 10) 
popupTeamB.config(width=24)
popupTeamB.grid(row = 4, column = 4, columnspan = 3, padx = 10)
mainloop() 
