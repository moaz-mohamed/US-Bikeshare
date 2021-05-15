import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
DAY_DATA = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
def get_filters():
    
    #Asks user to specify a city, month, and day to analyze.

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str(input("Enter a city from : chicago, new york city, washington\n"))
    city.lower()
    while (city not in CITY_DATA.keys()):
        print("invalid city, try again")
        city = str(input("\nEnter a city from : chicago, new york city, washington\n"))
        city.lower()


    # get user input for month (all, january, february, ... , june)
    month = str(input("\nEnter a month from : all, january, february, march, april, may, june\n"))
    month.lower()
    while (month not in MONTH_DATA):
        print("invalid month, try again")
        month = str(input("\nEnter a month from : all, january, february, march, april, may, june\n"))
        month.lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(input("\nEnter a day from : all, monday, tuesday, wednesday, thursday, friday, saturday, sunday\n"))
    day.lower()
    while (day not in DAY_DATA):
        print("invalid day, try again")
        day = str(input("\nEnter a day from : all, monday, tuesday, wednesday, thursday, friday, saturday, sunday\n"))
        day.lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    #Loads data for the specified city and filters by month and day if applicable.


    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
   

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print("\nMost Common month: " , common_month)
    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("\nMost Common day: " + common_day)
    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("\nMost Common hour: " , common_hour)
    ######
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
  

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("\nMost Common start station: " + common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("\nMost Common end station: " + common_end_station)

    # display most frequent combination of start station and end station trip
    df['Combination Station'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination_station = df['Combination Station'].mode()[0]
    print("\nMost Common combination of start to end station: " + common_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
 

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time: " , df['Trip Duration'].sum())

    # display mean travel time
    print("Mean travel time: " , df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):


    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Types:")
    print(user_types) 

    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("Gender:") 
        print(gender)
    except:
        print("No gender data for this city")


    # Display earliest, most recent, and most common year of birth
    
    try:
        #earliest
        print("Earliest year of birth")
        print(df['Birth Year'].min())

        #most recent
        print("Most recent year of birth")
        print(df['Birth Year'].max())

        #most common
        print("Most common year of birth")
        print(df['Birth Year'].mode()[0])
    except:
        print("No year of birth data for this city")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
