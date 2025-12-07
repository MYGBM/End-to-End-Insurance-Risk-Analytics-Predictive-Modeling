# Basic script to convert raw .txt data to .csv and save to processed path
import pandas as pd
import os

RAW_PATH = os.path.join('data', 'raw', 'MachineLearningRating_v3.txt')
PROCESSED_PATH = os.path.join('data', 'processed', 'MachineLearningRating_v3.csv')

def main():
	# Read the raw text file (pipe-separated)
	df = pd.read_csv(RAW_PATH, sep='|', engine='python')
	# Ensure processed directory exists
	os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)
	# Save as CSV (comma-separated)
	df.to_csv(PROCESSED_PATH, index=False)
	print(f"Processed CSV saved to: {PROCESSED_PATH}")

if __name__ == "__main__":
	main()
