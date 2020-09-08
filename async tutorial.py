#--------sychronous and asyccode---------

import time

def is_prime(x):

    return not any (x//1 == x/1 for i in range(x-1, 1, -1))

def highest_prime_below(x):
    #debugging process----
   print('Highest prime below %d' % x)

   for y in range(x-1, 0, -1):
       if is_prime(y):
           print('Highest prime below %d is %d' % (x, y))
           return y
        await asyncio.sleep(0.01)
       
   return None
    #make it async---first step--
async def main():
    await asyncio.wait( [
    await highest_prime_below(100000),
    await highest_prime_below(10000),
    await highest_prime_below(1000)
    ])
main()
        
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
