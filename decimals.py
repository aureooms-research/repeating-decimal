# run with python3

def main ( n , d , b = 10 ) :

	"""
		Details the steps of computing the first n 'decimals' of 1/d in base b.
	"""

	a = 1

	for i in range ( n ) :

		print( "%i -> %i * %i = %i" % ( i , a , b , a * b ) )
		a *= b
		print( "%i -> %i / %i = %i <--" % ( i , a , d , a // d ) )
		print( "%i -> %i %% %i = %i" % ( i , a , d , a % d ) )
		a %= d



if __name__ == '__main__' :

	import sys
	main( *map( int , sys.argv[1:] ) )

