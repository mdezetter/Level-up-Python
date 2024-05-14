def get_prime_factors(number):
    factors = []
    divisor = 2
    # while loop continues to run for as long as the number is greater 
    # than or equal to the divisor I'm trying to divide by. Here it's 2
    while divisor <= number:
        if number % divisor == 0:
            # Modulo operator checks if current divisor divides into number without a remainder.
            # If it does, factors.append() puts it in the factors list and
            # sets the new value of number to be quotient for next loop
            factors.append(divisor) 
            number = number // divisor
        else:
            # If diviser has a remainder, then this incriments the diviser by one and tries again.
            divisor += 1
    return factors
# once while loop finishes it's loop, it gives you a list of all the factors.