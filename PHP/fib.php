<?php

function fib($n)
{

  if($n<2)
    return 1;
  else
    return fib($n-2) + fib($n-1);
}
  
/* Function call to print Fibonacci series upto 6 numbers. */
 
echo fib(10);

?>