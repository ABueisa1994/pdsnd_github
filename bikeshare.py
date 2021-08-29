import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago','new york city','washington']
months = [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'All']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']

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
    while True:
        city = str(input("Select your city from the list 'Chicago, New York City, Washington' \n")).lower()
        if city not in cities:
            print('You entered invalid city, please try again')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input("Please enter the month you want to filter by or enter all for all months \n")).lower().title()
        if month not in months:
            print('You entered invalid input, please try again')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input("Please enter a day of the week you want to filter by or enter all for all days \n")).lower().title()
        if day not in days:
            print('You entered invalid input, please try again')
        else:
            break

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
# Read the files data from City Data Dictionary
    df = pd.read_csv(CITY_DATA[city])
# We need to convert the start time column into datatime to process data
    df['Start Time'] = pd.to_datetime(df['Start Time'])
# After the conversion we need to creat columns for the months and days
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

# Now we creat a filter for months
    if month != 'All':
        month = months.index(month) + 1
        df = df[df['month'] == month ]
# Now we creat a filter for days
    if day != 'All':
        df = df[df['day_of_week'] == day ]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_mode = df['month'].mode()[0]
    print(month_mode)
    print('The most common month is {}'.format(months[month_mode -1]))

    # TO DO: display the most common day of week
    print('The most common day is {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most common hour in use is {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common starting station is {}' .format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The most common ending station is {}' .format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    com_stations = df['Start Station'].map(str) + ' to ' + df['End Station']
    print('The Common Combination of Stations is {}' .format(com_stations.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_min, total_sec = divmod(df['Trip Duration'].sum(), 60)
    total_hours, total_min = divmod(total_min , 60)
    print('The duration of the trip is: ', total_hours, 'hours', total_min, 'minutes', total_sec, 'seconds.')

    # TO DO: display mean travel time
    tra_mean_min, tra_mean_sec = divmod(df['Trip Duration'].mean(), 60)
    tra_mean_hours, tra_mean_min = divmod( tra_mean_min , 60)
    print(' The travel mean time is :  ', tra_mean_hours, 'hours', tra_mean_min, 'minutes', tra_mean_sec, 'seconds.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The users catagories are \n {}' .format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    if ('Gender' not in df):
        print('Sorry, the gender data are not available for Washington')
    else:
        print('The genders are \n {}' .format(df['Gender'].value_counts()))

    # TO DO: Display earliest, most recent, and most common year of birth
    if ('Birth Year' not in df):
        print('Sorry, the birth year data are not available for Washington')
    else:
        print('The most common birth year is: {}' .format(df['Birth Year'].mode()[0]))
        print('The most recent birth year is: {}' .format(df['Birth Year'].max()))
        print('The earliest birth year is: {}' .format(df['Birth Year'].min()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df): 
    initial = 0
    ask = input('\nDo you want to display the data ? Enter yes to view or no to exit \n').lower()
    while ask == 'yes':
        try: 
            n = int(input('\nEnter the number of rows to display \n'))
            n = initial + n
            print(df.iloc[initial:n])
            ask = input('\nDo you want to view more rows ? Enter yes or no \n').lower()
            initial = n
            
        except ValueError:
            print('Invalid input, please use integers') 

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
