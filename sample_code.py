def digital_root(num):
  if num < 0:
    return -1
  while num >= 10:
    num = sum(int(d) for d in str(num))
  return num

if __name__ == "__main__":
  print("Application Started")
  x = digital_root(6832)
  print(f"The digital root of 6832 is: {x}")
