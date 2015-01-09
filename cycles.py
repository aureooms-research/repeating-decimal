
def nonrepeatingpart ( d , bfactor ) :

	"""
		Computes the length of the non repeating part in 1 / d decimals in
		base b. Returns tuple ( n , hascycle ) where n is the length of the
		non repeating part and hascycle determines if 1 / d cycles or not.
	"""

	n = 0

	for f in bfactor :

		m = 0

		while d % f == 0 :

			m += 1
			d //= f

		if m > n : n = m

	return n , d > 1


def cycle ( n , d , b ) :

	"""
		Computes the length of the cycle of 1 divided by d in base b
		with non repeating part of size n.
	"""

	a = 1

	for i in range( n ) :

		a *= b
		a %= d

	x = a

	a *= b
	a %= d

	l = 1

	while a != x :

		a *= b
		a %= d
		l += 1

	return l


