import tensorflow as tf
import numpy as np
from loader import Create_datasets


def main():
    datasets = Create_datasets("trainSet.txt","evalSet.txt","devSet.txt")
    

if __name__ == "__main__":
    main()