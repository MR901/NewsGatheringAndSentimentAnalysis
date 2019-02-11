
import argparse
from Sel__Executor import checkConfigAndTriggerSearch



BROWSER_CHOICE_MSG = """
Select from the following list of air cargo problems. You may choose more than
one by entering multiple selections separated by spaces.
"""

SEARCH_CHOICE_MSG = """
Select from the following list of search functions. You may choose more than
one by entering multiple selections separated by spaces.
"""

SEARCH_TEXT_MSG = """
type the text that you want to search. you may evenn search multiple search by just seperating the text by ";<blankspance>"
"""

INVALID_ARG_MSG = """
You must either use the -m flag to run in manual mode, or use both the -p and
-s flags to specify a list of problems and search algorithms to run. Valid
choices for each include:
"""

BROWSER = [['Chrome'],
            ['Mozilla'],
            ['EDGE']
          ]

SEARCHES = [['GoogleSearch'],
            ['GoogleNewsSearch'],
            ['GoogleScholarSearch'],
            ['GoogleImageSearch']
            ]


def manual():
    print(BROWSER_CHOICE_MSG)
    for idx, (name) in enumerate(BROWSER):
        print("    {!s}. {}".format(idx+1, name))
    b_choices = input("> ")#.split() ## only a single string will be selected not a list  seperated by <blankspace>
    print()
    
    print(SEARCH_CHOICE_MSG)
    for idx, (name) in enumerate(SEARCHES):
        print("    {!s}. {}".format(idx+1, name))
    s_choices = input("> ")#.split()
    
    print(BROWSER_CHOICE_MSG)
    searchFor = input("> ")
    searchForUpt = '["'+'", "'.join(searchFor.split('; '))+'"]'
    
    configSearch = {
        'useWhichBrowser' : [ ele for brwsr in BROWSER for ele in brwsr ][int(b_choices)-1],
        'searchUsing' : [ ele for srch in SEARCHES for ele in srch ][int(s_choices)-1],
        'searchFor' : searchForUpt,
        'outputFilePath' : '../data/output/ExtractedNews_{}.tsv'
    }
    
    checkConfigAndTriggerSearch(configSearch)
    
    
    print("\nYou can run this selection again automatically from the command " +
          "line\nwith the following command:")
    print("\n  python {} -p {} -s {} -sF {}\n".format(
        __file__, b_choices, s_choices, searchFor))



if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Solve air cargo planning problems " + 
        "using a variety of state space search methods including uninformed, greedy, " +
        "and informed heuristic search.")
    parser.add_argument('-m', '--manual', action="store_true",
                        help="Interactively select the problems and searches to run.")
    
    parser.add_argument('-b', '--browser', nargs= 1, choices=range(1, len(BROWSER)+1), type=int, metavar='', #nargs="+"
                        help="Specify the indices of the problems to solve as a list of space separated values. Choose from: {!s}".format(list(range(1, len(BROWSER)+1))),
                       default = 1)
    parser.add_argument('-s', '--searcher', nargs= 1, choices=range(1, len(SEARCHES)+1), type=int, metavar='',
                        help="Specify the indices of the search algorithms to use as a list of space separated values. Choose from: {!s}".format(list(range(1, len(SEARCHES)+1))),
                       default = 2)
    parser.add_argument('-sF', '--searchFor', metavar= '',
                        help='Type the String that you want to search')
    args = parser.parse_args()

    if args.manual:
        manual()
    elif args.browser and args.searcher and args.searchFor:
        main(list(sorted(set(args.problems))), list(sorted(set((args.searches)))))
    else:
        print()
        parser.print_help()
        print(INVALID_ARG_MSG)
        print("Problems\n-----------------")
        for idx, (name) in enumerate(BROWSER):
            print("    {!s}. {}".format(idx+1, name))
        print()
        print("Search Algorithms\n-----------------")
        for idx, (name) in enumerate(SEARCHES):
            print("    {!s}. {}".format(idx+1, name))
        print()
print("Use manual mode for interactive selection:\n\n\tpython initializeSearch.py -m\n")