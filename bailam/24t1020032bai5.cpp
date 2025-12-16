#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;
class Shape {
protected:
    string name;
public:
    Shape(string name) : name(name) {}
    virtual ~Shape() {}
    virtual double area() = 0;
    virtual double perimeter() = 0;
    string getName() {
        return name;
    }
};
class Rectangle : public Shape {
private:
    double width;
    double height;

public:
    Rectangle(string name, double width, double height) 
        : Shape(name), width(width), height(height) {}
    double area() override {
        return width * height;
    }
    double perimeter() override {
        return 2 * (width + height);
    }
};
class Circle : public Shape {
private:
    double radius;
    const double PI = 3.14159;

public:
    Circle(string name, double radius) 
        : Shape(name), radius(radius) {}
    double area() override {
        return PI * radius * radius;
    }
    double perimeter() override {
        return 2 * PI * radius;
    }
};

int main() {
    vector<Shape*> shapes;
    shapes.push_back(new Rectangle("Hinh Chu Nhat A", 4.0, 5.0));
    shapes.push_back(new Circle("Hinh Tron B", 3.0));
    shapes.push_back(new Rectangle("Hinh Chu Nhat C", 2.0, 8.0));
    double totalArea = 0.0;
    cout << "--- Chi tiet tung hinh ---" << endl;
    for (Shape* shape : shapes) {
        double currentArea = shape->area();
        totalArea += currentArea;
        cout << "Ten: " << shape->getName() 
             << " | Dien tich: " << currentArea 
             << " | Chu vi: " << shape->perimeter() << endl;
    }
    cout << "-------------------------" << endl;
    cout << "Tong dien tich cac hinh: " << totalArea << endl;
    for (Shape* shape : shapes) {
        delete shape;
    }
    shapes.clear();

    return 0;
}