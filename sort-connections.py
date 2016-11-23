#!/usr/bin/env python3

import sys

def readConnections():
    connections = []
    for line in sys.stdin:
        if line.rstrip() == "":
            break
        tokens = line.rstrip().split(" ")
        connections.append((tokens[0], tokens[1], int(tokens[2]), int(tokens[3])))

    return connections

def writeConnections(connections):
    for c in connections:
        sys.stdout.write("{} {} {} {}\n".format(
            c[0], c[1], c[2], c[3]
        ))

def main():
    connections = readConnections()
    connections.sort(key=lambda c: c[2])
    writeConnections(connections)

if __name__ == '__main__':
    main()
