# -*- coding: utf-8 -*-
"""
Created on Fri May  7 15:30:30 2021

@author: inbar
"""
import urllib,requests

def dict_destinations(destinations):#get all the data from the services and finding what is required
    
    api_key=input("entere your API:")
    leng= []
    data_citys = dict()
    cties=[]
    for city in destinations:
        this_city = city.rstrip("\n")
        data_citys[city] = arrange_data(get_reqsest_des(this_city,api_key),get_reqsest_loc(this_city,api_key))
        leng.append(data_citys[city][0])
        cties.append(city)
    three_far(leng,cties)
  
   
def get_reqsest_des(destinations,api_key): #the requests from the service "distancematrix"
    serviceurl = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    parms = dict() 
    parms["origins"] = 'תל אביב'
    parms["destinations"]=destinations
    parms["key"]= api_key
    
    url = serviceurl + urllib.parse.urlencode(parms)
    response_data= check_response(url)
    return response_data

def get_reqsest_loc(destinations,api_key): #the requests from the service "geocode"
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" %(destinations,api_key)
   
    response_data= check_response(url)
    return response_data

def check_response(url):# send the requests and return the response or if there is a problem
    try:
        response =requests.get(url)
        if not response.status_code == 200:
            print("HTTP error", response.status_code)
        else:
            try:
                response_data= response.json()
            except:
                print("response not is valid JSON format")
    except:
        print("something went wrong with response.get")
    return response_data

def arrange_data(data_distanc,data_location):#arrange data as a tuple
    the_tuple=(("Destination:"+data_distanc["rows"][0]["elements"][0]["distance"]["text"]),
               ("Duration:"+data_distanc["rows"][0]["elements"][0]["duration"]["text"]),
               ("Latitude:"+str(data_location["results"][0]["geometry"]["location"]["lat"])),
               ("Length:"+str(data_location["results"][0]["geometry"]["location"]["lng"])))
    return the_tuple
 
def three_far(lengths,des):# The 3 cities furthest from Tel Aviv and print them 
    lengths_int=[]
    for l in lengths:
        num=l.split(":")[1].split(" ")[0].split(",")
        lengths_int.append((int)(num[0]+num[1]))
    lengths_int.sort()
    lengths_int.reverse()
    i=0
    print("The 3 cities furthest from Tel Aviv is:")
    for city in des:
        if i<3:
            print("place:"+str(i+1)+", ia the city:"+city+" with the distance:"+str(lengths_int[i])+" km")
            i+=1
        
       
        
   
path_destinations="C:/Users/inbar/Desktop/Third_year/Second_Semester/Knowledge_data_engineering/Task/task4/dests.txt"
data = open(path_destinations,"r",encoding= "utf-8")
dict_destinations(data)

  
