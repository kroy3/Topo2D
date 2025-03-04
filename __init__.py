"""
Topo2d: A simple protein topology drawing tool.

This package parses PDB files to extract secondary structure elements
(helices and sheets) and generates a 2D topology diagram using matplotlib.

Version: 0.1.0
"""

__version__ = "0.1.0"

from .draw import draw_topology, parse_pdb
