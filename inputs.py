from ShapeTrap import Trapezoid

inp = input().split()
height = float(inp[0])
sides = [float(inp[x]) for x in range(1, len(inp))]
T = Trapezoid(height, *sides)
T.printResults()
