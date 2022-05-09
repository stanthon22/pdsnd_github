import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['all' , 'january' , 'february' , 'march', 'april','may' , 'june']
def get_filters() :
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago' , 'new york city' , 'washington'] 
    while True :
        city = input('Please Enter name of the city to analyze data , from chicago , New york city , Washington : ').lower()
        if city in cities :
            break 
    # TO DO: get user input for month (all, january, february, ... , june)
    #months = ['all' , 'january' , 'february' , 'march', 'april','may' , 'june']
    while True :
        month = input('\nEnter name of month you want to filter from January to June or all for no month filter : ').lower()
        if month in months :
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    week = [ 'all' , 'saturday' , 'sunday' , 'monday' , 'tuesday' , 'wednesday' , 'thursday' , 'friday' ] 
    while True :
        day = input('\nEnter name of day you want to filter or all for no day filter :').lower()
        if day in week :
            break
            
    
    print('-'*40)
    return city, month, day   #This Fun Return Three input from user (City , Month , Day)

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        #months = ['j' , 'january' , 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)
        df = df.loc[df['month'] == month]
    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]
   
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    #months = ['all' , 'j' , 'january' , 'february' , 'march', 'april','may' , 'june']
    common_month = df['month'].mode()[0]
    print("Most common month is : " , months[common_month].title())


    # TO DO: display the most common day of week
    print("Most common day of week is : " , df['day_of_week'].mode()[0] )


    # TO DO: display the most common start hour
    print("Most common start hour is : " , df['hour'].mode()[0]  )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print ("Most commonly used start station is : " , df['Start Station'].mode())


    # TO DO: display most commonly used end station
    print ("Most commonly used end station is : " , df['End Station'].mode())


    # TO DO: display most frequent combination of start station and end station trip
    print ("Most frequent combination of start station and end station trip is : " , df[['Start Station' , 'End Station']].mode().loc[0][0] ," and " , df[['Start Station' , 'End Station']].mode().loc[0][1])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travrl time is : " , df['Trip Duration'].sum()) 

    # TO DO: display mean travel time
    print("Average travel time is : " ,  df['Trip Duration'].mean())
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats( df , city ):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user Type is : " , df['User Type'].value_counts())


    # TO DO: Display counts of gender
    if city == 'chicago' or city == 'new york city'  :
        print("Counts of Gender is : " , df['Gender'].value_counts())
    # TO DO: Display earliest, most recent, and most common year of birth
        print("The Earliest common year of birth is : " , df['Birth Year'].min())
        print("The Most recent common year of birth is : " , df['Birth Year'].max())
        print("The Most common year of birth is : " , df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    #print 5 raws od data 
    print(df.head())
    count = 0
    #ask user if want ti display extra raws or no 
    while True:
        view_raw_data = input('\nDo you want to view more five row of data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        count = count + 5
        print(df.iloc[count:count+5])

    
def main():
    while True :
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df , city)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
    