import matplotlib.pyplot as plt
import matplotlib.patches as patches

def parse_pdb(pdb_file):
    """
    Parse the PDB file for HELIX and SHEET records.
    Returns a list of secondary structure elements, each as a dict:
      { 'type': 'helix' or 'sheet',
        'chain': chain identifier,
        'start': starting residue number,
        'end': ending residue number }
    """
    elements = []
    with open(pdb_file) as f:
        for line in f:
            if line.startswith("HELIX"):
                # PDB HELIX record:
                # Columns: start chain at col 20, start seq number (col 22-25),
                # end chain at col 32, end seq number (col 34-37)
                try:
                    chain = line[19].strip()
                    start = int(line[21:25].strip())
                    end = int(line[33:37].strip())
                    elements.append({
                        "type": "helix",
                        "chain": chain,
                        "start": start,
                        "end": end
                    })
                except Exception:
                    continue
            elif line.startswith("SHEET"):
                # PDB SHEET record:
                # Columns: start chain at col 21, start seq (col 22-26),
                # end chain at col 32, end seq (col 33-37)
                try:
                    chain = line[21].strip()
                    start = int(line[22:26].strip())
                    end = int(line[32:37].strip())
                    elements.append({
                        "type": "sheet",
                        "chain": chain,
                        "start": start,
                        "end": end
                    })
                except Exception:
                    continue
    return elements

def draw_topology(pdb_file, output_file=None):
    """
    Parse the given PDB file and draw a 2D topology diagram.
    The diagram is saved to output_file if provided, otherwise shown interactively.
    """
    elements = parse_pdb(pdb_file)
    if not elements:
        print("No secondary structure elements found in the PDB file.")
        return

    # Determine overall residue range (using only the first chain found)
    # For simplicity we use min and max over all elements.
    min_res = min(el["start"] for el in elements)
    max_res = max(el["end"] for el in elements)
    
    fig, ax = plt.subplots(figsize=(10, 3))
    
    # Draw a horizontal line representing the sequence
    ax.hlines(0, min_res - 5, max_res + 5, colors="black", linestyles="dashed", linewidth=1)
    
    # Draw each element as a shape above (helix) or below (sheet) the line.
    for el in elements:
        start = el["start"]
        end = el["end"]
        width = end - start
        if el["type"] == "helix":
            # Draw helix as a rectangle above the line
            rect = patches.Rectangle((start, 0.2), width, 0.6, linewidth=1,
                                     edgecolor="blue", facecolor="lightblue", alpha=0.7)
            ax.add_patch(rect)
            ax.text((start+end)/2, 1, f"Helix {el['chain']}:{start}-{end}", ha="center", va="bottom", fontsize=8)
        elif el["type"] == "sheet":
            # Draw sheet as an arrow below the line
            arrow = patches.FancyArrow(start, -0.2, width, 0, width=0.3,
                                       length_includes_head=True, head_width=0.5,
                                       head_length=width*0.05, edgecolor="green", facecolor="lightgreen", alpha=0.7)
            ax.add_patch(arrow)
            ax.text((start+end)/2, -1, f"Sheet {el['chain']}:{start}-{end}", ha="center", va="top", fontsize=8)
    
    ax.set_xlim(min_res - 5, max_res + 5)
    ax.set_ylim(-2, 2)
    ax.set_xlabel("Residue Number")
    ax.set_yticks([])
    ax.set_title("Protein Topology Diagram")
    plt.tight_layout()
    
    if output_file:
        plt.savefig(output_file, dpi=300)
        print(f"Topology diagram saved to {output_file}")
    else:
        plt.show()
