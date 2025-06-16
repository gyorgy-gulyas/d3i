# Generated from ./d3i/grammar/d3iGrammar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,52,785,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,1,0,5,0,100,8,0,10,0,12,0,103,9,0,1,0,5,
        0,106,8,0,10,0,12,0,109,9,0,1,0,1,0,1,1,5,1,114,8,1,10,1,12,1,117,
        9,1,1,1,1,1,1,1,1,2,5,2,123,8,2,10,2,12,2,126,9,2,1,2,5,2,129,8,
        2,10,2,12,2,132,9,2,1,2,5,2,135,8,2,10,2,12,2,138,9,2,1,2,1,2,1,
        2,1,2,5,2,144,8,2,10,2,12,2,147,9,2,1,2,1,2,1,3,5,3,152,8,3,10,3,
        12,3,155,9,3,1,3,1,3,1,3,1,4,1,4,1,5,5,5,163,8,5,10,5,12,5,166,9,
        5,1,5,5,5,169,8,5,10,5,12,5,172,9,5,1,5,1,5,1,5,1,5,5,5,178,8,5,
        10,5,12,5,181,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,
        6,194,8,6,1,7,5,7,197,8,7,10,7,12,7,200,9,7,1,7,5,7,203,8,7,10,7,
        12,7,206,9,7,1,7,1,7,1,7,3,7,211,8,7,1,7,1,7,5,7,215,8,7,10,7,12,
        7,218,9,7,1,7,1,7,1,8,1,8,1,8,3,8,225,8,8,1,9,5,9,228,8,9,10,9,12,
        9,231,9,9,1,9,5,9,234,8,9,10,9,12,9,237,9,9,1,9,1,9,1,9,1,9,1,10,
        5,10,244,8,10,10,10,12,10,247,9,10,1,10,5,10,250,8,10,10,10,12,10,
        253,9,10,1,10,1,10,1,10,1,10,5,10,259,8,10,10,10,12,10,262,9,10,
        1,10,1,10,1,11,1,11,1,11,3,11,269,8,11,1,12,5,12,272,8,12,10,12,
        12,12,275,9,12,1,12,5,12,278,8,12,10,12,12,12,281,9,12,1,12,1,12,
        1,12,1,12,1,13,5,13,288,8,13,10,13,12,13,291,9,13,1,13,5,13,294,
        8,13,10,13,12,13,297,9,13,1,13,1,13,1,13,3,13,302,8,13,1,13,1,13,
        5,13,306,8,13,10,13,12,13,309,9,13,1,13,1,13,1,14,1,14,1,14,3,14,
        316,8,14,1,15,5,15,319,8,15,10,15,12,15,322,9,15,1,15,5,15,325,8,
        15,10,15,12,15,328,9,15,1,15,1,15,1,15,1,15,1,16,5,16,335,8,16,10,
        16,12,16,338,9,16,1,16,5,16,341,8,16,10,16,12,16,344,9,16,1,16,1,
        16,1,16,3,16,349,8,16,1,16,1,16,5,16,353,8,16,10,16,12,16,356,9,
        16,1,16,1,16,1,17,1,17,3,17,362,8,17,1,18,5,18,365,8,18,10,18,12,
        18,368,9,18,1,18,5,18,371,8,18,10,18,12,18,374,9,18,1,18,1,18,1,
        18,1,18,1,19,5,19,381,8,19,10,19,12,19,384,9,19,1,19,5,19,387,8,
        19,10,19,12,19,390,9,19,1,19,1,19,1,19,3,19,395,8,19,1,19,1,19,5,
        19,399,8,19,10,19,12,19,402,9,19,1,19,1,19,1,20,1,20,1,20,3,20,409,
        8,20,1,21,5,21,412,8,21,10,21,12,21,415,9,21,1,21,5,21,418,8,21,
        10,21,12,21,421,9,21,1,21,1,21,1,21,1,21,1,22,5,22,428,8,22,10,22,
        12,22,431,9,22,1,22,5,22,434,8,22,10,22,12,22,437,9,22,1,22,1,22,
        1,22,1,22,5,22,443,8,22,10,22,12,22,446,9,22,1,22,1,22,1,23,1,23,
        1,23,3,23,453,8,23,1,24,3,24,456,8,24,1,24,1,24,1,25,5,25,461,8,
        25,10,25,12,25,464,9,25,1,25,5,25,467,8,25,10,25,12,25,470,9,25,
        1,25,1,25,1,25,3,25,475,8,25,1,25,1,25,5,25,479,8,25,10,25,12,25,
        482,9,25,1,25,1,25,1,26,1,26,3,26,488,8,26,1,27,5,27,491,8,27,10,
        27,12,27,494,9,27,1,27,5,27,497,8,27,10,27,12,27,500,9,27,1,27,1,
        27,1,27,1,27,1,28,5,28,507,8,28,10,28,12,28,510,9,28,1,28,5,28,513,
        8,28,10,28,12,28,516,9,28,1,28,1,28,1,28,1,28,1,28,1,29,5,29,524,
        8,29,10,29,12,29,527,9,29,1,29,5,29,530,8,29,10,29,12,29,533,9,29,
        1,29,1,29,1,29,1,29,5,29,539,8,29,10,29,12,29,542,9,29,1,29,1,29,
        1,30,1,30,1,30,1,30,3,30,550,8,30,1,31,5,31,553,8,31,10,31,12,31,
        556,9,31,1,31,5,31,559,8,31,10,31,12,31,562,9,31,1,31,1,31,1,31,
        1,31,1,31,1,31,5,31,570,8,31,10,31,12,31,573,9,31,1,31,1,31,1,32,
        1,32,1,32,1,32,3,32,581,8,32,1,33,5,33,584,8,33,10,33,12,33,587,
        9,33,1,33,5,33,590,8,33,10,33,12,33,593,9,33,1,33,1,33,1,33,3,33,
        598,8,33,1,33,1,33,5,33,602,8,33,10,33,12,33,605,9,33,1,33,1,33,
        1,33,3,33,610,8,33,1,33,1,33,5,33,614,8,33,10,33,12,33,617,9,33,
        1,34,5,34,620,8,34,10,34,12,34,623,9,34,1,34,5,34,626,8,34,10,34,
        12,34,629,9,34,1,34,1,34,1,34,1,34,1,35,5,35,636,8,35,10,35,12,35,
        639,9,35,1,35,5,35,642,8,35,10,35,12,35,645,9,35,1,35,1,35,1,36,
        5,36,650,8,36,10,36,12,36,653,9,36,1,36,5,36,656,8,36,10,36,12,36,
        659,9,36,1,36,1,36,1,36,1,36,5,36,665,8,36,10,36,12,36,668,9,36,
        1,36,1,36,1,37,1,37,1,37,3,37,675,8,37,1,38,1,38,1,38,1,38,3,38,
        681,8,38,1,39,1,39,1,40,1,40,1,40,1,40,1,40,3,40,690,8,40,1,41,1,
        41,1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,43,1,43,1,
        43,5,43,707,8,43,10,43,12,43,710,9,43,1,44,1,44,1,44,1,44,1,44,1,
        44,1,44,1,44,5,44,720,8,44,10,44,12,44,723,9,44,1,44,1,44,3,44,727,
        8,44,1,45,1,45,1,45,1,45,3,45,733,8,45,1,46,5,46,736,8,46,10,46,
        12,46,739,9,46,1,46,5,46,742,8,46,10,46,12,46,745,9,46,1,46,1,46,
        1,46,1,46,3,46,751,8,46,1,46,1,46,5,46,755,8,46,10,46,12,46,758,
        9,46,1,46,1,46,1,47,5,47,763,8,47,10,47,12,47,766,9,47,1,47,5,47,
        769,8,47,10,47,12,47,772,9,47,1,47,1,47,1,48,1,48,1,48,1,48,5,48,
        780,8,48,10,48,12,48,783,9,48,1,48,0,0,49,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,0,1,1,0,31,
        41,851,0,101,1,0,0,0,2,115,1,0,0,0,4,124,1,0,0,0,6,153,1,0,0,0,8,
        159,1,0,0,0,10,164,1,0,0,0,12,193,1,0,0,0,14,198,1,0,0,0,16,224,
        1,0,0,0,18,229,1,0,0,0,20,245,1,0,0,0,22,268,1,0,0,0,24,273,1,0,
        0,0,26,289,1,0,0,0,28,315,1,0,0,0,30,320,1,0,0,0,32,336,1,0,0,0,
        34,361,1,0,0,0,36,366,1,0,0,0,38,382,1,0,0,0,40,408,1,0,0,0,42,413,
        1,0,0,0,44,429,1,0,0,0,46,452,1,0,0,0,48,455,1,0,0,0,50,462,1,0,
        0,0,52,487,1,0,0,0,54,492,1,0,0,0,56,508,1,0,0,0,58,525,1,0,0,0,
        60,549,1,0,0,0,62,554,1,0,0,0,64,580,1,0,0,0,66,585,1,0,0,0,68,621,
        1,0,0,0,70,637,1,0,0,0,72,651,1,0,0,0,74,674,1,0,0,0,76,680,1,0,
        0,0,78,682,1,0,0,0,80,689,1,0,0,0,82,691,1,0,0,0,84,696,1,0,0,0,
        86,703,1,0,0,0,88,726,1,0,0,0,90,732,1,0,0,0,92,737,1,0,0,0,94,764,
        1,0,0,0,96,775,1,0,0,0,98,100,3,2,1,0,99,98,1,0,0,0,100,103,1,0,
        0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,107,1,0,0,0,103,101,1,0,0,
        0,104,106,3,4,2,0,105,104,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,
        0,107,108,1,0,0,0,108,110,1,0,0,0,109,107,1,0,0,0,110,111,5,0,0,
        1,111,1,1,0,0,0,112,114,5,50,0,0,113,112,1,0,0,0,114,117,1,0,0,0,
        115,113,1,0,0,0,115,116,1,0,0,0,116,118,1,0,0,0,117,115,1,0,0,0,
        118,119,5,21,0,0,119,120,3,86,43,0,120,3,1,0,0,0,121,123,3,6,3,0,
        122,121,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,
        125,130,1,0,0,0,126,124,1,0,0,0,127,129,5,50,0,0,128,127,1,0,0,0,
        129,132,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,136,1,0,0,0,
        132,130,1,0,0,0,133,135,3,88,44,0,134,133,1,0,0,0,135,138,1,0,0,
        0,136,134,1,0,0,0,136,137,1,0,0,0,137,139,1,0,0,0,138,136,1,0,0,
        0,139,140,5,17,0,0,140,141,5,48,0,0,141,145,5,6,0,0,142,144,3,8,
        4,0,143,142,1,0,0,0,144,147,1,0,0,0,145,143,1,0,0,0,145,146,1,0,
        0,0,146,148,1,0,0,0,147,145,1,0,0,0,148,149,5,7,0,0,149,5,1,0,0,
        0,150,152,5,50,0,0,151,150,1,0,0,0,152,155,1,0,0,0,153,151,1,0,0,
        0,153,154,1,0,0,0,154,156,1,0,0,0,155,153,1,0,0,0,156,157,5,48,0,
        0,157,158,3,86,43,0,158,7,1,0,0,0,159,160,3,10,5,0,160,9,1,0,0,0,
        161,163,5,50,0,0,162,161,1,0,0,0,163,166,1,0,0,0,164,162,1,0,0,0,
        164,165,1,0,0,0,165,170,1,0,0,0,166,164,1,0,0,0,167,169,3,88,44,
        0,168,167,1,0,0,0,169,172,1,0,0,0,170,168,1,0,0,0,170,171,1,0,0,
        0,171,173,1,0,0,0,172,170,1,0,0,0,173,174,5,15,0,0,174,175,5,48,
        0,0,175,179,5,6,0,0,176,178,3,12,6,0,177,176,1,0,0,0,178,181,1,0,
        0,0,179,177,1,0,0,0,179,180,1,0,0,0,180,182,1,0,0,0,181,179,1,0,
        0,0,182,183,5,7,0,0,183,11,1,0,0,0,184,194,3,92,46,0,185,194,3,14,
        7,0,186,194,3,26,13,0,187,194,3,44,22,0,188,194,3,50,25,0,189,194,
        3,56,28,0,190,194,3,72,36,0,191,194,3,58,29,0,192,194,3,62,31,0,
        193,184,1,0,0,0,193,185,1,0,0,0,193,186,1,0,0,0,193,187,1,0,0,0,
        193,188,1,0,0,0,193,189,1,0,0,0,193,190,1,0,0,0,193,191,1,0,0,0,
        193,192,1,0,0,0,194,13,1,0,0,0,195,197,5,50,0,0,196,195,1,0,0,0,
        197,200,1,0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,204,1,0,0,0,
        200,198,1,0,0,0,201,203,3,88,44,0,202,201,1,0,0,0,203,206,1,0,0,
        0,204,202,1,0,0,0,204,205,1,0,0,0,205,207,1,0,0,0,206,204,1,0,0,
        0,207,208,5,25,0,0,208,210,5,48,0,0,209,211,3,96,48,0,210,209,1,
        0,0,0,210,211,1,0,0,0,211,212,1,0,0,0,212,216,5,6,0,0,213,215,3,
        16,8,0,214,213,1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,216,217,1,
        0,0,0,217,219,1,0,0,0,218,216,1,0,0,0,219,220,5,7,0,0,220,15,1,0,
        0,0,221,225,3,18,9,0,222,225,3,92,46,0,223,225,3,14,7,0,224,221,
        1,0,0,0,224,222,1,0,0,0,224,223,1,0,0,0,225,17,1,0,0,0,226,228,5,
        50,0,0,227,226,1,0,0,0,228,231,1,0,0,0,229,227,1,0,0,0,229,230,1,
        0,0,0,230,235,1,0,0,0,231,229,1,0,0,0,232,234,3,88,44,0,233,232,
        1,0,0,0,234,237,1,0,0,0,235,233,1,0,0,0,235,236,1,0,0,0,236,238,
        1,0,0,0,237,235,1,0,0,0,238,239,5,48,0,0,239,240,5,3,0,0,240,241,
        3,76,38,0,241,19,1,0,0,0,242,244,5,50,0,0,243,242,1,0,0,0,244,247,
        1,0,0,0,245,243,1,0,0,0,245,246,1,0,0,0,246,251,1,0,0,0,247,245,
        1,0,0,0,248,250,3,88,44,0,249,248,1,0,0,0,250,253,1,0,0,0,251,249,
        1,0,0,0,251,252,1,0,0,0,252,254,1,0,0,0,253,251,1,0,0,0,254,255,
        5,26,0,0,255,256,5,48,0,0,256,260,5,6,0,0,257,259,3,22,11,0,258,
        257,1,0,0,0,259,262,1,0,0,0,260,258,1,0,0,0,260,261,1,0,0,0,261,
        263,1,0,0,0,262,260,1,0,0,0,263,264,5,7,0,0,264,21,1,0,0,0,265,269,
        3,24,12,0,266,269,3,92,46,0,267,269,3,20,10,0,268,265,1,0,0,0,268,
        266,1,0,0,0,268,267,1,0,0,0,269,23,1,0,0,0,270,272,5,50,0,0,271,
        270,1,0,0,0,272,275,1,0,0,0,273,271,1,0,0,0,273,274,1,0,0,0,274,
        279,1,0,0,0,275,273,1,0,0,0,276,278,3,88,44,0,277,276,1,0,0,0,278,
        281,1,0,0,0,279,277,1,0,0,0,279,280,1,0,0,0,280,282,1,0,0,0,281,
        279,1,0,0,0,282,283,5,48,0,0,283,284,5,3,0,0,284,285,3,76,38,0,285,
        25,1,0,0,0,286,288,5,50,0,0,287,286,1,0,0,0,288,291,1,0,0,0,289,
        287,1,0,0,0,289,290,1,0,0,0,290,295,1,0,0,0,291,289,1,0,0,0,292,
        294,3,88,44,0,293,292,1,0,0,0,294,297,1,0,0,0,295,293,1,0,0,0,295,
        296,1,0,0,0,296,298,1,0,0,0,297,295,1,0,0,0,298,299,5,16,0,0,299,
        301,5,48,0,0,300,302,3,96,48,0,301,300,1,0,0,0,301,302,1,0,0,0,302,
        303,1,0,0,0,303,307,5,6,0,0,304,306,3,28,14,0,305,304,1,0,0,0,306,
        309,1,0,0,0,307,305,1,0,0,0,307,308,1,0,0,0,308,310,1,0,0,0,309,
        307,1,0,0,0,310,311,5,7,0,0,311,27,1,0,0,0,312,316,3,30,15,0,313,
        316,3,92,46,0,314,316,3,14,7,0,315,312,1,0,0,0,315,313,1,0,0,0,315,
        314,1,0,0,0,316,29,1,0,0,0,317,319,5,50,0,0,318,317,1,0,0,0,319,
        322,1,0,0,0,320,318,1,0,0,0,320,321,1,0,0,0,321,326,1,0,0,0,322,
        320,1,0,0,0,323,325,3,88,44,0,324,323,1,0,0,0,325,328,1,0,0,0,326,
        324,1,0,0,0,326,327,1,0,0,0,327,329,1,0,0,0,328,326,1,0,0,0,329,
        330,5,48,0,0,330,331,5,3,0,0,331,332,3,76,38,0,332,31,1,0,0,0,333,
        335,5,50,0,0,334,333,1,0,0,0,335,338,1,0,0,0,336,334,1,0,0,0,336,
        337,1,0,0,0,337,342,1,0,0,0,338,336,1,0,0,0,339,341,3,88,44,0,340,
        339,1,0,0,0,341,344,1,0,0,0,342,340,1,0,0,0,342,343,1,0,0,0,343,
        345,1,0,0,0,344,342,1,0,0,0,345,346,5,20,0,0,346,348,5,48,0,0,347,
        349,3,96,48,0,348,347,1,0,0,0,348,349,1,0,0,0,349,350,1,0,0,0,350,
        354,5,6,0,0,351,353,3,34,17,0,352,351,1,0,0,0,353,356,1,0,0,0,354,
        352,1,0,0,0,354,355,1,0,0,0,355,357,1,0,0,0,356,354,1,0,0,0,357,
        358,5,7,0,0,358,33,1,0,0,0,359,362,3,36,18,0,360,362,3,92,46,0,361,
        359,1,0,0,0,361,360,1,0,0,0,362,35,1,0,0,0,363,365,5,50,0,0,364,
        363,1,0,0,0,365,368,1,0,0,0,366,364,1,0,0,0,366,367,1,0,0,0,367,
        372,1,0,0,0,368,366,1,0,0,0,369,371,3,88,44,0,370,369,1,0,0,0,371,
        374,1,0,0,0,372,370,1,0,0,0,372,373,1,0,0,0,373,375,1,0,0,0,374,
        372,1,0,0,0,375,376,5,48,0,0,376,377,5,3,0,0,377,378,3,76,38,0,378,
        37,1,0,0,0,379,381,5,50,0,0,380,379,1,0,0,0,381,384,1,0,0,0,382,
        380,1,0,0,0,382,383,1,0,0,0,383,388,1,0,0,0,384,382,1,0,0,0,385,
        387,3,88,44,0,386,385,1,0,0,0,387,390,1,0,0,0,388,386,1,0,0,0,388,
        389,1,0,0,0,389,391,1,0,0,0,390,388,1,0,0,0,391,392,5,18,0,0,392,
        394,5,48,0,0,393,395,3,96,48,0,394,393,1,0,0,0,394,395,1,0,0,0,395,
        396,1,0,0,0,396,400,5,6,0,0,397,399,3,40,20,0,398,397,1,0,0,0,399,
        402,1,0,0,0,400,398,1,0,0,0,400,401,1,0,0,0,401,403,1,0,0,0,402,
        400,1,0,0,0,403,404,5,7,0,0,404,39,1,0,0,0,405,409,3,42,21,0,406,
        409,3,92,46,0,407,409,3,14,7,0,408,405,1,0,0,0,408,406,1,0,0,0,408,
        407,1,0,0,0,409,41,1,0,0,0,410,412,5,50,0,0,411,410,1,0,0,0,412,
        415,1,0,0,0,413,411,1,0,0,0,413,414,1,0,0,0,414,419,1,0,0,0,415,
        413,1,0,0,0,416,418,3,88,44,0,417,416,1,0,0,0,418,421,1,0,0,0,419,
        417,1,0,0,0,419,420,1,0,0,0,420,422,1,0,0,0,421,419,1,0,0,0,422,
        423,5,48,0,0,423,424,5,3,0,0,424,425,3,76,38,0,425,43,1,0,0,0,426,
        428,5,50,0,0,427,426,1,0,0,0,428,431,1,0,0,0,429,427,1,0,0,0,429,
        430,1,0,0,0,430,435,1,0,0,0,431,429,1,0,0,0,432,434,3,88,44,0,433,
        432,1,0,0,0,434,437,1,0,0,0,435,433,1,0,0,0,435,436,1,0,0,0,436,
        438,1,0,0,0,437,435,1,0,0,0,438,439,5,14,0,0,439,440,5,48,0,0,440,
        444,5,6,0,0,441,443,3,46,23,0,442,441,1,0,0,0,443,446,1,0,0,0,444,
        442,1,0,0,0,444,445,1,0,0,0,445,447,1,0,0,0,446,444,1,0,0,0,447,
        448,5,7,0,0,448,45,1,0,0,0,449,453,3,48,24,0,450,453,3,92,46,0,451,
        453,3,14,7,0,452,449,1,0,0,0,452,450,1,0,0,0,452,451,1,0,0,0,453,
        47,1,0,0,0,454,456,5,28,0,0,455,454,1,0,0,0,455,456,1,0,0,0,456,
        457,1,0,0,0,457,458,3,38,19,0,458,49,1,0,0,0,459,461,5,50,0,0,460,
        459,1,0,0,0,461,464,1,0,0,0,462,460,1,0,0,0,462,463,1,0,0,0,463,
        468,1,0,0,0,464,462,1,0,0,0,465,467,3,88,44,0,466,465,1,0,0,0,467,
        470,1,0,0,0,468,466,1,0,0,0,468,469,1,0,0,0,469,471,1,0,0,0,470,
        468,1,0,0,0,471,472,5,27,0,0,472,474,5,48,0,0,473,475,3,96,48,0,
        474,473,1,0,0,0,474,475,1,0,0,0,475,476,1,0,0,0,476,480,5,6,0,0,
        477,479,3,52,26,0,478,477,1,0,0,0,479,482,1,0,0,0,480,478,1,0,0,
        0,480,481,1,0,0,0,481,483,1,0,0,0,482,480,1,0,0,0,483,484,5,7,0,
        0,484,51,1,0,0,0,485,488,3,54,27,0,486,488,3,92,46,0,487,485,1,0,
        0,0,487,486,1,0,0,0,488,53,1,0,0,0,489,491,5,50,0,0,490,489,1,0,
        0,0,491,494,1,0,0,0,492,490,1,0,0,0,492,493,1,0,0,0,493,498,1,0,
        0,0,494,492,1,0,0,0,495,497,3,88,44,0,496,495,1,0,0,0,497,500,1,
        0,0,0,498,496,1,0,0,0,498,499,1,0,0,0,499,501,1,0,0,0,500,498,1,
        0,0,0,501,502,5,48,0,0,502,503,5,3,0,0,503,504,3,76,38,0,504,55,
        1,0,0,0,505,507,5,50,0,0,506,505,1,0,0,0,507,510,1,0,0,0,508,506,
        1,0,0,0,508,509,1,0,0,0,509,514,1,0,0,0,510,508,1,0,0,0,511,513,
        3,88,44,0,512,511,1,0,0,0,513,516,1,0,0,0,514,512,1,0,0,0,514,515,
        1,0,0,0,515,517,1,0,0,0,516,514,1,0,0,0,517,518,5,23,0,0,518,519,
        5,48,0,0,519,520,5,3,0,0,520,521,5,48,0,0,521,57,1,0,0,0,522,524,
        5,50,0,0,523,522,1,0,0,0,524,527,1,0,0,0,525,523,1,0,0,0,525,526,
        1,0,0,0,526,531,1,0,0,0,527,525,1,0,0,0,528,530,3,88,44,0,529,528,
        1,0,0,0,530,533,1,0,0,0,531,529,1,0,0,0,531,532,1,0,0,0,532,534,
        1,0,0,0,533,531,1,0,0,0,534,535,5,24,0,0,535,536,5,48,0,0,536,540,
        5,6,0,0,537,539,3,60,30,0,538,537,1,0,0,0,539,542,1,0,0,0,540,538,
        1,0,0,0,540,541,1,0,0,0,541,543,1,0,0,0,542,540,1,0,0,0,543,544,
        5,7,0,0,544,59,1,0,0,0,545,550,3,66,33,0,546,550,3,92,46,0,547,550,
        3,14,7,0,548,550,3,32,16,0,549,545,1,0,0,0,549,546,1,0,0,0,549,547,
        1,0,0,0,549,548,1,0,0,0,550,61,1,0,0,0,551,553,5,50,0,0,552,551,
        1,0,0,0,553,556,1,0,0,0,554,552,1,0,0,0,554,555,1,0,0,0,555,560,
        1,0,0,0,556,554,1,0,0,0,557,559,3,88,44,0,558,557,1,0,0,0,559,562,
        1,0,0,0,560,558,1,0,0,0,560,561,1,0,0,0,561,563,1,0,0,0,562,560,
        1,0,0,0,563,564,5,22,0,0,564,565,5,48,0,0,565,566,5,30,0,0,566,567,
        5,45,0,0,567,571,5,6,0,0,568,570,3,64,32,0,569,568,1,0,0,0,570,573,
        1,0,0,0,571,569,1,0,0,0,571,572,1,0,0,0,572,574,1,0,0,0,573,571,
        1,0,0,0,574,575,5,7,0,0,575,63,1,0,0,0,576,581,3,66,33,0,577,581,
        3,92,46,0,578,581,3,20,10,0,579,581,3,32,16,0,580,576,1,0,0,0,580,
        577,1,0,0,0,580,578,1,0,0,0,580,579,1,0,0,0,581,65,1,0,0,0,582,584,
        5,50,0,0,583,582,1,0,0,0,584,587,1,0,0,0,585,583,1,0,0,0,585,586,
        1,0,0,0,586,591,1,0,0,0,587,585,1,0,0,0,588,590,3,88,44,0,589,588,
        1,0,0,0,590,593,1,0,0,0,591,589,1,0,0,0,591,592,1,0,0,0,592,594,
        1,0,0,0,593,591,1,0,0,0,594,595,5,48,0,0,595,597,5,4,0,0,596,598,
        3,68,34,0,597,596,1,0,0,0,597,598,1,0,0,0,598,603,1,0,0,0,599,600,
        5,2,0,0,600,602,3,68,34,0,601,599,1,0,0,0,602,605,1,0,0,0,603,601,
        1,0,0,0,603,604,1,0,0,0,604,606,1,0,0,0,605,603,1,0,0,0,606,609,
        5,5,0,0,607,608,5,3,0,0,608,610,3,70,35,0,609,607,1,0,0,0,609,610,
        1,0,0,0,610,615,1,0,0,0,611,612,5,12,0,0,612,614,3,70,35,0,613,611,
        1,0,0,0,614,617,1,0,0,0,615,613,1,0,0,0,615,616,1,0,0,0,616,67,1,
        0,0,0,617,615,1,0,0,0,618,620,5,50,0,0,619,618,1,0,0,0,620,623,1,
        0,0,0,621,619,1,0,0,0,621,622,1,0,0,0,622,627,1,0,0,0,623,621,1,
        0,0,0,624,626,3,88,44,0,625,624,1,0,0,0,626,629,1,0,0,0,627,625,
        1,0,0,0,627,628,1,0,0,0,628,630,1,0,0,0,629,627,1,0,0,0,630,631,
        5,48,0,0,631,632,5,3,0,0,632,633,3,76,38,0,633,69,1,0,0,0,634,636,
        5,50,0,0,635,634,1,0,0,0,636,639,1,0,0,0,637,635,1,0,0,0,637,638,
        1,0,0,0,638,643,1,0,0,0,639,637,1,0,0,0,640,642,3,88,44,0,641,640,
        1,0,0,0,642,645,1,0,0,0,643,641,1,0,0,0,643,644,1,0,0,0,644,646,
        1,0,0,0,645,643,1,0,0,0,646,647,3,76,38,0,647,71,1,0,0,0,648,650,
        5,50,0,0,649,648,1,0,0,0,650,653,1,0,0,0,651,649,1,0,0,0,651,652,
        1,0,0,0,652,657,1,0,0,0,653,651,1,0,0,0,654,656,3,88,44,0,655,654,
        1,0,0,0,656,659,1,0,0,0,657,655,1,0,0,0,657,658,1,0,0,0,658,660,
        1,0,0,0,659,657,1,0,0,0,660,661,5,13,0,0,661,662,5,48,0,0,662,666,
        5,6,0,0,663,665,3,74,37,0,664,663,1,0,0,0,665,668,1,0,0,0,666,664,
        1,0,0,0,666,667,1,0,0,0,667,669,1,0,0,0,668,666,1,0,0,0,669,670,
        5,7,0,0,670,73,1,0,0,0,671,675,3,92,46,0,672,675,3,14,7,0,673,675,
        3,66,33,0,674,671,1,0,0,0,674,672,1,0,0,0,674,673,1,0,0,0,675,75,
        1,0,0,0,676,681,3,78,39,0,677,681,3,80,40,0,678,681,3,82,41,0,679,
        681,3,84,42,0,680,676,1,0,0,0,680,677,1,0,0,0,680,678,1,0,0,0,680,
        679,1,0,0,0,681,77,1,0,0,0,682,683,7,0,0,0,683,79,1,0,0,0,684,690,
        3,86,43,0,685,686,5,44,0,0,686,687,5,8,0,0,687,688,5,47,0,0,688,
        690,5,9,0,0,689,684,1,0,0,0,689,685,1,0,0,0,690,81,1,0,0,0,691,692,
        5,42,0,0,692,693,5,8,0,0,693,694,3,76,38,0,694,695,5,9,0,0,695,83,
        1,0,0,0,696,697,5,43,0,0,697,698,5,8,0,0,698,699,3,76,38,0,699,700,
        5,2,0,0,700,701,3,76,38,0,701,702,5,9,0,0,702,85,1,0,0,0,703,708,
        5,48,0,0,704,705,5,1,0,0,705,707,5,48,0,0,706,704,1,0,0,0,707,710,
        1,0,0,0,708,706,1,0,0,0,708,709,1,0,0,0,709,87,1,0,0,0,710,708,1,
        0,0,0,711,712,5,10,0,0,712,727,5,48,0,0,713,714,5,10,0,0,714,715,
        5,48,0,0,715,716,5,4,0,0,716,721,3,90,45,0,717,718,5,2,0,0,718,720,
        3,90,45,0,719,717,1,0,0,0,720,723,1,0,0,0,721,719,1,0,0,0,721,722,
        1,0,0,0,722,724,1,0,0,0,723,721,1,0,0,0,724,725,5,5,0,0,725,727,
        1,0,0,0,726,711,1,0,0,0,726,713,1,0,0,0,727,89,1,0,0,0,728,733,3,
        86,43,0,729,733,5,45,0,0,730,733,5,46,0,0,731,733,5,47,0,0,732,728,
        1,0,0,0,732,729,1,0,0,0,732,730,1,0,0,0,732,731,1,0,0,0,733,91,1,
        0,0,0,734,736,5,50,0,0,735,734,1,0,0,0,736,739,1,0,0,0,737,735,1,
        0,0,0,737,738,1,0,0,0,738,743,1,0,0,0,739,737,1,0,0,0,740,742,3,
        88,44,0,741,740,1,0,0,0,742,745,1,0,0,0,743,741,1,0,0,0,743,744,
        1,0,0,0,744,746,1,0,0,0,745,743,1,0,0,0,746,747,5,19,0,0,747,748,
        5,48,0,0,748,750,5,6,0,0,749,751,3,94,47,0,750,749,1,0,0,0,750,751,
        1,0,0,0,751,756,1,0,0,0,752,753,5,2,0,0,753,755,3,94,47,0,754,752,
        1,0,0,0,755,758,1,0,0,0,756,754,1,0,0,0,756,757,1,0,0,0,757,759,
        1,0,0,0,758,756,1,0,0,0,759,760,5,7,0,0,760,93,1,0,0,0,761,763,5,
        50,0,0,762,761,1,0,0,0,763,766,1,0,0,0,764,762,1,0,0,0,764,765,1,
        0,0,0,765,770,1,0,0,0,766,764,1,0,0,0,767,769,3,88,44,0,768,767,
        1,0,0,0,769,772,1,0,0,0,770,768,1,0,0,0,770,771,1,0,0,0,771,773,
        1,0,0,0,772,770,1,0,0,0,773,774,5,48,0,0,774,95,1,0,0,0,775,776,
        5,29,0,0,776,781,3,86,43,0,777,778,5,2,0,0,778,780,3,86,43,0,779,
        777,1,0,0,0,780,783,1,0,0,0,781,779,1,0,0,0,781,782,1,0,0,0,782,
        97,1,0,0,0,783,781,1,0,0,0,95,101,107,115,124,130,136,145,153,164,
        170,179,193,198,204,210,216,224,229,235,245,251,260,268,273,279,
        289,295,301,307,315,320,326,336,342,348,354,361,366,372,382,388,
        394,400,408,413,419,429,435,444,452,455,462,468,474,480,487,492,
        498,508,514,525,531,540,549,554,560,571,580,585,591,597,603,609,
        615,621,627,637,643,651,657,666,674,680,689,708,721,726,732,737,
        743,750,756,764,770,781
    ]

