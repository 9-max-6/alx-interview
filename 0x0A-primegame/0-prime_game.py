#!/usr/bin/python3
def sieve_of_eratosthenes(n):
    """Returns a list of prime numbers up to n using the Sieve of Eratosthenes."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime

def count_prime_moves(n, is_prime):
    """Counts the number of valid moves in the game for a given n."""
    primes_removed = [False] * (n + 1)
    moves = 0
    for i in range(2, n + 1):
        if is_prime[i] and not primes_removed[i]:
            moves += 1
            for j in range(i, n + 1, i):
                primes_removed[j] = True
    return moves

def isWinner(x, nums):
    """
    Determines the winner of the Prime Game after x rounds.
    
    Parameters:
    x (int): Number of rounds
    nums (list): List containing n for each round
    
    Returns:
    str: Name of the player who won the most rounds, or None if a tie
    """
    if x < 1 or not nums:
        return None
    
    max_num = max(nums)
    
    # Use Sieve of Eratosthenes to find primes up to max_num
    is_prime = sieve_of_eratosthenes(max_num)
    
    maria_wins = 0
    ben_wins = 0
    
    # Play each round
    for n in nums:
        moves = count_prime_moves(n, is_prime)
        
        # Maria wins if the number of moves is odd, Ben wins if it's even
        if moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
