import tkinter as tk
from tkinter import *
from tkinter import ttk


master = Tk() 
master.geometry('500x500')
master.title('IPL Cricket Match Predictor')
l1 = Label(master, text = "Team A") 
l2 = Label(master, text = "Team B") 
  
# grid method to arrange labels in respective 
# rows and columns as specified 
l1.grid(row = 0, column = 0, sticky = W, pady = 10, padx = 20) 
l2.grid(row = 1, column = 0, sticky = W, pady = 10, padx = 20) 
  
#list of Teams in IPL
tkvar = StringVar(master)
choices = { 'Mumbai Indians','Kolkata Knight Riders','Royal Challengers Bangalore','Deccan Chargers','Chennai Super Kings','Rajasthan Royals','Delhi Daredevils','Gujarat Lions','Kings XI Punjab','Sunrisers Hyderabad','Rising Pune Supergiants','Kochi Tuskers Kerala','Pune Warriors'}
tkvar2 = StringVar(master)
choices2 = { 'Mumbai Indians','Kolkata Knight Riders','Royal Challengers Bangalore','Deccan Chargers','Chennai Super Kings','Rajasthan Royals','Delhi Daredevils','Gujarat Lions','Kings XI Punjab','Sunrisers Hyderabad','Rising Pune Supergiants','Kochi Tuskers Kerala','Pune Warriors'}
tkvar.set('Mumbai Indians') # set the default option
tkvar2.set('Mumbai Indians') # set the default option

popupTeamA = OptionMenu(master, tkvar, *choices)
popupTeamB = OptionMenu(master, tkvar2, *choices2)

e1 = Entry(master) 
e2 = Entry(master) 
  
# this will arrange entry widgets 
popupTeamA.grid(row = 0, column = 1, pady = 2) 
popupTeamB.grid(row = 1, column = 1, pady = 2) 
mainloop() 
