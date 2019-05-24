def series_sum(n):
  result = 0
  if n == 0:
    return '0.00'
  else:
      for i in range(0,n):
          result = result+1/(1+3*i)
  return "{:.2f}".format(result)
    
