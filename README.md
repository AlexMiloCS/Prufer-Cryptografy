# Prüfer Sequence Cryptography

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Graph Theory](https://img.shields.io/badge/Math-Graph_Theory-blue?style=for-the-badge)
![Cryptography](https://img.shields.io/badge/Security-Cryptography-black?style=for-the-badge)

A Python implementation that secures a communication network (represented as a tree graph) by encoding it into a **Prüfer sequence**, encrypting that sequence, and successfully decoding it back into the original network structure.

---

## Table of Contents
1. [About the Algorithm](#-about-the-algorithm)
2. [Features](#-features)
3. [Getting Started](#-getting-started)
4. [Usage & Example](#-usage--example)

---

## About the Algorithm
In combinatorial mathematics, a **Prüfer sequence** is a unique sequence associated with a labeled tree. For a tree with $n$ vertices, the sequence has a length of $n - 2$. 

This project uses this mathematical property to compress a network of communicating agents into a simple array of integers. Once the tree is reduced to a sequence, a simple mathematical shift cipher is applied to encrypt the data for secure transmission. The receiver then decrypts the sequence and uses the inverse Prüfer algorithm to perfectly reconstruct the communication tree.

---

## Features
* **Graph Parsing:** Automatically reads agent communication logs from a text file and builds an undirected graph.
* **Label Assignment:** Dynamically maps string-based agent names (e.g., "Alpha", "Bravo") to integer IDs required for Prüfer encoding.
* **Prüfer Encoding:** Identifies leaf nodes (agents with only one connection) and iteratively reduces the tree into an $n-2$ integer sequence.
* **Shift Encryption:** Applies a symmetric key $k$ (shift cipher) to the sequence to encrypt the transmission.
* **Prüfer Decoding:** Restores the exact tree edges from the decrypted sequence.

---

## Getting Started

### Prerequisites
* **Python 3.x** installed on your machine. No external libraries are required (uses standard Python libraries).

### Installation & Execution
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/Prufer-Cryptography.git](https://github.com/yourusername/Prufer-Cryptography.git)
   cd Prufer-Cryptography
   ```
2. **Run the script:**
   Ensure `agents.txt` is in the same directory as the script, then execute:
   ```bash
   python erg5.py
   ```
## Usage & Example

The program reads connections from a simple comma-separated text file named `agents.txt`. 

**Example `agents.txt` input:**
```text
Alpha,Charlie
Alpha,Golf
Bravo,Delta
Delta,Alpha
Delta,Echo
Echo,Fox
Echo,Hotel
```
**Expected Console Output:**
When you run the script, it prints every step of the cryptographic process:
```text
my agent numbers are: {'Alpha': 1, 'Charlie': 2, 'Golf': 3, 'Bravo': 4, 'Delta': 5, 'Echo': 6, 'Fox': 7, 'Hotel': 8}
my tree's connections are: [[1, 2], [1, 3], [1, 5], [5, 4], [5, 6], [6, 7], [6, 8]]
Prufers encoding of the graph: [1, 1, 5, 5, 6, 6]
Coded message sent: [3, 3, 7, 7, 8, 8]
Decoded message sent: [1, 1, 5, 5, 6, 6]
Prufers decoding of the graph: [[2, 1], [3, 1], [4, 5], [1, 5], [7, 6], [8, 6], [5, 6]]
```
