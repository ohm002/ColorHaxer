from modules import Class, Hax, ParseMap, colorhaxdecoder
import sys
import re
import os

colorhaxdecoder.ParseHax(open(sys.argv[1]).read().splitlines())
# i = input("press enter to exit")