#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <fcntl.h>
#include <iostream>
using namespace std;

class Animal {
public:
    void move(void) {
        cout << "Hi, it is animal's move" << endl;
    }
    virtual void eat(void){
        cout << "fuck" << endl;
    }
    virtual void hello(void){
        cout << "hello, we are all animals!" << endl;
    }
};

class Ass : public Animal {
public:
    void eat(void){
        cout << "Eat my ass!" << endl;
    }
    void hello(void){
        cout << "hello, I am not animal!" << endl;
    }
};

int main(){
        Animal* ss = new Ass();
        ss->eat();
        ss->move();
        ss->hello();
        return 0;
}

