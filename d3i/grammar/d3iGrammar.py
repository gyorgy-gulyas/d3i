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
        4,1,50,735,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,1,0,
        5,0,94,8,0,10,0,12,0,97,9,0,1,0,5,0,100,8,0,10,0,12,0,103,9,0,1,
        0,1,0,1,1,5,1,108,8,1,10,1,12,1,111,9,1,1,1,1,1,1,1,1,2,5,2,117,
        8,2,10,2,12,2,120,9,2,1,2,5,2,123,8,2,10,2,12,2,126,9,2,1,2,5,2,
        129,8,2,10,2,12,2,132,9,2,1,2,1,2,1,2,1,2,5,2,138,8,2,10,2,12,2,
        141,9,2,1,2,1,2,1,3,5,3,146,8,3,10,3,12,3,149,9,3,1,3,1,3,1,3,1,
        4,1,4,1,5,5,5,157,8,5,10,5,12,5,160,9,5,1,5,5,5,163,8,5,10,5,12,
        5,166,9,5,1,5,1,5,1,5,1,5,5,5,172,8,5,10,5,12,5,175,9,5,1,5,1,5,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,188,8,6,1,7,5,7,191,8,7,
        10,7,12,7,194,9,7,1,7,5,7,197,8,7,10,7,12,7,200,9,7,1,7,1,7,1,7,
        3,7,205,8,7,1,7,1,7,5,7,209,8,7,10,7,12,7,212,9,7,1,7,1,7,1,8,1,
        8,1,8,3,8,219,8,8,1,9,5,9,222,8,9,10,9,12,9,225,9,9,1,9,5,9,228,
        8,9,10,9,12,9,231,9,9,1,9,1,9,1,9,1,9,1,10,5,10,238,8,10,10,10,12,
        10,241,9,10,1,10,5,10,244,8,10,10,10,12,10,247,9,10,1,10,1,10,1,
        10,3,10,252,8,10,1,10,1,10,5,10,256,8,10,10,10,12,10,259,9,10,1,
        10,1,10,1,11,1,11,1,11,3,11,266,8,11,1,12,5,12,269,8,12,10,12,12,
        12,272,9,12,1,12,5,12,275,8,12,10,12,12,12,278,9,12,1,12,1,12,1,
        12,1,12,1,13,5,13,285,8,13,10,13,12,13,288,9,13,1,13,5,13,291,8,
        13,10,13,12,13,294,9,13,1,13,1,13,1,13,3,13,299,8,13,1,13,1,13,5,
        13,303,8,13,10,13,12,13,306,9,13,1,13,1,13,1,14,1,14,1,14,3,14,313,
        8,14,1,15,5,15,316,8,15,10,15,12,15,319,9,15,1,15,5,15,322,8,15,
        10,15,12,15,325,9,15,1,15,1,15,1,15,1,15,1,16,5,16,332,8,16,10,16,
        12,16,335,9,16,1,16,5,16,338,8,16,10,16,12,16,341,9,16,1,16,1,16,
        1,16,3,16,346,8,16,1,16,1,16,5,16,350,8,16,10,16,12,16,353,9,16,
        1,16,1,16,1,17,1,17,1,17,3,17,360,8,17,1,18,5,18,363,8,18,10,18,
        12,18,366,9,18,1,18,5,18,369,8,18,10,18,12,18,372,9,18,1,18,1,18,
        1,18,1,18,1,19,5,19,379,8,19,10,19,12,19,382,9,19,1,19,5,19,385,
        8,19,10,19,12,19,388,9,19,1,19,1,19,1,19,1,19,5,19,394,8,19,10,19,
        12,19,397,9,19,1,19,1,19,1,20,1,20,1,20,3,20,404,8,20,1,21,3,21,
        407,8,21,1,21,1,21,1,22,5,22,412,8,22,10,22,12,22,415,9,22,1,22,
        5,22,418,8,22,10,22,12,22,421,9,22,1,22,1,22,1,22,3,22,426,8,22,
        1,22,1,22,5,22,430,8,22,10,22,12,22,433,9,22,1,22,1,22,1,23,1,23,
        1,23,3,23,440,8,23,1,24,5,24,443,8,24,10,24,12,24,446,9,24,1,24,
        5,24,449,8,24,10,24,12,24,452,9,24,1,24,1,24,1,24,1,24,1,25,5,25,
        459,8,25,10,25,12,25,462,9,25,1,25,5,25,465,8,25,10,25,12,25,468,
        9,25,1,25,1,25,1,25,1,25,1,25,1,26,5,26,476,8,26,10,26,12,26,479,
        9,26,1,26,5,26,482,8,26,10,26,12,26,485,9,26,1,26,1,26,1,26,1,26,
        5,26,491,8,26,10,26,12,26,494,9,26,1,26,1,26,1,27,1,27,1,27,1,27,
        3,27,502,8,27,1,28,5,28,505,8,28,10,28,12,28,508,9,28,1,28,5,28,
        511,8,28,10,28,12,28,514,9,28,1,28,1,28,1,28,1,28,5,28,520,8,28,
        10,28,12,28,523,9,28,1,28,1,28,1,29,1,29,1,29,1,29,3,29,531,8,29,
        1,30,5,30,534,8,30,10,30,12,30,537,9,30,1,30,5,30,540,8,30,10,30,
        12,30,543,9,30,1,30,1,30,1,30,3,30,548,8,30,1,30,1,30,5,30,552,8,
        30,10,30,12,30,555,9,30,1,30,1,30,1,30,3,30,560,8,30,1,30,1,30,5,
        30,564,8,30,10,30,12,30,567,9,30,1,31,5,31,570,8,31,10,31,12,31,
        573,9,31,1,31,5,31,576,8,31,10,31,12,31,579,9,31,1,31,1,31,1,31,
        1,31,1,32,5,32,586,8,32,10,32,12,32,589,9,32,1,32,5,32,592,8,32,
        10,32,12,32,595,9,32,1,32,1,32,1,33,5,33,600,8,33,10,33,12,33,603,
        9,33,1,33,5,33,606,8,33,10,33,12,33,609,9,33,1,33,1,33,1,33,1,33,
        5,33,615,8,33,10,33,12,33,618,9,33,1,33,1,33,1,34,1,34,1,34,3,34,
        625,8,34,1,35,1,35,1,35,1,35,3,35,631,8,35,1,36,1,36,1,37,1,37,1,
        37,1,37,1,37,3,37,640,8,37,1,38,1,38,1,38,1,38,1,38,1,39,1,39,1,
        39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,5,40,657,8,40,10,40,12,40,
        660,9,40,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,5,41,670,8,41,10,
        41,12,41,673,9,41,1,41,1,41,3,41,677,8,41,1,42,1,42,1,42,1,42,3,
        42,683,8,42,1,43,5,43,686,8,43,10,43,12,43,689,9,43,1,43,5,43,692,
        8,43,10,43,12,43,695,9,43,1,43,1,43,1,43,1,43,3,43,701,8,43,1,43,
        1,43,5,43,705,8,43,10,43,12,43,708,9,43,1,43,1,43,1,44,5,44,713,
        8,44,10,44,12,44,716,9,44,1,44,5,44,719,8,44,10,44,12,44,722,9,44,
        1,44,1,44,1,45,1,45,1,45,1,45,5,45,730,8,45,10,45,12,45,733,9,45,
        1,45,0,0,46,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,
        82,84,86,88,90,0,1,1,0,29,39,799,0,95,1,0,0,0,2,109,1,0,0,0,4,118,
        1,0,0,0,6,147,1,0,0,0,8,153,1,0,0,0,10,158,1,0,0,0,12,187,1,0,0,
        0,14,192,1,0,0,0,16,218,1,0,0,0,18,223,1,0,0,0,20,239,1,0,0,0,22,
        265,1,0,0,0,24,270,1,0,0,0,26,286,1,0,0,0,28,312,1,0,0,0,30,317,
        1,0,0,0,32,333,1,0,0,0,34,359,1,0,0,0,36,364,1,0,0,0,38,380,1,0,
        0,0,40,403,1,0,0,0,42,406,1,0,0,0,44,413,1,0,0,0,46,439,1,0,0,0,
        48,444,1,0,0,0,50,460,1,0,0,0,52,477,1,0,0,0,54,501,1,0,0,0,56,506,
        1,0,0,0,58,530,1,0,0,0,60,535,1,0,0,0,62,571,1,0,0,0,64,587,1,0,
        0,0,66,601,1,0,0,0,68,624,1,0,0,0,70,630,1,0,0,0,72,632,1,0,0,0,
        74,639,1,0,0,0,76,641,1,0,0,0,78,646,1,0,0,0,80,653,1,0,0,0,82,676,
        1,0,0,0,84,682,1,0,0,0,86,687,1,0,0,0,88,714,1,0,0,0,90,725,1,0,
        0,0,92,94,3,2,1,0,93,92,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,
        1,0,0,0,96,101,1,0,0,0,97,95,1,0,0,0,98,100,3,4,2,0,99,98,1,0,0,
        0,100,103,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,104,1,0,0,0,
        103,101,1,0,0,0,104,105,5,0,0,1,105,1,1,0,0,0,106,108,5,48,0,0,107,
        106,1,0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,
        112,1,0,0,0,111,109,1,0,0,0,112,113,5,20,0,0,113,114,3,80,40,0,114,
        3,1,0,0,0,115,117,3,6,3,0,116,115,1,0,0,0,117,120,1,0,0,0,118,116,
        1,0,0,0,118,119,1,0,0,0,119,124,1,0,0,0,120,118,1,0,0,0,121,123,
        5,48,0,0,122,121,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,
        1,0,0,0,125,130,1,0,0,0,126,124,1,0,0,0,127,129,3,82,41,0,128,127,
        1,0,0,0,129,132,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,133,
        1,0,0,0,132,130,1,0,0,0,133,134,5,16,0,0,134,135,5,46,0,0,135,139,
        5,6,0,0,136,138,3,8,4,0,137,136,1,0,0,0,138,141,1,0,0,0,139,137,
        1,0,0,0,139,140,1,0,0,0,140,142,1,0,0,0,141,139,1,0,0,0,142,143,
        5,7,0,0,143,5,1,0,0,0,144,146,5,48,0,0,145,144,1,0,0,0,146,149,1,
        0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,150,1,0,0,0,149,147,1,
        0,0,0,150,151,5,46,0,0,151,152,3,80,40,0,152,7,1,0,0,0,153,154,3,
        10,5,0,154,9,1,0,0,0,155,157,5,48,0,0,156,155,1,0,0,0,157,160,1,
        0,0,0,158,156,1,0,0,0,158,159,1,0,0,0,159,164,1,0,0,0,160,158,1,
        0,0,0,161,163,3,82,41,0,162,161,1,0,0,0,163,166,1,0,0,0,164,162,
        1,0,0,0,164,165,1,0,0,0,165,167,1,0,0,0,166,164,1,0,0,0,167,168,
        5,15,0,0,168,169,5,46,0,0,169,173,5,6,0,0,170,172,3,12,6,0,171,170,
        1,0,0,0,172,175,1,0,0,0,173,171,1,0,0,0,173,174,1,0,0,0,174,176,
        1,0,0,0,175,173,1,0,0,0,176,177,5,7,0,0,177,11,1,0,0,0,178,188,3,
        86,43,0,179,188,3,14,7,0,180,188,3,20,10,0,181,188,3,38,19,0,182,
        188,3,44,22,0,183,188,3,50,25,0,184,188,3,66,33,0,185,188,3,52,26,
        0,186,188,3,56,28,0,187,178,1,0,0,0,187,179,1,0,0,0,187,180,1,0,
        0,0,187,181,1,0,0,0,187,182,1,0,0,0,187,183,1,0,0,0,187,184,1,0,
        0,0,187,185,1,0,0,0,187,186,1,0,0,0,188,13,1,0,0,0,189,191,5,48,
        0,0,190,189,1,0,0,0,191,194,1,0,0,0,192,190,1,0,0,0,192,193,1,0,
        0,0,193,198,1,0,0,0,194,192,1,0,0,0,195,197,3,82,41,0,196,195,1,
        0,0,0,197,200,1,0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,201,1,
        0,0,0,200,198,1,0,0,0,201,202,5,25,0,0,202,204,5,46,0,0,203,205,
        3,90,45,0,204,203,1,0,0,0,204,205,1,0,0,0,205,206,1,0,0,0,206,210,
        5,6,0,0,207,209,3,16,8,0,208,207,1,0,0,0,209,212,1,0,0,0,210,208,
        1,0,0,0,210,211,1,0,0,0,211,213,1,0,0,0,212,210,1,0,0,0,213,214,
        5,7,0,0,214,15,1,0,0,0,215,219,3,18,9,0,216,219,3,86,43,0,217,219,
        3,14,7,0,218,215,1,0,0,0,218,216,1,0,0,0,218,217,1,0,0,0,219,17,
        1,0,0,0,220,222,5,48,0,0,221,220,1,0,0,0,222,225,1,0,0,0,223,221,
        1,0,0,0,223,224,1,0,0,0,224,229,1,0,0,0,225,223,1,0,0,0,226,228,
        3,82,41,0,227,226,1,0,0,0,228,231,1,0,0,0,229,227,1,0,0,0,229,230,
        1,0,0,0,230,232,1,0,0,0,231,229,1,0,0,0,232,233,5,46,0,0,233,234,
        5,3,0,0,234,235,3,70,35,0,235,19,1,0,0,0,236,238,5,48,0,0,237,236,
        1,0,0,0,238,241,1,0,0,0,239,237,1,0,0,0,239,240,1,0,0,0,240,245,
        1,0,0,0,241,239,1,0,0,0,242,244,3,82,41,0,243,242,1,0,0,0,244,247,
        1,0,0,0,245,243,1,0,0,0,245,246,1,0,0,0,246,248,1,0,0,0,247,245,
        1,0,0,0,248,249,5,24,0,0,249,251,5,46,0,0,250,252,3,90,45,0,251,
        250,1,0,0,0,251,252,1,0,0,0,252,253,1,0,0,0,253,257,5,6,0,0,254,
        256,3,22,11,0,255,254,1,0,0,0,256,259,1,0,0,0,257,255,1,0,0,0,257,
        258,1,0,0,0,258,260,1,0,0,0,259,257,1,0,0,0,260,261,5,7,0,0,261,
        21,1,0,0,0,262,266,3,24,12,0,263,266,3,86,43,0,264,266,3,14,7,0,
        265,262,1,0,0,0,265,263,1,0,0,0,265,264,1,0,0,0,266,23,1,0,0,0,267,
        269,5,48,0,0,268,267,1,0,0,0,269,272,1,0,0,0,270,268,1,0,0,0,270,
        271,1,0,0,0,271,276,1,0,0,0,272,270,1,0,0,0,273,275,3,82,41,0,274,
        273,1,0,0,0,275,278,1,0,0,0,276,274,1,0,0,0,276,277,1,0,0,0,277,
        279,1,0,0,0,278,276,1,0,0,0,279,280,5,46,0,0,280,281,5,3,0,0,281,
        282,3,70,35,0,282,25,1,0,0,0,283,285,5,48,0,0,284,283,1,0,0,0,285,
        288,1,0,0,0,286,284,1,0,0,0,286,287,1,0,0,0,287,292,1,0,0,0,288,
        286,1,0,0,0,289,291,3,82,41,0,290,289,1,0,0,0,291,294,1,0,0,0,292,
        290,1,0,0,0,292,293,1,0,0,0,293,295,1,0,0,0,294,292,1,0,0,0,295,
        296,5,19,0,0,296,298,5,46,0,0,297,299,3,90,45,0,298,297,1,0,0,0,
        298,299,1,0,0,0,299,300,1,0,0,0,300,304,5,6,0,0,301,303,3,28,14,
        0,302,301,1,0,0,0,303,306,1,0,0,0,304,302,1,0,0,0,304,305,1,0,0,
        0,305,307,1,0,0,0,306,304,1,0,0,0,307,308,5,7,0,0,308,27,1,0,0,0,
        309,313,3,30,15,0,310,313,3,86,43,0,311,313,3,14,7,0,312,309,1,0,
        0,0,312,310,1,0,0,0,312,311,1,0,0,0,313,29,1,0,0,0,314,316,5,48,
        0,0,315,314,1,0,0,0,316,319,1,0,0,0,317,315,1,0,0,0,317,318,1,0,
        0,0,318,323,1,0,0,0,319,317,1,0,0,0,320,322,3,82,41,0,321,320,1,
        0,0,0,322,325,1,0,0,0,323,321,1,0,0,0,323,324,1,0,0,0,324,326,1,
        0,0,0,325,323,1,0,0,0,326,327,5,46,0,0,327,328,5,3,0,0,328,329,3,
        70,35,0,329,31,1,0,0,0,330,332,5,48,0,0,331,330,1,0,0,0,332,335,
        1,0,0,0,333,331,1,0,0,0,333,334,1,0,0,0,334,339,1,0,0,0,335,333,
        1,0,0,0,336,338,3,82,41,0,337,336,1,0,0,0,338,341,1,0,0,0,339,337,
        1,0,0,0,339,340,1,0,0,0,340,342,1,0,0,0,341,339,1,0,0,0,342,343,
        5,17,0,0,343,345,5,46,0,0,344,346,3,90,45,0,345,344,1,0,0,0,345,
        346,1,0,0,0,346,347,1,0,0,0,347,351,5,6,0,0,348,350,3,34,17,0,349,
        348,1,0,0,0,350,353,1,0,0,0,351,349,1,0,0,0,351,352,1,0,0,0,352,
        354,1,0,0,0,353,351,1,0,0,0,354,355,5,7,0,0,355,33,1,0,0,0,356,360,
        3,36,18,0,357,360,3,86,43,0,358,360,3,14,7,0,359,356,1,0,0,0,359,
        357,1,0,0,0,359,358,1,0,0,0,360,35,1,0,0,0,361,363,5,48,0,0,362,
        361,1,0,0,0,363,366,1,0,0,0,364,362,1,0,0,0,364,365,1,0,0,0,365,
        370,1,0,0,0,366,364,1,0,0,0,367,369,3,82,41,0,368,367,1,0,0,0,369,
        372,1,0,0,0,370,368,1,0,0,0,370,371,1,0,0,0,371,373,1,0,0,0,372,
        370,1,0,0,0,373,374,5,46,0,0,374,375,5,3,0,0,375,376,3,70,35,0,376,
        37,1,0,0,0,377,379,5,48,0,0,378,377,1,0,0,0,379,382,1,0,0,0,380,
        378,1,0,0,0,380,381,1,0,0,0,381,386,1,0,0,0,382,380,1,0,0,0,383,
        385,3,82,41,0,384,383,1,0,0,0,385,388,1,0,0,0,386,384,1,0,0,0,386,
        387,1,0,0,0,387,389,1,0,0,0,388,386,1,0,0,0,389,390,5,14,0,0,390,
        391,5,46,0,0,391,395,5,6,0,0,392,394,3,40,20,0,393,392,1,0,0,0,394,
        397,1,0,0,0,395,393,1,0,0,0,395,396,1,0,0,0,396,398,1,0,0,0,397,
        395,1,0,0,0,398,399,5,7,0,0,399,39,1,0,0,0,400,404,3,42,21,0,401,
        404,3,86,43,0,402,404,3,14,7,0,403,400,1,0,0,0,403,401,1,0,0,0,403,
        402,1,0,0,0,404,41,1,0,0,0,405,407,5,27,0,0,406,405,1,0,0,0,406,
        407,1,0,0,0,407,408,1,0,0,0,408,409,3,32,16,0,409,43,1,0,0,0,410,
        412,5,48,0,0,411,410,1,0,0,0,412,415,1,0,0,0,413,411,1,0,0,0,413,
        414,1,0,0,0,414,419,1,0,0,0,415,413,1,0,0,0,416,418,3,82,41,0,417,
        416,1,0,0,0,418,421,1,0,0,0,419,417,1,0,0,0,419,420,1,0,0,0,420,
        422,1,0,0,0,421,419,1,0,0,0,422,423,5,26,0,0,423,425,5,46,0,0,424,
        426,3,90,45,0,425,424,1,0,0,0,425,426,1,0,0,0,426,427,1,0,0,0,427,
        431,5,6,0,0,428,430,3,46,23,0,429,428,1,0,0,0,430,433,1,0,0,0,431,
        429,1,0,0,0,431,432,1,0,0,0,432,434,1,0,0,0,433,431,1,0,0,0,434,
        435,5,7,0,0,435,45,1,0,0,0,436,440,3,48,24,0,437,440,3,86,43,0,438,
        440,3,14,7,0,439,436,1,0,0,0,439,437,1,0,0,0,439,438,1,0,0,0,440,
        47,1,0,0,0,441,443,5,48,0,0,442,441,1,0,0,0,443,446,1,0,0,0,444,
        442,1,0,0,0,444,445,1,0,0,0,445,450,1,0,0,0,446,444,1,0,0,0,447,
        449,3,82,41,0,448,447,1,0,0,0,449,452,1,0,0,0,450,448,1,0,0,0,450,
        451,1,0,0,0,451,453,1,0,0,0,452,450,1,0,0,0,453,454,5,46,0,0,454,
        455,5,3,0,0,455,456,3,70,35,0,456,49,1,0,0,0,457,459,5,48,0,0,458,
        457,1,0,0,0,459,462,1,0,0,0,460,458,1,0,0,0,460,461,1,0,0,0,461,
        466,1,0,0,0,462,460,1,0,0,0,463,465,3,82,41,0,464,463,1,0,0,0,465,
        468,1,0,0,0,466,464,1,0,0,0,466,467,1,0,0,0,467,469,1,0,0,0,468,
        466,1,0,0,0,469,470,5,22,0,0,470,471,5,46,0,0,471,472,5,3,0,0,472,
        473,5,46,0,0,473,51,1,0,0,0,474,476,5,48,0,0,475,474,1,0,0,0,476,
        479,1,0,0,0,477,475,1,0,0,0,477,478,1,0,0,0,478,483,1,0,0,0,479,
        477,1,0,0,0,480,482,3,82,41,0,481,480,1,0,0,0,482,485,1,0,0,0,483,
        481,1,0,0,0,483,484,1,0,0,0,484,486,1,0,0,0,485,483,1,0,0,0,486,
        487,5,23,0,0,487,488,5,46,0,0,488,492,5,6,0,0,489,491,3,54,27,0,
        490,489,1,0,0,0,491,494,1,0,0,0,492,490,1,0,0,0,492,493,1,0,0,0,
        493,495,1,0,0,0,494,492,1,0,0,0,495,496,5,7,0,0,496,53,1,0,0,0,497,
        502,3,60,30,0,498,502,3,86,43,0,499,502,3,14,7,0,500,502,3,26,13,
        0,501,497,1,0,0,0,501,498,1,0,0,0,501,499,1,0,0,0,501,500,1,0,0,
        0,502,55,1,0,0,0,503,505,5,48,0,0,504,503,1,0,0,0,505,508,1,0,0,
        0,506,504,1,0,0,0,506,507,1,0,0,0,507,512,1,0,0,0,508,506,1,0,0,
        0,509,511,3,82,41,0,510,509,1,0,0,0,511,514,1,0,0,0,512,510,1,0,
        0,0,512,513,1,0,0,0,513,515,1,0,0,0,514,512,1,0,0,0,515,516,5,21,
        0,0,516,517,5,46,0,0,517,521,5,6,0,0,518,520,3,58,29,0,519,518,1,
        0,0,0,520,523,1,0,0,0,521,519,1,0,0,0,521,522,1,0,0,0,522,524,1,
        0,0,0,523,521,1,0,0,0,524,525,5,7,0,0,525,57,1,0,0,0,526,531,3,60,
        30,0,527,531,3,86,43,0,528,531,3,14,7,0,529,531,3,26,13,0,530,526,
        1,0,0,0,530,527,1,0,0,0,530,528,1,0,0,0,530,529,1,0,0,0,531,59,1,
        0,0,0,532,534,5,48,0,0,533,532,1,0,0,0,534,537,1,0,0,0,535,533,1,
        0,0,0,535,536,1,0,0,0,536,541,1,0,0,0,537,535,1,0,0,0,538,540,3,
        82,41,0,539,538,1,0,0,0,540,543,1,0,0,0,541,539,1,0,0,0,541,542,
        1,0,0,0,542,544,1,0,0,0,543,541,1,0,0,0,544,545,5,46,0,0,545,547,
        5,4,0,0,546,548,3,62,31,0,547,546,1,0,0,0,547,548,1,0,0,0,548,553,
        1,0,0,0,549,550,5,2,0,0,550,552,3,62,31,0,551,549,1,0,0,0,552,555,
        1,0,0,0,553,551,1,0,0,0,553,554,1,0,0,0,554,556,1,0,0,0,555,553,
        1,0,0,0,556,559,5,5,0,0,557,558,5,3,0,0,558,560,3,64,32,0,559,557,
        1,0,0,0,559,560,1,0,0,0,560,565,1,0,0,0,561,562,5,12,0,0,562,564,
        3,64,32,0,563,561,1,0,0,0,564,567,1,0,0,0,565,563,1,0,0,0,565,566,
        1,0,0,0,566,61,1,0,0,0,567,565,1,0,0,0,568,570,5,48,0,0,569,568,
        1,0,0,0,570,573,1,0,0,0,571,569,1,0,0,0,571,572,1,0,0,0,572,577,
        1,0,0,0,573,571,1,0,0,0,574,576,3,82,41,0,575,574,1,0,0,0,576,579,
        1,0,0,0,577,575,1,0,0,0,577,578,1,0,0,0,578,580,1,0,0,0,579,577,
        1,0,0,0,580,581,5,46,0,0,581,582,5,3,0,0,582,583,3,70,35,0,583,63,
        1,0,0,0,584,586,5,48,0,0,585,584,1,0,0,0,586,589,1,0,0,0,587,585,
        1,0,0,0,587,588,1,0,0,0,588,593,1,0,0,0,589,587,1,0,0,0,590,592,
        3,82,41,0,591,590,1,0,0,0,592,595,1,0,0,0,593,591,1,0,0,0,593,594,
        1,0,0,0,594,596,1,0,0,0,595,593,1,0,0,0,596,597,3,70,35,0,597,65,
        1,0,0,0,598,600,5,48,0,0,599,598,1,0,0,0,600,603,1,0,0,0,601,599,
        1,0,0,0,601,602,1,0,0,0,602,607,1,0,0,0,603,601,1,0,0,0,604,606,
        3,82,41,0,605,604,1,0,0,0,606,609,1,0,0,0,607,605,1,0,0,0,607,608,
        1,0,0,0,608,610,1,0,0,0,609,607,1,0,0,0,610,611,5,13,0,0,611,612,
        5,46,0,0,612,616,5,6,0,0,613,615,3,68,34,0,614,613,1,0,0,0,615,618,
        1,0,0,0,616,614,1,0,0,0,616,617,1,0,0,0,617,619,1,0,0,0,618,616,
        1,0,0,0,619,620,5,7,0,0,620,67,1,0,0,0,621,625,3,86,43,0,622,625,
        3,14,7,0,623,625,3,60,30,0,624,621,1,0,0,0,624,622,1,0,0,0,624,623,
        1,0,0,0,625,69,1,0,0,0,626,631,3,72,36,0,627,631,3,74,37,0,628,631,
        3,76,38,0,629,631,3,78,39,0,630,626,1,0,0,0,630,627,1,0,0,0,630,
        628,1,0,0,0,630,629,1,0,0,0,631,71,1,0,0,0,632,633,7,0,0,0,633,73,
        1,0,0,0,634,640,3,80,40,0,635,636,5,42,0,0,636,637,5,8,0,0,637,638,
        5,45,0,0,638,640,5,9,0,0,639,634,1,0,0,0,639,635,1,0,0,0,640,75,
        1,0,0,0,641,642,5,40,0,0,642,643,5,8,0,0,643,644,3,70,35,0,644,645,
        5,9,0,0,645,77,1,0,0,0,646,647,5,41,0,0,647,648,5,8,0,0,648,649,
        3,70,35,0,649,650,5,2,0,0,650,651,3,70,35,0,651,652,5,9,0,0,652,
        79,1,0,0,0,653,658,5,46,0,0,654,655,5,1,0,0,655,657,5,46,0,0,656,
        654,1,0,0,0,657,660,1,0,0,0,658,656,1,0,0,0,658,659,1,0,0,0,659,
        81,1,0,0,0,660,658,1,0,0,0,661,662,5,10,0,0,662,677,5,46,0,0,663,
        664,5,10,0,0,664,665,5,46,0,0,665,666,5,4,0,0,666,671,3,84,42,0,
        667,668,5,2,0,0,668,670,3,84,42,0,669,667,1,0,0,0,670,673,1,0,0,
        0,671,669,1,0,0,0,671,672,1,0,0,0,672,674,1,0,0,0,673,671,1,0,0,
        0,674,675,5,5,0,0,675,677,1,0,0,0,676,661,1,0,0,0,676,663,1,0,0,
        0,677,83,1,0,0,0,678,683,3,80,40,0,679,683,5,43,0,0,680,683,5,44,
        0,0,681,683,5,45,0,0,682,678,1,0,0,0,682,679,1,0,0,0,682,680,1,0,
        0,0,682,681,1,0,0,0,683,85,1,0,0,0,684,686,5,48,0,0,685,684,1,0,
        0,0,686,689,1,0,0,0,687,685,1,0,0,0,687,688,1,0,0,0,688,693,1,0,
        0,0,689,687,1,0,0,0,690,692,3,82,41,0,691,690,1,0,0,0,692,695,1,
        0,0,0,693,691,1,0,0,0,693,694,1,0,0,0,694,696,1,0,0,0,695,693,1,
        0,0,0,696,697,5,18,0,0,697,698,5,46,0,0,698,700,5,6,0,0,699,701,
        3,88,44,0,700,699,1,0,0,0,700,701,1,0,0,0,701,706,1,0,0,0,702,703,
        5,2,0,0,703,705,3,88,44,0,704,702,1,0,0,0,705,708,1,0,0,0,706,704,
        1,0,0,0,706,707,1,0,0,0,707,709,1,0,0,0,708,706,1,0,0,0,709,710,
        5,7,0,0,710,87,1,0,0,0,711,713,5,48,0,0,712,711,1,0,0,0,713,716,
        1,0,0,0,714,712,1,0,0,0,714,715,1,0,0,0,715,720,1,0,0,0,716,714,
        1,0,0,0,717,719,3,82,41,0,718,717,1,0,0,0,719,722,1,0,0,0,720,718,
        1,0,0,0,720,721,1,0,0,0,721,723,1,0,0,0,722,720,1,0,0,0,723,724,
        5,46,0,0,724,89,1,0,0,0,725,726,5,28,0,0,726,731,3,80,40,0,727,728,
        5,2,0,0,728,730,3,80,40,0,729,727,1,0,0,0,730,733,1,0,0,0,731,729,
        1,0,0,0,731,732,1,0,0,0,732,91,1,0,0,0,733,731,1,0,0,0,89,95,101,
        109,118,124,130,139,147,158,164,173,187,192,198,204,210,218,223,
        229,239,245,251,257,265,270,276,286,292,298,304,312,317,323,333,
        339,345,351,359,364,370,380,386,395,403,406,413,419,425,431,439,
        444,450,460,466,477,483,492,501,506,512,521,530,535,541,547,553,
        559,565,571,577,587,593,601,607,616,624,630,639,658,671,676,682,
        687,693,700,706,714,720,731
    ]

