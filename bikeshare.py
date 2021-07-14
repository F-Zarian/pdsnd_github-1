import time  # provides various time related functions. Will be used to calculate process duration in several functions.
import pandas as pd
import numpy as np
import calendar as cal # provides useful function related to the calendar, will need it in time_stats()

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAY_DATA = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters(city, month, day):
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for Chicago, New York City, or Washington?\n').lower()
    while city not in CITY_DATA:
        print('Oops, wrong city name! Please enter either Chicago, New York City or Washington:\n')
        city = input('Please enter a valid city name:\n').lower()  
    # TO DO: get user input for month (all, january, february, ... , june) 
    month =  input('Please enter all for no month filter or January through June to see data for the month:\n').lower()  
    while month not in MONTH_DATA:
        print('Oops, wrong month name! Please enter a valid month name:\n')
        month = input('Please enter a valid month name:\n').lower() 
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please enter all for no day filter or a day of the week, Sunday through Saturday to filter by the day\n').lower()
    while day not in DAY_DATA:
        print('Oops, wrong input! Please enter a valid name for the day of the week:\n')
        day = input('Please enter a valid day of the week name:\n').lower()
    print('-'*40)
    
    return city, month, day


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
    # TO DO: Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # TO DO: Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: Extract month and day of the week from Start Time column to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # TO DO: Filter by month if applicable
    if month != 'all':
        # use the index of the MONTH_DATA list to get the corresponding integer
        month = MONTH_DATA.index(month) + 1
        
        # Filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    most_common_month_name = cal.month_name[most_common_month]
    print('Most Common Bikeshare Month:', most_common_month_name)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most Common Bikeshare Day:', most_common_day)

    
    # TO DO: extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # TO DO: display the most common hour of day (from 0 to 23).
    popular_hr = df['hour'].mode()[0]
    print('Most Common Bikeshare Start Hour:', popular_hr)

    elapsed_time_secs = time.time() - start_time
    print("\nThis took %s seconds." % round(elapsed_time_secs, 2))
    print('-'*40)
    
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', common_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    common_start_end_station = (df['Start Station'] + ' - ' + df['End Station']).mode()[0]
    print('Most Common Combination of Start and End Stations:', common_start_end_station)

    elapsed_time_secs = time.time() - start_time
    print("\nThis took %s seconds." % round(elapsed_time_secs, 2))
    print('-'*40)
    
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_time = df['Trip Duration'].sum()
    print('Total Travel Time (seconds):', tot_time)
    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('Mean Travel Time (seconds):', avg_time)

    elapsed_time_secs = time.time() - start_time
    print("\nThis took %s seconds." % round(elapsed_time_secs, 2))
    print('-'*40)
    
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('Counts of User Types:', user_type_count)
    
    # TO DO: Display counts of gender
    while True:
        try:
            gender_count = df['Gender'].value_counts()
            print('Counts of Gender:', gender_count)
            break
        except:
            print('Gender data is not available for your selected city!')
            break
        
    # TO DO: Display earliest, most recent, and most common year of birth
    while True:
        try:
            earliest_birth_yr = int(df['Birth Year'].min())
            print('Earliest Year of Birth:', earliest_birth_yr)
            
            latest_birth_yr = int(df['Birth Year'].max())
            print('Most Recent Year of Birth:', latest_birth_yr)
        
            most_com_birth_yr = int(df['Birth Year'].mode()[0])
            print('Most Common Year of Birth:', most_com_birth_yr)
            break
        except:
            print('Birth Year data not available for your selected city!')
            break
                
    elapsed_time_secs = time.time() - start_time
    print("\nThis took %s seconds." % round(elapsed_time_secs, 2))
    print('-'*40)
    

def display_raw_data(df):
    """
    Displays raw data in an interactive manner. The script prompts the user whether they would like to see the raw data.
    If user answers 'yes', then the script prints 5 rows of the data at a time and continues prompting and priniting the
    next 5 rows at a time till the user chooses 'no'.  
    Args:
        (DataFrame) df: Pandas DataFrame containing city data filtered by month and day
    Returns:
        None. 
    """
    print('\nDisplaying raw data...\n')
    print(df.head())
    i = 0
    while True:
        raw_data = input('\nWould you like to see the next five rows of the raw data? Enter yes or no.\n').lower()
        pd.set_option('display.max_columns',200)
        if raw_data != 'yes':
            return
        i += 5
        print(df.iloc[i:i+5])
    elapsed_time_secs = time.time() - start_time
    print("\nThis took %s seconds." % round(elapsed_time_secs, 2))
    print('-'*40)
    
  
def main():
    while True:
        city, month, day = get_filters("chicago", "june", "all")
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        while True:
            raw_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n').lower()
            if raw_data != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart != 'yes':
            break
                    

if __name__ == "__main__":
	main()
    