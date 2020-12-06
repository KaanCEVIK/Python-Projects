# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:21:43 2020

@author: Kaan CEVIK
"""
ders=list()
grades={}
isim="Kazim Kaan CEVIK"
def lesson():
    counter=0
    total=0
    while(counter<=3):
        isim2= input("Lutfen isminizi ve soyadınızı giriniz:")
        if(isim2==isim):
            print("Welcome")
            num_les= int(input("Lutfen 5 adete kadar olacak sekilde ders sayınızı giriniz:"))
            if(num_les<3):
                fail=print("You failed in class")
                return fail
            elif(num_les>=3 and num_les<=5):
                for i in range(num_les):
                    ders.append(str(input("Please enter the name of " + str(i) + " th lessons name:"))) 
                grades["Midterm"]= 70
                grades["Final"]=90
                grades["Project"]=70
                Note1= grades["Midterm"]
                Note2= grades["Final"]
                Note3=grades["Project"]
                total=int((Note1*0.3)+(Note2*0.5)+(Note3*0.2))
                if(total>90):
                   print("Your grade:AA")
                   break
                elif (total<90 and total>70):
                   print("Your grade:BB")
                   break
                elif (total<70 and total>50):
                   print("Your grade:CC")
                   break
                elif (total<50 and total>30):
                   print("Your grade:DD")
                   break
                elif (total<30):
                   print("Your grade:FF  and You are failed")
                   break
            elif(num_les>5):
                exceed= print("You exceeded the limit of the lesson number")
                return exceed
        else:
            counter+=1
            if(counter==3):
                print("Please try again later")
                break

lesson()