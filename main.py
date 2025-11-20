import sys

from src.data_loader import load_data
from src.visualize import plot_features, plot_corr
from src.model import train_model

def main():
    print("Loading Data...")
    df = load_data()
    print(df.head())

    print("\nPlotting Data...")
    plot_features(df)
    plot_corr(df)

    print("\nTraining Model...")
    model, mse = train_model(df)

    print("\nModel coefficients: ", model.coef_)
    print("\nModel Intercept: ", model.intercept_)
    print("\nMean Squared Error: ", mse)

if __name__ == "__main__":
    main()

