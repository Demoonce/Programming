def triangle_area(b: float | int, h: float | int):
    print(b * h / 2)


def sort_three(a: float, b: float, c: float):
    arr = [a, b, c]
    print(min(arr))
    arr.remove(min(arr))
    m = max(arr)
    arr.remove(max(arr))
    print(arr[0])
    print(m)

def is_odd(a: int) -> bool:
	if a % 2 == 0:
		return True
	return False

def letter(a: str):
	if not a.isalpha():
		print("Not a letter")
		return
	vowels = ("a", "e", "i", "o", "u")
	a = a.lower()
	if a in vowels:
		print("Vowel")
	elif a == "y":
		print("Vowel or consonant")
	else:
		print("Consonant")

def eu(year: int):
	#no
	pass

def average(nums: list[int]):
	print(sum(nums)/len(nums))

def palindrome(s: str) -> bool:
	if reversed(s) == s:
		return True
	return False

def bin_to_dec(num: int):
	print("BIN:", bin(num))