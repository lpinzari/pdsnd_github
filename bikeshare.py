#title         : bikeshare.py
#description   : This program display an interactive menu to explore bikeshare dataset
#author        : Ludovico Pinzari
#usage         : python bikeshare.py
#notes         :
#python_version: 3.6.6
#=====================================================================================

# Import the modules needed to run the script
import sys, os, time
import colorama
import pandas as pd
import numpy as np

# data set to be analyzed
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nLet\'s explore some data!')

    msg_error = "\n\t\t\tInvalid selection, please try again."

    # get user input for city (chicago, new york city, washington).
    options = len(city_options)
    print('\n\tThe Bike Share System has data for {} major cities in the US'.format(options))
    while True:
        print('\nPlease enter a number between 1 and {} to select the city you want to analyze:'.format(options))
        print('\n\t'+ colorize('number','yellow')+'\t'+ colorize('city','green'))
        print('-'*40)
        for id,city in city_options.items():
            print("\n\t{}:\t{}".format(colorize(id,'yellow'),colorize(city,'green')))
        print('-'*40)
        choice = input("\n"+colorize('>> ','yellow'))
        if choice in city_options:
            city = city_options.get(choice)
            break
        else:
            os.system('clear')
            print(colorize(msg_error,'pink'))

    # get user input for month (all, january, february, ... , june)
    options = len(month_options)
    print('\nThis report will provide interesting insights about the bikesharing in {}'.format(colorize(city,'green')))
    
    key_press()

    print('\nThe US bikeshare system has data for {} months between {} and {}'.format(options-1,month_options.get('1'),month_options.get(str(options-1))))

    while True:
        print('\nPlease enter a number between 1 and {} to select the month you want to filter by, or {} to apply no month filter.'.format(options-1,options))
        print('\n\t'+ colorize('number','yellow')+'\t'+ colorize('month','green'))
        print('-'*40)
        for id,month in month_options.items():
            print("\n\t{}:\t{}".format(colorize(id,'yellow'),colorize(month,'green')))
        print('-'*40)
        choice = input("\n"+colorize('>> ','yellow'))
        if choice in month_options:
            month = month_options.get(choice)
            break
        else:
            os.system('clear')
            print(colorize(msg_error,'pink'))

    if month != 'all':
        print('\nWe will show some statistics about the bikesharing in {} during {}'.format(city,colorize(month,'green')))
    else:
        print('\nWe will show some statistics about the bikesharing in {} for {} the months'.format(city,colorize(month,'green')))


    key_press()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    options =len(week_day_options)
    print('\nThis report provides also information for the bikeshare during the week')
    while True:
        print('\nPlease enter a number between 1 and {} to select a day of the week to filter by,'.format(options-1))
        print('or {} to apply no month filter.'.format(options))
        print('\n\t'+ colorize('number','yellow')+'\t'+ colorize('day','green'))
        print('-'*40)
        for id,day in week_day_options.items():
            print("\n\t{}:\t{}".format(colorize(id,'yellow'),colorize(day,'green')))
        print('-'*40)
        choice = input("\n"+colorize('>> ','yellow'))
        if choice in week_day_options:
            day = week_day_options.get(choice)
            break
        else:
            os.system('clear')
            print(colorize(msg_error,'pink'))

    os.system('clear')

    print('\n\t'+colorize('Your final selection is','green'))
    print('\n\tattribute \tfilter')
    print('-'*40)
    print('\tcity      \t{}'.format(colorize(city,'green')))
    print('\n\tmonth     \t{}'.format(colorize(month,'green')))
    print('\n\tweek day  \t{}'.format(colorize(day,'green')))
    print('-'*40)
    return city,month,day

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
    file_name = CITY_DATA[city]
    print("The data for the city of {} are in the file: {} ".format(city,file_name))

    # load data file into a DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':

        # get the numerical index for the corresponding month
        month = int(getKeyByValue(month_options,month))

        # filter by month to create the new dataframe
        df = df[df['month']==month]

        # filter by day of week if applicable
        if day != 'all':

            # filter by day of week to create the new dataframe
            df = df[df['day_of_week']==day.title()]

    print('-'*40)

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n\t'+colorize('Calculating The Most Frequent Times of Travel','green')+'\n')
    start_time = time.time()

    # extract month, weekday and hour from the Start Time column
    month = df['Start Time'].dt.month
    weekday = df['Start Time'].dt.weekday_name
    start_hour = df['Start Time'].dt.hour

    # find the most popular month, day of week and start hour
    popular_month = month_options.get(str(month.mode()[0]))
    popular_weekday = weekday.mode()[0]
    popular_start_hour = start_hour.mode()[0]

    # display the computed statistics
    print('-'*40)
    print('\n\tmonth     \t',colorize(popular_month,'green'))
    print('\n\tweekday   \t',colorize(popular_weekday,'green'))
    print('\n\tstart hour\t',colorize(str(popular_start_hour),'green'))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n\t'+colorize('Calculating The Most Popular Stations and Trip','green')+'\n')
    start_time = time.time()

    # find the most popular start station, end station, combination of start and end station trip
    popular_start_station = df['Start Station'].value_counts().idxmax()
    popular_end_station = df['End Station'].value_counts().idxmax()
    comb_stations = df['Start Station'] + '-' + df['End Station']
    popular_comb_stations = comb_stations.value_counts().idxmax()

    # display the computed statistics
    print('-'*40)
    print('\n\tstart station\t',colorize(popular_start_station,'green'))
    print('\n\tend station\t',colorize(popular_end_station,'green'))
    print('\n\ttrip start\t',colorize(popular_comb_stations.split('-')[0],'green'))
    print('\n\ttrip end\t',colorize(popular_comb_stations.split('-')[1],'green'))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the number of trips and corresponding total and mean trip duration."""

    print('\n'+colorize('Calculating the number of trips and corresponding total and mean duration','green')+'\n')
    start_time = time.time()

    # calculate the total and mean travel time
    trips = df['Trip Duration'].size
    tot_travel_time = df['Trip Duration'].sum()
    avg_travel_time = df['Trip Duration'].mean()

    # display the computed statistics
    print('-'*40)
    print('\n\ttotal trips\t',colorize(str(trips),'green'))
    print('\n\ttotal duration\t',colorize(str(display_time(tot_travel_time)),'green'))
    print('\n\tmean duration\t',colorize(str(display_time(avg_travel_time)),'green'))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats\n')
    start_time_1 = time.time()

    print('\n\t'+colorize('Type ','yellow')+'    \t'+colorize('count','green'))
    print('-'*40)

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    for i in range(user_types.size):
        print('\n\t{}\t{}'.format(user_types.index[i],user_types.values[i]))

    print('\n\t'+colorize('Gender','yellow')+'    \t'+colorize('count','green'))
    print('-'*40)

    # Display counts of gender if applicable
    if 'Gender' in df.columns:
        gender_types = df['Gender'].value_counts()
        for i in range(gender_types.size):
            print('\n\t{}      \t{}'.format(gender_types.index[i],gender_types.values[i]))

    print("\nThis took %s seconds." % (time.time() - start_time_1))


    # Display earliest, most recent, and most common year of birth if applicable
    if 'Birth Year' in df.columns:

        key_press()
        start_time_2 = time.time()
        print('\n\t'+colorize('Birth of year statistics','green'))
        print('-'*40)
        earliest_birth_yr = int(df['Birth Year'].min())
        most_recent_birth_yr = int(df['Birth Year'].max())
        common_birth_yr = int(df['Birth Year'].mode()[0])
        print('\n\tearliest\t',colorize(str(earliest_birth_yr),'green'))
        print('\n\tmost recent\t',colorize(str(most_recent_birth_yr),'green'))
        print('\n\tcommon     \t',colorize(str(common_birth_yr),'green'))
        print("\nThis took %s seconds." % (time.time() - start_time_2))

    print('-'*40)

def display_records(df):
    """Displays the records in the data file."""

    print('\nWould you like to see the records (raw data) in the data?')
    print('\nPlease, enter '+colorize('yes','yellow')+' to display the first five records or any key to skip the visualization.')
    choice = input('\n'+colorize('>> ','yellow')).lower()
    row = 0

    while True:
        if choice !='yes':
            break
        else:
            #print(df.iloc[row:row + 5])
            records = df.iloc[row:row +5]
            print('\n\tTrip Information')
            print('-'*60)
            print(records[['Start Time','End Time','Trip Duration']])
            print('\nPress enter to display the next two columns about the Station information')
            input('\n>> ')
            os.system('clear')
            print('\n\tStation Information')
            print('-'*70)
            print(records[['Start Station','End Station']])
            print('\nPress enter to display the next three columns about the User information')
            input('\n>> ')
            os.system('clear')
            print('\n\tUser Information')
            print('-'*40)
            print(records[['User Type','Gender','Birth Year']])
            row += 5
            print('\nWould you like to see more data?')
            print('\nPlease, enter '+colorize('yes','yellow')+' or any key to skip the visualization')
            choice = input('\n'+colorize('>> ','yellow')).lower()


# ============================================
#             SUPPORT FUNCTIONS
# ============================================

def getKeyByValue(dictOfElements,valueToFind):
    """
        This function get the first key from a dictionary which has the given value
        Args:
            (obj) dictOfElements - a dictionary of elements
            (obj) valueToFind - the value in the dictionary to look for the key.

        Returns:
            (obj) key - the key with a value equal to valueToFind
        Note:
            if the value is not in the dictionary this function returns null
    """
    key = None
    for id,option in dictOfElements.items():
        if option == valueToFind:
            key = id
            break
    return key



def display_time(seconds):
    """
        This function converts the number of seconds into the
        number of weeks,days,hours,minutes and seconds (wdhms format)
        Args:
            (int) seconds - the seconds to convert
        Returns:
            (str) result - a description of seconds in the wdhms format
        Note:
            if the number of seconds is less than a week, the result string
            takes into account only days, hours, minutes and seconds. The start_time
            logic applies for the other intervals.
    """

    result = []

    intervals = (
        ('weeks', 604800),  # 60 * 60 * 24 * 7
        ('days', 86400),    # 60 * 60 * 24
        ('hours', 3600),    # 60 * 60
        ('minutes', 60),
        ('seconds', 1),
        )

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:4])


def key_press():
    print('\nPress enter to continue')
    input('\n>> ')
    os.system('clear')




# ===========================================
#           FILTER DEFINITIONS
# ===========================================

# list of cities to analyze
city_options = {
    '1': 'chicago',
    '2': 'new york',
    '3': 'washington'
}

# list of months to analyze
month_options = {
    '1': 'january',
    '2': 'february',
    '3': 'march',
    '4': 'april',
    '5': 'may',
    '6': 'june',
    '7': 'all'
}

# list of week days
week_day_options ={
    '1': 'monday',
    '2': 'tuesday',
    '3': 'wednesday',
    '4': 'thursday',
    '5': 'friday',
    '6': 'saturday',
    '7': 'all'
}


# Exit program
#def exit():
#    sys.exit()


# ===========================================
#  TERMINAL WINDOW COLORS AND HEADER MESSAGE
# ===========================================

header = """
    |     |  --------    -------
    |     |  |           |      \    |   | /  -------
    |     |   -------    |      /    |   |/   |
     \   /          |     ------     |   |\   ------
      ---  ----------    |      \    |   | \  |
                         |      /    |   |  \ |
                         -------              -------
