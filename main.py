from a_star import Node, a_star
import matplotlib.pyplot as plt


def main():
    nodes = [
        Node(ID=1, x=1, y=5, neighbours=[3]),
        Node(ID=2, x=3, y=5, neighbours=[3]),
        Node(ID=3, x=3, y=4, neighbours=[1, 2, 4, 6]),
        Node(ID=4, x=1, y=3, neighbours=[3, 5]),
        Node(ID=5, x=3, y=2, neighbours=[4, 6, 7]),
        Node(ID=6, x=4, y=3, neighbours=[3, 5]),
        Node(ID=7, x=2, y=1, neighbours=[5]),
    ]
    node_start = nodes[0]
    node_goal = nodes[-3]

    result = a_star(start=node_start, goal=node_goal, nodes=nodes)

    # PLOT RESULTS:

    # plot field
    x_list = [node.x for node in nodes]
    y_list = [node.y for node in nodes]
    plt.scatter(x_list, y_list)

    # plot found path
    if result is not None:
        parent = result[0]
        successor = parent
        for node in result:
            parent = node
            plt.text(node.x, node.y, f'{node.ID}', bbox={'facecolor': 'yellow', 'alpha': 1, 'pad': 10})
            plt.plot([successor.x, parent.x], [successor.y, parent.y])
            successor = node

    plt.show()


if __name__ == '__main__':
    main()

