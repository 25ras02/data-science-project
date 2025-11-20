import matplotlib.pyplot as plt

def plot_features(df):
    plt.figure()
    plt.scatter(df['feature1'], df['target'])
    plt.xlabel("Feature 1")
    plt.ylabel("Target")
    plt.title("Feature 1 vs Target")
    plt.show()

def plot_corr(df):
    plt.figure()
    plt.matshow(df.corr(), fignum=1)
    plt.title("Correlation Matrix")
    plt.colorbar()
    plt.show()