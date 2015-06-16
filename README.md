# FastNonDominatedSorting
This repository contains the delta version of the sorting function along with a global variables file

FastNonDomiantedSort.py contains a Sort Class which has a FastNonDominatedSorting Function and some other private functions:
The FastNonDominatedSort function takes a list of individuals [ID,string[2],tradesheet,per_min_mtm,parameter_list,status] And returns a list of lists, [[Front 1 individuals],[Front 2 individuals],[.....]]

Global Variables File:

a) The index of of the parameter list in the individual list is stored in the global variables file
DEFAULT: It has been set to 4 (where indexing of lists starts from 0)

b) The delta of the performance measures 1, and 2 need to be changed in the same file (as desired).

PLEASE NOTE THAT BOTH THE PERFORMANCE MEASURES SHOULD BE AT INDEX 0,1 of THE PARAMETER LIST AND SHOULD BE SUCH THAT
GREATER THE VALUE OF THE PERFORMANCE MEASURE, THE BETTER (as for example, NETPL/DD, NETPL/Trades)
