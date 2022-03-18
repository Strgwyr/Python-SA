class Trapezoid:
    def constructor(a = 0, b = 0, c = 0, d = 0, height = 0):
        a, b, c, d, e =list((input('Enter the measurements starting from the height top, bottom, left, and right: ')).split())
        f = float(b)
        g = float(c)
        h = float(d)
        i = float(e)
        height = float(a)
     
        Perimeter = f + g + h + i
        Area = height *(f + g) / 2
        print("\n Area of a Trapezoid = %.2f " %Area)
        print(" Perimiter of a Trapezoid = %.2f " %Perimeter) 
        print("I miss you")
        

    constructor()
    