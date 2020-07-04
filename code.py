import datetime
import time
import pandas as pd
import numpy as np

# A dictionary containing city name and its data file
CITY_DATA = { 'chicago': 'chicago.csv',
			  'new york city': 'new_york_city.csv',
			  'washington': 'washington.csv' }

# A dictionary highlighting all the valid months to be taken as inputs
valid_months = {'January': '1', 'February': '2', 'March': '3', 'April': '4', 'May': '5', 'June': '6'}

# A list of the valid days
Valid_days = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}

# Defining the filters function
def get_filters():
	"""This function collects the data from the user in order to access the correct data file
	Input:
	Interactive questions that the user answer
	Output:
	str city, str month, str day"""
	print("Hello! Let's explore some US bikeshare data!")
	# Getting the user input of the city
	answer = True
	while answer:
		city = input("Which city do you want to analyze? ")
		if city == 'ny' or city == 'New York' or city == 'NY':
			input_city = CITY_DATA['new york city']
			print("city is {} ".format(city))
			break
		elif city == 'wa' or city == 'WA' or city == 'Washington Dc':
			input_city = CITY_DATA['washington']
			print("city is {} ".format(city))
			break
		elif city == 'chica' or city == 'Chicago' or 'chicago':
			input_city = CITY_DATA['chicago']
			print("city is {} ".format(city))
			break
		elif city in CITY_DATA:
			answer = False
			print("You chose to view the results for {}".format(city.lower()))
			break
		elif city not in CITY_DATA:
			print("Oops, unfortunately this city isn't available")
			print("Please type a valid city")
			continue
	# Applying month filters
	while 1:
		month = input("Which month do you want to filter by? If you don't want to apply any filters, please type all. ").capitalize()
		if month.lower() == 'all':
			print("You chose to apply no filters.")
			break
		elif month not in valid_months:
			print("Oh no! Only the first half is available. Try typing another month in English!")
			#Return to start of the loop
			continue
		elif month in valid_months:
			print("You chose to view the results for the following month: {}".format(month))
			break
	# Applying day filters
	while answer:
		day = input("Which day do you want to filter by? If you don't want to apply any filters, please type all. ").capitalize()
		if day.lower() == 'all' :
			print("You chose to apply no filter")
			break
		elif day not in Valid_days:
			print('This is an invalid day. Please enter a valid day!')
			continue
		elif day in Valid_days:
			print("You chose to view the results for the following day: {}".format(day))
			break
	print('-'*40)
	return input_city, month, day

