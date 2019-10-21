def string_counter(x, y="a"):
  print(x.count(y))

string_counter("hello world", "o")
# 2
string_counter("hello world", "l")
# 3
string_counter("aaaaa")
# 5