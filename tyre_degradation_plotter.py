import pandas as pd
import matplotlib.pyplot as plt
import os

class TyreDegradationPlotter:
    def __init__(self, data_file):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), data_file)
        self.data = pd.read_csv(file_path)

    def plot_degradation(self, tyre_type):
        tyre_data = self.data[self.data['TyreType'] == tyre_type]
        plt.figure(figsize=(10, 6))
        plt.plot(tyre_data['Lap'], tyre_data['Wear'], label=f"{tyre_type} Tyre")
        plt.title(f"Tyre Degradation for {tyre_type} Tyre")
        plt.xlabel("Lap")
        plt.ylabel("Tyre Wear (%)")
        plt.legend()
        plt.grid(True)
        plt.show()

    def compare_degradation(self, tyre_types):
        plt.figure(figsize=(10, 6))
        for tyre_type in tyre_types:
            tyre_data = self.data[self.data['TyreType'] == tyre_type]
            plt.plot(tyre_data['Lap'], tyre_data['Wear'], label=f"{tyre_type} Tyre")

        plt.title("Comparison of Tyre Degradation Rates")
        plt.xlabel("Lap")
        plt.ylabel("Tyre Wear (%)")
        plt.legend()
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    data_file = "example_tyre_degradation.csv"
    plotter = TyreDegradationPlotter(data_file)
    plotter.plot_degradation(tyre_type="Soft")
    plotter.compare_degradation(tyre_types=["Soft", "Medium"])