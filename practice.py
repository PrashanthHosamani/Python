def factors(n):
  factors = []
  for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
      factors.append(i)
      if i != n // i:
        factors.append(n // i)
  return factors

def is_perfect_number(n):
  factors = factors(n)
  sum_of_factors = sum(factors)
  return sum_of_factors == n

def main():
  n = int(input("Enter a number: "))
  factors = factors(n)
  if is_perfect_number(n):
    print(f"n: {n}. factors: {factors}. perfect number")
  else:
    print(f"n: {n}. factors: {factors}. not a perfect number")