class d3iGrammar ( Parser ):

    grammarFileName = "d3iGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "','", "':'", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "'@'", "'=>'", "'|'", "'acl'", 
                     "'aggregate'", "'context'", "'domain'", "'entity'", 
                     "'enum'", "'event'", "'import'", "'interface'", "'repository'", 
                     "'service'", "'trait'", "'valueobject'", "'view'", 
                     "'root'", "'inherits'", "'integer'", "'number'", "'float'", 
                     "'date'", "'time'", "'dateTime'", "'string'", "'boolean'", 
                     "'bytes'", "'stream'", "'any'", "'list'", "'map'", 
                     "'external'" ]

    symbolicNames = [ "<INVALID>", "DOT", "COMMA", "SEMI", "LPAREN", "RPAREN", 
                      "LCURLY", "RCURLY", "LBARCKET", "RBRACKET", "AT", 
                      "ARROW", "PIPE", "ACL", "AGGREGATE", "CONTEXT", "DOMAIN", 
                      "ENTITY", "ENUM", "EVENT", "IMPORT", "INTERFACE", 
                      "REPOSITORY", "SERVICE", "TRAIT", "VALUEOBJECT", "VIEW", 
                      "ROOT", "INHERITS", "INTEGER", "NUMBER", "FLOAT", 
                      "DATE", "TIME", "DATETIME", "STRING", "BOOLEAN", "BYTES", 
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
    RULE_trait = 10
    RULE_trait_element = 11
    RULE_trait_object_member = 12
    RULE_event = 13
    RULE_event_element = 14
    RULE_event_member = 15
    RULE_entity = 16
    RULE_entity_element = 17
    RULE_entity_member = 18
    RULE_aggregate = 19
    RULE_aggregate_element = 20
    RULE_aggregate_entity = 21
    RULE_view = 22
    RULE_view_element = 23
    RULE_view_member = 24
    RULE_repository = 25
    RULE_service = 26
    RULE_service_element = 27
    RULE_interface = 28
    RULE_interface_element = 29
    RULE_operation = 30
    RULE_operation_param = 31
    RULE_operation_return = 32
    RULE_acl = 33
    RULE_acl_element = 34
    RULE_type = 35
    RULE_primitive_type = 36
    RULE_reference_type = 37
    RULE_list_type = 38
    RULE_map_type = 39
    RULE_qualifiedName = 40
    RULE_decorator = 41
    RULE_decorator_param = 42
    RULE_enum = 43
    RULE_enum_element = 44
    RULE_inherits = 45

    ruleNames =  [ "d3", "import_rule", "domain", "directive", "domain_element", 
                   "context", "context_element", "value_object", "value_object_element", 
                   "value_object_member", "trait", "trait_element", "trait_object_member", 
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
    DOMAIN=16
    ENTITY=17
    ENUM=18
    EVENT=19
    IMPORT=20
    INTERFACE=21
    REPOSITORY=22
    SERVICE=23
    TRAIT=24
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
            self.state = 95
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 92
                    self.import_rule() 
                self.state = 97
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 351843720954880) != 0):
                self.state = 98
                self.domain()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
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
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 106
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 112
            self.match(d3iGrammar.IMPORT)
            self.state = 113
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
            self.state = 118
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 115
                    self.directive() 
                self.state = 120
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 121
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 127
                self.decorator()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 133
            self.match(d3iGrammar.DOMAIN)
            self.state = 134
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 135
            self.match(d3iGrammar.LCURLY)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 281474976744448) != 0):
                self.state = 136
                self.domain_element()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
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
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 144
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 150
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 151
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
            self.state = 153
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
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 155
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.match(d3iGrammar.CONTEXT)
            self.state = 168
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 169
            self.match(d3iGrammar.LCURLY)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 281475109118976) != 0):
                self.state = 170
                self.context_element()
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 176
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


        def trait(self):
            return self.getTypedRuleContext(d3iGrammar.TraitContext,0)


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
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.enum()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.value_object()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 180
                self.trait()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 181
                self.aggregate()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 182
                self.view()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 183
                self.repository()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 184
                self.acl()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 185
                self.service()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 186
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
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 189
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 195
                self.decorator()
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 201
            self.match(d3iGrammar.VALUEOBJECT)
            self.state = 202
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 203
                self.inherits()


            self.state = 206
            self.match(d3iGrammar.LCURLY)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 351843754705920) != 0):
                self.state = 207
                self.value_object_element()
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 213
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
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.value_object_member()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 217
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
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 220
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 233
            self.match(d3iGrammar.SEMI)
            self.state = 234
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TraitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRAIT(self):
            return self.getToken(d3iGrammar.TRAIT, 0)

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


        def trait_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(d3iGrammar.Trait_elementContext)
            else:
                return self.getTypedRuleContext(d3iGrammar.Trait_elementContext,i)


        def getRuleIndex(self):
            return d3iGrammar.RULE_trait

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrait" ):
                listener.enterTrait(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrait" ):
                listener.exitTrait(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrait" ):
                return visitor.visitTrait(self)
            else:
                return visitor.visitChildren(self)




    def trait(self):

        localctx = d3iGrammar.TraitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_trait)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 236
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 242
                self.decorator()
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 248
            self.match(d3iGrammar.TRAIT)
            self.state = 249
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 250
                self.inherits()


            self.state = 253
            self.match(d3iGrammar.LCURLY)
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 351843754705920) != 0):
                self.state = 254
                self.trait_element()
                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 260
            self.match(d3iGrammar.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Trait_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def trait_object_member(self):
            return self.getTypedRuleContext(d3iGrammar.Trait_object_memberContext,0)


        def enum(self):
            return self.getTypedRuleContext(d3iGrammar.EnumContext,0)


        def value_object(self):
            return self.getTypedRuleContext(d3iGrammar.Value_objectContext,0)


        def getRuleIndex(self):
            return d3iGrammar.RULE_trait_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrait_element" ):
                listener.enterTrait_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrait_element" ):
                listener.exitTrait_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrait_element" ):
                return visitor.visitTrait_element(self)
            else:
                return visitor.visitChildren(self)




    def trait_element(self):

        localctx = d3iGrammar.Trait_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_trait_element)
        try:
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.trait_object_member()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 264
                self.value_object()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Trait_object_memberContext(ParserRuleContext):
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
            return d3iGrammar.RULE_trait_object_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrait_object_member" ):
                listener.enterTrait_object_member(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrait_object_member" ):
                listener.exitTrait_object_member(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrait_object_member" ):
                return visitor.visitTrait_object_member(self)
            else:
                return visitor.visitChildren(self)




    def trait_object_member(self):

        localctx = d3iGrammar.Trait_object_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_trait_object_member)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 267
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 280
            self.match(d3iGrammar.SEMI)
            self.state = 281
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
        self.enterRule(localctx, 26, self.RULE_event)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 283
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 289
                self.decorator()
                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 295
            self.match(d3iGrammar.EVENT)
            self.state = 296
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 297
                self.inherits()


            self.state = 300
            self.match(d3iGrammar.LCURLY)
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 351843754705920) != 0):
                self.state = 301
                self.event_element()
                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 307
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
        self.enterRule(localctx, 28, self.RULE_event_element)
        try:
            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.event_member()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 311
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
        self.enterRule(localctx, 30, self.RULE_event_member)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 314
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 319
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 323
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 320
                self.decorator()
                self.state = 325
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 326
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 327
            self.match(d3iGrammar.SEMI)
            self.state = 328
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
        self.enterRule(localctx, 32, self.RULE_entity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 330
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 336
                self.decorator()
                self.state = 341
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 342
            self.match(d3iGrammar.ENTITY)
            self.state = 343
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 344
                self.inherits()


            self.state = 347
            self.match(d3iGrammar.LCURLY)
            self.state = 351
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 351843754705920) != 0):
                self.state = 348
                self.entity_element()
                self.state = 353
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 354
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
        self.enterRule(localctx, 34, self.RULE_entity_element)
        try:
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.entity_member()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 358
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
        self.enterRule(localctx, 36, self.RULE_entity_member)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 361
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 366
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 374
            self.match(d3iGrammar.SEMI)
            self.state = 375
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
        self.enterRule(localctx, 38, self.RULE_aggregate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 377
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 382
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 383
                self.decorator()
                self.state = 388
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 389
            self.match(d3iGrammar.AGGREGATE)
            self.state = 390
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 391
            self.match(d3iGrammar.LCURLY)
            self.state = 395
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 281475144877056) != 0):
                self.state = 392
                self.aggregate_element()
                self.state = 397
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 398
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
        self.enterRule(localctx, 40, self.RULE_aggregate_element)
        try:
            self.state = 403
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.aggregate_entity()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 401
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 402
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
        self.enterRule(localctx, 42, self.RULE_aggregate_entity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 405
                self.match(d3iGrammar.ROOT)


            self.state = 408
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
        self.enterRule(localctx, 44, self.RULE_view)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
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
            self.match(d3iGrammar.VIEW)
            self.state = 423
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 425
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 424
                self.inherits()


            self.state = 427
            self.match(d3iGrammar.LCURLY)
            self.state = 431
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 351843754705920) != 0):
                self.state = 428
                self.view_element()
                self.state = 433
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 434
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
        self.enterRule(localctx, 46, self.RULE_view_element)
        try:
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.view_member()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 438
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
        self.enterRule(localctx, 48, self.RULE_view_member)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 441
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 446
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 450
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 447
                self.decorator()
                self.state = 452
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 453
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 454
            self.match(d3iGrammar.SEMI)
            self.state = 455
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
        self.enterRule(localctx, 50, self.RULE_repository)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 457
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 462
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.match(d3iGrammar.REPOSITORY)
            self.state = 470
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 471
            self.match(d3iGrammar.SEMI)
            self.state = 472
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
        self.enterRule(localctx, 52, self.RULE_service)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 474
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 479
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 483
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 480
                self.decorator()
                self.state = 485
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 486
            self.match(d3iGrammar.SERVICE)
            self.state = 487
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 488
            self.match(d3iGrammar.LCURLY)
            self.state = 492
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 351843755230208) != 0):
                self.state = 489
                self.service_element()
                self.state = 494
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 495
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
        self.enterRule(localctx, 54, self.RULE_service_element)
        try:
            self.state = 501
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 497
                self.operation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 498
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 499
                self.value_object()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 500
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
        self.enterRule(localctx, 56, self.RULE_interface)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 503
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 508
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 512
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 509
                self.decorator()
                self.state = 514
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 515
            self.match(d3iGrammar.INTERFACE)
            self.state = 516
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 517
            self.match(d3iGrammar.LCURLY)
            self.state = 521
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 351843755230208) != 0):
                self.state = 518
                self.interface_element()
                self.state = 523
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 524
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
        self.enterRule(localctx, 58, self.RULE_interface_element)
        try:
            self.state = 530
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 526
                self.operation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 527
                self.enum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 528
                self.value_object()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 529
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
        self.enterRule(localctx, 60, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 535
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 532
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 537
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 541
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 538
                self.decorator()
                self.state = 543
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 544
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 545
            self.match(d3iGrammar.LPAREN)

            self.state = 547
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 351843720889344) != 0):
                self.state = 546
                self.operation_param()


            self.state = 553
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 549
                self.match(d3iGrammar.COMMA)
                self.state = 550
                self.operation_param()
                self.state = 555
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 556
            self.match(d3iGrammar.RPAREN)

            self.state = 559
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 557
                self.match(d3iGrammar.SEMI)
                self.state = 558
                self.operation_return()


            self.state = 565
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 561
                self.match(d3iGrammar.PIPE)
                self.state = 562
                self.operation_return()
                self.state = 567
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
        self.enterRule(localctx, 62, self.RULE_operation_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 571
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 568
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 573
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 577
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 574
                self.decorator()
                self.state = 579
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 580
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 581
            self.match(d3iGrammar.SEMI)
            self.state = 582
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
        self.enterRule(localctx, 64, self.RULE_operation_return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 587
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 584
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 589
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 593
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 590
                self.decorator()
                self.state = 595
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 596
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
        self.enterRule(localctx, 66, self.RULE_acl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 601
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 598
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 603
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 607
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 604
                self.decorator()
                self.state = 609
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 610
            self.match(d3iGrammar.ACL)
            self.state = 611
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 612
            self.match(d3iGrammar.LCURLY)
            self.state = 616
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 351843754705920) != 0):
                self.state = 613
                self.acl_element()
                self.state = 618
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 619
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
        self.enterRule(localctx, 68, self.RULE_acl_element)
        try:
            self.state = 624
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 621
                self.enum()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 622
                self.value_object()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 623
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
        self.enterRule(localctx, 70, self.RULE_type)
        try:
            self.state = 630
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 626
                self.primitive_type()
                pass
            elif token in [42, 46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 627
                self.reference_type()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 3)
                self.state = 628
                self.list_type()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 4)
                self.state = 629
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
        self.enterRule(localctx, 72, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 632
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
        self.enterRule(localctx, 74, self.RULE_reference_type)
        try:
            self.state = 639
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 634
                self.qualifiedName()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 635
                self.match(d3iGrammar.EXTERNAL)
                self.state = 636
                self.match(d3iGrammar.LBARCKET)
                self.state = 637
                self.match(d3iGrammar.STRING_LITERAL)
                self.state = 638
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
        self.enterRule(localctx, 76, self.RULE_list_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 641
            self.match(d3iGrammar.LIST)
            self.state = 642
            self.match(d3iGrammar.LBARCKET)
            self.state = 643
            self.type_()
            self.state = 644
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
        self.enterRule(localctx, 78, self.RULE_map_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 646
            self.match(d3iGrammar.MAP)
            self.state = 647
            self.match(d3iGrammar.LBARCKET)
            self.state = 648
            self.type_()
            self.state = 649
            self.match(d3iGrammar.COMMA)
            self.state = 650
            self.type_()
            self.state = 651
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
        self.enterRule(localctx, 80, self.RULE_qualifiedName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 653
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 658
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 654
                self.match(d3iGrammar.DOT)
                self.state = 655
                self.match(d3iGrammar.IDENTIFIER)
                self.state = 660
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
        self.enterRule(localctx, 82, self.RULE_decorator)
        self._la = 0 # Token type
        try:
            self.state = 676
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 661
                self.match(d3iGrammar.AT)
                self.state = 662
                self.match(d3iGrammar.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 663
                self.match(d3iGrammar.AT)
                self.state = 664
                self.match(d3iGrammar.IDENTIFIER)
                self.state = 665
                self.match(d3iGrammar.LPAREN)
                self.state = 666
                self.decorator_param()
                self.state = 671
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 667
                    self.match(d3iGrammar.COMMA)
                    self.state = 668
                    self.decorator_param()
                    self.state = 673
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 674
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
        self.enterRule(localctx, 84, self.RULE_decorator_param)
        try:
            self.state = 682
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 678
                self.qualifiedName()
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 679
                self.match(d3iGrammar.INTEGER_CONSTANS)
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 3)
                self.state = 680
                self.match(d3iGrammar.NUMBER_CONSTANS)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 4)
                self.state = 681
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
        self.enterRule(localctx, 86, self.RULE_enum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 687
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 684
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 689
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 693
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 690
                self.decorator()
                self.state = 695
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 696
            self.match(d3iGrammar.ENUM)
            self.state = 697
            self.match(d3iGrammar.IDENTIFIER)
            self.state = 698
            self.match(d3iGrammar.LCURLY)
            self.state = 700
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 351843720889344) != 0):
                self.state = 699
                self.enum_element()


            self.state = 706
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 702
                self.match(d3iGrammar.COMMA)
                self.state = 703
                self.enum_element()
                self.state = 708
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 709
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
        self.enterRule(localctx, 88, self.RULE_enum_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 714
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 711
                self.match(d3iGrammar.DOCUMENT_LINE)
                self.state = 716
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 720
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 717
                self.decorator()
                self.state = 722
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 723
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
        self.enterRule(localctx, 90, self.RULE_inherits)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 725
            self.match(d3iGrammar.INHERITS)
            self.state = 726
            self.qualifiedName()
            self.state = 731
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 727
                self.match(d3iGrammar.COMMA)
                self.state = 728
                self.qualifiedName()
                self.state = 733
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





