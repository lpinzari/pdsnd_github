### Date created
21/10/2018

## Explore US Bikeshare Data

### Description
This project explores data related to bike share systems for three major cities in the United States - Chicago, New York City and Washington. It includes a Python script (_i.e. **bikeshare.py**_) to read and analyse data from _.csv_ files for either Washington, New York City or Chicago.

The script also creates a nice interactive menu on the CLI (_Command-Line Interface_) to allow users to choose the city and a variety of descriptive statistics for answering basic questions about the bike share system data.

Feel free to modify, update and improve it as depending on your needs and your expectations :wink: !

### Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. The _csv_ files can be downloaded from these links: [_chicago.csv_](https://drive.google.com/open?id=1GKv-PFvO3T89elSvRd7Qm0gmBXPbEd7Z), [_new york city.csv_](https://drive.google.com/open?id=1J06519Blh3GZTIJasuTZ0f85FNxWkw-O), [_washington.csv_](https://drive.google.com/open?id=1Pt4UNNHIPYzpRPNK4taygpT5EyzGoLhV) .

All three of the the data files contain the same core six columns:

* Start Time (_e.g._ 2017-01-01 00:07:57)
* End Time (_e.g._ 2017-01-01 00:20:53)
* Trip Duration ( in seconds _e.g._ 776)
* Start Station (_e.g._ Broadway & Barry Ave)
* End Station (_e.g._ Sedgwick St & North Ave)
* User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

* Gender
* Birth Year

The original files are provided by [Motivate](https://www.motivateco.com/), a bike share system provider, and can be accessed here if you would like to see them ([Chicago](https://www.divvybikes.com/system-data), [New York City](https://www.citibikenyc.com/system-data), [Washington](https://www.capitalbikeshare.com/system-data)). Some data wrangling has been performed to condense these files to the columns format indicated above.

### Questions Explored

The script answers the following questions about the bike share data.

What are:

1. Popular times of travel (_i.e._, occurs most often in the Start Time)

   * most common months
   * most common day of week
   * most common hour of day


2. Popular stations and trips

   * most common Start Station
   * most common End Station
   * most common trip from Start to End (_i.e._, most frequent combination of Start Station and End Station)


3. Trip Duration

   * total travel time
   * average travel time


4. User info

   * counts of each user type
   * counts of each gender (only available for New York city and Chicago)


### Supported Python version and libraries

To run the script, the following software requirements apply:

* Python 3, NumPy and Pandas.
* A terminal application (Terminal on Mac and Linux or Cygwin/ Git Bash on Windows)

### Usage

The following example demonstrates how to run it manually from the command line of Git Bash, but you could run it in any terminal application.

To do this, you should download the necessary project files ([_chicago.csv_](https://drive.google.com/open?id=1GKv-PFvO3T89elSvRd7Qm0gmBXPbEd7Z), [_new york city.csv_](https://drive.google.com/open?id=1J06519Blh3GZTIJasuTZ0f85FNxWkw-O), [_washington.csv_](https://drive.google.com/open?id=1Pt4UNNHIPYzpRPNK4taygpT5EyzGoLhV)) in the local directory of the script **_bikeshare.py_**, and execute the following command:

```
$ python bikeshare.py
```

### Author

Ludovico Pinzari

### License

MIT

### Credits

These are the blogs post that inspired me for this project:

* Stackoverflow:

 1. [python-function-to-convert-seconds-into-minutes-hours-and-days](https://stackoverflow.com/questions/4048651/python-function-to-convert-seconds-into-minutes-hours-and-days/4048773)

 2. [python-how-can-i-make-the-ansi-escape-codes-to-work-also-in-windows](https://stackoverflow.com/questions/12492810/python-how-can-i-make-the-ansi-escape-codes-to-work-also-in-windows)

* yassine: [writing-cool-cli-menus-with-python](https://yassine.tioual.com/index.php/2017/03/28/writing-cool-cli-menus-with-python/)

* bggofurther: [create-an-interactive-command-line-menu-using-python](https://www.bggofurther.com/2015/01/create-an-interactive-command-line-menu-using-python/)


### Acknowledgement
