#include <iostream>

using namespace std;

class Test
{
   public:
      Test(int len);             // 简单的构造函数
      Test(const Test &obj);  // 拷贝构造函数
      ~Test();                     // 析构函数
      Test& operator=(const Test &obj);

      int *a;
};

Test::Test(int len){
    cout<<"Test()"<<endl;
    a = new int(len);
}

Test::Test(const Test &obj){
    cout<<"Copy Test()"<<endl;
    a = new int(100);
}

Test::~Test(){
    cout<<"~Test()"<<endl;
}

Test& Test::operator=(const Test &obj){
    cout<<"="<<endl;
    if(this != &obj){
        this->a = new int(*obj.a);
    }
    return *this;
}

int main(){
    Test test(10), test2 = test, test3(20);

    cout<<*test.a<<" "<<*test2.a<<" "<<*test3.a<<endl;

    test3 = test;

    cout<<*test.a<<" "<<*test2.a<<" "<<*test3.a<<endl;
    
    return 0;
}
