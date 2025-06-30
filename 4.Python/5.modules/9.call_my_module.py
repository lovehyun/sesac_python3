# import mymodule
import mymodule as mm
# from mymodule import greet, goodbye, default_name

from mymodule import greet as gt

greeting = mm.greet("shpark")
print(greeting)

print(mm.goodbye())

print(mm.default_name)

print(gt("sesac"))
