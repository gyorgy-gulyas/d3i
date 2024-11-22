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
        4,1,43,472,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,1,0,5,0,78,8,0,10,0,
        12,0,81,9,0,1,0,1,0,1,1,5,1,86,8,1,10,1,12,1,89,9,1,1,1,5,1,92,8,
        1,10,1,12,1,95,9,1,1,1,1,1,1,1,1,1,5,1,101,8,1,10,1,12,1,104,9,1,
        1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,4,5,4,114,8,4,10,4,12,4,117,9,4,1,
        4,1,4,1,4,1,4,5,4,123,8,4,10,4,12,4,126,9,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,3,5,138,8,5,1,6,5,6,141,8,6,10,6,12,6,144,9,
        6,1,6,1,6,1,6,1,6,5,6,150,8,6,10,6,12,6,153,9,6,1,6,1,6,1,7,1,7,
        1,7,3,7,160,8,7,1,8,5,8,163,8,8,10,8,12,8,166,9,8,1,8,1,8,1,8,1,
        8,1,9,5,9,173,8,9,10,9,12,9,176,9,9,1,9,1,9,1,9,1,9,5,9,182,8,9,
        10,9,12,9,185,9,9,1,9,1,9,1,10,1,10,1,10,3,10,192,8,10,1,11,5,11,
        195,8,11,10,11,12,11,198,9,11,1,11,1,11,1,11,1,11,1,12,5,12,205,
        8,12,10,12,12,12,208,9,12,1,12,1,12,1,12,1,12,5,12,214,8,12,10,12,
        12,12,217,9,12,1,12,1,12,1,13,1,13,1,13,3,13,224,8,13,1,14,5,14,
        227,8,14,10,14,12,14,230,9,14,1,14,1,14,1,14,1,14,1,15,5,15,237,
        8,15,10,15,12,15,240,9,15,1,15,1,15,1,15,1,15,5,15,246,8,15,10,15,
        12,15,249,9,15,1,15,1,15,1,16,1,16,1,16,3,16,256,8,16,1,17,3,17,
        259,8,17,1,17,1,17,1,18,5,18,264,8,18,10,18,12,18,267,9,18,1,18,
        1,18,1,18,1,18,1,18,1,19,5,19,275,8,19,10,19,12,19,278,9,19,1,19,
        1,19,1,19,1,19,5,19,284,8,19,10,19,12,19,287,9,19,1,19,1,19,1,20,
        1,20,1,20,1,20,3,20,295,8,20,1,21,5,21,298,8,21,10,21,12,21,301,
        9,21,1,21,1,21,1,21,1,21,5,21,307,8,21,10,21,12,21,310,9,21,1,21,
        1,21,1,22,1,22,1,22,1,22,3,22,318,8,22,1,23,5,23,321,8,23,10,23,
        12,23,324,9,23,1,23,1,23,1,23,3,23,329,8,23,1,23,1,23,5,23,333,8,
        23,10,23,12,23,336,9,23,1,23,1,23,1,23,3,23,341,8,23,1,23,1,23,5,
        23,345,8,23,10,23,12,23,348,9,23,1,24,5,24,351,8,24,10,24,12,24,
        354,9,24,1,24,1,24,1,24,1,24,1,25,5,25,361,8,25,10,25,12,25,364,
        9,25,1,25,1,25,1,26,5,26,369,8,26,10,26,12,26,372,9,26,1,26,1,26,
        1,26,1,26,5,26,378,8,26,10,26,12,26,381,9,26,1,26,1,26,1,27,1,27,
        1,27,3,27,388,8,27,1,28,1,28,1,28,1,28,3,28,394,8,28,1,29,1,29,1,
        30,1,30,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,
        32,1,33,1,33,1,33,5,33,415,8,33,10,33,12,33,418,9,33,1,34,1,34,1,
        34,1,34,1,34,1,34,1,34,1,34,5,34,428,8,34,10,34,12,34,431,9,34,1,
        34,1,34,3,34,435,8,34,1,35,1,35,1,35,1,35,3,35,441,8,35,1,36,5,36,
        444,8,36,10,36,12,36,447,9,36,1,36,1,36,1,36,1,36,3,36,453,8,36,
        1,36,1,36,5,36,457,8,36,10,36,12,36,460,9,36,1,36,1,36,1,37,5,37,
        465,8,37,10,37,12,37,468,9,37,1,37,1,37,1,37,0,0,38,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        56,58,60,62,64,66,68,70,72,74,0,1,1,0,26,34,501,0,79,1,0,0,0,2,87,
        1,0,0,0,4,107,1,0,0,0,6,110,1,0,0,0,8,115,1,0,0,0,10,137,1,0,0,0,
        12,142,1,0,0,0,14,159,1,0,0,0,16,164,1,0,0,0,18,174,1,0,0,0,20,191,
        1,0,0,0,22,196,1,0,0,0,24,206,1,0,0,0,26,223,1,0,0,0,28,228,1,0,
        0,0,30,238,1,0,0,0,32,255,1,0,0,0,34,258,1,0,0,0,36,265,1,0,0,0,
        38,276,1,0,0,0,40,294,1,0,0,0,42,299,1,0,0,0,44,317,1,0,0,0,46,322,
        1,0,0,0,48,352,1,0,0,0,50,362,1,0,0,0,52,370,1,0,0,0,54,387,1,0,
        0,0,56,393,1,0,0,0,58,395,1,0,0,0,60,397,1,0,0,0,62,399,1,0,0,0,
        64,404,1,0,0,0,66,411,1,0,0,0,68,434,1,0,0,0,70,440,1,0,0,0,72,445,
        1,0,0,0,74,466,1,0,0,0,76,78,3,2,1,0,77,76,1,0,0,0,78,81,1,0,0,0,
        79,77,1,0,0,0,79,80,1,0,0,0,80,82,1,0,0,0,81,79,1,0,0,0,82,83,5,
        0,0,1,83,1,1,0,0,0,84,86,3,4,2,0,85,84,1,0,0,0,86,89,1,0,0,0,87,
        85,1,0,0,0,87,88,1,0,0,0,88,93,1,0,0,0,89,87,1,0,0,0,90,92,3,68,
        34,0,91,90,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,
        96,1,0,0,0,95,93,1,0,0,0,96,97,5,13,0,0,97,98,5,40,0,0,98,102,5,
        6,0,0,99,101,3,6,3,0,100,99,1,0,0,0,101,104,1,0,0,0,102,100,1,0,
        0,0,102,103,1,0,0,0,103,105,1,0,0,0,104,102,1,0,0,0,105,106,5,7,
        0,0,106,3,1,0,0,0,107,108,5,40,0,0,108,109,3,66,33,0,109,5,1,0,0,
        0,110,111,3,8,4,0,111,7,1,0,0,0,112,114,3,68,34,0,113,112,1,0,0,
        0,114,117,1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,118,1,0,0,
        0,117,115,1,0,0,0,118,119,5,14,0,0,119,120,5,40,0,0,120,124,5,6,
        0,0,121,123,3,10,5,0,122,121,1,0,0,0,123,126,1,0,0,0,124,122,1,0,
        0,0,124,125,1,0,0,0,125,127,1,0,0,0,126,124,1,0,0,0,127,128,5,7,
        0,0,128,9,1,0,0,0,129,138,3,72,36,0,130,138,3,12,6,0,131,138,3,24,
        12,0,132,138,3,30,15,0,133,138,3,36,18,0,134,138,3,52,26,0,135,138,
        3,38,19,0,136,138,3,42,21,0,137,129,1,0,0,0,137,130,1,0,0,0,137,
        131,1,0,0,0,137,132,1,0,0,0,137,133,1,0,0,0,137,134,1,0,0,0,137,
        135,1,0,0,0,137,136,1,0,0,0,138,11,1,0,0,0,139,141,3,68,34,0,140,
        139,1,0,0,0,141,144,1,0,0,0,142,140,1,0,0,0,142,143,1,0,0,0,143,
        145,1,0,0,0,144,142,1,0,0,0,145,146,5,21,0,0,146,147,5,40,0,0,147,
        151,5,6,0,0,148,150,3,14,7,0,149,148,1,0,0,0,150,153,1,0,0,0,151,
        149,1,0,0,0,151,152,1,0,0,0,152,154,1,0,0,0,153,151,1,0,0,0,154,
        155,5,7,0,0,155,13,1,0,0,0,156,160,3,16,8,0,157,160,3,72,36,0,158,
        160,3,12,6,0,159,156,1,0,0,0,159,157,1,0,0,0,159,158,1,0,0,0,160,
        15,1,0,0,0,161,163,3,68,34,0,162,161,1,0,0,0,163,166,1,0,0,0,164,
        162,1,0,0,0,164,165,1,0,0,0,165,167,1,0,0,0,166,164,1,0,0,0,167,
        168,5,40,0,0,168,169,5,3,0,0,169,170,3,56,28,0,170,17,1,0,0,0,171,
        173,3,68,34,0,172,171,1,0,0,0,173,176,1,0,0,0,174,172,1,0,0,0,174,
        175,1,0,0,0,175,177,1,0,0,0,176,174,1,0,0,0,177,178,5,15,0,0,178,
        179,5,40,0,0,179,183,5,6,0,0,180,182,3,20,10,0,181,180,1,0,0,0,182,
        185,1,0,0,0,183,181,1,0,0,0,183,184,1,0,0,0,184,186,1,0,0,0,185,
        183,1,0,0,0,186,187,5,7,0,0,187,19,1,0,0,0,188,192,3,22,11,0,189,
        192,3,72,36,0,190,192,3,12,6,0,191,188,1,0,0,0,191,189,1,0,0,0,191,
        190,1,0,0,0,192,21,1,0,0,0,193,195,3,68,34,0,194,193,1,0,0,0,195,
        198,1,0,0,0,196,194,1,0,0,0,196,197,1,0,0,0,197,199,1,0,0,0,198,
        196,1,0,0,0,199,200,5,40,0,0,200,201,5,3,0,0,201,202,3,56,28,0,202,
        23,1,0,0,0,203,205,3,68,34,0,204,203,1,0,0,0,205,208,1,0,0,0,206,
        204,1,0,0,0,206,207,1,0,0,0,207,209,1,0,0,0,208,206,1,0,0,0,209,
        210,5,16,0,0,210,211,5,40,0,0,211,215,5,6,0,0,212,214,3,26,13,0,
        213,212,1,0,0,0,214,217,1,0,0,0,215,213,1,0,0,0,215,216,1,0,0,0,
        216,218,1,0,0,0,217,215,1,0,0,0,218,219,5,7,0,0,219,25,1,0,0,0,220,
        224,3,28,14,0,221,224,3,72,36,0,222,224,3,12,6,0,223,220,1,0,0,0,
        223,221,1,0,0,0,223,222,1,0,0,0,224,27,1,0,0,0,225,227,3,68,34,0,
        226,225,1,0,0,0,227,230,1,0,0,0,228,226,1,0,0,0,228,229,1,0,0,0,
        229,231,1,0,0,0,230,228,1,0,0,0,231,232,5,40,0,0,232,233,5,3,0,0,
        233,234,3,56,28,0,234,29,1,0,0,0,235,237,3,68,34,0,236,235,1,0,0,
        0,237,240,1,0,0,0,238,236,1,0,0,0,238,239,1,0,0,0,239,241,1,0,0,
        0,240,238,1,0,0,0,241,242,5,17,0,0,242,243,5,40,0,0,243,247,5,6,
        0,0,244,246,3,32,16,0,245,244,1,0,0,0,246,249,1,0,0,0,247,245,1,
        0,0,0,247,248,1,0,0,0,248,250,1,0,0,0,249,247,1,0,0,0,250,251,5,
        7,0,0,251,31,1,0,0,0,252,256,3,34,17,0,253,256,3,72,36,0,254,256,
        3,12,6,0,255,252,1,0,0,0,255,253,1,0,0,0,255,254,1,0,0,0,256,33,
        1,0,0,0,257,259,5,24,0,0,258,257,1,0,0,0,258,259,1,0,0,0,259,260,
        1,0,0,0,260,261,3,24,12,0,261,35,1,0,0,0,262,264,3,68,34,0,263,262,
        1,0,0,0,264,267,1,0,0,0,265,263,1,0,0,0,265,266,1,0,0,0,266,268,
        1,0,0,0,267,265,1,0,0,0,268,269,5,23,0,0,269,270,5,40,0,0,270,271,
        5,3,0,0,271,272,3,66,33,0,272,37,1,0,0,0,273,275,3,68,34,0,274,273,
        1,0,0,0,275,278,1,0,0,0,276,274,1,0,0,0,276,277,1,0,0,0,277,279,
        1,0,0,0,278,276,1,0,0,0,279,280,5,18,0,0,280,281,5,40,0,0,281,285,
        5,6,0,0,282,284,3,40,20,0,283,282,1,0,0,0,284,287,1,0,0,0,285,283,
        1,0,0,0,285,286,1,0,0,0,286,288,1,0,0,0,287,285,1,0,0,0,288,289,
        5,7,0,0,289,39,1,0,0,0,290,295,3,46,23,0,291,295,3,72,36,0,292,295,
        3,12,6,0,293,295,3,18,9,0,294,290,1,0,0,0,294,291,1,0,0,0,294,292,
        1,0,0,0,294,293,1,0,0,0,295,41,1,0,0,0,296,298,3,68,34,0,297,296,
        1,0,0,0,298,301,1,0,0,0,299,297,1,0,0,0,299,300,1,0,0,0,300,302,
        1,0,0,0,301,299,1,0,0,0,302,303,5,19,0,0,303,304,5,40,0,0,304,308,
        5,6,0,0,305,307,3,44,22,0,306,305,1,0,0,0,307,310,1,0,0,0,308,306,
        1,0,0,0,308,309,1,0,0,0,309,311,1,0,0,0,310,308,1,0,0,0,311,312,
        5,7,0,0,312,43,1,0,0,0,313,318,3,46,23,0,314,318,3,72,36,0,315,318,
        3,12,6,0,316,318,3,18,9,0,317,313,1,0,0,0,317,314,1,0,0,0,317,315,
        1,0,0,0,317,316,1,0,0,0,318,45,1,0,0,0,319,321,3,68,34,0,320,319,
        1,0,0,0,321,324,1,0,0,0,322,320,1,0,0,0,322,323,1,0,0,0,323,325,
        1,0,0,0,324,322,1,0,0,0,325,326,5,40,0,0,326,328,5,4,0,0,327,329,
        3,48,24,0,328,327,1,0,0,0,328,329,1,0,0,0,329,334,1,0,0,0,330,331,
        5,2,0,0,331,333,3,48,24,0,332,330,1,0,0,0,333,336,1,0,0,0,334,332,
        1,0,0,0,334,335,1,0,0,0,335,337,1,0,0,0,336,334,1,0,0,0,337,340,
        5,5,0,0,338,339,5,3,0,0,339,341,3,50,25,0,340,338,1,0,0,0,340,341,
        1,0,0,0,341,346,1,0,0,0,342,343,5,12,0,0,343,345,3,50,25,0,344,342,
        1,0,0,0,345,348,1,0,0,0,346,344,1,0,0,0,346,347,1,0,0,0,347,47,1,
        0,0,0,348,346,1,0,0,0,349,351,3,68,34,0,350,349,1,0,0,0,351,354,
        1,0,0,0,352,350,1,0,0,0,352,353,1,0,0,0,353,355,1,0,0,0,354,352,
        1,0,0,0,355,356,5,40,0,0,356,357,5,3,0,0,357,358,3,56,28,0,358,49,
        1,0,0,0,359,361,3,68,34,0,360,359,1,0,0,0,361,364,1,0,0,0,362,360,
        1,0,0,0,362,363,1,0,0,0,363,365,1,0,0,0,364,362,1,0,0,0,365,366,
        3,56,28,0,366,51,1,0,0,0,367,369,3,68,34,0,368,367,1,0,0,0,369,372,
        1,0,0,0,370,368,1,0,0,0,370,371,1,0,0,0,371,373,1,0,0,0,372,370,
        1,0,0,0,373,374,5,20,0,0,374,375,5,40,0,0,375,379,5,6,0,0,376,378,
        3,54,27,0,377,376,1,0,0,0,378,381,1,0,0,0,379,377,1,0,0,0,379,380,
        1,0,0,0,380,382,1,0,0,0,381,379,1,0,0,0,382,383,5,7,0,0,383,53,1,
        0,0,0,384,388,3,72,36,0,385,388,3,12,6,0,386,388,3,46,23,0,387,384,
        1,0,0,0,387,385,1,0,0,0,387,386,1,0,0,0,388,55,1,0,0,0,389,394,3,
        58,29,0,390,394,3,60,30,0,391,394,3,62,31,0,392,394,3,64,32,0,393,
        389,1,0,0,0,393,390,1,0,0,0,393,391,1,0,0,0,393,392,1,0,0,0,394,
        57,1,0,0,0,395,396,7,0,0,0,396,59,1,0,0,0,397,398,3,66,33,0,398,
        61,1,0,0,0,399,400,5,35,0,0,400,401,5,8,0,0,401,402,3,56,28,0,402,
        403,5,9,0,0,403,63,1,0,0,0,404,405,5,36,0,0,405,406,5,8,0,0,406,
        407,3,56,28,0,407,408,5,2,0,0,408,409,3,56,28,0,409,410,5,9,0,0,
        410,65,1,0,0,0,411,416,5,40,0,0,412,413,5,1,0,0,413,415,5,40,0,0,
        414,412,1,0,0,0,415,418,1,0,0,0,416,414,1,0,0,0,416,417,1,0,0,0,
        417,67,1,0,0,0,418,416,1,0,0,0,419,420,5,10,0,0,420,435,5,40,0,0,
        421,422,5,10,0,0,422,423,5,40,0,0,423,424,5,4,0,0,424,429,3,70,35,
        0,425,426,5,2,0,0,426,428,3,70,35,0,427,425,1,0,0,0,428,431,1,0,
        0,0,429,427,1,0,0,0,429,430,1,0,0,0,430,432,1,0,0,0,431,429,1,0,
        0,0,432,433,5,5,0,0,433,435,1,0,0,0,434,419,1,0,0,0,434,421,1,0,
        0,0,435,69,1,0,0,0,436,441,3,66,33,0,437,441,5,37,0,0,438,441,5,
        38,0,0,439,441,5,39,0,0,440,436,1,0,0,0,440,437,1,0,0,0,440,438,
        1,0,0,0,440,439,1,0,0,0,441,71,1,0,0,0,442,444,3,68,34,0,443,442,
        1,0,0,0,444,447,1,0,0,0,445,443,1,0,0,0,445,446,1,0,0,0,446,448,
        1,0,0,0,447,445,1,0,0,0,448,449,5,22,0,0,449,450,5,40,0,0,450,452,
        5,6,0,0,451,453,3,74,37,0,452,451,1,0,0,0,452,453,1,0,0,0,453,458,
        1,0,0,0,454,455,5,2,0,0,455,457,3,74,37,0,456,454,1,0,0,0,457,460,
        1,0,0,0,458,456,1,0,0,0,458,459,1,0,0,0,459,461,1,0,0,0,460,458,
        1,0,0,0,461,462,5,7,0,0,462,73,1,0,0,0,463,465,3,68,34,0,464,463,
        1,0,0,0,465,468,1,0,0,0,466,464,1,0,0,0,466,467,1,0,0,0,467,469,
        1,0,0,0,468,466,1,0,0,0,469,470,5,40,0,0,470,75,1,0,0,0,49,79,87,
        93,102,115,124,137,142,151,159,164,174,183,191,196,206,215,223,228,
        238,247,255,258,265,276,285,294,299,308,317,322,328,334,340,346,
        352,362,370,379,387,393,416,429,434,440,445,452,458,466
    ]

