class Solution:
    def compress(self, chars):
        write = 0  # Write index
        read = 0   # Read index
        
        while read < len(chars):
            char = chars[read]
            count = 0
            
            # Count occurrences of the current character
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            # Write the character
            chars[write] = char
            write += 1
            
            # Write the count if more than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write
chars = ["a","a","b","b","c","c","c"]
sol = Solution()
length = sol.compress(chars)

print(length)          # Output: 6
print(chars[:length])  # Output: ['a', '2', 'b', '2', 'c', '3']
