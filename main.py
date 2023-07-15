import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import mode
import tkinter as tk
from tkinter import filedialog


# Function to analyze the data
def analyze_data(file_path):
    data = np.loadtxt(file_path, skiprows=1, usecols=(0, 2))

    # Extract X-axis data
    x_values = data[:, 0]

    # Calculate the minimum and maximum values
    min_value = np.min(x_values)
    max_value = np.max(x_values)

    return data, min_value, max_value


# Function to handle file selection
def select_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[('Data Files', '*.dat')])
    if file_path:
        data, min_value, max_value = analyze_data(file_path)
        plot_graph(data, min_value, max_value)


# Function to plot the graph
def plot_graph(data, min_value, max_value):
    # Extract X-axis data
    x_values = data[:, 0]

    # Plotting
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x_values, label='X-axis')
    ax.set_xlabel('X-axis')
    ax.set_title('X-axis Plot')

    # Highlight the minimum and maximum values with colored markers
    ax.plot(np.argmin(x_values), min_value, 'b*', label=f'Min: {min_value:.2f}')
    ax.plot(np.argmax(x_values), max_value, 'g^', label=f'Max: {max_value:.2f}')

    ax.legend()

    plt.show()

    return data


# Function to display mean
def show_mean():
    if file_path:
        data, _, _ = analyze_data(file_path)
        mean_value = np.mean(data[:, 1])
        mean_label.config(text="Mean: {:.2f}".format(mean_value))


# Function to display median
def show_median():
    if file_path:
        data, _, _ = analyze_data(file_path)
        median_value = np.median(data[:, 1])
        median_label.config(text="Median: {:.2f}".format(median_value))


# Function to display mode
def show_mode():
    if file_path:
        data, _, _ = analyze_data(file_path)
        mode_value = mode(data[:, 1]).mode[0]
        mode_label.config(text="Mode: {:.2f}".format(mode_value))


# Create the Tkinter app
def main():
    global file_path
    file_path = ""

    root = tk.Tk()
    root.title('Data Analysis')
    root.geometry("500x400")

    # Styling
    root.configure(bg="#f0f0f0")
    root.option_add('*Font', 'Arial 10')
    root.option_add('*Button.background', '#4c8caf')
    root.option_add('*Button.foreground', 'white')
    root.option_add('*Button.activeBackground', '#44779e')

    # File selection button
    file_button = tk.Button(root, text='Select File', command=select_file, width=30, height=2)
    file_button.pack(pady=20)

    # Buttons to show mean, median, and mode
    mean_button = tk.Button(root, text='Show Mean', command=show_mean, width=30, height=2)
    mean_button.pack(pady=5)

    median_button = tk.Button(root, text='Show Median', command=show_median, width=30, height=2)
    median_button.pack(pady=5)

    mode_button = tk.Button(root, text='Show Mode', command=show_mode, width=30, height=2)
    mode_button.pack(pady=5)

    # Labels to display mean, median, and mode values
    global mean_label
    mean_label = tk.Label(root, text="Mean: ", bg="#f0f0f0")
    mean_label.pack()

    global median_label
    median_label = tk.Label(root, text="Median: ", bg="#f0f0f0")
    median_label.pack()

    global mode_label
    mode_label = tk.Label(root, text="Mode: ", bg="#f0f0f0")
    mode_label.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
