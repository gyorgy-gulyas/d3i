# Generated from ./parser/grammar/d3iGrammar.g4 by ANTLR 4.13.2
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
        4,1,41,497,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,1,0,5,0,72,8,0,10,0,12,0,75,9,0,1,0,5,0,78,8,0,10,
        0,12,0,81,9,0,1,0,1,0,1,1,1,1,1,1,1,2,5,2,89,8,2,10,2,12,2,92,9,
        2,1,2,1,2,1,2,1,2,5,2,98,8,2,10,2,12,2,101,9,2,1,2,1,2,1,3,1,3,3,
        3,107,8,3,1,4,5,4,110,8,4,10,4,12,4,113,9,4,1,4,1,4,1,4,1,4,5,4,
        119,8,4,10,4,12,4,122,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,3,5,135,8,5,1,6,5,6,138,8,6,10,6,12,6,141,9,6,1,6,1,6,1,6,
        1,6,5,6,147,8,6,10,6,12,6,150,9,6,1,6,1,6,1,7,5,7,155,8,7,10,7,12,
        7,158,9,7,1,7,1,7,1,7,1,7,1,7,3,7,165,8,7,1,8,5,8,168,8,8,10,8,12,
        8,171,9,8,1,8,1,8,1,8,1,8,5,8,177,8,8,10,8,12,8,180,9,8,1,8,1,8,
        1,9,5,9,185,8,9,10,9,12,9,188,9,9,1,9,1,9,1,9,1,9,1,9,3,9,195,8,
        9,1,10,5,10,198,8,10,10,10,12,10,201,9,10,1,10,1,10,1,10,1,10,5,
        10,207,8,10,10,10,12,10,210,9,10,1,10,1,10,1,11,5,11,215,8,11,10,
        11,12,11,218,9,11,1,11,1,11,1,11,1,11,1,11,3,11,225,8,11,1,12,5,
        12,228,8,12,10,12,12,12,231,9,12,1,12,1,12,1,12,1,12,5,12,237,8,
        12,10,12,12,12,240,9,12,1,12,1,12,1,13,3,13,245,8,13,1,13,1,13,1,
        13,3,13,250,8,13,1,14,5,14,253,8,14,10,14,12,14,256,9,14,1,14,1,
        14,1,14,1,14,1,14,1,15,5,15,264,8,15,10,15,12,15,267,9,15,1,15,1,
        15,1,15,1,15,5,15,273,8,15,10,15,12,15,276,9,15,1,15,1,15,1,16,1,
        16,1,16,3,16,283,8,16,1,17,5,17,286,8,17,10,17,12,17,289,9,17,1,
        17,1,17,1,17,1,17,5,17,295,8,17,10,17,12,17,298,9,17,1,17,1,17,1,
        18,1,18,1,18,3,18,305,8,18,1,19,5,19,308,8,19,10,19,12,19,311,9,
        19,1,19,1,19,1,19,3,19,316,8,19,1,19,1,19,5,19,320,8,19,10,19,12,
        19,323,9,19,1,19,1,19,3,19,327,8,19,1,20,5,20,330,8,20,10,20,12,
        20,333,9,20,1,20,1,20,1,20,1,20,1,21,1,21,5,21,341,8,21,10,21,12,
        21,344,9,21,1,21,1,21,1,21,5,21,349,8,21,10,21,12,21,352,9,21,1,
        21,5,21,355,8,21,10,21,12,21,358,9,21,1,22,5,22,361,8,22,10,22,12,
        22,364,9,22,1,22,1,22,1,22,1,22,5,22,370,8,22,10,22,12,22,373,9,
        22,1,22,1,22,1,23,1,23,1,23,3,23,380,8,23,1,24,5,24,383,8,24,10,
        24,12,24,386,9,24,1,24,1,24,1,24,3,24,391,8,24,1,24,1,24,5,24,395,
        8,24,10,24,12,24,398,9,24,1,24,1,24,1,24,1,24,1,25,5,25,405,8,25,
        10,25,12,25,408,9,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,3,26,417,
        8,26,1,27,1,27,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,3,29,437,8,29,1,30,1,30,1,30,5,30,
        442,8,30,10,30,12,30,445,9,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,
        1,31,5,31,455,8,31,10,31,12,31,458,9,31,1,31,1,31,3,31,462,8,31,
        1,32,1,32,1,32,1,32,3,32,468,8,32,1,33,5,33,471,8,33,10,33,12,33,
        474,9,33,1,33,1,33,1,33,1,33,1,33,1,33,5,33,482,8,33,10,33,12,33,
        485,9,33,1,33,1,33,1,34,5,34,490,8,34,10,34,12,34,493,9,34,1,34,
        1,34,1,34,0,0,35,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,0,1,1,0,24,32,
        533,0,73,1,0,0,0,2,84,1,0,0,0,4,90,1,0,0,0,6,106,1,0,0,0,8,111,1,
        0,0,0,10,134,1,0,0,0,12,139,1,0,0,0,14,164,1,0,0,0,16,169,1,0,0,
        0,18,194,1,0,0,0,20,199,1,0,0,0,22,224,1,0,0,0,24,229,1,0,0,0,26,
        249,1,0,0,0,28,254,1,0,0,0,30,265,1,0,0,0,32,282,1,0,0,0,34,287,
        1,0,0,0,36,304,1,0,0,0,38,309,1,0,0,0,40,331,1,0,0,0,42,338,1,0,
        0,0,44,362,1,0,0,0,46,379,1,0,0,0,48,384,1,0,0,0,50,406,1,0,0,0,
        52,416,1,0,0,0,54,418,1,0,0,0,56,420,1,0,0,0,58,436,1,0,0,0,60,438,
        1,0,0,0,62,461,1,0,0,0,64,467,1,0,0,0,66,472,1,0,0,0,68,491,1,0,
        0,0,70,72,3,2,1,0,71,70,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,
        1,0,0,0,74,79,1,0,0,0,75,73,1,0,0,0,76,78,3,4,2,0,77,76,1,0,0,0,
        78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,82,1,0,0,0,81,79,1,
        0,0,0,82,83,5,0,0,1,83,1,1,0,0,0,84,85,5,38,0,0,85,86,3,60,30,0,
        86,3,1,0,0,0,87,89,3,62,31,0,88,87,1,0,0,0,89,92,1,0,0,0,90,88,1,
        0,0,0,90,91,1,0,0,0,91,93,1,0,0,0,92,90,1,0,0,0,93,94,5,12,0,0,94,
        95,5,38,0,0,95,99,5,6,0,0,96,98,3,6,3,0,97,96,1,0,0,0,98,101,1,0,
        0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,102,1,0,0,0,101,99,1,0,0,0,
        102,103,5,7,0,0,103,5,1,0,0,0,104,107,3,8,4,0,105,107,3,16,8,0,106,
        104,1,0,0,0,106,105,1,0,0,0,107,7,1,0,0,0,108,110,3,62,31,0,109,
        108,1,0,0,0,110,113,1,0,0,0,111,109,1,0,0,0,111,112,1,0,0,0,112,
        114,1,0,0,0,113,111,1,0,0,0,114,115,5,13,0,0,115,116,5,38,0,0,116,
        120,5,6,0,0,117,119,3,10,5,0,118,117,1,0,0,0,119,122,1,0,0,0,120,
        118,1,0,0,0,120,121,1,0,0,0,121,123,1,0,0,0,122,120,1,0,0,0,123,
        124,5,7,0,0,124,9,1,0,0,0,125,135,3,20,10,0,126,135,3,66,33,0,127,
        135,3,12,6,0,128,135,3,24,12,0,129,135,3,28,14,0,130,135,3,44,22,
        0,131,135,3,16,8,0,132,135,3,30,15,0,133,135,3,34,17,0,134,125,1,
        0,0,0,134,126,1,0,0,0,134,127,1,0,0,0,134,128,1,0,0,0,134,129,1,
        0,0,0,134,130,1,0,0,0,134,131,1,0,0,0,134,132,1,0,0,0,134,133,1,
        0,0,0,135,11,1,0,0,0,136,138,3,62,31,0,137,136,1,0,0,0,138,141,1,
        0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,142,1,0,0,0,141,139,1,
        0,0,0,142,143,5,20,0,0,143,144,5,38,0,0,144,148,5,6,0,0,145,147,
        3,14,7,0,146,145,1,0,0,0,147,150,1,0,0,0,148,146,1,0,0,0,148,149,
        1,0,0,0,149,151,1,0,0,0,150,148,1,0,0,0,151,152,5,7,0,0,152,13,1,
        0,0,0,153,155,3,62,31,0,154,153,1,0,0,0,155,158,1,0,0,0,156,154,
        1,0,0,0,156,157,1,0,0,0,157,159,1,0,0,0,158,156,1,0,0,0,159,160,
        5,38,0,0,160,161,5,3,0,0,161,165,3,52,26,0,162,165,3,66,33,0,163,
        165,3,12,6,0,164,156,1,0,0,0,164,162,1,0,0,0,164,163,1,0,0,0,165,
        15,1,0,0,0,166,168,3,62,31,0,167,166,1,0,0,0,168,171,1,0,0,0,169,
        167,1,0,0,0,169,170,1,0,0,0,170,172,1,0,0,0,171,169,1,0,0,0,172,
        173,5,14,0,0,173,174,5,38,0,0,174,178,5,6,0,0,175,177,3,18,9,0,176,
        175,1,0,0,0,177,180,1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,
        181,1,0,0,0,180,178,1,0,0,0,181,182,5,7,0,0,182,17,1,0,0,0,183,185,
        3,62,31,0,184,183,1,0,0,0,185,188,1,0,0,0,186,184,1,0,0,0,186,187,
        1,0,0,0,187,189,1,0,0,0,188,186,1,0,0,0,189,190,5,38,0,0,190,191,
        5,3,0,0,191,195,3,52,26,0,192,195,3,66,33,0,193,195,3,12,6,0,194,
        186,1,0,0,0,194,192,1,0,0,0,194,193,1,0,0,0,195,19,1,0,0,0,196,198,
        3,62,31,0,197,196,1,0,0,0,198,201,1,0,0,0,199,197,1,0,0,0,199,200,
        1,0,0,0,200,202,1,0,0,0,201,199,1,0,0,0,202,203,5,15,0,0,203,204,
        5,38,0,0,204,208,5,6,0,0,205,207,3,22,11,0,206,205,1,0,0,0,207,210,
        1,0,0,0,208,206,1,0,0,0,208,209,1,0,0,0,209,211,1,0,0,0,210,208,
        1,0,0,0,211,212,5,7,0,0,212,21,1,0,0,0,213,215,3,62,31,0,214,213,
        1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,219,
        1,0,0,0,218,216,1,0,0,0,219,220,5,38,0,0,220,221,5,3,0,0,221,225,
        3,52,26,0,222,225,3,66,33,0,223,225,3,12,6,0,224,216,1,0,0,0,224,
        222,1,0,0,0,224,223,1,0,0,0,225,23,1,0,0,0,226,228,3,62,31,0,227,
        226,1,0,0,0,228,231,1,0,0,0,229,227,1,0,0,0,229,230,1,0,0,0,230,
        232,1,0,0,0,231,229,1,0,0,0,232,233,5,16,0,0,233,234,5,38,0,0,234,
        238,5,6,0,0,235,237,3,26,13,0,236,235,1,0,0,0,237,240,1,0,0,0,238,
        236,1,0,0,0,238,239,1,0,0,0,239,241,1,0,0,0,240,238,1,0,0,0,241,
        242,5,7,0,0,242,25,1,0,0,0,243,245,5,23,0,0,244,243,1,0,0,0,244,
        245,1,0,0,0,245,246,1,0,0,0,246,250,3,20,10,0,247,250,3,66,33,0,
        248,250,3,12,6,0,249,244,1,0,0,0,249,247,1,0,0,0,249,248,1,0,0,0,
        250,27,1,0,0,0,251,253,3,62,31,0,252,251,1,0,0,0,253,256,1,0,0,0,
        254,252,1,0,0,0,254,255,1,0,0,0,255,257,1,0,0,0,256,254,1,0,0,0,
        257,258,5,22,0,0,258,259,5,38,0,0,259,260,5,3,0,0,260,261,5,38,0,
        0,261,29,1,0,0,0,262,264,3,62,31,0,263,262,1,0,0,0,264,267,1,0,0,
        0,265,263,1,0,0,0,265,266,1,0,0,0,266,268,1,0,0,0,267,265,1,0,0,
        0,268,269,5,17,0,0,269,270,5,38,0,0,270,274,5,6,0,0,271,273,3,32,
        16,0,272,271,1,0,0,0,273,276,1,0,0,0,274,272,1,0,0,0,274,275,1,0,
        0,0,275,277,1,0,0,0,276,274,1,0,0,0,277,278,5,7,0,0,278,31,1,0,0,
        0,279,283,3,38,19,0,280,283,3,66,33,0,281,283,3,12,6,0,282,279,1,
        0,0,0,282,280,1,0,0,0,282,281,1,0,0,0,283,33,1,0,0,0,284,286,3,62,
        31,0,285,284,1,0,0,0,286,289,1,0,0,0,287,285,1,0,0,0,287,288,1,0,
        0,0,288,290,1,0,0,0,289,287,1,0,0,0,290,291,5,18,0,0,291,292,5,38,
        0,0,292,296,5,6,0,0,293,295,3,36,18,0,294,293,1,0,0,0,295,298,1,
        0,0,0,296,294,1,0,0,0,296,297,1,0,0,0,297,299,1,0,0,0,298,296,1,
        0,0,0,299,300,5,7,0,0,300,35,1,0,0,0,301,305,3,38,19,0,302,305,3,
        66,33,0,303,305,3,12,6,0,304,301,1,0,0,0,304,302,1,0,0,0,304,303,
        1,0,0,0,305,37,1,0,0,0,306,308,3,62,31,0,307,306,1,0,0,0,308,311,
        1,0,0,0,309,307,1,0,0,0,309,310,1,0,0,0,310,312,1,0,0,0,311,309,
        1,0,0,0,312,313,5,38,0,0,313,315,5,4,0,0,314,316,3,40,20,0,315,314,
        1,0,0,0,315,316,1,0,0,0,316,321,1,0,0,0,317,318,5,2,0,0,318,320,
        3,40,20,0,319,317,1,0,0,0,320,323,1,0,0,0,321,319,1,0,0,0,321,322,
        1,0,0,0,322,324,1,0,0,0,323,321,1,0,0,0,324,326,5,5,0,0,325,327,
        3,42,21,0,326,325,1,0,0,0,326,327,1,0,0,0,327,39,1,0,0,0,328,330,
        3,62,31,0,329,328,1,0,0,0,330,333,1,0,0,0,331,329,1,0,0,0,331,332,
        1,0,0,0,332,334,1,0,0,0,333,331,1,0,0,0,334,335,5,38,0,0,335,336,
        5,3,0,0,336,337,3,52,26,0,337,41,1,0,0,0,338,342,5,3,0,0,339,341,
        3,62,31,0,340,339,1,0,0,0,341,344,1,0,0,0,342,340,1,0,0,0,342,343,
        1,0,0,0,343,345,1,0,0,0,344,342,1,0,0,0,345,356,3,52,26,0,346,350,
        5,11,0,0,347,349,3,62,31,0,348,347,1,0,0,0,349,352,1,0,0,0,350,348,
        1,0,0,0,350,351,1,0,0,0,351,353,1,0,0,0,352,350,1,0,0,0,353,355,
        3,52,26,0,354,346,1,0,0,0,355,358,1,0,0,0,356,354,1,0,0,0,356,357,
        1,0,0,0,357,43,1,0,0,0,358,356,1,0,0,0,359,361,3,62,31,0,360,359,
        1,0,0,0,361,364,1,0,0,0,362,360,1,0,0,0,362,363,1,0,0,0,363,365,
        1,0,0,0,364,362,1,0,0,0,365,366,5,19,0,0,366,367,5,38,0,0,367,371,
        5,6,0,0,368,370,3,46,23,0,369,368,1,0,0,0,370,373,1,0,0,0,371,369,
        1,0,0,0,371,372,1,0,0,0,372,374,1,0,0,0,373,371,1,0,0,0,374,375,
        5,7,0,0,375,45,1,0,0,0,376,380,3,66,33,0,377,380,3,12,6,0,378,380,
        3,48,24,0,379,376,1,0,0,0,379,377,1,0,0,0,379,378,1,0,0,0,380,47,
        1,0,0,0,381,383,3,62,31,0,382,381,1,0,0,0,383,386,1,0,0,0,384,382,
        1,0,0,0,384,385,1,0,0,0,385,387,1,0,0,0,386,384,1,0,0,0,387,388,
        5,38,0,0,388,390,5,4,0,0,389,391,3,50,25,0,390,389,1,0,0,0,390,391,
        1,0,0,0,391,396,1,0,0,0,392,393,5,2,0,0,393,395,3,50,25,0,394,392,
        1,0,0,0,395,398,1,0,0,0,396,394,1,0,0,0,396,397,1,0,0,0,397,399,
        1,0,0,0,398,396,1,0,0,0,399,400,5,5,0,0,400,401,5,3,0,0,401,402,
        3,52,26,0,402,49,1,0,0,0,403,405,3,62,31,0,404,403,1,0,0,0,405,408,
        1,0,0,0,406,404,1,0,0,0,406,407,1,0,0,0,407,409,1,0,0,0,408,406,
        1,0,0,0,409,410,5,38,0,0,410,411,5,3,0,0,411,412,3,52,26,0,412,51,
        1,0,0,0,413,417,3,54,27,0,414,417,3,56,28,0,415,417,3,58,29,0,416,
        413,1,0,0,0,416,414,1,0,0,0,416,415,1,0,0,0,417,53,1,0,0,0,418,419,
        7,0,0,0,419,55,1,0,0,0,420,421,3,60,30,0,421,57,1,0,0,0,422,423,
        5,33,0,0,423,424,5,8,0,0,424,425,3,52,26,0,425,426,5,2,0,0,426,427,
        3,52,26,0,427,428,5,9,0,0,428,437,1,0,0,0,429,430,5,34,0,0,430,431,
        5,8,0,0,431,432,3,52,26,0,432,433,5,2,0,0,433,434,3,52,26,0,434,
        435,5,9,0,0,435,437,1,0,0,0,436,422,1,0,0,0,436,429,1,0,0,0,437,
        59,1,0,0,0,438,443,5,38,0,0,439,440,5,1,0,0,440,442,5,38,0,0,441,
        439,1,0,0,0,442,445,1,0,0,0,443,441,1,0,0,0,443,444,1,0,0,0,444,
        61,1,0,0,0,445,443,1,0,0,0,446,447,5,10,0,0,447,462,5,38,0,0,448,
        449,5,10,0,0,449,450,5,38,0,0,450,451,5,4,0,0,451,456,3,64,32,0,
        452,453,5,2,0,0,453,455,3,64,32,0,454,452,1,0,0,0,455,458,1,0,0,
        0,456,454,1,0,0,0,456,457,1,0,0,0,457,459,1,0,0,0,458,456,1,0,0,
        0,459,460,5,5,0,0,460,462,1,0,0,0,461,446,1,0,0,0,461,448,1,0,0,
        0,462,63,1,0,0,0,463,468,3,60,30,0,464,468,5,35,0,0,465,468,5,36,
        0,0,466,468,5,37,0,0,467,463,1,0,0,0,467,464,1,0,0,0,467,465,1,0,
        0,0,467,466,1,0,0,0,468,65,1,0,0,0,469,471,3,62,31,0,470,469,1,0,
        0,0,471,474,1,0,0,0,472,470,1,0,0,0,472,473,1,0,0,0,473,475,1,0,
        0,0,474,472,1,0,0,0,475,476,5,21,0,0,476,477,5,38,0,0,477,478,5,
        6,0,0,478,483,3,68,34,0,479,480,5,2,0,0,480,482,3,68,34,0,481,479,
        1,0,0,0,482,485,1,0,0,0,483,481,1,0,0,0,483,484,1,0,0,0,484,486,
        1,0,0,0,485,483,1,0,0,0,486,487,5,7,0,0,487,67,1,0,0,0,488,490,3,
        62,31,0,489,488,1,0,0,0,490,493,1,0,0,0,491,489,1,0,0,0,491,492,
        1,0,0,0,492,494,1,0,0,0,493,491,1,0,0,0,494,495,5,38,0,0,495,69,
        1,0,0,0,55,73,79,90,99,106,111,120,134,139,148,156,164,169,178,186,
        194,199,208,216,224,229,238,244,249,254,265,274,282,287,296,304,
        309,315,321,326,331,342,350,356,362,371,379,384,390,396,406,416,
        436,443,456,461,467,472,483,491
    ]