class d3iGrammar ( Parser ):

    grammarFileName = "d3iGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "','", "':'", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "'@'", "'=>'", "'|'", "'domain'", 
                     "'context'", "'event'", "'entity'", "'aggregate'", 
                     "'service'", "'interface'", "'acl'", "'valueobject'", 
                     "'enum'", "'repository'", "'root'", "'or'", "'integer'", 
                     "'number'", "'float'", "'date'", "'time'", "'dateTime'", 
                     "'string'", "'boolean'", "'bytes'", "'list'", "'map'" ]

    symbolicNames = [ "<INVALID>", "DOT", "COMMA", "SEMI", "LPAREN", "RPAREN", 
                      "LCURLY", "RCURLY", "LBARCKET", "RBRACKET", "AT", 
                      "ARROW", "PIPE", "DOMAIN", "CONTEXT", "EVENT", "ENTITY", 
                      "AGGREGATE", "SERVICE", "INTERFACE", "ACL", "VALUEOBJECT", 
                      "ENUM", "REPOSITORY", "ROOT", "OR", "INTEGER", "NUMBER", 
                      "FLOAT", "DATE", "TIME", "DATETIME", "STRING", "BOOLEAN", 
                      "BYTES", "LIST", "MAP", "INTEGER_CONSTANS", "NUMBER_CONSTANS", 
                      "STRING_LITERAL", "IDENTIFIER", "WS", "LINE_COMMENT", 
                      "BLOCK_COMMENT" ]

    RULE_d3i = 0
    RULE_domain = 1
    RULE_directive = 2
    RULE_domain_element = 3
    RULE_context = 4
    RULE_context_element = 5
    RULE_value_object = 6
    RULE_value_object_element = 7
    RULE_value_object_member = 8
    RULE_event = 9
    RULE_event_element = 10
    RULE_event_member = 11
    RULE_entity = 12
    RULE_entity_element = 13
    RULE_entity_member = 14
    RULE_aggregate = 15
    RULE_aggregate_element = 16
    RULE_aggregate_entity = 17
    RULE_repository = 18
    RULE_service = 19
    RULE_service_element = 20
    RULE_interface = 21
    RULE_interface_element = 22
    RULE_operation = 23
    RULE_operation_param = 24
    RULE_operation_return = 25
    RULE_acl = 26
    RULE_acl_element = 27
    RULE_type = 28
    RULE_primitive_type = 29
    RULE_reference_type = 30
    RULE_list_type = 31
    RULE_map_type = 32
    RULE_qualifiedName = 33
    RULE_decorator = 34
    RULE_decorator_param = 35
    RULE_enum = 36
    RULE_enum_element = 37

    ruleNames =  [ "d3i", "domain", "directive", "domain_element", "context", 
                   "context_element", "value_object", "value_object_element", 
                   "value_object_member", "event", "event_element", "event_member", 
                   "entity", "entity_element", "entity_member", "aggregate", 
                   "aggregate_element", "aggregate_entity", "repository", 
                   "service", "service_element", "interface", "interface_element", 
                   "operation", "operation_param", "operation_return", "acl", 
                   "acl_element", "type", "primitive_type", "reference_type", 
                   "list_type", "map_type", "qualifiedName", "decorator", 
                   "decorator_param", "enum", "enum_element" ]

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
    DOMAIN=13
    CONTEXT=14
    EVENT=15
    ENTITY=16
    AGGREGATE=17
    SERVICE=18
    INTERFACE=19
    ACL=20
    VALUEOBJECT=21
    ENUM=22
    REPOSITORY=23
    ROOT=24
    OR=25
    INTEGER=26
    NUMBER=27
    FLOAT=28
    DATE=29
    TIME=30
    DATETIME=31
    STRING=32
    BOOLEAN=33
    BYTES=34
    LIST=35
    MAP=36
    INTEGER_CONSTANS=37
    NUMBER_CONSTANS=38
    STRING_LITERAL=39
    IDENTIFIER=40
    WS=41
    LINE_COMMENT=42
    BLOCK_COMMENT=43

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitD3i" ):
                return visitor.visitD3i(self)
            else:
                return visitor.visitChildren(self)




    def d3i(self):

        localctx = d3iGrammar.D3iContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_d3i)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099511636992) != 0):
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
        self.enterRule(localctx, 2, self.RULE_domain)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 84
                self.directive()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 90
                self.decorator()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
            self.match(d3iGrammar.DOMAIN)
            self.state = 97
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 98
            self.match(d3iGrammar.LCURLY)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10 or _la==14:
                self.state = 99
                self.domain_element()
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 105
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
        self.enterRule(localctx, 4, self.RULE_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 108
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
        self.enterRule(localctx, 6, self.RULE_domain_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
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
        self.enterRule(localctx, 8, self.RULE_context)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 112
                self.decorator()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118
            self.match(d3iGrammar.CONTEXT)
            self.state = 119
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 120
            self.match(d3iGrammar.LCURLY)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16712704) != 0):
                self.state = 121
                self.context_element()
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
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


        def entity(self):
            return self.getTypedRuleContext(d3iGrammar.EntityContext,0)


        def aggregate(self):
            return self.getTypedRuleContext(d3iGrammar.AggregateContext,0)


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
        self.enterRule(localctx, 10, self.RULE_context_element)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.enum()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.value_object()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
                self.entity()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 132
                self.aggregate()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 133
                self.repository()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 134
                self.acl()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 135
                self.service()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 136
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
        self.enterRule(localctx, 12, self.RULE_value_object)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 139
                self.decorator()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 145
            self.match(d3iGrammar.VALUEOBJECT)
            self.state = 146
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 147
            self.match(d3iGrammar.LCURLY)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099517920256) != 0):
                self.state = 148
                self.value_object_element()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 154
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
        self.enterRule(localctx, 14, self.RULE_value_object_element)
        try:
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.value_object_member()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 158
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
        self.enterRule(localctx, 16, self.RULE_value_object_member)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 161
                self.decorator()
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 167
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 168
            self.match(d3iGrammar.SEMI)
            self.state = 169
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

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


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
        self.enterRule(localctx, 18, self.RULE_event)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 171
                self.decorator()
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 177
            self.match(d3iGrammar.EVENT)
            self.state = 178
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 179
            self.match(d3iGrammar.LCURLY)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099517920256) != 0):
                self.state = 180
                self.event_element()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 186
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
        self.enterRule(localctx, 20, self.RULE_event_element)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.event_member()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 190
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
        self.enterRule(localctx, 22, self.RULE_event_member)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 193
                self.decorator()
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 199
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 200
            self.match(d3iGrammar.SEMI)
            self.state = 201
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

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.DecoratorContext,i)


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
        self.enterRule(localctx, 24, self.RULE_entity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 203
                self.decorator()
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 209
            self.match(d3iGrammar.ENTITY)
            self.state = 210
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 211
            self.match(d3iGrammar.LCURLY)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099517920256) != 0):
                self.state = 212
                self.entity_element()
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 218
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
        self.enterRule(localctx, 26, self.RULE_entity_element)
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.entity_member()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 222
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
        self.enterRule(localctx, 28, self.RULE_entity_member)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 225
                self.decorator()
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 231
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 232
            self.match(d3iGrammar.SEMI)
            self.state = 233
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
        self.enterRule(localctx, 30, self.RULE_aggregate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
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
            self.match(d3iGrammar.AGGREGATE)
            self.state = 242
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 243
            self.match(d3iGrammar.LCURLY)
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 23135232) != 0):
                self.state = 244
                self.aggregate_element()
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 250
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
        self.enterRule(localctx, 32, self.RULE_aggregate_element)
        try:
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.aggregate_entity()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 254
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
        self.enterRule(localctx, 34, self.RULE_aggregate_entity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 257
                self.match(d3iGrammar.ROOT)


            self.state = 260
            self.entity()
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

        def IDENTIFIER(self):
            return self.getToken(d3iGrammar.IDENTIFIER, 0)

        def SEMI(self):
            return self.getToken(d3iGrammar.SEMI, 0)

        def qualifiedName(self):
            return self.getTypedRuleContext(d3iGrammar.QualifiedNameContext,0)


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
        self.enterRule(localctx, 36, self.RULE_repository)
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
            self.match(d3iGrammar.REPOSITORY)
            self.state = 269
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 270
            self.match(d3iGrammar.SEMI)
            self.state = 271
            self.qualifiedName()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitService" ):
                return visitor.visitService(self)
            else:
                return visitor.visitChildren(self)




    def service(self):

        localctx = d3iGrammar.ServiceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_service)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 273
                self.decorator()
                self.state = 278
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 279
            self.match(d3iGrammar.SERVICE)
            self.state = 280
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 281
            self.match(d3iGrammar.LCURLY)
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099517953024) != 0):
                self.state = 282
                self.service_element()
                self.state = 287
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 288
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
        self.enterRule(localctx, 40, self.RULE_service_element)
        try:
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.operation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 292
                self.value_object()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 293
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
        self.enterRule(localctx, 42, self.RULE_interface)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 296
                self.decorator()
                self.state = 301
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 302
            self.match(d3iGrammar.INTERFACE)
            self.state = 303
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 304
            self.match(d3iGrammar.LCURLY)
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099517953024) != 0):
                self.state = 305
                self.interface_element()
                self.state = 310
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 311
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
        self.enterRule(localctx, 44, self.RULE_interface_element)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.operation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 315
                self.value_object()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 316
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
        self.enterRule(localctx, 46, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 319
                self.decorator()
                self.state = 324
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 325
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 326
            self.match(d3iGrammar.LPAREN)

            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10 or _la==40:
                self.state = 327
                self.operation_param()


            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 330
                self.match(d3iGrammar.COMMA)
                self.state = 331
                self.operation_param()
                self.state = 336
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 337
            self.match(d3iGrammar.RPAREN)

            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 338
                self.match(d3iGrammar.SEMI)
                self.state = 339
                self.operation_return()


            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 342
                self.match(d3iGrammar.PIPE)
                self.state = 343
                self.operation_return()
                self.state = 348
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
        self.enterRule(localctx, 48, self.RULE_operation_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 349
                self.decorator()
                self.state = 354
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 355
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 356
            self.match(d3iGrammar.SEMI)
            self.state = 357
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
        self.enterRule(localctx, 50, self.RULE_operation_return)
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
        self.enterRule(localctx, 52, self.RULE_acl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 367
                self.decorator()
                self.state = 372
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 373
            self.match(d3iGrammar.ACL)
            self.state = 374
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 375
            self.match(d3iGrammar.LCURLY)
            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099517920256) != 0):
                self.state = 376
                self.acl_element()
                self.state = 381
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 382
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
        self.enterRule(localctx, 54, self.RULE_acl_element)
        try:
            self.state = 387
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.enum()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.value_object()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 386
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
        self.enterRule(localctx, 56, self.RULE_type)
        try:
            self.state = 393
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27, 28, 29, 30, 31, 32, 33, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.primitive_type()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 390
                self.reference_type()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 3)
                self.state = 391
                self.list_type()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 4)
                self.state = 392
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
        self.enterRule(localctx, 58, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 34292629504) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReference_type" ):
                return visitor.visitReference_type(self)
            else:
                return visitor.visitChildren(self)




    def reference_type(self):

        localctx = d3iGrammar.Reference_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_reference_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.qualifiedName()
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
        self.enterRule(localctx, 62, self.RULE_list_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(d3iGrammar.LIST)
            self.state = 400
            self.match(d3iGrammar.LBARCKET)
            self.state = 401
            self.type_()
            self.state = 402
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
        self.enterRule(localctx, 64, self.RULE_map_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(d3iGrammar.MAP)
            self.state = 405
            self.match(d3iGrammar.LBARCKET)
            self.state = 406
            self.type_()
            self.state = 407
            self.match(d3iGrammar.COMMA)
            self.state = 408
            self.type_()
            self.state = 409
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
        self.enterRule(localctx, 66, self.RULE_qualifiedName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 416
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 412
                self.match(d3iGrammar.DOT)
                self.state = 413
                self.match(d3iGrammar.IDENTIFIER)
                self.state = 418
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
        self.enterRule(localctx, 68, self.RULE_decorator)
        self._la = 0 # Token type
        try:
            self.state = 434
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 419
                self.match(d3iGrammar.AT)
                self.state = 420
                self.match(d3iGrammar.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 421
                self.match(d3iGrammar.AT)
                self.state = 422
                self.match(d3iGrammar.IDENTIFIER)
                self.state = 423
                self.match(d3iGrammar.LPAREN)
                self.state = 424
                self.decorator_param()
                self.state = 429
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 425
                    self.match(d3iGrammar.COMMA)
                    self.state = 426
                    self.decorator_param()
                    self.state = 431
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 432
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
        self.enterRule(localctx, 70, self.RULE_decorator_param)
        try:
            self.state = 440
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.qualifiedName()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.match(d3iGrammar.INTEGER_CONSTANS)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 438
                self.match(d3iGrammar.NUMBER_CONSTANS)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 4)
                self.state = 439
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
        self.enterRule(localctx, 72, self.RULE_enum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 442
                self.decorator()
                self.state = 447
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 448
            self.match(d3iGrammar.ENUM)
            self.state = 449
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 450
            self.match(d3iGrammar.LCURLY)
            self.state = 452
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10 or _la==40:
                self.state = 451
                self.enum_element()


            self.state = 458
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 454
                self.match(d3iGrammar.COMMA)
                self.state = 455
                self.enum_element()
                self.state = 460
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 461
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnum_element" ):
                return visitor.visitEnum_element(self)
            else:
                return visitor.visitChildren(self)




    def enum_element(self):

        localctx = d3iGrammar.Enum_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_enum_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 463
                self.decorator()
                self.state = 468
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 469
            self.match(d3iGrammar.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





