# -*- coding: utf-8 -*-
"""

johnwoates
CPSC 223P-01
Thu Jan 28, 2021
joates@fullerton.edu

"""

import lists

sports_teams = [lists.football_teams, lists.baseball_teams, lists.basketball_teams]

# Print out all the school lunches on the menu, but substitute bratwurst 
# wherever you see hot dogs
# Use list comprehension. Just print the list directly so the output will
# include the brackets and quotations (['item 1', item 2' ... and so on])
schoolLunches = [substitute.replace("hot dogs","bratwurst") for substitute in lists.school_lunches]
print(schoolLunches)
# Use zip to iterate over two lists at the same time
# Print out questions and answers in a loop
# Format them: "What is your <question>? My <question> is <answer>."
for q,a in zip(lists.questions, lists.answers):
    print("What is your {}?".format(q), "My {} is {}.".format(q,a))

# Manipulate the nested lists of sports teams to print all teams from New York
# and all teams from Los Angeles.  Just print the lists directly so the output will
# include the brackets and quotations (['team 1', team 2' ... and so on])
NewYork_sportsTeams = [teams for list in sports_teams for teams in list if "New York" in teams]
print(NewYork_sportsTeams)

LA_sportsTeams = [teams for list in sports_teams for teams in list if "Los Angeles" in teams]
print(LA_sportsTeams)