class d3iGrammar ( Parser ):

    grammarFileName = "d3iGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "','", "':'", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "'@'", "'|'", "'domain'", "'context'", 
                     "'event'", "'entity'", "'aggregate'", "'service'", 
                     "'interface'", "'acl'", "'valueObject'", "'enum'", 
                     "'repository'", "'root'", "'integer'", "'number'", 
                     "'float'", "'date'", "'time'", "'dateTime'", "'string'", 
                     "'boolean'", "'bytes'", "'list'", "'map'" ]

    symbolicNames = [ "<INVALID>", "DOT", "COMMA", "SEMI", "LPAREN", "RPAREN", 
                      "LCURLY", "RCURLY", "LBARCKET", "RBRACKET", "AT", 
                      "PIPE", "DOMAIN", "CONTEXT", "EVENT", "ENTITY", "AGGREGATE", 
                      "SERVICE", "INTERFACE", "ACL", "VALUEOBJECT", "ENUM", 
                      "REPOSITORY", "ROOT", "INTEGER", "NUMBER", "FLOAT", 
                      "DATE", "TIME", "DATETIME", "STRING", "BOOLEAN", "BYTES", 
                      "LIST", "MAP", "INTEGER_CONSTANS", "NUMBER_CONSTANS", 
                      "STRING_LITERAL", "IDENTIFIER", "WS", "LINE_COMMENT", 
                      "BLOCK_COMMENT" ]

    RULE_d3i = 0
    RULE_directive = 1
    RULE_domain = 2
    RULE_domain_element = 3
    RULE_context = 4
    RULE_context_element = 5
    RULE_value_object = 6
    RULE_value_object_member = 7
    RULE_event = 8
    RULE_event_member = 9
    RULE_entity = 10
    RULE_entity_member = 11
    RULE_aggregate = 12
    RULE_aggregate_element = 13
    RULE_repository = 14
    RULE_service = 15
    RULE_service_element = 16
    RULE_interface = 17
    RULE_interface_element = 18
    RULE_operation = 19
    RULE_operation_param = 20
    RULE_operation_return = 21
    RULE_acl = 22
    RULE_acl_element = 23
    RULE_acl_function = 24
    RULE_acl_function_param = 25
    RULE_type = 26
    RULE_primitive_type = 27
    RULE_reference_type = 28
    RULE_container_type = 29
    RULE_qualifiedName = 30
    RULE_decorator = 31
    RULE_decorator_param = 32
    RULE_enum = 33
    RULE_enum_element = 34

    ruleNames =  [ "d3i", "directive", "domain", "domain_element", "context", 
                   "context_element", "value_object", "value_object_member", 
                   "event", "event_member", "entity", "entity_member", "aggregate", 
                   "aggregate_element", "repository", "service", "service_element", 
                   "interface", "interface_element", "operation", "operation_param", 
                   "operation_return", "acl", "acl_element", "acl_function", 
                   "acl_function_param", "type", "primitive_type", "reference_type", 
                   "container_type", "qualifiedName", "decorator", "decorator_param", 
                   "enum", "enum_element" ]

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
    PIPE=11
    DOMAIN=12
    CONTEXT=13
    EVENT=14
    ENTITY=15
    AGGREGATE=16
    SERVICE=17
    INTERFACE=18
    ACL=19
    VALUEOBJECT=20
    ENUM=21
    REPOSITORY=22
    ROOT=23
    INTEGER=24
    NUMBER=25
    FLOAT=26
    DATE=27
    TIME=28
    DATETIME=29
    STRING=30
    BOOLEAN=31
    BYTES=32
    LIST=33
    MAP=34
    INTEGER_CONSTANS=35
    NUMBER_CONSTANS=36
    STRING_LITERAL=37
    IDENTIFIER=38
    WS=39
    LINE_COMMENT=40
    BLOCK_COMMENT=41

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class D3iContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(d3iGrammar.EOF, 0)

        def directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DirectiveContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DirectiveContext,i)


        def domain(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DomainContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DomainContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_d3i

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterD3i" ):
                listener.enterD3i(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitD3i" ):
                listener.exitD3i(self)




    def d3i(self):

        localctx = d3iGrammar.D3iContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_d3i)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 70
                self.directive()
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10 or _la==12:
                self.state = 76
                self.domain()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 82
            self.match(d3iGrammar.EOF)
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


        def getRuleIndex(self):
            return d3iGrammar.RULE_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirective" ):
                listener.enterDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirective" ):
                listener.exitDirective(self)




    def directive(self):

        localctx = d3iGrammar.DirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 85
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




    def domain(self):

        localctx = d3iGrammar.DomainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_domain)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 87
                self.decorator()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 93
            self.match(d3iGrammar.DOMAIN)
            self.state = 94
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 95
            self.match(d3iGrammar.LCURLY)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 25600) != 0):
                self.state = 96
                self.domain_element()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 102
            self.match(d3iGrammar.RCURLY)
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


        def event(self):
            return self.getTypedRuleContext(d3iGrammar.EventContext,0)


        def getRuleIndex(self):
            return d3iGrammar.RULE_domain_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDomain_element" ):
                listener.enterDomain_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDomain_element" ):
                listener.exitDomain_element(self)




    def domain_element(self):

        localctx = d3iGrammar.Domain_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_domain_element)
        try:
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.context()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.event()
                pass


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




    def context(self):

        localctx = d3iGrammar.ContextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_context)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 108
                self.decorator()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 114
            self.match(d3iGrammar.CONTEXT)
            self.state = 115
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 116
            self.match(d3iGrammar.LCURLY)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8373248) != 0):
                self.state = 117
                self.context_element()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 123
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

        def entity(self):
            return self.getTypedRuleContext(d3iGrammar.EntityContext,0)


        def enum(self):
            return self.getTypedRuleContext(d3iGrammar.EnumContext,0)


        def value_object(self):
            return self.getTypedRuleContext(d3iGrammar.Value_objectContext,0)


        def aggregate(self):
            return self.getTypedRuleContext(d3iGrammar.AggregateContext,0)


        def repository(self):
            return self.getTypedRuleContext(d3iGrammar.RepositoryContext,0)


        def acl(self):
            return self.getTypedRuleContext(d3iGrammar.AclContext,0)


        def event(self):
            return self.getTypedRuleContext(d3iGrammar.EventContext,0)


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




    def context_element(self):

        localctx = d3iGrammar.Context_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_context_element)
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.entity()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 127
                self.value_object()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 128
                self.aggregate()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 129
                self.repository()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 130
                self.acl()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 131
                self.event()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 132
                self.service()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 133
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

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def value_object_member(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.Value_object_memberContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.Value_object_memberContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_value_object

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue_object" ):
                listener.enterValue_object(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue_object" ):
                listener.exitValue_object(self)




    def value_object(self):

        localctx = d3iGrammar.Value_objectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_value_object)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 136
                self.decorator()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
            self.match(d3iGrammar.VALUEOBJECT)
            self.state = 143
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 144
            self.match(d3iGrammar.LCURLY)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274881053696) != 0):
                self.state = 145
                self.value_object_member()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 151
            self.match(d3iGrammar.RCURLY)
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


        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def enum(self):
            return self.getTypedRuleContext(d3iGrammar.EnumContext,0)


        def value_object(self):
            return self.getTypedRuleContext(d3iGrammar.Value_objectContext,0)


        def getRuleIndex(self):
            return d3iGrammar.RULE_value_object_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue_object_member" ):
                listener.enterValue_object_member(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue_object_member" ):
                listener.exitValue_object_member(self)




    def value_object_member(self):

        localctx = d3iGrammar.Value_object_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_value_object_member)
        self._la = 0 # Token type
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 153
                    self.decorator()
                    self.state = 158
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 159
                self.match(d3iGrammar.IDENTIFIER)
                self.state = 160
                self.match(d3iGrammar.SEMI)
                self.state = 161
                self.type_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 163
                self.value_object()
                pass


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

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def event_member(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.Event_memberContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.Event_memberContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_event

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvent" ):
                listener.enterEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvent" ):
                listener.exitEvent(self)




    def event(self):

        localctx = d3iGrammar.EventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_event)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 166
                self.decorator()
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 172
            self.match(d3iGrammar.EVENT)
            self.state = 173
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 174
            self.match(d3iGrammar.LCURLY)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274881053696) != 0):
                self.state = 175
                self.event_member()
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 181
            self.match(d3iGrammar.RCURLY)
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


        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def enum(self):
            return self.getTypedRuleContext(d3iGrammar.EnumContext,0)


        def value_object(self):
            return self.getTypedRuleContext(d3iGrammar.Value_objectContext,0)


        def getRuleIndex(self):
            return d3iGrammar.RULE_event_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvent_member" ):
                listener.enterEvent_member(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvent_member" ):
                listener.exitEvent_member(self)




    def event_member(self):

        localctx = d3iGrammar.Event_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_event_member)
        self._la = 0 # Token type
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 183
                    self.decorator()
                    self.state = 188
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 189
                self.match(d3iGrammar.IDENTIFIER)
                self.state = 190
                self.match(d3iGrammar.SEMI)
                self.state = 191
                self.type_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 193
                self.value_object()
                pass


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

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def entity_member(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.Entity_memberContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.Entity_memberContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_entity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntity" ):
                listener.enterEntity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntity" ):
                listener.exitEntity(self)




    def entity(self):

        localctx = d3iGrammar.EntityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_entity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 196
                self.decorator()
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 202
            self.match(d3iGrammar.ENTITY)
            self.state = 203
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 204
            self.match(d3iGrammar.LCURLY)
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274881053696) != 0):
                self.state = 205
                self.entity_member()
                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 211
            self.match(d3iGrammar.RCURLY)
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


        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def enum(self):
            return self.getTypedRuleContext(d3iGrammar.EnumContext,0)


        def value_object(self):
            return self.getTypedRuleContext(d3iGrammar.Value_objectContext,0)


        def getRuleIndex(self):
            return d3iGrammar.RULE_entity_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntity_member" ):
                listener.enterEntity_member(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntity_member" ):
                listener.exitEntity_member(self)




    def entity_member(self):

        localctx = d3iGrammar.Entity_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_entity_member)
        self._la = 0 # Token type
        try:
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 213
                    self.decorator()
                    self.state = 218
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 219
                self.match(d3iGrammar.IDENTIFIER)
                self.state = 220
                self.match(d3iGrammar.SEMI)
                self.state = 221
                self.type_()
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




    def aggregate(self):

        localctx = d3iGrammar.AggregateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_aggregate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 226
                self.decorator()
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 232
            self.match(d3iGrammar.AGGREGATE)
            self.state = 233
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 234
            self.match(d3iGrammar.LCURLY)
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 11568128) != 0):
                self.state = 235
                self.aggregate_element()
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 241
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

        def entity(self):
            return self.getTypedRuleContext(d3iGrammar.EntityContext,0)


        def ROOT(self):
            return self.getToken(d3iGrammar.ROOT, 0)

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




    def aggregate_element(self):

        localctx = d3iGrammar.Aggregate_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_aggregate_element)
        self._la = 0 # Token type
        try:
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 243
                    self.match(d3iGrammar.ROOT)


                self.state = 246
                self.entity()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 248
                self.value_object()
                pass


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




    def repository(self):

        localctx = d3iGrammar.RepositoryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_repository)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 251
                self.decorator()
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 257
            self.match(d3iGrammar.REPOSITORY)
            self.state = 258
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 259
            self.match(d3iGrammar.SEMI)
            self.state = 260
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




    def service(self):

        localctx = d3iGrammar.ServiceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_service)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 262
                self.decorator()
                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 268
            self.match(d3iGrammar.SERVICE)
            self.state = 269
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 270
            self.match(d3iGrammar.LCURLY)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274881053696) != 0):
                self.state = 271
                self.service_element()
                self.state = 276
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 277
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


        def getRuleIndex(self):
            return d3iGrammar.RULE_service_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterService_element" ):
                listener.enterService_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitService_element" ):
                listener.exitService_element(self)




    def service_element(self):

        localctx = d3iGrammar.Service_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_service_element)
        try:
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.operation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 281
                self.value_object()
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




    def interface(self):

        localctx = d3iGrammar.InterfaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_interface)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 284
                self.decorator()
                self.state = 289
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 290
            self.match(d3iGrammar.INTERFACE)
            self.state = 291
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 292
            self.match(d3iGrammar.LCURLY)
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274881053696) != 0):
                self.state = 293
                self.interface_element()
                self.state = 298
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 299
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


        def getRuleIndex(self):
            return d3iGrammar.RULE_interface_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterface_element" ):
                listener.enterInterface_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterface_element" ):
                listener.exitInterface_element(self)




    def interface_element(self):

        localctx = d3iGrammar.Interface_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_interface_element)
        try:
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.operation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 303
                self.value_object()
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

        def operation_return(self):
            return self.getTypedRuleContext(d3iGrammar.Operation_returnContext,0)


        def getRuleIndex(self):
            return d3iGrammar.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)




    def operation(self):

        localctx = d3iGrammar.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 306
                self.decorator()
                self.state = 311
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 312
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 313
            self.match(d3iGrammar.LPAREN)
            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10 or _la==38:
                self.state = 314
                self.operation_param()


            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 317
                self.match(d3iGrammar.COMMA)
                self.state = 318
                self.operation_param()
                self.state = 323
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 324
            self.match(d3iGrammar.RPAREN)
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 325
                self.operation_return()


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




    def operation_param(self):

        localctx = d3iGrammar.Operation_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_operation_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 328
                self.decorator()
                self.state = 333
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 334
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 335
            self.match(d3iGrammar.SEMI)
            self.state = 336
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

        def SEMI(self):
            return self.getToken(d3iGrammar.SEMI, 0)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.TypeContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.TypeContext,i)


        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def PIPE(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.PIPE)
            else:
                return self.getToken(d3iGrammar.PIPE, i)

        def getRuleIndex(self):
            return d3iGrammar.RULE_operation_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation_return" ):
                listener.enterOperation_return(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation_return" ):
                listener.exitOperation_return(self)




    def operation_return(self):

        localctx = d3iGrammar.Operation_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_operation_return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(d3iGrammar.SEMI)
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
            self.type_()
            self.state = 356
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 346
                self.match(d3iGrammar.PIPE)
                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 347
                    self.decorator()
                    self.state = 352
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 353
                self.type_()
                self.state = 358
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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




    def acl(self):

        localctx = d3iGrammar.AclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_acl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 359
                self.decorator()
                self.state = 364
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 365
            self.match(d3iGrammar.ACL)
            self.state = 366
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 367
            self.match(d3iGrammar.LCURLY)
            self.state = 371
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274881053696) != 0):
                self.state = 368
                self.acl_element()
                self.state = 373
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 374
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


        def acl_function(self):
            return self.getTypedRuleContext(d3iGrammar.Acl_functionContext,0)


        def getRuleIndex(self):
            return d3iGrammar.RULE_acl_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcl_element" ):
                listener.enterAcl_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcl_element" ):
                listener.exitAcl_element(self)




    def acl_element(self):

        localctx = d3iGrammar.Acl_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_acl_element)
        try:
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.enum()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.value_object()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 378
                self.acl_function()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Acl_functionContext(ParserRuleContext):
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

        def SEMI(self):
            return self.getToken(d3iGrammar.SEMI, 0)

        def type_(self):
            return self.getTypedRuleContext(d3iGrammar.TypeContext,0)


        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def acl_function_param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.Acl_function_paramContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.Acl_function_paramContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(d3iGrammar.COMMA)
            else:
                return self.getToken(d3iGrammar.COMMA, i)

        def getRuleIndex(self):
            return d3iGrammar.RULE_acl_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcl_function" ):
                listener.enterAcl_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcl_function" ):
                listener.exitAcl_function(self)




    def acl_function(self):

        localctx = d3iGrammar.Acl_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_acl_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 381
                self.decorator()
                self.state = 386
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 387
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 388
            self.match(d3iGrammar.LPAREN)
            self.state = 390
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10 or _la==38:
                self.state = 389
                self.acl_function_param()


            self.state = 396
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 392
                self.match(d3iGrammar.COMMA)
                self.state = 393
                self.acl_function_param()
                self.state = 398
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 399
            self.match(d3iGrammar.RPAREN)
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


    class Acl_function_paramContext(ParserRuleContext):
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


        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_acl_function_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcl_function_param" ):
                listener.enterAcl_function_param(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcl_function_param" ):
                listener.exitAcl_function_param(self)




    def acl_function_param(self):

        localctx = d3iGrammar.Acl_function_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_acl_function_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 403
                self.decorator()
                self.state = 408
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 409
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 410
            self.match(d3iGrammar.SEMI)
            self.state = 411
            self.type_()
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


        def container_type(self):
            return self.getTypedRuleContext(d3iGrammar.Container_typeContext,0)


        def getRuleIndex(self):
            return d3iGrammar.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = d3iGrammar.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_type)
        try:
            self.state = 416
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24, 25, 26, 27, 28, 29, 30, 31, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.primitive_type()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 414
                self.reference_type()
                pass
            elif token in [33, 34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 415
                self.container_type()
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

        def getRuleIndex(self):
            return d3iGrammar.RULE_primitive_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitive_type" ):
                listener.enterPrimitive_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitive_type" ):
                listener.exitPrimitive_type(self)




    def primitive_type(self):

        localctx = d3iGrammar.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8573157376) != 0)):
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


        def getRuleIndex(self):
            return d3iGrammar.RULE_reference_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReference_type" ):
                listener.enterReference_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReference_type" ):
                listener.exitReference_type(self)




    def reference_type(self):

        localctx = d3iGrammar.Reference_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_reference_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.qualifiedName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Container_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIST(self):
            return self.getToken(d3iGrammar.LIST, 0)

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

        def MAP(self):
            return self.getToken(d3iGrammar.MAP, 0)

        def getRuleIndex(self):
            return d3iGrammar.RULE_container_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContainer_type" ):
                listener.enterContainer_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContainer_type" ):
                listener.exitContainer_type(self)




    def container_type(self):

        localctx = d3iGrammar.Container_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_container_type)
        try:
            self.state = 436
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.match(d3iGrammar.LIST)
                self.state = 423
                self.match(d3iGrammar.LBARCKET)
                self.state = 424
                self.type_()
                self.state = 425
                self.match(d3iGrammar.COMMA)
                self.state = 426
                self.type_()
                self.state = 427
                self.match(d3iGrammar.RBRACKET)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
                self.match(d3iGrammar.MAP)
                self.state = 430
                self.match(d3iGrammar.LBARCKET)
                self.state = 431
                self.type_()
                self.state = 432
                self.match(d3iGrammar.COMMA)
                self.state = 433
                self.type_()
                self.state = 434
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




    def qualifiedName(self):

        localctx = d3iGrammar.QualifiedNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_qualifiedName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 443
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 439
                self.match(d3iGrammar.DOT)
                self.state = 440
                self.match(d3iGrammar.IDENTIFIER)
                self.state = 445
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




    def decorator(self):

        localctx = d3iGrammar.DecoratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_decorator)
        self._la = 0 # Token type
        try:
            self.state = 461
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.match(d3iGrammar.AT)
                self.state = 447
                self.match(d3iGrammar.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.match(d3iGrammar.AT)
                self.state = 449
                self.match(d3iGrammar.IDENTIFIER)
                self.state = 450
                self.match(d3iGrammar.LPAREN)
                self.state = 451
                self.decorator_param()
                self.state = 456
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 452
                    self.match(d3iGrammar.COMMA)
                    self.state = 453
                    self.decorator_param()
                    self.state = 458
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 459
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




    def decorator_param(self):

        localctx = d3iGrammar.Decorator_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_decorator_param)
        try:
            self.state = 467
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 463
                self.qualifiedName()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 464
                self.match(d3iGrammar.INTEGER_CONSTANS)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 465
                self.match(d3iGrammar.NUMBER_CONSTANS)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 4)
                self.state = 466
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

        def enum_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.Enum_elementContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.Enum_elementContext,i)


        def RCURLY(self):
            return self.getToken(d3iGrammar.RCURLY, 0)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


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




    def enum(self):

        localctx = d3iGrammar.EnumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_enum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 469
                self.decorator()
                self.state = 474
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 475
            self.match(d3iGrammar.ENUM)
            self.state = 476
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 477
            self.match(d3iGrammar.LCURLY)
            self.state = 478
            self.enum_element()
            self.state = 483
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 479
                self.match(d3iGrammar.COMMA)
                self.state = 480
                self.enum_element()
                self.state = 485
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 486
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




    def enum_element(self):

        localctx = d3iGrammar.Enum_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_enum_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 488
                self.decorator()
                self.state = 493
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 494
            self.match(d3iGrammar.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





