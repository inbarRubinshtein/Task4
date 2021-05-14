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
        this_city = city.strip("\n")
        arrange = arrange_data(get_reqsest_des(this_city,api_key),get_reqsest_loc(this_city,api_key),city)
        data_citys[city] = arrange
        if not "there" in arrange:
            leng.append(data_citys[city][0])
        else:
            leng.append(0)
        cties.append(city)
    print("***********")
    print(data_citys)
    print("***********")
    three_far(leng,data_citys)
  
   
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

def arrange_data(data_distanc,data_location,city):#arrange data as a tuple
    print()
    try:
        Destination=data_distanc["rows"][0]["elements"][0]["distance"]["text"]
        Duration=data_distanc["rows"][0]["elements"][0]["duration"]["text"]
        Latitude=str(data_location["results"][0]["geometry"]["location"]["lat"])
        Length=str(data_location["results"][0]["geometry"]["location"]["lng"])
        print(" the city:"+city+", is "+Destination+" and "+Duration+" from Tel Aviv")
        print(" the location is:"+Latitude+"lat and "+Length+" len ")
        the_tuple=(("Destination:"+Destination),
                   ("Duration:"+Duration),
                   ("Latitude:"+Latitude),
                   ("Length:"+Length))
    except:
        wrong="there is no data"
        print(" the city:"+city+", "+wrong)
        return wrong
    return the_tuple
 

def three_far(lengths,des):# The 3 cities furthest from Tel Aviv and print them 
    lengths_int=[]
    city_length=dict()
    for city in des:
        try:
            num=des[city][0].split(":")[1].split(" ")[0].split(",")
            lengths_int.append((int)(num[0]+num[1]))
            city_length[city]=(int)(num[0]+num[1])
        except:
            lengths_int.append(0)
            city_length[city]=0
    lengths_int.sort()
    lengths_int.reverse()
    i=0
    print("The 3 cities furthest from Tel Aviv is:")
    for l in lengths_int:
        if i<3:   
            for city in city_length:
                if city_length[city]==l:
                     print("place:"+str(i+1)+", ia the city:"+city+" with the distance:"+str(lengths_int[i])+" km")
                     i+=1
   
       
                  
        
       
        
   
path_destinations="C:/Users/inbar/Desktop/Third_year/Second_Semester/Knowledge_data_engineering/Task/task4/dests.txt"
data = open(path_destinations,"r",encoding= "utf-8")
dict_destinations(data)

  
