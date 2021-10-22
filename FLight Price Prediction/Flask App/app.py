from logging import INFO
from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("model_pickle.pkl", "rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    
    # Airline Names
    
    Jet_Airways = 0                      
    IndiGo = 0                              
    Air_India = 0                           
    Multiple_carriers = 0                    
    SpiceJet= 0                              
    Vistara= 0                               
    Air_Asia= 0                              
    GoAir= 0                                 
    Multiple_carriers_Premium_economy = 0     
    Jet_Airways_Business = 0                  
    Vistara_Premium_economy = 0                
    Trujet = 0
    
    # Sources
    s_Delhi = 0
    s_Kolkata = 0   
    s_Banglore = 0    
    s_Mumbai = 0  
    s_Chennai = 0
    
    # Dest
    
    d_Cochin = 0
    d_Banglore = 0     
    d_Delhi = 0        
    d_New_Delhi = 0     
    d_Hyderabad = 0
    d_Kolkata = 0
    
    # Stops
    
    non_stop = 0
    one_stop = 0     
    two_stops = 0     
    three_stops = 0       
    four_stops = 0
    
    # add
    
    No_info = 0                         
    In_flight_meal_not_included = 0
    No_check_in_baggage_included = 0  
    one_Long_layover = 0               
    Change_airports = 0                   
    Business_class  = 0                  
    No_Info =  0                
    one_Short_layover =  0                 
    two_Long_layover = 0           
    Red_eye_flight = 0
    
    
    if request.method == "POST":
        
        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
        
        # Departure
        Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
        
        # Arrival
        date_arr = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
        
        # Duration
        dur_hour = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)
        
        airline=request.form['airline']
        
        if (airline == "Jet Airways"):
            
            Jet_Airways = 1                         
            IndiGo = 0                              
            Air_India = 0                           
            Multiple_carriers = 0                    
            SpiceJet= 0                              
            Vistara= 0                               
            Air_Asia= 0                              
            GoAir= 0                                 
            Multiple_carriers_Premium_economy = 0     
            Jet_Airways_Business = 0                  
            Vistara_Premium_economy = 0                
            Trujet = 0
            
        elif(airline == "IndiGo"):
            
            Jet_Airways = 0                      
            IndiGo = 1                              
            Air_India = 0                           
            Multiple_carriers = 0                    
            SpiceJet= 0                              
            Vistara= 0                               
            Air_Asia= 0                              
            GoAir= 0                                 
            Multiple_carriers_Premium_economy = 0     
            Jet_Airways_Business = 0                  
            Vistara_Premium_economy = 0                
            Trujet = 0
            
        elif(airline == "Air India"):
            
            Jet_Airways = 0                      
            IndiGo = 0                            
            Air_India = 1                           
            Multiple_carriers = 0                    
            SpiceJet= 0                              
            Vistara= 0                               
            Air_Asia= 0                              
            GoAir= 0                                 
            Multiple_carriers_Premium_economy = 0     
            Jet_Airways_Business = 0                  
            Vistara_Premium_economy = 0                
            Trujet = 0
            
        elif(airline == "Multiple carriers"):
            
            Jet_Airways = 0                      
            IndiGo = 0                            
            Air_India = 0                         
            Multiple_carriers = 1                    
            SpiceJet= 0                              
            Vistara= 0                               
            Air_Asia= 0                              
            GoAir= 0                                 
            Multiple_carriers_Premium_economy = 0     
            Jet_Airways_Business = 0                  
            Vistara_Premium_economy = 0                
            Trujet = 0
            
        elif (airline == "SpiceJet"):
            
            Jet_Airways = 0                      
            IndiGo = 0                            
            Air_India = 0                         
            Multiple_carriers = 0              
            SpiceJet= 1                              
            Vistara= 0                               
            Air_Asia= 0                              
            GoAir= 0                                 
            Multiple_carriers_Premium_economy = 0     
            Jet_Airways_Business = 0                  
            Vistara_Premium_economy = 0                
            Trujet = 0
            
        elif (airline == "Vistara"):
            
            Jet_Airways = 0                      
            IndiGo = 0                            
            Air_India = 0                         
            Multiple_carriers = 0              
            SpiceJet= 0                           
            Vistara= 1                              
            Air_Asia= 0                              
            GoAir= 0                                 
            Multiple_carriers_Premium_economy = 0     
            Jet_Airways_Business = 0                  
            Vistara_Premium_economy = 0                
            Trujet = 0
            
        elif (airline == "Air Asia"):
            
            Jet_Airways = 0                      
            IndiGo = 0                            
            Air_India = 0                         
            Multiple_carriers = 0              
            SpiceJet= 0                           
            Vistara= 0                   
            Air_Asia= 1                              
            GoAir= 0                                 
            Multiple_carriers_Premium_economy = 0     
            Jet_Airways_Business = 0                  
            Vistara_Premium_economy = 0                
            Trujet = 0
            
        elif (airline == "GoAir"):
            
            Jet_Airways = 0                      
            IndiGo = 0                            
            Air_India = 0                         
            Multiple_carriers = 0              
            SpiceJet= 0                           
            Vistara= 0                   
            Air_Asia= 0                         
            GoAir= 1                              
            Multiple_carriers_Premium_economy = 0     
            Jet_Airways_Business = 0                  
            Vistara_Premium_economy = 0                
            Trujet = 0
            
        elif (airline == "Multiple carriers Premium economy"):
            
            Jet_Airways = 0                      
            IndiGo = 0                            
            Air_India = 0                         
            Multiple_carriers = 0              
            SpiceJet= 0                           
            Vistara= 0                   
            Air_Asia= 0                         
            GoAir= 0                          
            Multiple_carriers_Premium_economy = 1 
            Jet_Airways_Business = 0                  
            Vistara_Premium_economy = 0                
            Trujet = 0
            
        elif (airline == "Jet Airways Business"):
            
            Jet_Airways = 0                      
            IndiGo = 0                            
            Air_India = 0                         
            Multiple_carriers = 0              
            SpiceJet= 0                           
            Vistara= 0                   
            Air_Asia= 0                         
            GoAir= 0                          
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1                  
            Vistara_Premium_economy = 0                
            Trujet = 0
            
        elif (airline == "Vistara Premium economy"):
            
            Jet_Airways = 0                      
            IndiGo = 0                            
            Air_India = 0                         
            Multiple_carriers = 0              
            SpiceJet= 0                           
            Vistara= 0                   
            Air_Asia= 0                         
            GoAir= 0                          
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0                 
            Vistara_Premium_economy = 1                
            Trujet = 0
            
        elif (airline == "Trujet"):
            
            Jet_Airways = 0                      
            IndiGo = 0                            
            Air_India = 0                         
            Multiple_carriers = 0              
            SpiceJet= 0                           
            Vistara= 0                   
            Air_Asia= 0                         
            GoAir= 0                          
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0                 
            Vistara_Premium_economy = 0            
            Trujet = 1
            
        Source = request.form["Source"]
        
        if (Source == "Delhi"):
            
            s_Delhi = 1
            s_Kolkata = 0   
            s_Banglore = 0    
            s_Mumbai = 0  
            s_Chennai = 0
            
        elif(Source == "Kolkata"):
            
            s_Delhi = 0
            s_Kolkata = 1
            s_Banglore = 0    
            s_Mumbai = 0  
            s_Chennai = 0
            
        elif(Source == "Banglore"):
            
            s_Delhi = 0
            s_Kolkata = 0
            s_Banglore = 1    
            s_Mumbai = 0  
            s_Chennai = 0
            
        elif(Source == "Mumbai"):
            
            s_Delhi = 0
            s_Kolkata = 0
            s_Banglore = 0    
            s_Mumbai = 1
            s_Chennai = 0
            
        elif(Source == "Chennai"):
            
            s_Delhi = 0
            s_Kolkata = 0
            s_Banglore = 0    
            s_Mumbai = 0
            s_Chennai = 1
            
            
        Dest = request.form["Destination"]
        
        if (Dest == "Cochin"):
            
            d_Cochin = 1
            d_Banglore = 0     
            d_Delhi = 0        
            d_New_Delhi = 0     
            d_Hyderabad = 0
            d_Kolkata = 0
            
        elif (Dest == "Banglore"):
            
            d_Cochin = 0
            d_Banglore = 1
            d_Delhi = 0        
            d_New_Delhi = 0     
            d_Hyderabad = 0
            d_Kolkata = 0
            
        elif (Dest == "Delhi"):
            
            d_Cochin = 0
            d_Banglore = 0
            d_Delhi = 1        
            d_New_Delhi = 0     
            d_Hyderabad = 0
            d_Kolkata = 0
            
        elif (Dest == "New_Delhi"):
            
            d_Cochin = 0
            d_Banglore = 0
            d_Delhi = 0      
            d_New_Delhi = 1    
            d_Hyderabad = 0
            d_Kolkata = 0
            
        elif (Dest == "Hyderabad"):
            
            d_Cochin = 0
            d_Banglore = 0
            d_Delhi = 0      
            d_New_Delhi = 0    
            d_Hyderabad = 1
            d_Kolkata = 0
            
        elif (Dest == "Kolkata"):
            
            d_Cochin = 0
            d_Banglore = 0
            d_Delhi = 0      
            d_New_Delhi = 0    
            d_Hyderabad = 0
            d_Kolkata = 1
            
        # Total Stops
        Total_stops = int(request.form["stops"])
        
        if(Total_stops == 0):
            
            non_stop = 1
            one_stop = 0     
            two_stops = 0     
            three_stops = 0       
            four_stops = 0
            
        elif(Total_stops == 1):
            
            non_stop = 0
            one_stop = 1     
            two_stops = 0     
            three_stops = 0       
            four_stops = 0
            
        elif(Total_stops == 2):
            
            non_stop = 0
            one_stop = 0     
            two_stops = 1     
            three_stops = 0       
            four_stops = 0
                    
        elif(Total_stops == 3):
            
            non_stop = 0
            one_stop = 0     
            two_stops = 0     
            three_stops = 1       
            four_stops = 0

        elif(Total_stops == 4):
            
            non_stop = 0
            one_stop = 0     
            two_stops = 0     
            three_stops = 0       
            four_stops = 1
            
        addition = request.form["Destination"]
        
        if (addition == "No info"):
            
            No_info = 1                         
            In_flight_meal_not_included = 0   
            No_check_in_baggage_included = 0     
            one_Long_layover = 0                    
            Change_airports = 0                    
            Business_class  = 0                    
            No_Info = 0                            
            one_Short_layover = 0                    
            two_Long_layover = 0                     
            Red_eye_flight = 0
            
        elif(addition == "In-flight meal not included"):
            
            No_info = 0                         
            In_flight_meal_not_included = 1
            No_check_in_baggage_included = 0     
            one_Long_layover = 0                    
            Change_airports = 0                    
            Business_class  = 0                    
            No_Info = 0                            
            one_Short_layover = 0                    
            two_Long_layover = 0                     
            Red_eye_flight = 0
            
        elif(addition == "No check-in baggage included"):
            
            No_info = 0                         
            In_flight_meal_not_included = 0
            No_check_in_baggage_included = 1     
            one_Long_layover = 0                    
            Change_airports = 0                    
            Business_class  = 0                    
            No_Info = 0                            
            one_Short_layover = 0                    
            two_Long_layover = 0                     
            Red_eye_flight = 0
            
        elif(addition == "1 Long layover"):
            
            No_info = 0                         
            In_flight_meal_not_included = 0
            No_check_in_baggage_included = 0  
            one_Long_layover = 1                   
            Change_airports = 0                    
            Business_class  = 0                    
            No_Info = 0                            
            one_Short_layover = 0                    
            two_Long_layover = 0                     
            Red_eye_flight = 0
            
        elif(addition == "Change airports"):
            
            No_info = 0                         
            In_flight_meal_not_included = 0
            No_check_in_baggage_included = 0  
            one_Long_layover = 0               
            Change_airports = 1                   
            Business_class  = 0                    
            No_Info = 0                            
            one_Short_layover = 0                    
            two_Long_layover = 0                     
            Red_eye_flight = 0
            
        elif(addition == "Business class"):
            
            No_info = 0                         
            In_flight_meal_not_included = 0
            No_check_in_baggage_included = 0  
            one_Long_layover = 0               
            Change_airports = 0                   
            Business_class  = 1                    
            No_Info = 0                            
            one_Short_layover = 0                    
            two_Long_layover = 0                     
            Red_eye_flight = 0
            
        elif(addition == "No Info"):
            
            No_info = 0                         
            In_flight_meal_not_included = 0
            No_check_in_baggage_included = 0  
            one_Long_layover = 0               
            Change_airports = 0                   
            Business_class  = 0                  
            No_Info = 1                    
            one_Short_layover = 0                    
            two_Long_layover = 0                     
            Red_eye_flight = 0
        
        elif(addition == "1 Short layover"):
            
            No_info = 0                         
            In_flight_meal_not_included = 0
            No_check_in_baggage_included = 0  
            one_Long_layover = 0               
            Change_airports = 0                   
            Business_class  = 0                  
            No_Info =  0                
            one_Short_layover = 1                    
            two_Long_layover = 0                     
            Red_eye_flight = 0
            
        elif(addition == "2 Long layover"):
            
            No_info = 0                         
            In_flight_meal_not_included = 0
            No_check_in_baggage_included = 0  
            one_Long_layover = 0               
            Change_airports = 0                   
            Business_class  = 0                  
            No_Info =  0                
            one_Short_layover =  0                 
            two_Long_layover = 1                   
            Red_eye_flight = 0
            
        elif(addition == "Red-eye flight"):
            
            No_info = 0                         
            In_flight_meal_not_included = 0
            No_check_in_baggage_included = 0  
            one_Long_layover = 0               
            Change_airports = 0                   
            Business_class  = 0                  
            No_Info =  0                
            one_Short_layover =  0                 
            two_Long_layover = 0           
            Red_eye_flight = 1
            
            
        # Prediction
        
        price_f = model.predict([[
            Journey_day,Journey_month,Dep_hour,Dep_min,
            Arrival_hour,Arrival_min,dur_hour,dur_min,
            Air_India,GoAir,IndiGo,Jet_Airways,Multiple_carriers,
            Multiple_carriers_Premium_economy,SpiceJet,
            Trujet,Vistara,Vistara_Premium_economy,s_Chennai,
            s_Delhi,s_Kolkata,s_Mumbai,d_Cochin,d_Delhi,d_Hyderabad,
            d_Kolkata,d_New_Delhi,two_stops,three_stops,four_stops,
            non_stop,Change_airports,In_flight_meal_not_included,
            No_Info,No_check_in_baggage_included,No_info,Red_eye_flight
        ]])
        
        print(price_f)
        
        output=round(price_f[0],2)
        
        return render_template('results.html',prediction_text="Your Flight price is Rs. {}".format(output))


    return render_template("results.html")



if __name__ == "__main__":
    app.run(debug=True)