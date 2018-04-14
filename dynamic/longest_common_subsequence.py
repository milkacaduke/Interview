

def longest_common_subsequence(seq1, seq2):
	"""
		ex: abcdaf
				acbcf

		ans: abcf


			_ s e q 2
		_ 0 0 0 0 0
		s 0
		e 0
		q 0
		1 0

	"""
	m = len(seq1) + 1 # +1 for the table setup |
	n = len(seq2) + 1 # +1 for the table setup <->

	# create our matrix
	matrix = [[0 for _ in range(n)] for _ in range(m)]
	max_length = 0
	
	for i in range(1, m):
		for j in range(1, n):

			if seq1[i-1] == seq2[j-1]: #offset cuz we buffed 1 element in m and n
				matrix[i][j] = 1 + matrix[i-1][j-1]
			else:
				matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
			
			max_length = max(max_length, matrix[i][j])

	return max_length


# main stuff
if __name__ == '__main__':
	seq1 = "ABCDGHLQR"
	seq2 = "AEDPHR"
	expected_ans = 4

	assert expected_ans == longest_common_subsequence(seq1, seq2)



longest_common_subsequence(["a","b","c"], ["d","e"])





