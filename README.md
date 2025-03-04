# Topo2d

**Topo2d** is a simple Python package that generates 2D topology diagrams for proteins by parsing PDB files. It extracts secondary structure elements such as helices and sheets from the PDB file and produces an annotated diagram using matplotlib. This tool is especially useful for visualizing protein structures in a simplified 2D format for analysis or publication purposes.

---

## Features

- **PDB Parsing:**  
  Extracts HELIX and SHEET records from a PDB file to identify secondary structure elements.

- **2D Diagram Drawing:**  
  Generates a clear and concise 2D topology diagram using matplotlib. Helices are displayed as colored rectangles and sheets as arrows.

- **Command-line Interface (CLI):**  
  Easily run the tool from the command line to process your PDB file and output an image.

- **Python API:**  
  Import functions directly into your Python scripts to integrate protein topology visualization into your data analysis workflows.

- **Pip Installable:**  
  Install the package using pip for a smooth integration into your Python environment.

---

## Installation

### Prerequisites

- **Python 3.6+**  
- **pip**

### Install via PyPI

If Topo2d is available on PyPI, you can install it using pip:

```bash
pip install topo2d
```

### Install from Source

1. **Clone the Repository or Download the Source Code:**

   ```bash
   git clone https://github.com/yourusername/topo2d.git
   cd topo2d
   ```

2. **Install in Editable Mode (Development Mode):**

   ```bash
   pip install -e .
   ```

   This installs the package and creates a console script (`topo2d`) that you can run from the command line.

3. **Or Build and Install:**

   Create a source distribution and wheel:

   ```bash
   python setup.py sdist bdist_wheel
   ```

   Then install the built package:

   ```bash
   pip install dist/topo2d-0.1.0-py3-none-any.whl
   ```

---

## Usage

### Command-line Interface

After installing, you can run Topo2d directly from your terminal:

```bash
topo2d path/to/your_file.pdb -o output_image.png
```

- **`path/to/your_file.pdb`**: Path to the input PDB file.
- **`-o output_image.png`**: (Optional) Save the generated topology diagram as an image file (e.g., PNG).  
  If you omit the `-o` flag, the diagram will be displayed interactively using matplotlib's viewer.

### Python API

You can also use Topo2d directly in your Python scripts:

```python
from topo2d.draw import draw_topology

# To display the topology diagram interactively:
draw_topology("path/to/your_file.pdb")

# To save the topology diagram to a file:
draw_topology("path/to/your_file.pdb", output_file="topology_diagram.png")
```

This makes it easy to integrate Topo2d into larger bioinformatics workflows or data analysis pipelines.

---

## Example

Suppose you have a PDB file named `protein.pdb` with the relevant HELIX and SHEET records. You can create a topology diagram by running:

```bash
topo2d protein.pdb -o protein_topology.png
```

This command will parse the PDB file and save the resulting diagram as `protein_topology.png`. Alternatively, to view the diagram without saving, run:

```bash
topo2d protein.pdb
```

The tool will then open a matplotlib window displaying the 2D topology diagram.

---

## Contributing

Contributions, suggestions, and feature requests are welcome! If you encounter any issues or have ideas for improvements, please open an issue or submit a pull request on the [GitHub repository](https://github.com/yourusername/topo2d).

---

## License

Topo2d is distributed under the GNU General Public License v2 (GPLv2). See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

Topo2d is inspired by **TopDraw**, a Tcl/Tk-based sketchpad for protein topology diagrams created by Charlie Bond (2000–2002). Special thanks to all the contributors and maintainers in the bioinformatics community for providing useful tools and libraries that make projects like this possible.

---

## Contact

For questions, comments, or suggestions, please contact:  
**Kushal Raj Roy** – [kushalrajroy1@gmail.com](mailto:kushalrajroy1@gmail.com)

Enjoy using Topo2d and happy coding!

