# Nikhil Kumar G - nkumarg@stevens.edu

# GitHub Url:

https://github.com/nikhil-01a/Python-Adventure-Game

# Estimate of how many hours you spent on the project

I used the pomodoro technique just like previous assignment to estimate the time I spent on this project. With each pomodoro consisting of 50 minutes of work, over the span of last 2 weeks collectively I was able to complete 20 pomodoros which is equivalent to around 17 hours of work in my case.

# Description of how I tested the code

Commands:

1. To run testcases using test harness:

### python test.py

2. To run the program with my custom map called 'quest.map':

### python adventure.py quest.map

I made use of the skills I gained from the test harness project and customized it to fit the needs of this project. Then, I went ahead and wrote test casses for each verb.

The test harness is located in the root directory by name: 'test.py' and all the testcases are in the 'test' folder of root directory with their names in this format:
'adventure.testcase.in'
'adventure.testcase.out'

The test harness uses the '.in' files for input commands and compares the runtime output with the '.out' files stored in the 'test' folder.

To test the baseline behaviour there are test files for each verb in the 'test' folder with filenames as:

1. Go : 'adventure.Go.in' and 'adventure.Go.out'
2. Look : 'adventure.Look.in' and 'adventure.Look.out'
3. Get and Inventory : 'adventure.GetInv.in' and 'adventure.GetInv.out'
4. Quit : 'adventure.quit.in' and 'adventure.quit.out'

# Any bugs or issues you could not resolve

There are no bugs in my program.

# An example of a difficult issue or bug and how you resolved it

There were multiple bottlenecks but the most stubborn issue was to make the autograder pass all its test cases. I had to revisit my code again and again to fix whitespaces, new lines and modify certain responses.

# A list of the three extensions you’ve chosen to implement, with appropriate detail on them for the CAs to evaluate them.

The three extensions I chose are:

1. abreviations
2. help
3. drop

I have written testcases to test each extension. You will find the testcases in the 'test' folder with filenames as:

1. abreviations : 'adventure.ambig.in' and 'adventure.ambig.out'
2. help : 'adventure.help.in' and 'adventure.help.out'
3. drop : 'adventure.drop.in' and 'adventure.drop.out'

Command to run all the testcases:

### python test.py

Apart from test cases one can run the program with my map 'quest.map':

### python adventure.py quest.map

and try commands like the below for each when the program is running:

1. abreviations : 'go s' , 'go south'
2. help : 'help'
3. drop : 'drop compass' and then 'look' to see the dropped item in the room

## A new map file that uses every extension (as applicable—help doesn’t affect the map)

The new map file that i wrote is called "quest.map" and it is situated in the root directory of the project. Every extension verb works with this map without any issue. Obviously, the default verbs are applicable to this map as well.
This 'quest.map' map file has 6 rooms in it.
