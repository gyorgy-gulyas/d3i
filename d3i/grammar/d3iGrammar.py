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
        4,1,43,471,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,1,0,5,0,78,8,0,10,0,
        12,0,81,9,0,1,0,1,0,1,1,5,1,86,8,1,10,1,12,1,89,9,1,1,1,5,1,92,8,
        1,10,1,12,1,95,9,1,1,1,1,1,1,1,1,1,5,1,101,8,1,10,1,12,1,104,9,1,
        1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,4,5,4,114,8,4,10,4,12,4,117,9,4,1,
        4,1,4,1,4,1,4,5,4,123,8,4,10,4,12,4,126,9,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,3,5,137,8,5,1,6,5,6,140,8,6,10,6,12,6,143,9,6,1,
        6,1,6,1,6,1,6,5,6,149,8,6,10,6,12,6,152,9,6,1,6,1,6,1,7,1,7,1,7,
        3,7,159,8,7,1,8,5,8,162,8,8,10,8,12,8,165,9,8,1,8,1,8,1,8,1,8,1,
        9,5,9,172,8,9,10,9,12,9,175,9,9,1,9,1,9,1,9,1,9,5,9,181,8,9,10,9,
        12,9,184,9,9,1,9,1,9,1,10,1,10,1,10,3,10,191,8,10,1,11,5,11,194,
        8,11,10,11,12,11,197,9,11,1,11,1,11,1,11,1,11,1,12,5,12,204,8,12,
        10,12,12,12,207,9,12,1,12,1,12,1,12,1,12,5,12,213,8,12,10,12,12,
        12,216,9,12,1,12,1,12,1,13,1,13,1,13,3,13,223,8,13,1,14,5,14,226,
        8,14,10,14,12,14,229,9,14,1,14,1,14,1,14,1,14,1,15,5,15,236,8,15,
        10,15,12,15,239,9,15,1,15,1,15,1,15,1,15,5,15,245,8,15,10,15,12,
        15,248,9,15,1,15,1,15,1,16,1,16,1,16,3,16,255,8,16,1,17,3,17,258,
        8,17,1,17,1,17,1,18,5,18,263,8,18,10,18,12,18,266,9,18,1,18,1,18,
        1,18,1,18,1,18,1,19,5,19,274,8,19,10,19,12,19,277,9,19,1,19,1,19,
        1,19,1,19,5,19,283,8,19,10,19,12,19,286,9,19,1,19,1,19,1,20,1,20,
        1,20,1,20,3,20,294,8,20,1,21,5,21,297,8,21,10,21,12,21,300,9,21,
        1,21,1,21,1,21,1,21,5,21,306,8,21,10,21,12,21,309,9,21,1,21,1,21,
        1,22,1,22,1,22,1,22,3,22,317,8,22,1,23,5,23,320,8,23,10,23,12,23,
        323,9,23,1,23,1,23,1,23,3,23,328,8,23,1,23,1,23,5,23,332,8,23,10,
        23,12,23,335,9,23,1,23,1,23,1,23,3,23,340,8,23,1,23,1,23,5,23,344,
        8,23,10,23,12,23,347,9,23,1,24,5,24,350,8,24,10,24,12,24,353,9,24,
        1,24,1,24,1,24,1,24,1,25,5,25,360,8,25,10,25,12,25,363,9,25,1,25,
        1,25,1,26,5,26,368,8,26,10,26,12,26,371,9,26,1,26,1,26,1,26,1,26,
        5,26,377,8,26,10,26,12,26,380,9,26,1,26,1,26,1,27,1,27,1,27,3,27,
        387,8,27,1,28,1,28,1,28,1,28,3,28,393,8,28,1,29,1,29,1,30,1,30,1,
        31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,
        33,1,33,5,33,414,8,33,10,33,12,33,417,9,33,1,34,1,34,1,34,1,34,1,
        34,1,34,1,34,1,34,5,34,427,8,34,10,34,12,34,430,9,34,1,34,1,34,3,
        34,434,8,34,1,35,1,35,1,35,1,35,3,35,440,8,35,1,36,5,36,443,8,36,
        10,36,12,36,446,9,36,1,36,1,36,1,36,1,36,3,36,452,8,36,1,36,1,36,
        5,36,456,8,36,10,36,12,36,459,9,36,1,36,1,36,1,37,5,37,464,8,37,
        10,37,12,37,467,9,37,1,37,1,37,1,37,0,0,38,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        62,64,66,68,70,72,74,0,1,1,0,26,34,499,0,79,1,0,0,0,2,87,1,0,0,0,
        4,107,1,0,0,0,6,110,1,0,0,0,8,115,1,0,0,0,10,136,1,0,0,0,12,141,
        1,0,0,0,14,158,1,0,0,0,16,163,1,0,0,0,18,173,1,0,0,0,20,190,1,0,
        0,0,22,195,1,0,0,0,24,205,1,0,0,0,26,222,1,0,0,0,28,227,1,0,0,0,
        30,237,1,0,0,0,32,254,1,0,0,0,34,257,1,0,0,0,36,264,1,0,0,0,38,275,
        1,0,0,0,40,293,1,0,0,0,42,298,1,0,0,0,44,316,1,0,0,0,46,321,1,0,
        0,0,48,351,1,0,0,0,50,361,1,0,0,0,52,369,1,0,0,0,54,386,1,0,0,0,
        56,392,1,0,0,0,58,394,1,0,0,0,60,396,1,0,0,0,62,398,1,0,0,0,64,403,
        1,0,0,0,66,410,1,0,0,0,68,433,1,0,0,0,70,439,1,0,0,0,72,444,1,0,
        0,0,74,465,1,0,0,0,76,78,3,2,1,0,77,76,1,0,0,0,78,81,1,0,0,0,79,
        77,1,0,0,0,79,80,1,0,0,0,80,82,1,0,0,0,81,79,1,0,0,0,82,83,5,0,0,
        1,83,1,1,0,0,0,84,86,3,4,2,0,85,84,1,0,0,0,86,89,1,0,0,0,87,85,1,
        0,0,0,87,88,1,0,0,0,88,93,1,0,0,0,89,87,1,0,0,0,90,92,3,68,34,0,
        91,90,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,96,1,
        0,0,0,95,93,1,0,0,0,96,97,5,13,0,0,97,98,5,40,0,0,98,102,5,6,0,0,
        99,101,3,6,3,0,100,99,1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,
        103,1,0,0,0,103,105,1,0,0,0,104,102,1,0,0,0,105,106,5,7,0,0,106,
        3,1,0,0,0,107,108,5,40,0,0,108,109,3,66,33,0,109,5,1,0,0,0,110,111,
        3,8,4,0,111,7,1,0,0,0,112,114,3,68,34,0,113,112,1,0,0,0,114,117,
        1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,118,1,0,0,0,117,115,
        1,0,0,0,118,119,5,14,0,0,119,120,5,40,0,0,120,124,5,6,0,0,121,123,
        3,10,5,0,122,121,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,
        1,0,0,0,125,127,1,0,0,0,126,124,1,0,0,0,127,128,5,7,0,0,128,9,1,
        0,0,0,129,137,3,72,36,0,130,137,3,12,6,0,131,137,3,30,15,0,132,137,
        3,36,18,0,133,137,3,52,26,0,134,137,3,38,19,0,135,137,3,42,21,0,
        136,129,1,0,0,0,136,130,1,0,0,0,136,131,1,0,0,0,136,132,1,0,0,0,
        136,133,1,0,0,0,136,134,1,0,0,0,136,135,1,0,0,0,137,11,1,0,0,0,138,
        140,3,68,34,0,139,138,1,0,0,0,140,143,1,0,0,0,141,139,1,0,0,0,141,
        142,1,0,0,0,142,144,1,0,0,0,143,141,1,0,0,0,144,145,5,21,0,0,145,
        146,5,40,0,0,146,150,5,6,0,0,147,149,3,14,7,0,148,147,1,0,0,0,149,
        152,1,0,0,0,150,148,1,0,0,0,150,151,1,0,0,0,151,153,1,0,0,0,152,
        150,1,0,0,0,153,154,5,7,0,0,154,13,1,0,0,0,155,159,3,16,8,0,156,
        159,3,72,36,0,157,159,3,12,6,0,158,155,1,0,0,0,158,156,1,0,0,0,158,
        157,1,0,0,0,159,15,1,0,0,0,160,162,3,68,34,0,161,160,1,0,0,0,162,
        165,1,0,0,0,163,161,1,0,0,0,163,164,1,0,0,0,164,166,1,0,0,0,165,
        163,1,0,0,0,166,167,5,40,0,0,167,168,5,3,0,0,168,169,3,56,28,0,169,
        17,1,0,0,0,170,172,3,68,34,0,171,170,1,0,0,0,172,175,1,0,0,0,173,
        171,1,0,0,0,173,174,1,0,0,0,174,176,1,0,0,0,175,173,1,0,0,0,176,
        177,5,15,0,0,177,178,5,40,0,0,178,182,5,6,0,0,179,181,3,20,10,0,
        180,179,1,0,0,0,181,184,1,0,0,0,182,180,1,0,0,0,182,183,1,0,0,0,
        183,185,1,0,0,0,184,182,1,0,0,0,185,186,5,7,0,0,186,19,1,0,0,0,187,
        191,3,22,11,0,188,191,3,72,36,0,189,191,3,12,6,0,190,187,1,0,0,0,
        190,188,1,0,0,0,190,189,1,0,0,0,191,21,1,0,0,0,192,194,3,68,34,0,
        193,192,1,0,0,0,194,197,1,0,0,0,195,193,1,0,0,0,195,196,1,0,0,0,
        196,198,1,0,0,0,197,195,1,0,0,0,198,199,5,40,0,0,199,200,5,3,0,0,
        200,201,3,56,28,0,201,23,1,0,0,0,202,204,3,68,34,0,203,202,1,0,0,
        0,204,207,1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,208,1,0,0,
        0,207,205,1,0,0,0,208,209,5,16,0,0,209,210,5,40,0,0,210,214,5,6,
        0,0,211,213,3,26,13,0,212,211,1,0,0,0,213,216,1,0,0,0,214,212,1,
        0,0,0,214,215,1,0,0,0,215,217,1,0,0,0,216,214,1,0,0,0,217,218,5,
        7,0,0,218,25,1,0,0,0,219,223,3,28,14,0,220,223,3,72,36,0,221,223,
        3,12,6,0,222,219,1,0,0,0,222,220,1,0,0,0,222,221,1,0,0,0,223,27,
        1,0,0,0,224,226,3,68,34,0,225,224,1,0,0,0,226,229,1,0,0,0,227,225,
        1,0,0,0,227,228,1,0,0,0,228,230,1,0,0,0,229,227,1,0,0,0,230,231,
        5,40,0,0,231,232,5,3,0,0,232,233,3,56,28,0,233,29,1,0,0,0,234,236,
        3,68,34,0,235,234,1,0,0,0,236,239,1,0,0,0,237,235,1,0,0,0,237,238,
        1,0,0,0,238,240,1,0,0,0,239,237,1,0,0,0,240,241,5,17,0,0,241,242,
        5,40,0,0,242,246,5,6,0,0,243,245,3,32,16,0,244,243,1,0,0,0,245,248,
        1,0,0,0,246,244,1,0,0,0,246,247,1,0,0,0,247,249,1,0,0,0,248,246,
        1,0,0,0,249,250,5,7,0,0,250,31,1,0,0,0,251,255,3,34,17,0,252,255,
        3,72,36,0,253,255,3,12,6,0,254,251,1,0,0,0,254,252,1,0,0,0,254,253,
        1,0,0,0,255,33,1,0,0,0,256,258,5,24,0,0,257,256,1,0,0,0,257,258,
        1,0,0,0,258,259,1,0,0,0,259,260,3,24,12,0,260,35,1,0,0,0,261,263,
        3,68,34,0,262,261,1,0,0,0,263,266,1,0,0,0,264,262,1,0,0,0,264,265,
        1,0,0,0,265,267,1,0,0,0,266,264,1,0,0,0,267,268,5,23,0,0,268,269,
        5,40,0,0,269,270,5,3,0,0,270,271,5,40,0,0,271,37,1,0,0,0,272,274,
        3,68,34,0,273,272,1,0,0,0,274,277,1,0,0,0,275,273,1,0,0,0,275,276,
        1,0,0,0,276,278,1,0,0,0,277,275,1,0,0,0,278,279,5,18,0,0,279,280,
        5,40,0,0,280,284,5,6,0,0,281,283,3,40,20,0,282,281,1,0,0,0,283,286,
        1,0,0,0,284,282,1,0,0,0,284,285,1,0,0,0,285,287,1,0,0,0,286,284,
        1,0,0,0,287,288,5,7,0,0,288,39,1,0,0,0,289,294,3,46,23,0,290,294,
        3,72,36,0,291,294,3,12,6,0,292,294,3,18,9,0,293,289,1,0,0,0,293,
        290,1,0,0,0,293,291,1,0,0,0,293,292,1,0,0,0,294,41,1,0,0,0,295,297,
        3,68,34,0,296,295,1,0,0,0,297,300,1,0,0,0,298,296,1,0,0,0,298,299,
        1,0,0,0,299,301,1,0,0,0,300,298,1,0,0,0,301,302,5,19,0,0,302,303,
        5,40,0,0,303,307,5,6,0,0,304,306,3,44,22,0,305,304,1,0,0,0,306,309,
        1,0,0,0,307,305,1,0,0,0,307,308,1,0,0,0,308,310,1,0,0,0,309,307,
        1,0,0,0,310,311,5,7,0,0,311,43,1,0,0,0,312,317,3,46,23,0,313,317,
        3,72,36,0,314,317,3,12,6,0,315,317,3,18,9,0,316,312,1,0,0,0,316,
        313,1,0,0,0,316,314,1,0,0,0,316,315,1,0,0,0,317,45,1,0,0,0,318,320,
        3,68,34,0,319,318,1,0,0,0,320,323,1,0,0,0,321,319,1,0,0,0,321,322,
        1,0,0,0,322,324,1,0,0,0,323,321,1,0,0,0,324,325,5,40,0,0,325,327,
        5,4,0,0,326,328,3,48,24,0,327,326,1,0,0,0,327,328,1,0,0,0,328,333,
        1,0,0,0,329,330,5,2,0,0,330,332,3,48,24,0,331,329,1,0,0,0,332,335,
        1,0,0,0,333,331,1,0,0,0,333,334,1,0,0,0,334,336,1,0,0,0,335,333,
        1,0,0,0,336,339,5,5,0,0,337,338,5,3,0,0,338,340,3,50,25,0,339,337,
        1,0,0,0,339,340,1,0,0,0,340,345,1,0,0,0,341,342,5,12,0,0,342,344,
        3,50,25,0,343,341,1,0,0,0,344,347,1,0,0,0,345,343,1,0,0,0,345,346,
        1,0,0,0,346,47,1,0,0,0,347,345,1,0,0,0,348,350,3,68,34,0,349,348,
        1,0,0,0,350,353,1,0,0,0,351,349,1,0,0,0,351,352,1,0,0,0,352,354,
        1,0,0,0,353,351,1,0,0,0,354,355,5,40,0,0,355,356,5,3,0,0,356,357,
        3,56,28,0,357,49,1,0,0,0,358,360,3,68,34,0,359,358,1,0,0,0,360,363,
        1,0,0,0,361,359,1,0,0,0,361,362,1,0,0,0,362,364,1,0,0,0,363,361,
        1,0,0,0,364,365,3,56,28,0,365,51,1,0,0,0,366,368,3,68,34,0,367,366,
        1,0,0,0,368,371,1,0,0,0,369,367,1,0,0,0,369,370,1,0,0,0,370,372,
        1,0,0,0,371,369,1,0,0,0,372,373,5,20,0,0,373,374,5,40,0,0,374,378,
        5,6,0,0,375,377,3,54,27,0,376,375,1,0,0,0,377,380,1,0,0,0,378,376,
        1,0,0,0,378,379,1,0,0,0,379,381,1,0,0,0,380,378,1,0,0,0,381,382,
        5,7,0,0,382,53,1,0,0,0,383,387,3,72,36,0,384,387,3,12,6,0,385,387,
        3,46,23,0,386,383,1,0,0,0,386,384,1,0,0,0,386,385,1,0,0,0,387,55,
        1,0,0,0,388,393,3,58,29,0,389,393,3,60,30,0,390,393,3,62,31,0,391,
        393,3,64,32,0,392,388,1,0,0,0,392,389,1,0,0,0,392,390,1,0,0,0,392,
        391,1,0,0,0,393,57,1,0,0,0,394,395,7,0,0,0,395,59,1,0,0,0,396,397,
        3,66,33,0,397,61,1,0,0,0,398,399,5,35,0,0,399,400,5,8,0,0,400,401,
        3,56,28,0,401,402,5,9,0,0,402,63,1,0,0,0,403,404,5,36,0,0,404,405,
        5,8,0,0,405,406,3,56,28,0,406,407,5,2,0,0,407,408,3,56,28,0,408,
        409,5,9,0,0,409,65,1,0,0,0,410,415,5,40,0,0,411,412,5,1,0,0,412,
        414,5,40,0,0,413,411,1,0,0,0,414,417,1,0,0,0,415,413,1,0,0,0,415,
        416,1,0,0,0,416,67,1,0,0,0,417,415,1,0,0,0,418,419,5,10,0,0,419,
        434,5,40,0,0,420,421,5,10,0,0,421,422,5,40,0,0,422,423,5,4,0,0,423,
        428,3,70,35,0,424,425,5,2,0,0,425,427,3,70,35,0,426,424,1,0,0,0,
        427,430,1,0,0,0,428,426,1,0,0,0,428,429,1,0,0,0,429,431,1,0,0,0,
        430,428,1,0,0,0,431,432,5,5,0,0,432,434,1,0,0,0,433,418,1,0,0,0,
        433,420,1,0,0,0,434,69,1,0,0,0,435,440,3,66,33,0,436,440,5,37,0,
        0,437,440,5,38,0,0,438,440,5,39,0,0,439,435,1,0,0,0,439,436,1,0,
        0,0,439,437,1,0,0,0,439,438,1,0,0,0,440,71,1,0,0,0,441,443,3,68,
        34,0,442,441,1,0,0,0,443,446,1,0,0,0,444,442,1,0,0,0,444,445,1,0,
        0,0,445,447,1,0,0,0,446,444,1,0,0,0,447,448,5,22,0,0,448,449,5,40,
        0,0,449,451,5,6,0,0,450,452,3,74,37,0,451,450,1,0,0,0,451,452,1,
        0,0,0,452,457,1,0,0,0,453,454,5,2,0,0,454,456,3,74,37,0,455,453,
        1,0,0,0,456,459,1,0,0,0,457,455,1,0,0,0,457,458,1,0,0,0,458,460,
        1,0,0,0,459,457,1,0,0,0,460,461,5,7,0,0,461,73,1,0,0,0,462,464,3,
        68,34,0,463,462,1,0,0,0,464,467,1,0,0,0,465,463,1,0,0,0,465,466,
        1,0,0,0,466,468,1,0,0,0,467,465,1,0,0,0,468,469,5,40,0,0,469,75,
        1,0,0,0,49,79,87,93,102,115,124,136,141,150,158,163,173,182,190,
        195,205,214,222,227,237,246,254,257,264,275,284,293,298,307,316,
        321,327,333,339,345,351,361,369,378,386,392,415,428,433,439,444,
        451,457,465
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16647168) != 0):
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
            self.state = 136
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
                self.aggregate()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 132
                self.repository()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 133
                self.acl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 134
                self.service()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 135
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
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 138
                self.decorator()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 144
            self.match(d3iGrammar.VALUEOBJECT)
            self.state = 145
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 146
            self.match(d3iGrammar.LCURLY)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099517920256) != 0):
                self.state = 147
                self.value_object_element()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 153
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
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.value_object_member()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 157
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
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 160
                self.decorator()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 166
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 167
            self.match(d3iGrammar.SEMI)
            self.state = 168
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
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 170
                self.decorator()
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 176
            self.match(d3iGrammar.EVENT)
            self.state = 177
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 178
            self.match(d3iGrammar.LCURLY)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099517920256) != 0):
                self.state = 179
                self.event_element()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 185
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
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.event_member()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 189
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
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 192
                self.decorator()
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 198
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 199
            self.match(d3iGrammar.SEMI)
            self.state = 200
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
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 202
                self.decorator()
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 208
            self.match(d3iGrammar.ENTITY)
            self.state = 209
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 210
            self.match(d3iGrammar.LCURLY)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099517920256) != 0):
                self.state = 211
                self.entity_element()
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 217
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
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.entity_member()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
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
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 224
                self.decorator()
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 230
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 231
            self.match(d3iGrammar.SEMI)
            self.state = 232
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
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 234
                self.decorator()
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 240
            self.match(d3iGrammar.AGGREGATE)
            self.state = 241
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 242
            self.match(d3iGrammar.LCURLY)
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 23135232) != 0):
                self.state = 243
                self.aggregate_element()
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 249
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
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.aggregate_entity()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 253
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
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 256
                self.match(d3iGrammar.ROOT)


            self.state = 259
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
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 261
                self.decorator()
                self.state = 266
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 267
            self.match(d3iGrammar.REPOSITORY)
            self.state = 268
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 269
            self.match(d3iGrammar.SEMI)
            self.state = 270
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
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 272
                self.decorator()
                self.state = 277
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 278
            self.match(d3iGrammar.SERVICE)
            self.state = 279
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 280
            self.match(d3iGrammar.LCURLY)
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099517953024) != 0):
                self.state = 281
                self.service_element()
                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 287
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
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.operation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 291
                self.value_object()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 292
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
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 295
                self.decorator()
                self.state = 300
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 301
            self.match(d3iGrammar.INTERFACE)
            self.state = 302
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 303
            self.match(d3iGrammar.LCURLY)
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099517953024) != 0):
                self.state = 304
                self.interface_element()
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
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.operation()
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

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 315
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
            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 318
                self.decorator()
                self.state = 323
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 324
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 325
            self.match(d3iGrammar.LPAREN)

            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10 or _la==40:
                self.state = 326
                self.operation_param()


            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 329
                self.match(d3iGrammar.COMMA)
                self.state = 330
                self.operation_param()
                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 336
            self.match(d3iGrammar.RPAREN)

            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 337
                self.match(d3iGrammar.SEMI)
                self.state = 338
                self.operation_return()


            self.state = 345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 341
                self.match(d3iGrammar.PIPE)
                self.state = 342
                self.operation_return()
                self.state = 347
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
            self.state = 351
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 348
                self.decorator()
                self.state = 353
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 354
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 355
            self.match(d3iGrammar.SEMI)
            self.state = 356
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
            self.state = 361
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 358
                self.decorator()
                self.state = 363
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 364
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
            self.state = 369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 366
                self.decorator()
                self.state = 371
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 372
            self.match(d3iGrammar.ACL)
            self.state = 373
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 374
            self.match(d3iGrammar.LCURLY)
            self.state = 378
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099517920256) != 0):
                self.state = 375
                self.acl_element()
                self.state = 380
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 381
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
            self.state = 386
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.enum()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
                self.value_object()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 385
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
            self.state = 392
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27, 28, 29, 30, 31, 32, 33, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.primitive_type()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.reference_type()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 3)
                self.state = 390
                self.list_type()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 4)
                self.state = 391
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
            self.state = 394
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
            self.state = 396
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
            self.state = 398
            self.match(d3iGrammar.LIST)
            self.state = 399
            self.match(d3iGrammar.LBARCKET)
            self.state = 400
            self.type_()
            self.state = 401
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
            self.state = 403
            self.match(d3iGrammar.MAP)
            self.state = 404
            self.match(d3iGrammar.LBARCKET)
            self.state = 405
            self.type_()
            self.state = 406
            self.match(d3iGrammar.COMMA)
            self.state = 407
            self.type_()
            self.state = 408
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
            self.state = 410
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 415
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 411
                self.match(d3iGrammar.DOT)
                self.state = 412
                self.match(d3iGrammar.IDENTIFIER)
                self.state = 417
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
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.match(d3iGrammar.AT)
                self.state = 419
                self.match(d3iGrammar.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 420
                self.match(d3iGrammar.AT)
                self.state = 421
                self.match(d3iGrammar.IDENTIFIER)
                self.state = 422
                self.match(d3iGrammar.LPAREN)
                self.state = 423
                self.decorator_param()
                self.state = 428
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 424
                    self.match(d3iGrammar.COMMA)
                    self.state = 425
                    self.decorator_param()
                    self.state = 430
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 431
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
            self.state = 439
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.qualifiedName()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 436
                self.match(d3iGrammar.INTEGER_CONSTANS)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 437
                self.match(d3iGrammar.NUMBER_CONSTANS)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 4)
                self.state = 438
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
            self.state = 444
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 441
                self.decorator()
                self.state = 446
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 447
            self.match(d3iGrammar.ENUM)
            self.state = 448
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 449
            self.match(d3iGrammar.LCURLY)
            self.state = 451
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10 or _la==40:
                self.state = 450
                self.enum_element()


            self.state = 457
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 453
                self.match(d3iGrammar.COMMA)
                self.state = 454
                self.enum_element()
                self.state = 459
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 460
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
            self.state = 465
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 462
                self.decorator()
                self.state = 467
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 468
            self.match(d3iGrammar.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





