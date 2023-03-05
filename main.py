def solution(n):
  if "str_primario" not in dir(solution):
    inteiro_maximo = 10_000
    set_numerico = [True] * inteiro_maximo

    set_numerico[0] = set_numerico[1] = False

    sieve_final = inteiro_maximo**0.5

    for numero, eh_primario in enumerate(set_numerico):
      if numero <= sieve_final:
        if eh_primario:
          for multiplo in range(numero**2, inteiro_maximo, numero):
            set_numerico[multiplo] = False
      else:
        break

    str_primario = "".join([str(x) for x, y in enumerate(set_numerico) if y])
    solution.prime_str = str_primario

  return solution.prime_str[n:n + 5]


print(solution(3))
'''import time

start = time.time()
for n in range(10000):
  print(solution(n))
print(f'{(time.time() - start)} seconds')'''