# Defining the load data function
def load_data(input_city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
    (str) city - name of the city to analyze
    (str) month - name of the month to filter by, or "all" to apply no month filter
    (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
    df - Pandas DataFrame containing city data filtered by month and day
    """
    # Reading the csv file based on user inputs
    df = pd.read_csv('{}'.format(input_city))
    # Adding some new columns to the DataFrame
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['date']= df['Start Time'].dt.date
    df['time']= df['Start Time'].dt.time
    df['month']= df['Start Time'].dt.month
    df['day']= df['Start Time'].dt.day
    df['d_name'] = df['Start Time'].dt.dayofweek
    # Reading and appling month filters if existing
    while True:
        if month == 'January' or month == 'january' or month == 'jan' or month == 'Jan' or month == '1':
            df = df[df.month.isin([1])]
            break
        elif month == 'February' or month == 'february' or month == 'feb' or month == 'Feb' or month == '2':
            df = df[df.month.isin([2])]
            break
        elif month == 'March' or month == 'march' or month == 'mar' or month == 'Mar' or month == '3':
            df = df[df.month.isin([3])]
            break
        elif month == 'April' or month == 'april' or month == 'ap' or month == 'Ap' or month == '4':
            df = df[df.month.isin([4])]
            break
        elif month == 'May' or month == 'may' or month == '5':
            df = df[df.month.isin([5])]
            break
        elif month == 'June' or month == 'june' or month == '6':
            df = df[df.month.isin([6])]
            break
        else:
            break
    # Reading and applying day filters if existing
    while True:
        if day == 'Monday' or day == 'monday' or day == 'mon' or day == 'Mon':
            df = df[df.d_name.isin([0])]
            print(df)
            break
        elif day == 'Tuesday' or day == 'tuesday' or day == 'tues' or day == 'Tues':
            df = df[df.d_name.isin([1])]
            print(df)
            break
        elif day == 'Wednesday' or day == 'wednesday' or day == 'wed' or day == 'Wed':
            df = df[df.d_name.isin([2])]
            print(df)
            break
        elif day == 'Thursday' or day == 'thursday' or day == 'thurs' or day == 'Thurs':
            df = df[df.d_name.isin([3])]
            print(df)
            break
        elif day == 'Friday' or day == 'friday' or day == 'fri' or day == 'Fri':
            df = df[df.d_name.isin([4])]
            print(df)
            break
        elif day == 'Saturday' or day == 'saturday' or day == 'sat' or day == 'Sat':
            df = df[df.d_name.isin([5])]
            print(df)
            break
        elif day == 'Sunday' or day == 'sunday' or day == 'sun' or day == 'Sun':
            df = df[df.d_name.isin([6])]
            print(df)
            break
        else:
            print(df)
            break
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # Display the most common month
    common_month= df['month'].mode()[0]
    print("The most common month is: \n" , common_month)
    # Display the most common day of week
    common_day= df['day'].mode()[0]
    print("The most common day is: \n", common_day)
    # Display the most common start hour
    df['hour']= df['Start Time'].dt.hour
    common_hour= df['hour'].mode()[0]
    print('The most common hour is: \n', common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    start_station= df['Start Station'].value_counts()
    common_start_station= df['Start Station'].mode()[0]
    print('The most common start station is: \n', common_start_station)
    # display most commonly used end station
    end_station= df['End Station'].value_counts()
    common_end_station= df['End Station'].mode()[0]
    print('The most common end station is: \n', common_end_station)
    # display most frequent combination of start station and end station trip
    df['popular_lines'] = df['Start Station'] + ' to ' + df['End Station']
    common_popular_lines = df['popular_lines'].mode()[0]
    print('The most common popular line is: \n', common_popular_lines)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    total_travel_time= df['Trip Duration'].sum()
    print('The total travel time is: \n', total_travel_time)
    # display mean travel time
    mean_travel_time= df['Trip Duration'].mean()
    print('The average travel time is: \n', mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    user_counts= df['User Type'].value_counts()
    print('Here is the user counts: \n', user_counts)
    # Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('Here is the gender count: \n', gender)
    else:
        print("Ops, no gender information available in this city.")
    # Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest_year_of_birth = df['Birth_Year'].min()
        print('The earlist year of birth is: \n', earliest_year_of_birth)
        recent_year_of_birth = df['Birth_Year'].max()
        print('The recent year of birth is: \n', recent_year_of_birth)
        common_year_of_birth = df['Birth Year'].mode()[0]
        print('The most common year of birth is: \n', common_birth)
    else:
        print("Ops, no birth year information available in this city.")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """ Raw data is displayed to the user, 5 lines at a time, if they choose to view it.
    Arg:
    df
    output:
    a view of the raw data """
    # Check if the input is accepted or not
    answer = True
    while answer:
        display = input("Do you want to see the raw data? Type either 'yes' or 'no' ")
        accepted_input = ['yes', 'no']
        if display.lower() not in accepted_input:
            print("Sorry, I don't understand that! Please type 'yes' or 'no' ")
            continue
        else:
            answer = False
            break
    # Present the data if yes and exist this function if no
    head = 0
    tail = 5
    while True:
        if display.lower() == 'yes':
            print(df[df.columns[0:14]].iloc[head:tail])
            while True:
                display_more = input("Do you want to view more data? ")
                if display_more.lower() == 'yes':
                    head += 5
                    tail += 5
                    print(df[df.columns[0:14]].iloc[head:tail])
                    continue
                elif display_more.lower() == 'no':
                    print("You don't want to view more data")
                    break
            break
        elif display.lower() == 'no':
            break

def main():
    while True:
        input_city, month, day = get_filters()
        df = load_data(input_city, month, day)
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
