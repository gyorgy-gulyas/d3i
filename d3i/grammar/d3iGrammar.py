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
        4,1,50,681,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,1,0,5,0,88,8,0,10,0,12,0,91,9,0,1,
        0,5,0,94,8,0,10,0,12,0,97,9,0,1,0,1,0,1,1,5,1,102,8,1,10,1,12,1,
        105,9,1,1,1,1,1,1,1,1,2,5,2,111,8,2,10,2,12,2,114,9,2,1,2,5,2,117,
        8,2,10,2,12,2,120,9,2,1,2,5,2,123,8,2,10,2,12,2,126,9,2,1,2,1,2,
        1,2,1,2,5,2,132,8,2,10,2,12,2,135,9,2,1,2,1,2,1,3,5,3,140,8,3,10,
        3,12,3,143,9,3,1,3,1,3,1,3,1,4,1,4,1,5,5,5,151,8,5,10,5,12,5,154,
        9,5,1,5,5,5,157,8,5,10,5,12,5,160,9,5,1,5,1,5,1,5,1,5,5,5,166,8,
        5,10,5,12,5,169,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,
        181,8,6,1,7,5,7,184,8,7,10,7,12,7,187,9,7,1,7,5,7,190,8,7,10,7,12,
        7,193,9,7,1,7,1,7,1,7,3,7,198,8,7,1,7,1,7,5,7,202,8,7,10,7,12,7,
        205,9,7,1,7,1,7,1,8,1,8,1,8,3,8,212,8,8,1,9,5,9,215,8,9,10,9,12,
        9,218,9,9,1,9,5,9,221,8,9,10,9,12,9,224,9,9,1,9,1,9,1,9,1,9,1,10,
        5,10,231,8,10,10,10,12,10,234,9,10,1,10,5,10,237,8,10,10,10,12,10,
        240,9,10,1,10,1,10,1,10,3,10,245,8,10,1,10,1,10,5,10,249,8,10,10,
        10,12,10,252,9,10,1,10,1,10,1,11,1,11,1,11,3,11,259,8,11,1,12,5,
        12,262,8,12,10,12,12,12,265,9,12,1,12,5,12,268,8,12,10,12,12,12,
        271,9,12,1,12,1,12,1,12,1,12,1,13,5,13,278,8,13,10,13,12,13,281,
        9,13,1,13,5,13,284,8,13,10,13,12,13,287,9,13,1,13,1,13,1,13,3,13,
        292,8,13,1,13,1,13,5,13,296,8,13,10,13,12,13,299,9,13,1,13,1,13,
        1,14,1,14,1,14,3,14,306,8,14,1,15,5,15,309,8,15,10,15,12,15,312,
        9,15,1,15,5,15,315,8,15,10,15,12,15,318,9,15,1,15,1,15,1,15,1,15,
        1,16,5,16,325,8,16,10,16,12,16,328,9,16,1,16,5,16,331,8,16,10,16,
        12,16,334,9,16,1,16,1,16,1,16,1,16,5,16,340,8,16,10,16,12,16,343,
        9,16,1,16,1,16,1,17,1,17,1,17,3,17,350,8,17,1,18,3,18,353,8,18,1,
        18,1,18,1,19,5,19,358,8,19,10,19,12,19,361,9,19,1,19,5,19,364,8,
        19,10,19,12,19,367,9,19,1,19,1,19,1,19,3,19,372,8,19,1,19,1,19,5,
        19,376,8,19,10,19,12,19,379,9,19,1,19,1,19,1,20,1,20,1,20,3,20,386,
        8,20,1,21,5,21,389,8,21,10,21,12,21,392,9,21,1,21,5,21,395,8,21,
        10,21,12,21,398,9,21,1,21,1,21,1,21,1,21,1,22,5,22,405,8,22,10,22,
        12,22,408,9,22,1,22,5,22,411,8,22,10,22,12,22,414,9,22,1,22,1,22,
        1,22,1,22,1,22,1,23,5,23,422,8,23,10,23,12,23,425,9,23,1,23,5,23,
        428,8,23,10,23,12,23,431,9,23,1,23,1,23,1,23,1,23,5,23,437,8,23,
        10,23,12,23,440,9,23,1,23,1,23,1,24,1,24,1,24,1,24,3,24,448,8,24,
        1,25,5,25,451,8,25,10,25,12,25,454,9,25,1,25,5,25,457,8,25,10,25,
        12,25,460,9,25,1,25,1,25,1,25,1,25,5,25,466,8,25,10,25,12,25,469,
        9,25,1,25,1,25,1,26,1,26,1,26,1,26,3,26,477,8,26,1,27,5,27,480,8,
        27,10,27,12,27,483,9,27,1,27,5,27,486,8,27,10,27,12,27,489,9,27,
        1,27,1,27,1,27,3,27,494,8,27,1,27,1,27,5,27,498,8,27,10,27,12,27,
        501,9,27,1,27,1,27,1,27,3,27,506,8,27,1,27,1,27,5,27,510,8,27,10,
        27,12,27,513,9,27,1,28,5,28,516,8,28,10,28,12,28,519,9,28,1,28,5,
        28,522,8,28,10,28,12,28,525,9,28,1,28,1,28,1,28,1,28,1,29,5,29,532,
        8,29,10,29,12,29,535,9,29,1,29,5,29,538,8,29,10,29,12,29,541,9,29,
        1,29,1,29,1,30,5,30,546,8,30,10,30,12,30,549,9,30,1,30,5,30,552,
        8,30,10,30,12,30,555,9,30,1,30,1,30,1,30,1,30,5,30,561,8,30,10,30,
        12,30,564,9,30,1,30,1,30,1,31,1,31,1,31,3,31,571,8,31,1,32,1,32,
        1,32,1,32,3,32,577,8,32,1,33,1,33,1,34,1,34,1,34,1,34,1,34,3,34,
        586,8,34,1,35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,1,36,1,36,
        1,36,1,37,1,37,1,37,5,37,603,8,37,10,37,12,37,606,9,37,1,38,1,38,
        1,38,1,38,1,38,1,38,1,38,1,38,5,38,616,8,38,10,38,12,38,619,9,38,
        1,38,1,38,3,38,623,8,38,1,39,1,39,1,39,1,39,3,39,629,8,39,1,40,5,
        40,632,8,40,10,40,12,40,635,9,40,1,40,5,40,638,8,40,10,40,12,40,
        641,9,40,1,40,1,40,1,40,1,40,3,40,647,8,40,1,40,1,40,5,40,651,8,
        40,10,40,12,40,654,9,40,1,40,1,40,1,41,5,41,659,8,41,10,41,12,41,
        662,9,41,1,41,5,41,665,8,41,10,41,12,41,668,9,41,1,41,1,41,1,42,
        1,42,1,42,1,42,5,42,676,8,42,10,42,12,42,679,9,42,1,42,0,0,43,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,
        48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,0,1,1,0,
        29,39,739,0,89,1,0,0,0,2,103,1,0,0,0,4,112,1,0,0,0,6,141,1,0,0,0,
        8,147,1,0,0,0,10,152,1,0,0,0,12,180,1,0,0,0,14,185,1,0,0,0,16,211,
        1,0,0,0,18,216,1,0,0,0,20,232,1,0,0,0,22,258,1,0,0,0,24,263,1,0,
        0,0,26,279,1,0,0,0,28,305,1,0,0,0,30,310,1,0,0,0,32,326,1,0,0,0,
        34,349,1,0,0,0,36,352,1,0,0,0,38,359,1,0,0,0,40,385,1,0,0,0,42,390,
        1,0,0,0,44,406,1,0,0,0,46,423,1,0,0,0,48,447,1,0,0,0,50,452,1,0,
        0,0,52,476,1,0,0,0,54,481,1,0,0,0,56,517,1,0,0,0,58,533,1,0,0,0,
        60,547,1,0,0,0,62,570,1,0,0,0,64,576,1,0,0,0,66,578,1,0,0,0,68,585,
        1,0,0,0,70,587,1,0,0,0,72,592,1,0,0,0,74,599,1,0,0,0,76,622,1,0,
        0,0,78,628,1,0,0,0,80,633,1,0,0,0,82,660,1,0,0,0,84,671,1,0,0,0,
        86,88,3,2,1,0,87,86,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,
        0,0,0,90,95,1,0,0,0,91,89,1,0,0,0,92,94,3,4,2,0,93,92,1,0,0,0,94,
        97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,98,1,0,0,0,97,95,1,0,0,
        0,98,99,5,0,0,1,99,1,1,0,0,0,100,102,5,48,0,0,101,100,1,0,0,0,102,
        105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,106,1,0,0,0,105,
        103,1,0,0,0,106,107,5,21,0,0,107,108,3,74,37,0,108,3,1,0,0,0,109,
        111,3,6,3,0,110,109,1,0,0,0,111,114,1,0,0,0,112,110,1,0,0,0,112,
        113,1,0,0,0,113,118,1,0,0,0,114,112,1,0,0,0,115,117,5,48,0,0,116,
        115,1,0,0,0,117,120,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,
        124,1,0,0,0,120,118,1,0,0,0,121,123,3,76,38,0,122,121,1,0,0,0,123,
        126,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,127,1,0,0,0,126,
        124,1,0,0,0,127,128,5,17,0,0,128,129,5,46,0,0,129,133,5,6,0,0,130,
        132,3,8,4,0,131,130,1,0,0,0,132,135,1,0,0,0,133,131,1,0,0,0,133,
        134,1,0,0,0,134,136,1,0,0,0,135,133,1,0,0,0,136,137,5,7,0,0,137,
        5,1,0,0,0,138,140,5,48,0,0,139,138,1,0,0,0,140,143,1,0,0,0,141,139,
        1,0,0,0,141,142,1,0,0,0,142,144,1,0,0,0,143,141,1,0,0,0,144,145,
        5,46,0,0,145,146,3,74,37,0,146,7,1,0,0,0,147,148,3,10,5,0,148,9,
        1,0,0,0,149,151,5,48,0,0,150,149,1,0,0,0,151,154,1,0,0,0,152,150,
        1,0,0,0,152,153,1,0,0,0,153,158,1,0,0,0,154,152,1,0,0,0,155,157,
        3,76,38,0,156,155,1,0,0,0,157,160,1,0,0,0,158,156,1,0,0,0,158,159,
        1,0,0,0,159,161,1,0,0,0,160,158,1,0,0,0,161,162,5,15,0,0,162,163,
        5,46,0,0,163,167,5,6,0,0,164,166,3,12,6,0,165,164,1,0,0,0,166,169,
        1,0,0,0,167,165,1,0,0,0,167,168,1,0,0,0,168,170,1,0,0,0,169,167,
        1,0,0,0,170,171,5,7,0,0,171,11,1,0,0,0,172,181,3,80,40,0,173,181,
        3,14,7,0,174,181,3,32,16,0,175,181,3,38,19,0,176,181,3,44,22,0,177,
        181,3,60,30,0,178,181,3,46,23,0,179,181,3,50,25,0,180,172,1,0,0,
        0,180,173,1,0,0,0,180,174,1,0,0,0,180,175,1,0,0,0,180,176,1,0,0,
        0,180,177,1,0,0,0,180,178,1,0,0,0,180,179,1,0,0,0,181,13,1,0,0,0,
        182,184,5,48,0,0,183,182,1,0,0,0,184,187,1,0,0,0,185,183,1,0,0,0,
        185,186,1,0,0,0,186,191,1,0,0,0,187,185,1,0,0,0,188,190,3,76,38,
        0,189,188,1,0,0,0,190,193,1,0,0,0,191,189,1,0,0,0,191,192,1,0,0,
        0,192,194,1,0,0,0,193,191,1,0,0,0,194,195,5,25,0,0,195,197,5,46,
        0,0,196,198,3,84,42,0,197,196,1,0,0,0,197,198,1,0,0,0,198,199,1,
        0,0,0,199,203,5,6,0,0,200,202,3,16,8,0,201,200,1,0,0,0,202,205,1,
        0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,206,1,0,0,0,205,203,1,
        0,0,0,206,207,5,7,0,0,207,15,1,0,0,0,208,212,3,18,9,0,209,212,3,
        80,40,0,210,212,3,14,7,0,211,208,1,0,0,0,211,209,1,0,0,0,211,210,
        1,0,0,0,212,17,1,0,0,0,213,215,5,48,0,0,214,213,1,0,0,0,215,218,
        1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,222,1,0,0,0,218,216,
        1,0,0,0,219,221,3,76,38,0,220,219,1,0,0,0,221,224,1,0,0,0,222,220,
        1,0,0,0,222,223,1,0,0,0,223,225,1,0,0,0,224,222,1,0,0,0,225,226,
        5,46,0,0,226,227,5,3,0,0,227,228,3,64,32,0,228,19,1,0,0,0,229,231,
        5,48,0,0,230,229,1,0,0,0,231,234,1,0,0,0,232,230,1,0,0,0,232,233,
        1,0,0,0,233,238,1,0,0,0,234,232,1,0,0,0,235,237,3,76,38,0,236,235,
        1,0,0,0,237,240,1,0,0,0,238,236,1,0,0,0,238,239,1,0,0,0,239,241,
        1,0,0,0,240,238,1,0,0,0,241,242,5,20,0,0,242,244,5,46,0,0,243,245,
        3,84,42,0,244,243,1,0,0,0,244,245,1,0,0,0,245,246,1,0,0,0,246,250,
        5,6,0,0,247,249,3,22,11,0,248,247,1,0,0,0,249,252,1,0,0,0,250,248,
        1,0,0,0,250,251,1,0,0,0,251,253,1,0,0,0,252,250,1,0,0,0,253,254,
        5,7,0,0,254,21,1,0,0,0,255,259,3,24,12,0,256,259,3,80,40,0,257,259,
        3,14,7,0,258,255,1,0,0,0,258,256,1,0,0,0,258,257,1,0,0,0,259,23,
        1,0,0,0,260,262,5,48,0,0,261,260,1,0,0,0,262,265,1,0,0,0,263,261,
        1,0,0,0,263,264,1,0,0,0,264,269,1,0,0,0,265,263,1,0,0,0,266,268,
        3,76,38,0,267,266,1,0,0,0,268,271,1,0,0,0,269,267,1,0,0,0,269,270,
        1,0,0,0,270,272,1,0,0,0,271,269,1,0,0,0,272,273,5,46,0,0,273,274,
        5,3,0,0,274,275,3,64,32,0,275,25,1,0,0,0,276,278,5,48,0,0,277,276,
        1,0,0,0,278,281,1,0,0,0,279,277,1,0,0,0,279,280,1,0,0,0,280,285,
        1,0,0,0,281,279,1,0,0,0,282,284,3,76,38,0,283,282,1,0,0,0,284,287,
        1,0,0,0,285,283,1,0,0,0,285,286,1,0,0,0,286,288,1,0,0,0,287,285,
        1,0,0,0,288,289,5,18,0,0,289,291,5,46,0,0,290,292,3,84,42,0,291,
        290,1,0,0,0,291,292,1,0,0,0,292,293,1,0,0,0,293,297,5,6,0,0,294,
        296,3,28,14,0,295,294,1,0,0,0,296,299,1,0,0,0,297,295,1,0,0,0,297,
        298,1,0,0,0,298,300,1,0,0,0,299,297,1,0,0,0,300,301,5,7,0,0,301,
        27,1,0,0,0,302,306,3,30,15,0,303,306,3,80,40,0,304,306,3,14,7,0,
        305,302,1,0,0,0,305,303,1,0,0,0,305,304,1,0,0,0,306,29,1,0,0,0,307,
        309,5,48,0,0,308,307,1,0,0,0,309,312,1,0,0,0,310,308,1,0,0,0,310,
        311,1,0,0,0,311,316,1,0,0,0,312,310,1,0,0,0,313,315,3,76,38,0,314,
        313,1,0,0,0,315,318,1,0,0,0,316,314,1,0,0,0,316,317,1,0,0,0,317,
        319,1,0,0,0,318,316,1,0,0,0,319,320,5,46,0,0,320,321,5,3,0,0,321,
        322,3,64,32,0,322,31,1,0,0,0,323,325,5,48,0,0,324,323,1,0,0,0,325,
        328,1,0,0,0,326,324,1,0,0,0,326,327,1,0,0,0,327,332,1,0,0,0,328,
        326,1,0,0,0,329,331,3,76,38,0,330,329,1,0,0,0,331,334,1,0,0,0,332,
        330,1,0,0,0,332,333,1,0,0,0,333,335,1,0,0,0,334,332,1,0,0,0,335,
        336,5,14,0,0,336,337,5,46,0,0,337,341,5,6,0,0,338,340,3,34,17,0,
        339,338,1,0,0,0,340,343,1,0,0,0,341,339,1,0,0,0,341,342,1,0,0,0,
        342,344,1,0,0,0,343,341,1,0,0,0,344,345,5,7,0,0,345,33,1,0,0,0,346,
        350,3,36,18,0,347,350,3,80,40,0,348,350,3,14,7,0,349,346,1,0,0,0,
        349,347,1,0,0,0,349,348,1,0,0,0,350,35,1,0,0,0,351,353,5,27,0,0,
        352,351,1,0,0,0,352,353,1,0,0,0,353,354,1,0,0,0,354,355,3,26,13,
        0,355,37,1,0,0,0,356,358,5,48,0,0,357,356,1,0,0,0,358,361,1,0,0,
        0,359,357,1,0,0,0,359,360,1,0,0,0,360,365,1,0,0,0,361,359,1,0,0,
        0,362,364,3,76,38,0,363,362,1,0,0,0,364,367,1,0,0,0,365,363,1,0,
        0,0,365,366,1,0,0,0,366,368,1,0,0,0,367,365,1,0,0,0,368,369,5,26,
        0,0,369,371,5,46,0,0,370,372,3,84,42,0,371,370,1,0,0,0,371,372,1,
        0,0,0,372,373,1,0,0,0,373,377,5,6,0,0,374,376,3,40,20,0,375,374,
        1,0,0,0,376,379,1,0,0,0,377,375,1,0,0,0,377,378,1,0,0,0,378,380,
        1,0,0,0,379,377,1,0,0,0,380,381,5,7,0,0,381,39,1,0,0,0,382,386,3,
        42,21,0,383,386,3,80,40,0,384,386,3,14,7,0,385,382,1,0,0,0,385,383,
        1,0,0,0,385,384,1,0,0,0,386,41,1,0,0,0,387,389,5,48,0,0,388,387,
        1,0,0,0,389,392,1,0,0,0,390,388,1,0,0,0,390,391,1,0,0,0,391,396,
        1,0,0,0,392,390,1,0,0,0,393,395,3,76,38,0,394,393,1,0,0,0,395,398,
        1,0,0,0,396,394,1,0,0,0,396,397,1,0,0,0,397,399,1,0,0,0,398,396,
        1,0,0,0,399,400,5,46,0,0,400,401,5,3,0,0,401,402,3,64,32,0,402,43,
        1,0,0,0,403,405,5,48,0,0,404,403,1,0,0,0,405,408,1,0,0,0,406,404,
        1,0,0,0,406,407,1,0,0,0,407,412,1,0,0,0,408,406,1,0,0,0,409,411,
        3,76,38,0,410,409,1,0,0,0,411,414,1,0,0,0,412,410,1,0,0,0,412,413,
        1,0,0,0,413,415,1,0,0,0,414,412,1,0,0,0,415,416,5,23,0,0,416,417,
        5,46,0,0,417,418,5,3,0,0,418,419,5,46,0,0,419,45,1,0,0,0,420,422,
        5,48,0,0,421,420,1,0,0,0,422,425,1,0,0,0,423,421,1,0,0,0,423,424,
        1,0,0,0,424,429,1,0,0,0,425,423,1,0,0,0,426,428,3,76,38,0,427,426,
        1,0,0,0,428,431,1,0,0,0,429,427,1,0,0,0,429,430,1,0,0,0,430,432,
        1,0,0,0,431,429,1,0,0,0,432,433,5,24,0,0,433,434,5,46,0,0,434,438,
        5,6,0,0,435,437,3,48,24,0,436,435,1,0,0,0,437,440,1,0,0,0,438,436,
        1,0,0,0,438,439,1,0,0,0,439,441,1,0,0,0,440,438,1,0,0,0,441,442,
        5,7,0,0,442,47,1,0,0,0,443,448,3,54,27,0,444,448,3,80,40,0,445,448,
        3,14,7,0,446,448,3,20,10,0,447,443,1,0,0,0,447,444,1,0,0,0,447,445,
        1,0,0,0,447,446,1,0,0,0,448,49,1,0,0,0,449,451,5,48,0,0,450,449,
        1,0,0,0,451,454,1,0,0,0,452,450,1,0,0,0,452,453,1,0,0,0,453,458,
        1,0,0,0,454,452,1,0,0,0,455,457,3,76,38,0,456,455,1,0,0,0,457,460,
        1,0,0,0,458,456,1,0,0,0,458,459,1,0,0,0,459,461,1,0,0,0,460,458,
        1,0,0,0,461,462,5,22,0,0,462,463,5,46,0,0,463,467,5,6,0,0,464,466,
        3,52,26,0,465,464,1,0,0,0,466,469,1,0,0,0,467,465,1,0,0,0,467,468,
        1,0,0,0,468,470,1,0,0,0,469,467,1,0,0,0,470,471,5,7,0,0,471,51,1,
        0,0,0,472,477,3,54,27,0,473,477,3,80,40,0,474,477,3,14,7,0,475,477,
        3,20,10,0,476,472,1,0,0,0,476,473,1,0,0,0,476,474,1,0,0,0,476,475,
        1,0,0,0,477,53,1,0,0,0,478,480,5,48,0,0,479,478,1,0,0,0,480,483,
        1,0,0,0,481,479,1,0,0,0,481,482,1,0,0,0,482,487,1,0,0,0,483,481,
        1,0,0,0,484,486,3,76,38,0,485,484,1,0,0,0,486,489,1,0,0,0,487,485,
        1,0,0,0,487,488,1,0,0,0,488,490,1,0,0,0,489,487,1,0,0,0,490,491,
        5,46,0,0,491,493,5,4,0,0,492,494,3,56,28,0,493,492,1,0,0,0,493,494,
        1,0,0,0,494,499,1,0,0,0,495,496,5,2,0,0,496,498,3,56,28,0,497,495,
        1,0,0,0,498,501,1,0,0,0,499,497,1,0,0,0,499,500,1,0,0,0,500,502,
        1,0,0,0,501,499,1,0,0,0,502,505,5,5,0,0,503,504,5,3,0,0,504,506,
        3,58,29,0,505,503,1,0,0,0,505,506,1,0,0,0,506,511,1,0,0,0,507,508,
        5,12,0,0,508,510,3,58,29,0,509,507,1,0,0,0,510,513,1,0,0,0,511,509,
        1,0,0,0,511,512,1,0,0,0,512,55,1,0,0,0,513,511,1,0,0,0,514,516,5,
        48,0,0,515,514,1,0,0,0,516,519,1,0,0,0,517,515,1,0,0,0,517,518,1,
        0,0,0,518,523,1,0,0,0,519,517,1,0,0,0,520,522,3,76,38,0,521,520,
        1,0,0,0,522,525,1,0,0,0,523,521,1,0,0,0,523,524,1,0,0,0,524,526,
        1,0,0,0,525,523,1,0,0,0,526,527,5,46,0,0,527,528,5,3,0,0,528,529,
        3,64,32,0,529,57,1,0,0,0,530,532,5,48,0,0,531,530,1,0,0,0,532,535,
        1,0,0,0,533,531,1,0,0,0,533,534,1,0,0,0,534,539,1,0,0,0,535,533,
        1,0,0,0,536,538,3,76,38,0,537,536,1,0,0,0,538,541,1,0,0,0,539,537,
        1,0,0,0,539,540,1,0,0,0,540,542,1,0,0,0,541,539,1,0,0,0,542,543,
        3,64,32,0,543,59,1,0,0,0,544,546,5,48,0,0,545,544,1,0,0,0,546,549,
        1,0,0,0,547,545,1,0,0,0,547,548,1,0,0,0,548,553,1,0,0,0,549,547,
        1,0,0,0,550,552,3,76,38,0,551,550,1,0,0,0,552,555,1,0,0,0,553,551,
        1,0,0,0,553,554,1,0,0,0,554,556,1,0,0,0,555,553,1,0,0,0,556,557,
        5,13,0,0,557,558,5,46,0,0,558,562,5,6,0,0,559,561,3,62,31,0,560,
        559,1,0,0,0,561,564,1,0,0,0,562,560,1,0,0,0,562,563,1,0,0,0,563,
        565,1,0,0,0,564,562,1,0,0,0,565,566,5,7,0,0,566,61,1,0,0,0,567,571,
        3,80,40,0,568,571,3,14,7,0,569,571,3,54,27,0,570,567,1,0,0,0,570,
        568,1,0,0,0,570,569,1,0,0,0,571,63,1,0,0,0,572,577,3,66,33,0,573,
        577,3,68,34,0,574,577,3,70,35,0,575,577,3,72,36,0,576,572,1,0,0,
        0,576,573,1,0,0,0,576,574,1,0,0,0,576,575,1,0,0,0,577,65,1,0,0,0,
        578,579,7,0,0,0,579,67,1,0,0,0,580,586,3,74,37,0,581,582,5,42,0,
        0,582,583,5,8,0,0,583,584,5,45,0,0,584,586,5,9,0,0,585,580,1,0,0,
        0,585,581,1,0,0,0,586,69,1,0,0,0,587,588,5,40,0,0,588,589,5,8,0,
        0,589,590,3,64,32,0,590,591,5,9,0,0,591,71,1,0,0,0,592,593,5,41,
        0,0,593,594,5,8,0,0,594,595,3,64,32,0,595,596,5,2,0,0,596,597,3,
        64,32,0,597,598,5,9,0,0,598,73,1,0,0,0,599,604,5,46,0,0,600,601,
        5,1,0,0,601,603,5,46,0,0,602,600,1,0,0,0,603,606,1,0,0,0,604,602,
        1,0,0,0,604,605,1,0,0,0,605,75,1,0,0,0,606,604,1,0,0,0,607,608,5,
        10,0,0,608,623,5,46,0,0,609,610,5,10,0,0,610,611,5,46,0,0,611,612,
        5,4,0,0,612,617,3,78,39,0,613,614,5,2,0,0,614,616,3,78,39,0,615,
        613,1,0,0,0,616,619,1,0,0,0,617,615,1,0,0,0,617,618,1,0,0,0,618,
        620,1,0,0,0,619,617,1,0,0,0,620,621,5,5,0,0,621,623,1,0,0,0,622,
        607,1,0,0,0,622,609,1,0,0,0,623,77,1,0,0,0,624,629,3,74,37,0,625,
        629,5,43,0,0,626,629,5,44,0,0,627,629,5,45,0,0,628,624,1,0,0,0,628,
        625,1,0,0,0,628,626,1,0,0,0,628,627,1,0,0,0,629,79,1,0,0,0,630,632,
        5,48,0,0,631,630,1,0,0,0,632,635,1,0,0,0,633,631,1,0,0,0,633,634,
        1,0,0,0,634,639,1,0,0,0,635,633,1,0,0,0,636,638,3,76,38,0,637,636,
        1,0,0,0,638,641,1,0,0,0,639,637,1,0,0,0,639,640,1,0,0,0,640,642,
        1,0,0,0,641,639,1,0,0,0,642,643,5,19,0,0,643,644,5,46,0,0,644,646,
        5,6,0,0,645,647,3,82,41,0,646,645,1,0,0,0,646,647,1,0,0,0,647,652,
        1,0,0,0,648,649,5,2,0,0,649,651,3,82,41,0,650,648,1,0,0,0,651,654,
        1,0,0,0,652,650,1,0,0,0,652,653,1,0,0,0,653,655,1,0,0,0,654,652,
        1,0,0,0,655,656,5,7,0,0,656,81,1,0,0,0,657,659,5,48,0,0,658,657,
        1,0,0,0,659,662,1,0,0,0,660,658,1,0,0,0,660,661,1,0,0,0,661,666,
        1,0,0,0,662,660,1,0,0,0,663,665,3,76,38,0,664,663,1,0,0,0,665,668,
        1,0,0,0,666,664,1,0,0,0,666,667,1,0,0,0,667,669,1,0,0,0,668,666,
        1,0,0,0,669,670,5,46,0,0,670,83,1,0,0,0,671,672,5,28,0,0,672,677,
        3,74,37,0,673,674,5,2,0,0,674,676,3,74,37,0,675,673,1,0,0,0,676,
        679,1,0,0,0,677,675,1,0,0,0,677,678,1,0,0,0,678,85,1,0,0,0,679,677,
        1,0,0,0,82,89,95,103,112,118,124,133,141,152,158,167,180,185,191,
        197,203,211,216,222,232,238,244,250,258,263,269,279,285,291,297,
        305,310,316,326,332,341,349,352,359,365,371,377,385,390,396,406,
        412,423,429,438,447,452,458,467,476,481,487,493,499,505,511,517,
        523,533,539,547,553,562,570,576,585,604,617,622,628,633,639,646,
        652,660,666,677
    ]

