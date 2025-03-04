import argparse
from topo2d.draw import draw_topology

def main():
    parser = argparse.ArgumentParser(
        description="Draw a 2D protein topology diagram from a PDB file."
    )
    parser.add_argument("pdb_file", help="Input PDB file")
    parser.add_argument("-o", "--output", help="Output image file (e.g., diagram.png)")
    args = parser.parse_args()
    
    draw_topology(args.pdb_file, output_file=args.output)

if __name__ == "__main__":
    main()
