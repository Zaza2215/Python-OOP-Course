class User:
	name = "Test"
	age = 17


if __name__ == "__main__":
	# task 1
	class User1:
		version = 100

	print(getattr(User1, 'version'))

	# task 2
	class User2:
		pass

	setattr(User2, 'version', 100)
	print(getattr(User2, 'version'))

	# task 3
	class User3:
		version = 100

	print(dir(User3))
	delattr(User3, 'version')
	print(dir(User3))
	