class d3iGrammar ( Parser ):

    grammarFileName = "d3iGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "','", "':'", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "'@'", "'=>'", "'|'", "'acl'", 
                     "'aggregate'", "'context'", "'composite'", "'domain'", 
                     "'entity'", "'enum'", "'event'", "'import'", "'interface'", 
                     "'repository'", "'service'", "'valueobject'", "'dto'", 
                     "'view'", "'root'", "'inherits'", "'version'", "'integer'", 
                     "'number'", "'float'", "'date'", "'time'", "'dateTime'", 
                     "'string'", "'boolean'", "'bytes'", "'stream'", "'any'", 
                     "'list'", "'map'", "'external'" ]

    symbolicNames = [ "<INVALID>", "DOT", "COMMA", "SEMI", "LPAREN", "RPAREN", 
                      "LCURLY", "RCURLY", "LBARCKET", "RBRACKET", "AT", 
                      "ARROW", "PIPE", "ACL", "AGGREGATE", "CONTEXT", "COMPOSITE", 
                      "DOMAIN", "ENTITY", "ENUM", "EVENT", "IMPORT", "INTERFACE", 
                      "REPOSITORY", "SERVICE", "VALUEOBJECT", "DTO", "VIEW", 
                      "ROOT", "INHERITS", "VERSION", "INTEGER", "NUMBER", 
                      "FLOAT", "DATE", "TIME", "DATETIME", "STRING", "BOOLEAN", 
                      "BYTES", "STREAM", "ANY", "LIST", "MAP", "EXTERNAL", 
                      "INTEGER_CONSTANS", "NUMBER_CONSTANS", "STRING_LITERAL", 
                      "IDENTIFIER", "WS", "DOCUMENT_LINE", "LINE_COMMENT", 
                      "BLOCK_COMMENT" ]

    RULE_d3 = 0
    RULE_import_rule = 1
    RULE_domain = 2
    RULE_directive = 3
    RULE_domain_element = 4
    RULE_context = 5
    RULE_context_element = 6
    RULE_value_object = 7
    RULE_value_object_element = 8
    RULE_value_object_member = 9
    RULE_dto = 10
    RULE_dto_element = 11
    RULE_dto_member = 12
    RULE_composite = 13
    RULE_composite_element = 14
    RULE_composite_member = 15
    RULE_event = 16
    RULE_event_element = 17
    RULE_event_member = 18
    RULE_entity = 19
    RULE_entity_element = 20
    RULE_entity_member = 21
    RULE_aggregate = 22
    RULE_aggregate_element = 23
    RULE_aggregate_entity = 24
    RULE_view = 25
    RULE_view_element = 26
    RULE_view_member = 27
    RULE_repository = 28
    RULE_service = 29
    RULE_service_element = 30
    RULE_interface = 31
    RULE_interface_element = 32
    RULE_operation = 33
    RULE_operation_param = 34
    RULE_operation_return = 35
    RULE_acl = 36
    RULE_acl_element = 37
    RULE_type = 38
    RULE_primitive_type = 39
    RULE_reference_type = 40
    RULE_list_type = 41
    RULE_map_type = 42
    RULE_qualifiedName = 43
    RULE_decorator = 44
    RULE_decorator_param = 45
    RULE_enum = 46
    RULE_enum_element = 47
    RULE_inherits = 48

    ruleNames =  [ "d3", "import_rule", "domain", "directive", "domain_element", 
                   "context", "context_element", "value_object", "value_object_element", 
                   "value_object_member", "dto", "dto_element", "dto_member", 
                   "composite", "composite_element", "composite_member", 
                   "event", "event_element", "event_member", "entity", "entity_element", 
                   "entity_member", "aggregate", "aggregate_element", "aggregate_entity", 
                   "view", "view_element", "view_member", "repository", 
                   "service", "service_element", "interface", "interface_element", 
                   "operation", "operation_param", "operation_return", "acl", 
                   "acl_element", "type", "primitive_type", "reference_type", 
                   "list_type", "map_type", "qualifiedName", "decorator", 
                   "decorator_param", "enum", "enum_element", "inherits" ]

    EOF = Token.EOF
    DOT=1
    COMMA=2
    SEMI=3
    LPAREN=4
    RPAREN=5
    LCURLY=6
    RCURLY=7
    LBARCKET=8
    RBRACKET=9
    AT=10
    ARROW=11
    PIPE=12
    ACL=13
    AGGREGATE=14
    CONTEXT=15
    COMPOSITE=16
    DOMAIN=17
    ENTITY=18
    ENUM=19
    EVENT=20
    IMPORT=21
    INTERFACE=22
    REPOSITORY=23
    SERVICE=24
    VALUEOBJECT=25
    DTO=26
    VIEW=27
    ROOT=28
    INHERITS=29
    VERSION=30
    INTEGER=31
    NUMBER=32
    FLOAT=33
    DATE=34
    TIME=35
    DATETIME=36
    STRING=37
    BOOLEAN=38
    BYTES=39
    STREAM=40
    ANY=41
    LIST=42
    MAP=43
    EXTERNAL=44
    INTEGER_CONSTANS=45
    NUMBER_CONSTANS=46
    STRING_LITERAL=47
    IDENTIFIER=48
    WS=49
    DOCUMENT_LINE=50
    LINE_COMMENT=51
    BLOCK_COMMENT=52

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class D3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(d3iGrammar.EOF, 0)

        def import_rule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.Import_ruleContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.Import_ruleContext,i)


        def domain(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DomainContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DomainContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_d3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterD3" ):
                listener.enterD3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitD3" ):
                listener.exitD3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitD3" ):
                return visitor.visitD3(self)
            else:
                return visitor.visitChildren(self)




    def d3(self):

        localctx = d3iGrammar.D3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_d3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 98
                    self.import_rule() 
                self.state = 103
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1407374883685376) != 0):
                self.state = 104
                self.domain()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 110
            self.match(d3iGrammar.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_ruleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(d3iGrammar.IMPORT, 0)

        def qualifiedName(self):
            return self.getTypedRuleContext(d3iGrammar.QualifiedNameContext,0)


        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def getRuleIndex(self):
            return d3iGrammar.RULE_import_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_rule" ):
                listener.enterImport_rule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_rule" ):
                listener.exitImport_rule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_rule" ):
                return visitor.visitImport_rule(self)
            else:
                return visitor.visitChildren(self)




    def import_rule(self):

        localctx = d3iGrammar.Import_ruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_import_rule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 112
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118
            self.match(d3iGrammar.IMPORT)
            self.state = 119
            self.qualifiedName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DomainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOMAIN(self):
            return self.getToken(d3iGrammar.DOMAIN, 0)

        def IDENTIFIER(self):
            return self.getToken(d3iGrammar.IDENTIFIER, 0)

        def LCURLY(self):
            return self.getToken(d3iGrammar.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(d3iGrammar.RCURLY, 0)

        def directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DirectiveContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DirectiveContext,i)


        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def domain_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.Domain_elementContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.Domain_elementContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_domain

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDomain" ):
                listener.enterDomain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDomain" ):
                listener.exitDomain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDomain" ):
                return visitor.visitDomain(self)
            else:
                return visitor.visitChildren(self)




    def domain(self):

        localctx = d3iGrammar.DomainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_domain)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 121
                    self.directive() 
                self.state = 126
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 127
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 133
                self.decorator()
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 139
            self.match(d3iGrammar.DOMAIN)
            self.state = 140
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 141
            self.match(d3iGrammar.LCURLY)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1125899906876416) != 0):
                self.state = 142
                self.domain_element()
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 148
            self.match(d3iGrammar.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(d3iGrammar.IDENTIFIER, 0)

        def qualifiedName(self):
            return self.getTypedRuleContext(d3iGrammar.QualifiedNameContext,0)


        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def getRuleIndex(self):
            return d3iGrammar.RULE_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirective" ):
                listener.enterDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirective" ):
                listener.exitDirective(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirective" ):
                return visitor.visitDirective(self)
            else:
                return visitor.visitChildren(self)




    def directive(self):

        localctx = d3iGrammar.DirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_directive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 150
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 156
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 157
            self.qualifiedName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Domain_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def context(self):
            return self.getTypedRuleContext(d3iGrammar.ContextContext,0)


        def getRuleIndex(self):
            return d3iGrammar.RULE_domain_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDomain_element" ):
                listener.enterDomain_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDomain_element" ):
                listener.exitDomain_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDomain_element" ):
                return visitor.visitDomain_element(self)
            else:
                return visitor.visitChildren(self)




    def domain_element(self):

        localctx = d3iGrammar.Domain_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_domain_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.context()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTEXT(self):
            return self.getToken(d3iGrammar.CONTEXT, 0)

        def IDENTIFIER(self):
            return self.getToken(d3iGrammar.IDENTIFIER, 0)

        def LCURLY(self):
            return self.getToken(d3iGrammar.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(d3iGrammar.RCURLY, 0)

        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def context_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.Context_elementContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.Context_elementContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_context

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContext" ):
                listener.enterContext(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContext" ):
                listener.exitContext(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContext" ):
                return visitor.visitContext(self)
            else:
                return visitor.visitChildren(self)




    def context(self):

        localctx = d3iGrammar.ContextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_context)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 161
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 167
                self.decorator()
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 173
            self.match(d3iGrammar.CONTEXT)
            self.state = 174
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 175
            self.match(d3iGrammar.LCURLY)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1125900104590336) != 0):
                self.state = 176
                self.context_element()
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 182
            self.match(d3iGrammar.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Context_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enum(self):
            return self.getTypedRuleContext(d3iGrammar.EnumContext,0)


        def value_object(self):
            return self.getTypedRuleContext(d3iGrammar.Value_objectContext,0)


        def composite(self):
            return self.getTypedRuleContext(d3iGrammar.CompositeContext,0)


        def aggregate(self):
            return self.getTypedRuleContext(d3iGrammar.AggregateContext,0)


        def view(self):
            return self.getTypedRuleContext(d3iGrammar.ViewContext,0)


        def repository(self):
            return self.getTypedRuleContext(d3iGrammar.RepositoryContext,0)


        def acl(self):
            return self.getTypedRuleContext(d3iGrammar.AclContext,0)


        def service(self):
            return self.getTypedRuleContext(d3iGrammar.ServiceContext,0)


        def interface(self):
            return self.getTypedRuleContext(d3iGrammar.InterfaceContext,0)


        def getRuleIndex(self):
            return d3iGrammar.RULE_context_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContext_element" ):
                listener.enterContext_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContext_element" ):
                listener.exitContext_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContext_element" ):
                return visitor.visitContext_element(self)
            else:
                return visitor.visitChildren(self)




    def context_element(self):

        localctx = d3iGrammar.Context_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_context_element)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.enum()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.value_object()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 186
                self.composite()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 187
                self.aggregate()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 188
                self.view()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 189
                self.repository()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 190
                self.acl()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 191
                self.service()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 192
                self.interface()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_objectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VALUEOBJECT(self):
            return self.getToken(d3iGrammar.VALUEOBJECT, 0)

        def IDENTIFIER(self):
            return self.getToken(d3iGrammar.IDENTIFIER, 0)

        def LCURLY(self):
            return self.getToken(d3iGrammar.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(d3iGrammar.RCURLY, 0)

        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def inherits(self):
            return self.getTypedRuleContext(d3iGrammar.InheritsContext,0)


        def value_object_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.Value_object_elementContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.Value_object_elementContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_value_object

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue_object" ):
                listener.enterValue_object(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue_object" ):
                listener.exitValue_object(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_object" ):
                return visitor.visitValue_object(self)
            else:
                return visitor.visitChildren(self)




    def value_object(self):

        localctx = d3iGrammar.Value_objectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_value_object)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 195
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 201
                self.decorator()
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 207
            self.match(d3iGrammar.VALUEOBJECT)
            self.state = 208
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 209
                self.inherits()


            self.state = 212
            self.match(d3iGrammar.LCURLY)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1407374917633024) != 0):
                self.state = 213
                self.value_object_element()
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 219
            self.match(d3iGrammar.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_object_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value_object_member(self):
            return self.getTypedRuleContext(d3iGrammar.Value_object_memberContext,0)


        def enum(self):
            return self.getTypedRuleContext(d3iGrammar.EnumContext,0)


        def value_object(self):
            return self.getTypedRuleContext(d3iGrammar.Value_objectContext,0)


        def getRuleIndex(self):
            return d3iGrammar.RULE_value_object_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue_object_element" ):
                listener.enterValue_object_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue_object_element" ):
                listener.exitValue_object_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_object_element" ):
                return visitor.visitValue_object_element(self)
            else:
                return visitor.visitChildren(self)




    def value_object_element(self):

        localctx = d3iGrammar.Value_object_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_value_object_element)
        try:
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.value_object_member()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 223
                self.value_object()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_object_memberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(d3iGrammar.IDENTIFIER, 0)

        def SEMI(self):
            return self.getToken(d3iGrammar.SEMI, 0)

        def type_(self):
            return self.getTypedRuleContext(d3iGrammar.TypeContext,0)


        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_value_object_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue_object_member" ):
                listener.enterValue_object_member(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue_object_member" ):
                listener.exitValue_object_member(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_object_member" ):
                return visitor.visitValue_object_member(self)
            else:
                return visitor.visitChildren(self)




    def value_object_member(self):

        localctx = d3iGrammar.Value_object_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_value_object_member)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 226
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 232
                self.decorator()
                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 238
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 239
            self.match(d3iGrammar.SEMI)
            self.state = 240
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DtoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DTO(self):
            return self.getToken(d3iGrammar.DTO, 0)

        def IDENTIFIER(self):
            return self.getToken(d3iGrammar.IDENTIFIER, 0)

        def LCURLY(self):
            return self.getToken(d3iGrammar.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(d3iGrammar.RCURLY, 0)

        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def dto_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.Dto_elementContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.Dto_elementContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_dto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDto" ):
                listener.enterDto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDto" ):
                listener.exitDto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDto" ):
                return visitor.visitDto(self)
            else:
                return visitor.visitChildren(self)




    def dto(self):

        localctx = d3iGrammar.DtoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_dto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 242
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 248
                self.decorator()
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 254
            self.match(d3iGrammar.DTO)
            self.state = 255
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 256
            self.match(d3iGrammar.LCURLY)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1407374951187456) != 0):
                self.state = 257
                self.dto_element()
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 263
            self.match(d3iGrammar.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dto_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dto_member(self):
            return self.getTypedRuleContext(d3iGrammar.Dto_memberContext,0)


        def enum(self):
            return self.getTypedRuleContext(d3iGrammar.EnumContext,0)


        def dto(self):
            return self.getTypedRuleContext(d3iGrammar.DtoContext,0)


        def getRuleIndex(self):
            return d3iGrammar.RULE_dto_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDto_element" ):
                listener.enterDto_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDto_element" ):
                listener.exitDto_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDto_element" ):
                return visitor.visitDto_element(self)
            else:
                return visitor.visitChildren(self)




    def dto_element(self):

        localctx = d3iGrammar.Dto_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_dto_element)
        try:
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.dto_member()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 267
                self.dto()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dto_memberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(d3iGrammar.IDENTIFIER, 0)

        def SEMI(self):
            return self.getToken(d3iGrammar.SEMI, 0)

        def type_(self):
            return self.getTypedRuleContext(d3iGrammar.TypeContext,0)


        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_dto_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDto_member" ):
                listener.enterDto_member(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDto_member" ):
                listener.exitDto_member(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDto_member" ):
                return visitor.visitDto_member(self)
            else:
                return visitor.visitChildren(self)




    def dto_member(self):

        localctx = d3iGrammar.Dto_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_dto_member)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 270
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 276
                self.decorator()
                self.state = 281
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 282
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 283
            self.match(d3iGrammar.SEMI)
            self.state = 284
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompositeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMPOSITE(self):
            return self.getToken(d3iGrammar.COMPOSITE, 0)

        def IDENTIFIER(self):
            return self.getToken(d3iGrammar.IDENTIFIER, 0)

        def LCURLY(self):
            return self.getToken(d3iGrammar.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(d3iGrammar.RCURLY, 0)

        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def inherits(self):
            return self.getTypedRuleContext(d3iGrammar.InheritsContext,0)


        def composite_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.Composite_elementContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.Composite_elementContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_composite

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComposite" ):
                listener.enterComposite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComposite" ):
                listener.exitComposite(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposite" ):
                return visitor.visitComposite(self)
            else:
                return visitor.visitChildren(self)




    def composite(self):

        localctx = d3iGrammar.CompositeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_composite)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 286
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 291
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 292
                self.decorator()
                self.state = 297
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 298
            self.match(d3iGrammar.COMPOSITE)
            self.state = 299
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 301
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 300
                self.inherits()


            self.state = 303
            self.match(d3iGrammar.LCURLY)
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1407374917633024) != 0):
                self.state = 304
                self.composite_element()
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 310
            self.match(d3iGrammar.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Composite_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def composite_member(self):
            return self.getTypedRuleContext(d3iGrammar.Composite_memberContext,0)


        def enum(self):
            return self.getTypedRuleContext(d3iGrammar.EnumContext,0)


        def value_object(self):
            return self.getTypedRuleContext(d3iGrammar.Value_objectContext,0)


        def getRuleIndex(self):
            return d3iGrammar.RULE_composite_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComposite_element" ):
                listener.enterComposite_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComposite_element" ):
                listener.exitComposite_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposite_element" ):
                return visitor.visitComposite_element(self)
            else:
                return visitor.visitChildren(self)




    def composite_element(self):

        localctx = d3iGrammar.Composite_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_composite_element)
        try:
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.composite_member()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 314
                self.value_object()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Composite_memberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(d3iGrammar.IDENTIFIER, 0)

        def SEMI(self):
            return self.getToken(d3iGrammar.SEMI, 0)

        def type_(self):
            return self.getTypedRuleContext(d3iGrammar.TypeContext,0)


        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_composite_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComposite_member" ):
                listener.enterComposite_member(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComposite_member" ):
                listener.exitComposite_member(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposite_member" ):
                return visitor.visitComposite_member(self)
            else:
                return visitor.visitChildren(self)




    def composite_member(self):

        localctx = d3iGrammar.Composite_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_composite_member)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 317
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 322
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 323
                self.decorator()
                self.state = 328
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 329
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 330
            self.match(d3iGrammar.SEMI)
            self.state = 331
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EVENT(self):
            return self.getToken(d3iGrammar.EVENT, 0)

        def IDENTIFIER(self):
            return self.getToken(d3iGrammar.IDENTIFIER, 0)

        def LCURLY(self):
            return self.getToken(d3iGrammar.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(d3iGrammar.RCURLY, 0)

        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def inherits(self):
            return self.getTypedRuleContext(d3iGrammar.InheritsContext,0)


        def event_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.Event_elementContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.Event_elementContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_event

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvent" ):
                listener.enterEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvent" ):
                listener.exitEvent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEvent" ):
                return visitor.visitEvent(self)
            else:
                return visitor.visitChildren(self)




    def event(self):

        localctx = d3iGrammar.EventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_event)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 333
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 338
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 342
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 339
                self.decorator()
                self.state = 344
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 345
            self.match(d3iGrammar.EVENT)
            self.state = 346
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 347
                self.inherits()


            self.state = 350
            self.match(d3iGrammar.LCURLY)
            self.state = 354
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1407374884078592) != 0):
                self.state = 351
                self.event_element()
                self.state = 356
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 357
            self.match(d3iGrammar.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Event_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def event_member(self):
            return self.getTypedRuleContext(d3iGrammar.Event_memberContext,0)


        def enum(self):
            return self.getTypedRuleContext(d3iGrammar.EnumContext,0)


        def getRuleIndex(self):
            return d3iGrammar.RULE_event_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvent_element" ):
                listener.enterEvent_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvent_element" ):
                listener.exitEvent_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEvent_element" ):
                return visitor.visitEvent_element(self)
            else:
                return visitor.visitChildren(self)




    def event_element(self):

        localctx = d3iGrammar.Event_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_event_element)
        try:
            self.state = 361
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.event_member()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 360
                self.enum()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Event_memberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(d3iGrammar.IDENTIFIER, 0)

        def SEMI(self):
            return self.getToken(d3iGrammar.SEMI, 0)

        def type_(self):
            return self.getTypedRuleContext(d3iGrammar.TypeContext,0)


        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_event_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvent_member" ):
                listener.enterEvent_member(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvent_member" ):
                listener.exitEvent_member(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEvent_member" ):
                return visitor.visitEvent_member(self)
            else:
                return visitor.visitChildren(self)




    def event_member(self):

        localctx = d3iGrammar.Event_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_event_member)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 363
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 368
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 372
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 369
                self.decorator()
                self.state = 374
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 375
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 376
            self.match(d3iGrammar.SEMI)
            self.state = 377
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTITY(self):
            return self.getToken(d3iGrammar.ENTITY, 0)

        def IDENTIFIER(self):
            return self.getToken(d3iGrammar.IDENTIFIER, 0)

        def LCURLY(self):
            return self.getToken(d3iGrammar.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(d3iGrammar.RCURLY, 0)

        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def inherits(self):
            return self.getTypedRuleContext(d3iGrammar.InheritsContext,0)


        def entity_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.Entity_elementContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.Entity_elementContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_entity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntity" ):
                listener.enterEntity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntity" ):
                listener.exitEntity(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntity" ):
                return visitor.visitEntity(self)
            else:
                return visitor.visitChildren(self)




    def entity(self):

        localctx = d3iGrammar.EntityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_entity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 379
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 384
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 385
                self.decorator()
                self.state = 390
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 391
            self.match(d3iGrammar.ENTITY)
            self.state = 392
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 394
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 393
                self.inherits()


            self.state = 396
            self.match(d3iGrammar.LCURLY)
            self.state = 400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1407374917633024) != 0):
                self.state = 397
                self.entity_element()
                self.state = 402
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 403
            self.match(d3iGrammar.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Entity_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entity_member(self):
            return self.getTypedRuleContext(d3iGrammar.Entity_memberContext,0)


        def enum(self):
            return self.getTypedRuleContext(d3iGrammar.EnumContext,0)


        def value_object(self):
            return self.getTypedRuleContext(d3iGrammar.Value_objectContext,0)


        def getRuleIndex(self):
            return d3iGrammar.RULE_entity_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntity_element" ):
                listener.enterEntity_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntity_element" ):
                listener.exitEntity_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntity_element" ):
                return visitor.visitEntity_element(self)
            else:
                return visitor.visitChildren(self)




    def entity_element(self):

        localctx = d3iGrammar.Entity_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_entity_element)
        try:
            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                self.entity_member()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 406
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 407
                self.value_object()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Entity_memberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(d3iGrammar.IDENTIFIER, 0)

        def SEMI(self):
            return self.getToken(d3iGrammar.SEMI, 0)

        def type_(self):
            return self.getTypedRuleContext(d3iGrammar.TypeContext,0)


        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_entity_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntity_member" ):
                listener.enterEntity_member(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntity_member" ):
                listener.exitEntity_member(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntity_member" ):
                return visitor.visitEntity_member(self)
            else:
                return visitor.visitChildren(self)




    def entity_member(self):

        localctx = d3iGrammar.Entity_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_entity_member)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 410
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 415
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 419
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 416
                self.decorator()
                self.state = 421
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 422
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 423
            self.match(d3iGrammar.SEMI)
            self.state = 424
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGGREGATE(self):
            return self.getToken(d3iGrammar.AGGREGATE, 0)

        def IDENTIFIER(self):
            return self.getToken(d3iGrammar.IDENTIFIER, 0)

        def LCURLY(self):
            return self.getToken(d3iGrammar.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(d3iGrammar.RCURLY, 0)

        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def aggregate_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.Aggregate_elementContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.Aggregate_elementContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_aggregate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregate" ):
                listener.enterAggregate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregate" ):
                listener.exitAggregate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregate" ):
                return visitor.visitAggregate(self)
            else:
                return visitor.visitChildren(self)




    def aggregate(self):

        localctx = d3iGrammar.AggregateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_aggregate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 426
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 431
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 435
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 432
                self.decorator()
                self.state = 437
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 438
            self.match(d3iGrammar.AGGREGATE)
            self.state = 439
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 440
            self.match(d3iGrammar.LCURLY)
            self.state = 444
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1125900209619968) != 0):
                self.state = 441
                self.aggregate_element()
                self.state = 446
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 447
            self.match(d3iGrammar.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Aggregate_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aggregate_entity(self):
            return self.getTypedRuleContext(d3iGrammar.Aggregate_entityContext,0)


        def enum(self):
            return self.getTypedRuleContext(d3iGrammar.EnumContext,0)


        def value_object(self):
            return self.getTypedRuleContext(d3iGrammar.Value_objectContext,0)


        def getRuleIndex(self):
            return d3iGrammar.RULE_aggregate_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregate_element" ):
                listener.enterAggregate_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregate_element" ):
                listener.exitAggregate_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregate_element" ):
                return visitor.visitAggregate_element(self)
            else:
                return visitor.visitChildren(self)




    def aggregate_element(self):

        localctx = d3iGrammar.Aggregate_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_aggregate_element)
        try:
            self.state = 452
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                self.aggregate_entity()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 450
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 451
                self.value_object()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Aggregate_entityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entity(self):
            return self.getTypedRuleContext(d3iGrammar.EntityContext,0)


        def ROOT(self):
            return self.getToken(d3iGrammar.ROOT, 0)

        def getRuleIndex(self):
            return d3iGrammar.RULE_aggregate_entity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregate_entity" ):
                listener.enterAggregate_entity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregate_entity" ):
                listener.exitAggregate_entity(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregate_entity" ):
                return visitor.visitAggregate_entity(self)
            else:
                return visitor.visitChildren(self)




    def aggregate_entity(self):

        localctx = d3iGrammar.Aggregate_entityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_aggregate_entity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 454
                self.match(d3iGrammar.ROOT)


            self.state = 457
            self.entity()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ViewContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VIEW(self):
            return self.getToken(d3iGrammar.VIEW, 0)

        def IDENTIFIER(self):
            return self.getToken(d3iGrammar.IDENTIFIER, 0)

        def LCURLY(self):
            return self.getToken(d3iGrammar.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(d3iGrammar.RCURLY, 0)

        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def inherits(self):
            return self.getTypedRuleContext(d3iGrammar.InheritsContext,0)


        def view_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.View_elementContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.View_elementContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_view

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterView" ):
                listener.enterView(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitView" ):
                listener.exitView(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitView" ):
                return visitor.visitView(self)
            else:
                return visitor.visitChildren(self)




    def view(self):

        localctx = d3iGrammar.ViewContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_view)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 459
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 464
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 468
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 465
                self.decorator()
                self.state = 470
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 471
            self.match(d3iGrammar.VIEW)
            self.state = 472
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 474
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 473
                self.inherits()


            self.state = 476
            self.match(d3iGrammar.LCURLY)
            self.state = 480
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1407374884078592) != 0):
                self.state = 477
                self.view_element()
                self.state = 482
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 483
            self.match(d3iGrammar.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class View_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def view_member(self):
            return self.getTypedRuleContext(d3iGrammar.View_memberContext,0)


        def enum(self):
            return self.getTypedRuleContext(d3iGrammar.EnumContext,0)


        def getRuleIndex(self):
            return d3iGrammar.RULE_view_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterView_element" ):
                listener.enterView_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitView_element" ):
                listener.exitView_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitView_element" ):
                return visitor.visitView_element(self)
            else:
                return visitor.visitChildren(self)




    def view_element(self):

        localctx = d3iGrammar.View_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_view_element)
        try:
            self.state = 487
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 485
                self.view_member()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 486
                self.enum()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class View_memberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(d3iGrammar.IDENTIFIER, 0)

        def SEMI(self):
            return self.getToken(d3iGrammar.SEMI, 0)

        def type_(self):
            return self.getTypedRuleContext(d3iGrammar.TypeContext,0)


        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_view_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterView_member" ):
                listener.enterView_member(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitView_member" ):
                listener.exitView_member(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitView_member" ):
                return visitor.visitView_member(self)
            else:
                return visitor.visitChildren(self)




    def view_member(self):

        localctx = d3iGrammar.View_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_view_member)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 489
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 494
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 498
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 495
                self.decorator()
                self.state = 500
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 501
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 502
            self.match(d3iGrammar.SEMI)
            self.state = 503
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepositoryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPOSITORY(self):
            return self.getToken(d3iGrammar.REPOSITORY, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.IDENTIFIER)
            else:
                return self.getToken(d3iGrammar.IDENTIFIER, i)

        def SEMI(self):
            return self.getToken(d3iGrammar.SEMI, 0)

        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_repository

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepository" ):
                listener.enterRepository(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepository" ):
                listener.exitRepository(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepository" ):
                return visitor.visitRepository(self)
            else:
                return visitor.visitChildren(self)




    def repository(self):

        localctx = d3iGrammar.RepositoryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_repository)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 505
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 510
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 514
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 511
                self.decorator()
                self.state = 516
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 517
            self.match(d3iGrammar.REPOSITORY)
            self.state = 518
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 519
            self.match(d3iGrammar.SEMI)
            self.state = 520
            self.match(d3iGrammar.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ServiceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SERVICE(self):
            return self.getToken(d3iGrammar.SERVICE, 0)

        def IDENTIFIER(self):
            return self.getToken(d3iGrammar.IDENTIFIER, 0)

        def LCURLY(self):
            return self.getToken(d3iGrammar.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(d3iGrammar.RCURLY, 0)

        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def service_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.Service_elementContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.Service_elementContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_service

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterService" ):
                listener.enterService(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitService" ):
                listener.exitService(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitService" ):
                return visitor.visitService(self)
            else:
                return visitor.visitChildren(self)




    def service(self):

        localctx = d3iGrammar.ServiceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_service)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 522
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 527
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 531
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 528
                self.decorator()
                self.state = 533
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 534
            self.match(d3iGrammar.SERVICE)
            self.state = 535
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 536
            self.match(d3iGrammar.LCURLY)
            self.state = 540
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1407374918681600) != 0):
                self.state = 537
                self.service_element()
                self.state = 542
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 543
            self.match(d3iGrammar.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Service_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operation(self):
            return self.getTypedRuleContext(d3iGrammar.OperationContext,0)


        def enum(self):
            return self.getTypedRuleContext(d3iGrammar.EnumContext,0)


        def value_object(self):
            return self.getTypedRuleContext(d3iGrammar.Value_objectContext,0)


        def event(self):
            return self.getTypedRuleContext(d3iGrammar.EventContext,0)


        def getRuleIndex(self):
            return d3iGrammar.RULE_service_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterService_element" ):
                listener.enterService_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitService_element" ):
                listener.exitService_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitService_element" ):
                return visitor.visitService_element(self)
            else:
                return visitor.visitChildren(self)




    def service_element(self):

        localctx = d3iGrammar.Service_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_service_element)
        try:
            self.state = 549
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 545
                self.operation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 546
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 547
                self.value_object()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 548
                self.event()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERFACE(self):
            return self.getToken(d3iGrammar.INTERFACE, 0)

        def IDENTIFIER(self):
            return self.getToken(d3iGrammar.IDENTIFIER, 0)

        def VERSION(self):
            return self.getToken(d3iGrammar.VERSION, 0)

        def INTEGER_CONSTANS(self):
            return self.getToken(d3iGrammar.INTEGER_CONSTANS, 0)

        def LCURLY(self):
            return self.getToken(d3iGrammar.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(d3iGrammar.RCURLY, 0)

        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def interface_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.Interface_elementContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.Interface_elementContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_interface

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterface" ):
                listener.enterInterface(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterface" ):
                listener.exitInterface(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface" ):
                return visitor.visitInterface(self)
            else:
                return visitor.visitChildren(self)




    def interface(self):

        localctx = d3iGrammar.InterfaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_interface)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 554
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 551
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 556
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 560
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 557
                self.decorator()
                self.state = 562
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 563
            self.match(d3iGrammar.INTERFACE)
            self.state = 564
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 565
            self.match(d3iGrammar.VERSION)
            self.state = 566
            self.match(d3iGrammar.INTEGER_CONSTANS)
            self.state = 567
            self.match(d3iGrammar.LCURLY)
            self.state = 571
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1407374952236032) != 0):
                self.state = 568
                self.interface_element()
                self.state = 573
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 574
            self.match(d3iGrammar.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operation(self):
            return self.getTypedRuleContext(d3iGrammar.OperationContext,0)


        def enum(self):
            return self.getTypedRuleContext(d3iGrammar.EnumContext,0)


        def dto(self):
            return self.getTypedRuleContext(d3iGrammar.DtoContext,0)


        def event(self):
            return self.getTypedRuleContext(d3iGrammar.EventContext,0)


        def getRuleIndex(self):
            return d3iGrammar.RULE_interface_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterface_element" ):
                listener.enterInterface_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterface_element" ):
                listener.exitInterface_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_element" ):
                return visitor.visitInterface_element(self)
            else:
                return visitor.visitChildren(self)




    def interface_element(self):

        localctx = d3iGrammar.Interface_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_interface_element)
        try:
            self.state = 580
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 576
                self.operation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 577
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 578
                self.dto()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 579
                self.event()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(d3iGrammar.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(d3iGrammar.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(d3iGrammar.RPAREN, 0)

        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def operation_param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.Operation_paramContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.Operation_paramContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.COMMA)
            else:
                return self.getToken(d3iGrammar.COMMA, i)

        def SEMI(self):
            return self.getToken(d3iGrammar.SEMI, 0)

        def operation_return(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.Operation_returnContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.Operation_returnContext,i)


        def PIPE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.PIPE)
            else:
                return self.getToken(d3iGrammar.PIPE, i)

        def getRuleIndex(self):
            return d3iGrammar.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation" ):
                return visitor.visitOperation(self)
            else:
                return visitor.visitChildren(self)




    def operation(self):

        localctx = d3iGrammar.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 582
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 587
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 591
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 588
                self.decorator()
                self.state = 593
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 594
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 595
            self.match(d3iGrammar.LPAREN)

            self.state = 597
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1407374883554304) != 0):
                self.state = 596
                self.operation_param()


            self.state = 603
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 599
                self.match(d3iGrammar.COMMA)
                self.state = 600
                self.operation_param()
                self.state = 605
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 606
            self.match(d3iGrammar.RPAREN)

            self.state = 609
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 607
                self.match(d3iGrammar.SEMI)
                self.state = 608
                self.operation_return()


            self.state = 615
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 611
                self.match(d3iGrammar.PIPE)
                self.state = 612
                self.operation_return()
                self.state = 617
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operation_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(d3iGrammar.IDENTIFIER, 0)

        def SEMI(self):
            return self.getToken(d3iGrammar.SEMI, 0)

        def type_(self):
            return self.getTypedRuleContext(d3iGrammar.TypeContext,0)


        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_operation_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation_param" ):
                listener.enterOperation_param(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation_param" ):
                listener.exitOperation_param(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation_param" ):
                return visitor.visitOperation_param(self)
            else:
                return visitor.visitChildren(self)




    def operation_param(self):

        localctx = d3iGrammar.Operation_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_operation_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 621
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 618
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 623
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 627
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 624
                self.decorator()
                self.state = 629
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 630
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 631
            self.match(d3iGrammar.SEMI)
            self.state = 632
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operation_returnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(d3iGrammar.TypeContext,0)


        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_operation_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation_return" ):
                listener.enterOperation_return(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation_return" ):
                listener.exitOperation_return(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation_return" ):
                return visitor.visitOperation_return(self)
            else:
                return visitor.visitChildren(self)




    def operation_return(self):

        localctx = d3iGrammar.Operation_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_operation_return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 637
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 634
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 639
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 643
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 640
                self.decorator()
                self.state = 645
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 646
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACL(self):
            return self.getToken(d3iGrammar.ACL, 0)

        def IDENTIFIER(self):
            return self.getToken(d3iGrammar.IDENTIFIER, 0)

        def LCURLY(self):
            return self.getToken(d3iGrammar.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(d3iGrammar.RCURLY, 0)

        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def acl_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.Acl_elementContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.Acl_elementContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_acl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcl" ):
                listener.enterAcl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcl" ):
                listener.exitAcl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAcl" ):
                return visitor.visitAcl(self)
            else:
                return visitor.visitChildren(self)




    def acl(self):

        localctx = d3iGrammar.AclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_acl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 651
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 648
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 653
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 657
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 654
                self.decorator()
                self.state = 659
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 660
            self.match(d3iGrammar.ACL)
            self.state = 661
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 662
            self.match(d3iGrammar.LCURLY)
            self.state = 666
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1407374917633024) != 0):
                self.state = 663
                self.acl_element()
                self.state = 668
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 669
            self.match(d3iGrammar.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Acl_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enum(self):
            return self.getTypedRuleContext(d3iGrammar.EnumContext,0)


        def value_object(self):
            return self.getTypedRuleContext(d3iGrammar.Value_objectContext,0)


        def operation(self):
            return self.getTypedRuleContext(d3iGrammar.OperationContext,0)


        def getRuleIndex(self):
            return d3iGrammar.RULE_acl_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcl_element" ):
                listener.enterAcl_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcl_element" ):
                listener.exitAcl_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAcl_element" ):
                return visitor.visitAcl_element(self)
            else:
                return visitor.visitChildren(self)




    def acl_element(self):

        localctx = d3iGrammar.Acl_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_acl_element)
        try:
            self.state = 674
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,81,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 671
                self.enum()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 672
                self.value_object()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 673
                self.operation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(d3iGrammar.Primitive_typeContext,0)


        def reference_type(self):
            return self.getTypedRuleContext(d3iGrammar.Reference_typeContext,0)


        def list_type(self):
            return self.getTypedRuleContext(d3iGrammar.List_typeContext,0)


        def map_type(self):
            return self.getTypedRuleContext(d3iGrammar.Map_typeContext,0)


        def getRuleIndex(self):
            return d3iGrammar.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = d3iGrammar.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_type)
        try:
            self.state = 680
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 676
                self.primitive_type()
                pass
            elif token in [44, 48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 677
                self.reference_type()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 3)
                self.state = 678
                self.list_type()
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 4)
                self.state = 679
                self.map_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(d3iGrammar.INTEGER, 0)

        def NUMBER(self):
            return self.getToken(d3iGrammar.NUMBER, 0)

        def FLOAT(self):
            return self.getToken(d3iGrammar.FLOAT, 0)

        def DATE(self):
            return self.getToken(d3iGrammar.DATE, 0)

        def TIME(self):
            return self.getToken(d3iGrammar.TIME, 0)

        def DATETIME(self):
            return self.getToken(d3iGrammar.DATETIME, 0)

        def STRING(self):
            return self.getToken(d3iGrammar.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(d3iGrammar.BOOLEAN, 0)

        def BYTES(self):
            return self.getToken(d3iGrammar.BYTES, 0)

        def STREAM(self):
            return self.getToken(d3iGrammar.STREAM, 0)

        def ANY(self):
            return self.getToken(d3iGrammar.ANY, 0)

        def getRuleIndex(self):
            return d3iGrammar.RULE_primitive_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitive_type" ):
                listener.enterPrimitive_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitive_type" ):
                listener.exitPrimitive_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = d3iGrammar.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 682
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4395899027456) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Reference_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qualifiedName(self):
            return self.getTypedRuleContext(d3iGrammar.QualifiedNameContext,0)


        def EXTERNAL(self):
            return self.getToken(d3iGrammar.EXTERNAL, 0)

        def LBARCKET(self):
            return self.getToken(d3iGrammar.LBARCKET, 0)

        def STRING_LITERAL(self):
            return self.getToken(d3iGrammar.STRING_LITERAL, 0)

        def RBRACKET(self):
            return self.getToken(d3iGrammar.RBRACKET, 0)

        def getRuleIndex(self):
            return d3iGrammar.RULE_reference_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReference_type" ):
                listener.enterReference_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReference_type" ):
                listener.exitReference_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReference_type" ):
                return visitor.visitReference_type(self)
            else:
                return visitor.visitChildren(self)




    def reference_type(self):

        localctx = d3iGrammar.Reference_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_reference_type)
        try:
            self.state = 689
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 684
                self.qualifiedName()
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 2)
                self.state = 685
                self.match(d3iGrammar.EXTERNAL)
                self.state = 686
                self.match(d3iGrammar.LBARCKET)
                self.state = 687
                self.match(d3iGrammar.STRING_LITERAL)
                self.state = 688
                self.match(d3iGrammar.RBRACKET)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIST(self):
            return self.getToken(d3iGrammar.LIST, 0)

        def LBARCKET(self):
            return self.getToken(d3iGrammar.LBARCKET, 0)

        def type_(self):
            return self.getTypedRuleContext(d3iGrammar.TypeContext,0)


        def RBRACKET(self):
            return self.getToken(d3iGrammar.RBRACKET, 0)

        def getRuleIndex(self):
            return d3iGrammar.RULE_list_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_type" ):
                listener.enterList_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_type" ):
                listener.exitList_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_type" ):
                return visitor.visitList_type(self)
            else:
                return visitor.visitChildren(self)




    def list_type(self):

        localctx = d3iGrammar.List_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_list_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 691
            self.match(d3iGrammar.LIST)
            self.state = 692
            self.match(d3iGrammar.LBARCKET)
            self.state = 693
            self.type_()
            self.state = 694
            self.match(d3iGrammar.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Map_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAP(self):
            return self.getToken(d3iGrammar.MAP, 0)

        def LBARCKET(self):
            return self.getToken(d3iGrammar.LBARCKET, 0)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.TypeContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.TypeContext,i)


        def COMMA(self):
            return self.getToken(d3iGrammar.COMMA, 0)

        def RBRACKET(self):
            return self.getToken(d3iGrammar.RBRACKET, 0)

        def getRuleIndex(self):
            return d3iGrammar.RULE_map_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMap_type" ):
                listener.enterMap_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMap_type" ):
                listener.exitMap_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMap_type" ):
                return visitor.visitMap_type(self)
            else:
                return visitor.visitChildren(self)




    def map_type(self):

        localctx = d3iGrammar.Map_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_map_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 696
            self.match(d3iGrammar.MAP)
            self.state = 697
            self.match(d3iGrammar.LBARCKET)
            self.state = 698
            self.type_()
            self.state = 699
            self.match(d3iGrammar.COMMA)
            self.state = 700
            self.type_()
            self.state = 701
            self.match(d3iGrammar.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QualifiedNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.IDENTIFIER)
            else:
                return self.getToken(d3iGrammar.IDENTIFIER, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOT)
            else:
                return self.getToken(d3iGrammar.DOT, i)

        def getRuleIndex(self):
            return d3iGrammar.RULE_qualifiedName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQualifiedName" ):
                listener.enterQualifiedName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQualifiedName" ):
                listener.exitQualifiedName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQualifiedName" ):
                return visitor.visitQualifiedName(self)
            else:
                return visitor.visitChildren(self)




    def qualifiedName(self):

        localctx = d3iGrammar.QualifiedNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_qualifiedName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 703
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 708
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 704
                self.match(d3iGrammar.DOT)
                self.state = 705
                self.match(d3iGrammar.IDENTIFIER)
                self.state = 710
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecoratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self):
            return self.getToken(d3iGrammar.AT, 0)

        def IDENTIFIER(self):
            return self.getToken(d3iGrammar.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(d3iGrammar.LPAREN, 0)

        def decorator_param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.Decorator_paramContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.Decorator_paramContext,i)


        def RPAREN(self):
            return self.getToken(d3iGrammar.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.COMMA)
            else:
                return self.getToken(d3iGrammar.COMMA, i)

        def getRuleIndex(self):
            return d3iGrammar.RULE_decorator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecorator" ):
                listener.enterDecorator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecorator" ):
                listener.exitDecorator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecorator" ):
                return visitor.visitDecorator(self)
            else:
                return visitor.visitChildren(self)




    def decorator(self):

        localctx = d3iGrammar.DecoratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_decorator)
        self._la = 0 # Token type
        try:
            self.state = 726
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,86,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 711
                self.match(d3iGrammar.AT)
                self.state = 712
                self.match(d3iGrammar.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 713
                self.match(d3iGrammar.AT)
                self.state = 714
                self.match(d3iGrammar.IDENTIFIER)
                self.state = 715
                self.match(d3iGrammar.LPAREN)
                self.state = 716
                self.decorator_param()
                self.state = 721
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 717
                    self.match(d3iGrammar.COMMA)
                    self.state = 718
                    self.decorator_param()
                    self.state = 723
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 724
                self.match(d3iGrammar.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decorator_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qualifiedName(self):
            return self.getTypedRuleContext(d3iGrammar.QualifiedNameContext,0)


        def INTEGER_CONSTANS(self):
            return self.getToken(d3iGrammar.INTEGER_CONSTANS, 0)

        def NUMBER_CONSTANS(self):
            return self.getToken(d3iGrammar.NUMBER_CONSTANS, 0)

        def STRING_LITERAL(self):
            return self.getToken(d3iGrammar.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return d3iGrammar.RULE_decorator_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecorator_param" ):
                listener.enterDecorator_param(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecorator_param" ):
                listener.exitDecorator_param(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecorator_param" ):
                return visitor.visitDecorator_param(self)
            else:
                return visitor.visitChildren(self)




    def decorator_param(self):

        localctx = d3iGrammar.Decorator_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_decorator_param)
        try:
            self.state = 732
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 728
                self.qualifiedName()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 729
                self.match(d3iGrammar.INTEGER_CONSTANS)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 3)
                self.state = 730
                self.match(d3iGrammar.NUMBER_CONSTANS)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 4)
                self.state = 731
                self.match(d3iGrammar.STRING_LITERAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENUM(self):
            return self.getToken(d3iGrammar.ENUM, 0)

        def IDENTIFIER(self):
            return self.getToken(d3iGrammar.IDENTIFIER, 0)

        def LCURLY(self):
            return self.getToken(d3iGrammar.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(d3iGrammar.RCURLY, 0)

        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def enum_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.Enum_elementContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.Enum_elementContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.COMMA)
            else:
                return self.getToken(d3iGrammar.COMMA, i)

        def getRuleIndex(self):
            return d3iGrammar.RULE_enum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnum" ):
                listener.enterEnum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnum" ):
                listener.exitEnum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnum" ):
                return visitor.visitEnum(self)
            else:
                return visitor.visitChildren(self)




    def enum(self):

        localctx = d3iGrammar.EnumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_enum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 737
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 734
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 739
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 743
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 740
                self.decorator()
                self.state = 745
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 746
            self.match(d3iGrammar.ENUM)
            self.state = 747
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 748
            self.match(d3iGrammar.LCURLY)
            self.state = 750
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1407374883554304) != 0):
                self.state = 749
                self.enum_element()


            self.state = 756
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 752
                self.match(d3iGrammar.COMMA)
                self.state = 753
                self.enum_element()
                self.state = 758
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 759
            self.match(d3iGrammar.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Enum_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(d3iGrammar.IDENTIFIER, 0)

        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(d3iGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_enum_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnum_element" ):
                listener.enterEnum_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnum_element" ):
                listener.exitEnum_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnum_element" ):
                return visitor.visitEnum_element(self)
            else:
                return visitor.visitChildren(self)




    def enum_element(self):

        localctx = d3iGrammar.Enum_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_enum_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 764
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 761
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 766
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 770
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 767
                self.decorator()
                self.state = 772
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 773
            self.match(d3iGrammar.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InheritsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INHERITS(self):
            return self.getToken(d3iGrammar.INHERITS, 0)

        def qualifiedName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.QualifiedNameContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.QualifiedNameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.COMMA)
            else:
                return self.getToken(d3iGrammar.COMMA, i)

        def getRuleIndex(self):
            return d3iGrammar.RULE_inherits

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInherits" ):
                listener.enterInherits(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInherits" ):
                listener.exitInherits(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInherits" ):
                return visitor.visitInherits(self)
            else:
                return visitor.visitChildren(self)




    def inherits(self):

        localctx = d3iGrammar.InheritsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_inherits)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 775
            self.match(d3iGrammar.INHERITS)
            self.state = 776
            self.qualifiedName()
            self.state = 781
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 777
                self.match(d3iGrammar.COMMA)
                self.state = 778
                self.qualifiedName()
                self.state = 783
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





