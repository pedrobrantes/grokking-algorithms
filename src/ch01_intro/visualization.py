import matplotlib.pyplot as plt
import numpy as np
import os

def plot_complexity():
    """Plots the comparison between Linear and Binary Search time complexities."""
    
    # Grants 'assets' diretory exists
    os.makedirs('assets', exist_ok=True)

    # Data range (number of elements)
    n = np.linspace(1, 100, 100)
    
    # Complexities
    linear_time = n  # O(n)
    binary_time = np.log2(n)  # O(log n)
    
    plt.figure(figsize=(10, 6))
    plt.plot(n, linear_time, label='Simple Search O(n)', color='red', linestyle='--')
    plt.plot(n, binary_time, label='Binary Search O(log n)', color='blue', linewidth=2)
    
    plt.title('Time Complexity Comparison: Linear vs Binary Search')
    plt.xlabel('Number of Elements (n)')
    plt.ylabel('Operations (Steps)')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    # Save the plot
    output_path = 'assets/binary_search_complexity.png'
    plt.savefig(output_path)
    print(f"Graph saved to {output_path}")

if __name__ == "__main__":
    plot_complexity()
