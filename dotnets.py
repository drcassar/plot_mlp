# Inspired by
# https://tgmstat.wordpress.com/2013/06/12/draw-neural-network-diagrams-graphviz/

# UPDATE HISTORY
# April, 2018 - 2to3 - Madhavun Candadai
# September, 2022 - formatting and simplifying make

LAYERS = [3, 5, 5, 5, 5, 2]
PENWIDTH = 15
FONT = "Hilda 10"


if __name__ == "__main__":

    layers_str = ["Input"] + ["Hidden"] * (len(LAYERS) - 2) + ["Output"]
    layers_col = ["none"] + ["none"] * (len(LAYERS) - 2) + ["none"]
    layers_fill = ["black"] + ["gray"] * (len(LAYERS) - 2) + ["black"]

    print("digraph G {")
    print('\tfontname = "{}"'.format(FONT))
    print("\trankdir=LR")
    print("\tsplines=line")
    print("\tnodesep=.08;")
    print("\tranksep=1;")
    print("\tedge [color=black, arrowsize=.5];")
    print(
        '\tnode [fixedsize=true,label="",style=filled,'
        + "color=none,fillcolor=gray,shape=circle]\n"
    )

    # Clusters
    for i in range(0, len(LAYERS)):
        print(("\tsubgraph cluster_{} {{".format(i)))
        print(("\t\tcolor={};".format(layers_col[i])))
        print(
            (
                "\t\tnode [style=filled, color=white, PENWIDTH={},"
                "fillcolor={} shape=circle];".format(PENWIDTH, layers_fill[i])
            )
        )

        print(("\t\t"), end=" ")

        for a in range(LAYERS[i]):
            print("l{}{} ".format(i + 1, a), end=" ")

        print(";")
        print(("\t\tlabel = {};".format(layers_str[i])))

        print("\t}\n")

    # Nodes
    for i in range(1, len(LAYERS)):
        for a in range(LAYERS[i - 1]):
            for b in range(LAYERS[i]):
                print("\tl{}{} -> l{}{}".format(i, a, i + 1, b))

    print("}")
