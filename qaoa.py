import numpy as np
from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

# Define the Max-Cut problem
def max_cut(graph):
    n = len(graph)
    # Create a quantum circuit
    qc = QuantumCircuit(n)
    # Initialize qubits
    qc.h(range(n))  # Apply Hadamard gate to all qubits

    # Define the cost Hamiltonian
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] == 1:
                qc.cx(i, j)  # Apply CNOT gate

    # Measure the qubits
    qc.measure_all()
    return qc

# Example graph representation (adjacency matrix)
graph = [[0, 1, 0, 1],
         [1, 0, 1, 0],
         [0, 1, 0, 1],
         [1, 0, 1, 0]]

# Create the circuit
circuit = max_cut(graph)

# Execute the circuit
from qiskit_aer import AerSimulator
backend = AerSimulator()
compiled_circuit = transpile(circuit, backend)
job = backend.run(compiled_circuit)
result = job.result()
counts = result.get_counts()

# Plot the results
plot_histogram(counts)
