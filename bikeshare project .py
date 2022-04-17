import time
import pandas as pd
import numpy as np

city_information= {'chicago': 'chicago.csv',
                   'new york city': 'new_york_city.csv',
                   'washington': 'washington.csv'}

# define name of citys as C 
C=['chicago','new york city','washington']
# define name of months as M
M=['january', 'february', 'march', 'april', 'may', 'june','all']
# define name of months as days
D= ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']

def user_inputs():
    """ the function takes the user input (city,month,day) and get filter it by using while loop 
    
    """
    
    
    #introduction of our program to user
    print('Hi let\'s analyze and explore some important information in our bikeshare data ')
    #take your username and welcome 
    print('please,enter your name')
    user_name=input().title()
    print('welcome to our program Mr. or Mrs',format(user_name))
    
    #to know and define which city we will use and filter it by while loop
    city =input('please, enter the name city (chicago or new york city or washington) :\n\n').lower()
    while city not in C :
        print('Sorry '+user_name+', your input is wrong this should be:( chicago or new york city or washington )')
        city=input('take care again ,you should enter the city as above :\n\n').lower()
    
    #to know and define which month we will use and filter it by while loop
    month = input('please, enter your month  ( january or february or march or april or may or june or all ) :\n\n').lower()
    while month not in M :
        print('Sorry '+user_name+', your input is wrong this should be:( january or february or march or april or may or june or all )')
        month=input('take care again ,you should enter the month as above :\n\n').lower()
        
    #to know and define which day we will use and filter it by while loop
    day = input('please, enter your day ( sunday or monday or tuesday or wednesday or thursday or friday or saturday or all ) :\n\n').lower()
    while day not in D :
        print('Sorry '+user_name+', your input is wrong this should be:( sunday or monday or tuesday or wednesday or thursday or friday or saturday or all )')
        month=input('take care again ,you should enter the day as above :\n\n').lower()
        
    print('-'*50)
    
    return city, month, day



def load_data(city,month,day):
    """ the function takes the information from user input (city,month,day) and applying load_data 
    
    """
    
    #1.convert excel_file into data_frame
    df = pd.read_csv(city_information[city])

    #2.convert 'the start time' into data_time    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #3.create new column 'month'
    df['month'] = df['Start Time'].dt.month
    
    #4.create new column'day of week'
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # apply filter for month entered by user 
    if month != 'all':
        
        #1.define months variable
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        
        month = months.index(month) + 1
        
        # create the new dataframe for month
        df = df[df['month'] == month]

    # apply filter for day entered by user
    
    if day != 'all':
        
        # create the new dataframe for day
        df = df[df['day_of_week'] == day.title()]

    return df


def status_time(df):
    """ the function takes the load data  and show the user important information about 
    the most common month ,the most common day of week ,the most common day ,the most common start hour
    to know the user about them
    """
    
    print ('it is appear below the most frequent times of travel')
    
    start_time=time.time()
    
    # display the most common month in our programm
    most_common_month =df['month'].mode()[0]
    define_months={1:'january',2:'february', 3:'march', 4:'april', 5:'may',6:'june'}
    print('the common popular  month:',most_common_month,'(',define_months[most_common_month],')')

    # display the most common day of week in our programm
    most_common_day_of_week =df['day_of_week'].mode()[0]
    print('this is the most day of week:', most_common_day_of_week)
    
    # display the most common start hour in our programm
    most_common_start_time =df['Start Time'].mode()[0]
    print('this is the most common start hour:', most_common_start_time )
    
    #define this took seconds
    print("\nThis is taking %s seconds." % (time.time() - start_time))

    print('-'*50)
    

def status_trip_durations(df):
    """ the function used to dispaly important inforamtion about the trip duration status 
    as the total travel time ,the average time
    """
    
    print('it is below the trip duration status :')
    
    start_time=time.time()
    
    #define trip duration status (total_travel_time)
    trip_total_traveltime=df['Trip Duration'].sum()
    print("the total travel time for trips :",trip_total_traveltime)
    
    #define trip duration status (the mean_travel_time)
    trip_mean_traveltime=df['Trip Duration'].mean()
    print("the average time for trips : ",trip_mean_traveltime)
    
    #define this took seconds
    print("\nThis is taking %s seconds." % (time.time() - start_time))
    print('-'*50)
    
    
def station_status(df):
    """ the function used to display important inforamtion about the station_status 
    as the common start station ,the common End station,most common combination 
    """
    
    print('it is below the trip station status :')    
    
    start_time=time.time()
    
    # display the most common start station in our programm
    tripCommon_start_station=df['Start Station'].mode()[0]
    print("this is the most common start station:",tripCommon_start_station)
    
    
    # display the most common end station in our programm
    tripCommon_end_station=df['End Station'].mode()[0]
    print("this is the most common End station:",tripCommon_end_station)
    
    
    # display the most common trip from start to end in our programm
    most_freq_combination=df.groupby(['Start Station','End Station']).size().idxmax()
    print("most common combination of ( start station trip and end station trip ) : ",most_freq_combination)
    
    #define this took seconds
    print("\nThis is taking %s seconds." % (time.time() - start_time))
    print('-'*50)
    
    
def user_info(df):
    """ the function used to display important inforamtion about the user_information 
    as gender ,how much people (subscribe and customer ),birthday of user
    """
    
    print('it is below the user status :')
    
    start_time=time.time()
    
    #display the user information (types) in our programm
    counts_userinfo_types=df['User Type'].value_counts().to_frame()
    print('the user type')
    print(counts_userinfo_types)
    
    #display the user information (Gender) in our programm ( Chicago and New York City)
    if 'Gender' in df.columns :

        userinfo_genders=df['Gender'].value_counts().to_frame()
        
        print('the user Gender :')
        print(userinfo_genders)
    
    #display the user information (birth_year) in our programm ( Chicago and New York City)
    if 'Birth Year' in df.columns :
        
        min_birth_year=df['Birth Year'].min()
        print("the earliest of birth day userinfo :",int(min_birth_year))
        
        max_birthyear_userinfo=df['Birth Year'].max()
        print("the recent of birth day userinfo :",int(max_birthyear_userinfo))
        
        comm_birthyear_users=df['Birth Year'].mode()[0]
        print('the most common of birth day userinfo :',int(comm_birthyear_users))
        
        
    #define this took seconds
    
    print("\nThis is taking %s seconds." % (time.time() - start_time))
    print('-'*50)   
    
    

         
            
def ask_for_raw(df):
    """ the function used to ask user if he want to see the first five row 
    """
    A=0
    
    # to user see first 5 raws if he want
    while True :
        
        print("do you want to see sample (first {} raws)  (yes or no) :\n".format(A+5))
        raw=input().lower()
        
        if raw=='yes':
            A+=5
            first_raw=df.head(A)
            print('the is the raws you want to show :')
            print(first_raw)   
        elif raw=='no' :
              print('thanks .....')
              break
        else:
             print("try again ,the word must be (yes or no )")
                
        
            
def main():
    
    """ the function used to operate the program and for restart the if the user want 
    """
    
    while True:
        
         city, month, day = user_inputs()
         
         df = load_data(city, month, day)
         
         
         status_time(df)
         
         station_status(df)
         
         status_trip_durations(df)
         
         user_info(df)
         
         
         ask_for_raw(df)
         
         restart_programm = input('\nWould you like to restart the programm? Enter yes or no.\n')
         
         if restart_programm.lower() != 'yes':
             break


if __name__ == "__main__":
	main()