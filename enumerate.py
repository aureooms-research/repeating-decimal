# run with python3

from primes import phi , ufactor

from cycles import cycle , nonrepeatingpart


def main ( b = 10 ) :
	"""
		For all d > 0, if 1/d
			has either a cycle length of 0
			or a cycle length that divides phi( d )

		b is the base, works with any base that can represent rationals
		i.e. any base greater or equal to 2
	"""

	d = 1

	# compute the unique prime factors of base b
	bfactor = ufactor( b )

	# forever
	while True :

		# skip the numbers made only of prime factors of b
		# they are the only numbers that can have no cycle

		n , hascycle = nonrepeatingpart( d , bfactor )

		if hascycle :

			# compute phi( d ) and cycle( n , d , b )
			p , c = phi( d ) , cycle( n , d , b )

			# check if condition holds
			v = p % c == 0

			# output the result
			print( d , p , c , v )

			# if condition does not hold -> break
			if not v : break

		# next number
		d += 1



if __name__ == '__main__' :

	import sys
	main( *map( int , sys.argv[1:] ) )

