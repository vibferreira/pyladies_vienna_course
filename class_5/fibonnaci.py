# Fibonnaci Sequence --> transform into a function

user_seq = int(input("Input the size of the Fibonnaci sequence: "))

def fibonacci (seq_size):
	""" Calculates the fibonacci sequence within a given sequenece size
	user\n
	seq_size: size of the sequence"""

	fibo_num = 1
	fibo_seq = 0
	print(f"The fibonacci sequence is: \n{fibo_seq}")

	for i in range(seq_size):
		fibo_seq += fibo_num
		print(fibo_seq)
		fibo_num = (fibo_seq - fibo_num)

fibonacci(user_seq)
