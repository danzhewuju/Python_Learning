#!usr/bin/python
import PICaculate

yh = "00123234.190000"
ch = "3456"
# yh = yh[:yh.index(".")]+yh[yh.index(".")+1:]
print(PICaculate.format_number(yh))
