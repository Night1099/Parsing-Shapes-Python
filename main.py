import csv
from Shapes3D import Cube, Cuboid, Cylinder, Sphere, Prism

totalCount = 0

def main():
    global totalCount
    shapes = []
    with open("shapes.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == "cube":
                shapes.append(Cube(float(row[1])))
            elif row[0] == "cuboid":
                shapes.append(Cuboid(float(row[1]), float(row[2]), float(row[3])))
            elif row [0] == "cylinder":
                shapes.append(Cylinder(float(row[1]), float(row[2])))
            elif row [0] == "sphere":
                shapes.append(Sphere(float(row[1])))
            elif row [0] == "prism":
                shapes.append(Prism(float(row[1]), float(row[2]), float(row[3])))
            elif row[0] == "area":
                area = 0
                for shape in shapes:
                    area += shape.GetArea()
                resulta = area * float(row[1])
                totalCount += resulta
                shapes.clear()
            elif row[0] == "volume":
                volume = 0
                for shape in shapes:
                    volume += shape.GetVolume()
                resultv = volume * float(row[1])
                totalCount += resultv
                shapes.clear()

if __name__ == "__main__":
    main()
    print(f"Here's your total {totalCount}")