"""
colors = {
          'green': "\033[1;92m",
          'yellow':"\033[1;93m",
          'pink':"\033[1;95m"
}


def colorize(string, color):
    if not color in colors: return string
    return colors[color] + string + "\033[0;0m"


# ===========================================
#             MAIN PROGRAM
# ===========================================

# Main Program

def main():
    colorama.init()
    while True:
        # retrive city, month and day of the week to analyse
        os.system('clear')
        print(colorize(header,'yellow'))
        print(colorize('\tHello, welcome to US bikeshare explorer !','yellow'))
        key_press()
        city,month,day = get_filters()


        key_press()

        df = load_data(city, month, day)
        time_stats(df)


        key_press()

        station_stats(df)


        key_press()

        trip_duration_stats(df)


        key_press()

        user_stats(df)


        key_press()

        display_records(df)

        print('\nWould you like to restart?')
        print('\nPlease, enter '+colorize('yes','yellow')+' or any key to quit the program')
        restart = input('\n'+colorize('>> ','yellow')).lower()

        if restart != 'yes':
            print('\n'+colorize('I hope you enjoied this interactive experience !','yellow'))
            print('\n'+colorize('THANK YOU & SEE YOU SOON :)','green'))
            break




if __name__ == "__main__":
    # Launch main program
    main()
