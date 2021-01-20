import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city=input('Would you like to see data for (chicago, new york city, washington)?').lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('Invalid input please enter one of the three cities correctly')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True :
        month=input('\n which month would you like to filer the data by ? \n').lower()
        if month in ['all','january','february','march','april','may','june']:
            break
        else:
            print('\n Invalid input,please enter valid input \n')
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        day=input('\n please enter which day of the week \n').lower()
        if day in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
            break
        else:
            print('\nInvalid input,please enter valid input \n')
        

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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is {}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('The most common day is {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    hour = df['Start Time'].dt.hour
    print('The most common start hour is {}'.format(hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common start station is {} \n'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The most common end station is {} \n'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent combination of start statio and end station trip is {} \n'
          .format(df.groupby(['Start Station','End Station']).size().nlargest(1)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    minute, second = divmod(df['Trip Duration'].sum(), 60)
    hour, minute = divmod(minute, 60)
    day, hour = divmod(hour,24)
    
    # TO DO: display total travel time
    print('The total travel time is {} days,{} hours, {} minuts , {} seconds \n'.format(day,hour,minute,second))
    
    # TO DO: display mean travel time
    if minute > 60:
        hour, minute = divmod(minute, 60)
        print('The average travel duration is {} hours, {} minuts ,{} seconds \n'.format(hour,minute,second))
    else:
        print('The average travel duration is {} minuts and {} seconds \n'.format(minute,second))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types \n',df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        print('Counts of genders \n',df['Gender'].value_counts())
    except:
        print("\nThere is no 'Gender' column in this file.")
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
          print('The earliest year of birth is {} \n'.format(df['Birth Year'].min()))
          print('The most recent year of birth is {} \n'.format(df['Birth Year'].max()))
          print('The most common year of birth is {} \n'.format(df['Birth Year'].mode()[0]))
    else:
        print('No year to show \n')
                                                             

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def raw_data(df):
    choice=input('Do you want to see 5 lines of raw data ? Yes/No \n').lower()
    lines=0
    while True:
        if choice=='yes':
            print(df.iloc[lines:lines+5])
            lines+=5
            choice=input('Do you want to see 5 lines of raw data ? Yes/No \n').lower()
        else:
            break
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
