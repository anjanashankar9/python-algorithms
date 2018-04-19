"""
Implementing binary search in the array.
Binary search works in a sorted array.

It works on the divide and conquer approach.
Every iteration the search space is halved.

Binary search compares the middle element of the array to the search element.
If it matches, function returns this index.
If it doesn't it is checked whether the element to be searched is smaller or
larger than the middle element.

If the element is smaller, the search space is the first half of the array.
If the element is larger, the search space is the second half of the array.

The process is continued with smaller search spaces.

returns index if there is a match.
returns None otherwise.
"""


def search(arr, key):
  """
  Linear search an element in the given array
  :param arr: List of elements
  :param key: Key to be searched
  :return: True if found, False otherwise
  """
  low = 0
  high = len(arr) - 1
  while(low <= high):
    mid = (low + high) / 2
    if key == arr[mid]:
      return mid
    elif key < arr[mid]:
      high = mid-1
    elif key > arr[mid]:
      low = mid+1
  return None


if __name__ == "__main__":
  arr = [1,2,3,4,5,6,7,8,9,10,11,12,13]

  print(search(arr, 0))
  print(search(arr, 1))
  print(search(arr, 4))
  print(search(arr, key=12))
  print(search(arr, 15))