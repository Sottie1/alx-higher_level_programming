 of unsorted integers"""


 def find_peak(list_of_i#!/usr/bin/python3
"""Finds a peak in a listntegers):
    """Finds a peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    lo = 0
    hi = len(list_of_integers)
    mid = ((hi - lo) // 2return list_of_integers[0]
    if hi == 2:
       ) + lo
    mid = int(mid)
    if hi == 1:
         return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    ifers[mid + 1]:
        return find_peak(list_of_int mid > 0 and list_of_integers[mid] < list_of_integegers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
