#include <iostream>
#include <string>
#include <vector>
using namespace std;
class Student {
protected:
    string id;
    string name;
public:
    Student(string id, string name) {
        this->id = id;
        this->name = name;
    }
    virtual void display() {
        cout << "Student ID: " << id << " | Name: " << name << endl;
    }
    virtual ~Student() {}
};
class StudentIT : public Student {
private:
    float cppScore;
public:
    StudentIT(string id, string name, float cppScore) : Student(id, name) {
        this->cppScore = cppScore;
    }
    void display() override {
        cout << "StudentIT ID: " << id 
             << " | Name: " << name 
             << " | C++ Score: " << cppScore << endl;
    }
};

int main() {
    cout << "--- DEMO QUAN LY SINH VIEN (DA HINH) ---" << endl;
    Student* s1 = new Student("SV001", "Nguyen Van A");
    Student* s2 = new StudentIT("IT001", "Tran Thi B", 9.5);

    cout << "\n1. Hien thi sinh vien co ban:" << endl;
    s1->display(); 

    cout << "\n2. Hien thi sinh vien IT (Da hinh):" << endl;
    s2->display(); 
    delete s1;
    delete s2;

    cout << "\n--- Vi du voi mang (Vector) ---" << endl;
    vector<Student*> listStudent;
    listStudent.push_back(new Student("SV002", "Le Van C"));
    listStudent.push_back(new StudentIT("IT002", "Pham Van D", 8.0));

    for (Student* s : listStudent) {
        s->display();
    }
    for (Student* s : listStudent) {
        delete s;
    }

    return 0;
}