"""

An integer that is not co-prime to 10 but has a prime factor other than 2 or 5
has a reciprocal that is eventually periodic, but with a non-repeating sequence
of digits that precede the repeating part. The reciprocal can be expressed as:

    \frac{1}{2^a 5^b p^k q^\ell \cdots}\, ,

where a and b are not both zero.

This fraction can also be expressed as:

    \frac{5^{a-b}}{10^a p^k q^\ell \cdots}\, ,

if a > b, or as

    \frac{2^{b-a}}{10^b p^k q^\ell \cdots}\, ,

if b > a, or as

    \frac{1}{10^a p^k q^\ell \cdots}\, ,

if a = b.

The decimal has:

	An initial transient of max(a, b) digits after the decimal point. Some or
	all of the digits in the transient can be zeros.
	A subsequent repetend which is the same as that for the fraction
	\frac{1}{p^k q^\ell \cdots}.

For example 1/28 = 0.03571428571428…:

    the initial non-repeating digits are 03; and
    the subsequent repeating digits are 571428.

"""



def transient ( d , bfactor ) :

	"""
		Computes the length of the non repeating part in 1 / d decimals in
		base b. Returns tuple ( n , hasrepetend ) where n is the length of the
		non repeating part and hasrepetend determines if 1 / d repeats or not.
	"""

	n = 0

	for f in bfactor :

		m = 0

		while d % f == 0 :

			m += 1
			d //= f

		if m > n : n = m

	return n , d > 1


def repetend ( n , d , b ) :

	"""
		Computes the length of the repetend of 1 divided by d in base b
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


