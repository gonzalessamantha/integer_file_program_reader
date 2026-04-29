class NumberProcessor:

    def __init__(self, input_file="numbers.txt"):
        self.input_file = input_file
        self.even_file = "even.txt"
        self.odd_file = "odd.txt"
        self.numbers = []

    def read_numbers(self):
        try:
            with open(self.input_file, 'r') as file:
                lines = file.readlines()
                self.numbers = []

                for i, line in enumerate(lines):
                    if i >= 20:  # Stop after reading 20 numbers
                        break
                    try:
                        num = int(line.strip())
                        self.numbers.append(num)
                    except ValueError:
                        print(f"Warning: Invalid number on line {i + 1}: '{line.strip()}' - skipping")
                        continue

                if len(self.numbers) != 20:
                    raise ValueError(f"Expected exactly 20 numbers, found {len(self.numbers)}")

            print(f"Successfully read {len(self.numbers)} numbers from {self.input_file}")

        except FileNotFoundError:
            raise FileNotFoundError(
                f"Input file '{self.input_file}' not found. Please create it with 20 integers, one per line.")

    def classify_numbers(self):
        even_numbers = []
        odd_numbers = []

        for num in self.numbers:
            if num % 2 == 0:
                even_numbers.append(num)
            else:
                odd_numbers.append(num)

        print(f"Even numbers: {len(even_numbers)}")
        print(f"Odd numbers: {len(odd_numbers)}")

        return even_numbers, odd_numbers

    def write_even_numbers(self, even_numbers):
        with open(self.even_file, 'w') as file:
            for num in even_numbers:
                file.write(f"{num}\n")
        print(f"Even numbers written to {self.even_file}")

    def write_odd_numbers(self, odd_numbers):
        with open(self.odd_file, 'w') as file:
            for num in odd_numbers:
                file.write(f"{num}\n")
        print(f"Odd numbers written to {self.odd_file}")

    def process(self):
        print("Starting number processing...")
        print("-" * 40)

        # Step 1: Read numbers
        self.read_numbers()

        # Step 2: Classify numbers
        even_numbers, odd_numbers = self.classify_numbers()

        # Step 3: Write to files
        self.write_even_numbers(even_numbers)
        self.write_odd_numbers(odd_numbers)

        print("-" * 40)
        print("Processing completed successfully!")


def create_sample_file():
    import random

    with open("numbers.txt", 'w') as file:
        for _ in range(20):
            num = random.randint(-100, 100)  # Random numbers between -100 and 100
            file.write(f"{num}\n")

    print("Sample numbers.txt file created with 20 random integers.")


def main():
    try:
        # Uncomment the line below to create a sample file for testing
        # create_sample_file()

        # Create processor instance and run
        processor = NumberProcessor("numbers.txt")
        processor.process()

    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Run create_sample_file() first or create numbers.txt manually.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()