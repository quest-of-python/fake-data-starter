import random
from typing import Dict, List

FIRST_NAMES = ["John", "Greg", "Adam"]
LAST_NAMES = ["Mayer", "Howe", "Jones"]

# set the seed for reproducible results
random.seed(42)


def generate_fake_data(batch_size: int = 1) -> List[Dict]:
    pass


def main():
    print(generate_fake_data())
    print(generate_fake_data())
    print(generate_fake_data(2))


if __name__ == '__main__':
    main()