class d3iGrammar ( Parser ):

    grammarFileName = "d3iGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "','", "':'", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "'@'", "'=>'", "'|'", "'acl'", 
                     "'aggregate'", "'context'", "'composit'", "'domain'", 
                     "'entity'", "'enum'", "'event'", "'import'", "'interface'", 
                     "'repository'", "'service'", "'valueobject'", "'view'", 
                     "'root'", "'inherits'", "'integer'", "'number'", "'float'", 
                     "'date'", "'time'", "'dateTime'", "'string'", "'boolean'", 
                     "'bytes'", "'stream'", "'any'", "'list'", "'map'", 
                     "'external'" ]

    symbolicNames = [ "<INVALID>", "DOT", "COMMA", "SEMI", "LPAREN", "RPAREN", 
                      "LCURLY", "RCURLY", "LBARCKET", "RBRACKET", "AT", 
                      "ARROW", "PIPE", "ACL", "AGGREGATE", "CONTEXT", "COMPOSIT", 
                      "DOMAIN", "ENTITY", "ENUM", "EVENT", "IMPORT", "INTERFACE", 
                      "REPOSITORY", "SERVICE", "VALUEOBJECT", "VIEW", "ROOT", 
                      "INHERITS", "INTEGER", "NUMBER", "FLOAT", "DATE", 
                      "TIME", "DATETIME", "STRING", "BOOLEAN", "BYTES", 
                      "STREAM", "ANY", "LIST", "MAP", "EXTERNAL", "INTEGER_CONSTANS", 
                      "NUMBER_CONSTANS", "STRING_LITERAL", "IDENTIFIER", 
                      "WS", "DOCUMENT_LINE", "LINE_COMMENT", "BLOCK_COMMENT" ]

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
    RULE_event = 10
    RULE_event_element = 11
    RULE_event_member = 12
    RULE_entity = 13
    RULE_entity_element = 14
    RULE_entity_member = 15
    RULE_aggregate = 16
    RULE_aggregate_element = 17
    RULE_aggregate_entity = 18
    RULE_view = 19
    RULE_view_element = 20
    RULE_view_member = 21
    RULE_repository = 22
    RULE_service = 23
    RULE_service_element = 24
    RULE_interface = 25
    RULE_interface_element = 26
    RULE_operation = 27
    RULE_operation_param = 28
    RULE_operation_return = 29
    RULE_acl = 30
    RULE_acl_element = 31
    RULE_type = 32
    RULE_primitive_type = 33
    RULE_reference_type = 34
    RULE_list_type = 35
    RULE_map_type = 36
    RULE_qualifiedName = 37
    RULE_decorator = 38
    RULE_decorator_param = 39
    RULE_enum = 40
    RULE_enum_element = 41
    RULE_inherits = 42

    ruleNames =  [ "d3", "import_rule", "domain", "directive", "domain_element", 
                   "context", "context_element", "value_object", "value_object_element", 
                   "value_object_member", "event", "event_element", "event_member", 
                   "entity", "entity_element", "entity_member", "aggregate", 
                   "aggregate_element", "aggregate_entity", "view", "view_element", 
                   "view_member", "repository", "service", "service_element", 
                   "interface", "interface_element", "operation", "operation_param", 
                   "operation_return", "acl", "acl_element", "type", "primitive_type", 
                   "reference_type", "list_type", "map_type", "qualifiedName", 
                   "decorator", "decorator_param", "enum", "enum_element", 
                   "inherits" ]

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
    COMPOSIT=16
    DOMAIN=17
    ENTITY=18
    ENUM=19
    EVENT=20
    IMPORT=21
    INTERFACE=22
    REPOSITORY=23
    SERVICE=24
    VALUEOBJECT=25
    VIEW=26
    ROOT=27
    INHERITS=28
    INTEGER=29
    NUMBER=30
    FLOAT=31
    DATE=32
    TIME=33
    DATETIME=34
    STRING=35
    BOOLEAN=36
    BYTES=37
    STREAM=38
    ANY=39
    LIST=40
    MAP=41
    EXTERNAL=42
    INTEGER_CONSTANS=43
    NUMBER_CONSTANS=44
    STRING_LITERAL=45
    IDENTIFIER=46
    WS=47
    DOCUMENT_LINE=48
    LINE_COMMENT=49
    BLOCK_COMMENT=50

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
            self.state = 89
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 86
                    self.import_rule() 
                self.state = 91
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 351843721020416) != 0):
                self.state = 92
                self.domain()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
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
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 100
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.match(d3iGrammar.IMPORT)
            self.state = 107
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
            self.state = 112
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 109
                    self.directive() 
                self.state = 114
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 115
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 121
                self.decorator()
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
            self.match(d3iGrammar.DOMAIN)
            self.state = 128
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 129
            self.match(d3iGrammar.LCURLY)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 281474976744448) != 0):
                self.state = 130
                self.domain_element()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 136
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
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 138
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 144
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 145
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
            self.state = 147
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
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 149
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 155
                self.decorator()
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 161
            self.match(d3iGrammar.CONTEXT)
            self.state = 162
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 163
            self.match(d3iGrammar.LCURLY)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 281475107283968) != 0):
                self.state = 164
                self.context_element()
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 170
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
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.enum()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.value_object()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 174
                self.aggregate()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 175
                self.view()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 176
                self.repository()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 177
                self.acl()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 178
                self.service()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 179
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
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 182
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 188
                self.decorator()
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 194
            self.match(d3iGrammar.VALUEOBJECT)
            self.state = 195
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 196
                self.inherits()


            self.state = 199
            self.match(d3iGrammar.LCURLY)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 351843754968064) != 0):
                self.state = 200
                self.value_object_element()
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 206
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
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.value_object_member()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 210
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
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 213
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 219
                self.decorator()
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 225
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 226
            self.match(d3iGrammar.SEMI)
            self.state = 227
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
        self.enterRule(localctx, 20, self.RULE_event)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 229
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 235
                self.decorator()
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 241
            self.match(d3iGrammar.EVENT)
            self.state = 242
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 243
                self.inherits()


            self.state = 246
            self.match(d3iGrammar.LCURLY)
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 351843754968064) != 0):
                self.state = 247
                self.event_element()
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 253
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


        def value_object(self):
            return self.getTypedRuleContext(d3iGrammar.Value_objectContext,0)


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
        self.enterRule(localctx, 22, self.RULE_event_element)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.event_member()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 257
                self.value_object()
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
        self.enterRule(localctx, 24, self.RULE_event_member)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 260
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 266
                self.decorator()
                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 272
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 273
            self.match(d3iGrammar.SEMI)
            self.state = 274
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
        self.enterRule(localctx, 26, self.RULE_entity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 276
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 281
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 282
                self.decorator()
                self.state = 287
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 288
            self.match(d3iGrammar.ENTITY)
            self.state = 289
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 290
                self.inherits()


            self.state = 293
            self.match(d3iGrammar.LCURLY)
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 351843754968064) != 0):
                self.state = 294
                self.entity_element()
                self.state = 299
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 300
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
        self.enterRule(localctx, 28, self.RULE_entity_element)
        try:
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.entity_member()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 304
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
        self.enterRule(localctx, 30, self.RULE_entity_member)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 307
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 316
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 313
                self.decorator()
                self.state = 318
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 319
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 320
            self.match(d3iGrammar.SEMI)
            self.state = 321
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
        self.enterRule(localctx, 32, self.RULE_aggregate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 323
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 328
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 329
                self.decorator()
                self.state = 334
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 335
            self.match(d3iGrammar.AGGREGATE)
            self.state = 336
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 337
            self.match(d3iGrammar.LCURLY)
            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 281475145270272) != 0):
                self.state = 338
                self.aggregate_element()
                self.state = 343
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 344
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
        self.enterRule(localctx, 34, self.RULE_aggregate_element)
        try:
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.aggregate_entity()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 348
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
        self.enterRule(localctx, 36, self.RULE_aggregate_entity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 351
                self.match(d3iGrammar.ROOT)


            self.state = 354
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
        self.enterRule(localctx, 38, self.RULE_view)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 356
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 361
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 365
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 362
                self.decorator()
                self.state = 367
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 368
            self.match(d3iGrammar.VIEW)
            self.state = 369
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 371
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 370
                self.inherits()


            self.state = 373
            self.match(d3iGrammar.LCURLY)
            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 351843754968064) != 0):
                self.state = 374
                self.view_element()
                self.state = 379
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 380
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


        def value_object(self):
            return self.getTypedRuleContext(d3iGrammar.Value_objectContext,0)


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
        self.enterRule(localctx, 40, self.RULE_view_element)
        try:
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.view_member()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 384
                self.value_object()
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
        self.enterRule(localctx, 42, self.RULE_view_member)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 387
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 392
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 396
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 393
                self.decorator()
                self.state = 398
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 399
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 400
            self.match(d3iGrammar.SEMI)
            self.state = 401
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
        self.enterRule(localctx, 44, self.RULE_repository)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 403
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 408
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 412
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 409
                self.decorator()
                self.state = 414
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 415
            self.match(d3iGrammar.REPOSITORY)
            self.state = 416
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 417
            self.match(d3iGrammar.SEMI)
            self.state = 418
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
        self.enterRule(localctx, 46, self.RULE_service)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 420
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 425
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 429
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 426
                self.decorator()
                self.state = 431
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 432
            self.match(d3iGrammar.SERVICE)
            self.state = 433
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 434
            self.match(d3iGrammar.LCURLY)
            self.state = 438
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 351843756016640) != 0):
                self.state = 435
                self.service_element()
                self.state = 440
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 441
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
        self.enterRule(localctx, 48, self.RULE_service_element)
        try:
            self.state = 447
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 443
                self.operation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 444
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 445
                self.value_object()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 446
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
        self.enterRule(localctx, 50, self.RULE_interface)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 449
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 454
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 458
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 455
                self.decorator()
                self.state = 460
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 461
            self.match(d3iGrammar.INTERFACE)
            self.state = 462
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 463
            self.match(d3iGrammar.LCURLY)
            self.state = 467
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 351843756016640) != 0):
                self.state = 464
                self.interface_element()
                self.state = 469
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 470
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


        def value_object(self):
            return self.getTypedRuleContext(d3iGrammar.Value_objectContext,0)


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
        self.enterRule(localctx, 52, self.RULE_interface_element)
        try:
            self.state = 476
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 472
                self.operation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 473
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 474
                self.value_object()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 475
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
        self.enterRule(localctx, 54, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 478
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 483
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 487
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 484
                self.decorator()
                self.state = 489
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 490
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 491
            self.match(d3iGrammar.LPAREN)

            self.state = 493
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 351843720889344) != 0):
                self.state = 492
                self.operation_param()


            self.state = 499
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 495
                self.match(d3iGrammar.COMMA)
                self.state = 496
                self.operation_param()
                self.state = 501
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 502
            self.match(d3iGrammar.RPAREN)

            self.state = 505
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 503
                self.match(d3iGrammar.SEMI)
                self.state = 504
                self.operation_return()


            self.state = 511
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 507
                self.match(d3iGrammar.PIPE)
                self.state = 508
                self.operation_return()
                self.state = 513
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
        self.enterRule(localctx, 56, self.RULE_operation_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 514
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 519
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 523
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 520
                self.decorator()
                self.state = 525
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 526
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 527
            self.match(d3iGrammar.SEMI)
            self.state = 528
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
        self.enterRule(localctx, 58, self.RULE_operation_return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 530
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 535
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 539
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 536
                self.decorator()
                self.state = 541
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 542
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
        self.enterRule(localctx, 60, self.RULE_acl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 544
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 549
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 553
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 550
                self.decorator()
                self.state = 555
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 556
            self.match(d3iGrammar.ACL)
            self.state = 557
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 558
            self.match(d3iGrammar.LCURLY)
            self.state = 562
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 351843754968064) != 0):
                self.state = 559
                self.acl_element()
                self.state = 564
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 565
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
        self.enterRule(localctx, 62, self.RULE_acl_element)
        try:
            self.state = 570
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 567
                self.enum()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 568
                self.value_object()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 569
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
        self.enterRule(localctx, 64, self.RULE_type)
        try:
            self.state = 576
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 572
                self.primitive_type()
                pass
            elif token in [42, 46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 573
                self.reference_type()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 3)
                self.state = 574
                self.list_type()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 4)
                self.state = 575
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
        self.enterRule(localctx, 66, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 578
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1098974756864) != 0)):
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
        self.enterRule(localctx, 68, self.RULE_reference_type)
        try:
            self.state = 585
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 580
                self.qualifiedName()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 581
                self.match(d3iGrammar.EXTERNAL)
                self.state = 582
                self.match(d3iGrammar.LBARCKET)
                self.state = 583
                self.match(d3iGrammar.STRING_LITERAL)
                self.state = 584
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
        self.enterRule(localctx, 70, self.RULE_list_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 587
            self.match(d3iGrammar.LIST)
            self.state = 588
            self.match(d3iGrammar.LBARCKET)
            self.state = 589
            self.type_()
            self.state = 590
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
        self.enterRule(localctx, 72, self.RULE_map_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            self.match(d3iGrammar.MAP)
            self.state = 593
            self.match(d3iGrammar.LBARCKET)
            self.state = 594
            self.type_()
            self.state = 595
            self.match(d3iGrammar.COMMA)
            self.state = 596
            self.type_()
            self.state = 597
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
        self.enterRule(localctx, 74, self.RULE_qualifiedName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 599
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 604
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 600
                self.match(d3iGrammar.DOT)
                self.state = 601
                self.match(d3iGrammar.IDENTIFIER)
                self.state = 606
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
        self.enterRule(localctx, 76, self.RULE_decorator)
        self._la = 0 # Token type
        try:
            self.state = 622
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,73,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 607
                self.match(d3iGrammar.AT)
                self.state = 608
                self.match(d3iGrammar.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 609
                self.match(d3iGrammar.AT)
                self.state = 610
                self.match(d3iGrammar.IDENTIFIER)
                self.state = 611
                self.match(d3iGrammar.LPAREN)
                self.state = 612
                self.decorator_param()
                self.state = 617
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 613
                    self.match(d3iGrammar.COMMA)
                    self.state = 614
                    self.decorator_param()
                    self.state = 619
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 620
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
        self.enterRule(localctx, 78, self.RULE_decorator_param)
        try:
            self.state = 628
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 624
                self.qualifiedName()
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 625
                self.match(d3iGrammar.INTEGER_CONSTANS)
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 3)
                self.state = 626
                self.match(d3iGrammar.NUMBER_CONSTANS)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 4)
                self.state = 627
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
        self.enterRule(localctx, 80, self.RULE_enum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 633
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 630
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 635
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 639
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 636
                self.decorator()
                self.state = 641
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 642
            self.match(d3iGrammar.ENUM)
            self.state = 643
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 644
            self.match(d3iGrammar.LCURLY)
            self.state = 646
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 351843720889344) != 0):
                self.state = 645
                self.enum_element()


            self.state = 652
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 648
                self.match(d3iGrammar.COMMA)
                self.state = 649
                self.enum_element()
                self.state = 654
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 655
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
        self.enterRule(localctx, 82, self.RULE_enum_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 660
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 657
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 662
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 666
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 663
                self.decorator()
                self.state = 668
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 669
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
        self.enterRule(localctx, 84, self.RULE_inherits)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 671
            self.match(d3iGrammar.INHERITS)
            self.state = 672
            self.qualifiedName()
            self.state = 677
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 673
                self.match(d3iGrammar.COMMA)
                self.state = 674
                self.qualifiedName()
                self.state = 679
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





