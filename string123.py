message = input("Enter a message: ")

print("First character:", message[0])
print("Last chracter:", message[-1])
print("Middle character:", message[int(len(message) / 2)])
print("Even idex character:", message[0::2])
print("Odd index charater:", message[1::2])
print("Reversed message:", message[::-1])