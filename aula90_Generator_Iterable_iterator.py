import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(lista)) # 8448728 Bites
print(sys.getsizeof(generator)) # 192 Bites

print(generator)
print()
#for n in generator:
#     print(n)

