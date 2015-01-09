import functools

@functools.lru_cache( None )
def ufactor ( n , d = 2 ) :
	"""
		n prime factors lister, one unique copy per factor
	"""

	while n > 1:

		if n % d == 0:
			n //= d
			while n % d == 0 : n //= d
			return [d] + ufactor( n , d + 1 )

		else : d += 1

	return []


@functools.lru_cache( None )
def phi ( n ) :
	"""
		Computes the euler phi function of n
		http://en.wikipedia.org/wiki/Euler's_totient_function
	"""

	for p in ufactor( n ) : n -= n // p
	return n
