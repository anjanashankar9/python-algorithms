"""
Implementing linear search for elements in the array.
Linear search goes through the given array one element at a time,
returns True if there is a match.
returns False otherwise.

Complexity: O(n)
"""

def search(arr, key):
  """
  Linear search an element in the given array
  :param arr: List of elements
  :param key: Key to be searched
  :return: True if found, False otherwise
  """
  for a in arr:
    if key == a:
      return True
  return False


if __name__ == "__main__":
  arr = [1,2,3,4,5,6,7,8,9,10,11,12]
  print(search(arr, 0))
  print(search(arr, 4))
  print(search(arr, key=12))
  print(search(arr, 15))