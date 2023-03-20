#include <iostream>

using namespace std;

string add(string a, string b){
    int a_num = stoi(a);
    int b_num = stoi(b);
    return to_string(a_num+b_num);
}

string multiply(string a, string b){
    int a_num = stoi(a);
    int b_num = stoi(b);
    return to_string(a_num*b_num);
}

struct BigInt{
    string value = "0";
    BigInt& operator+=(const int rhs){
        value = add(value,to_string(rhs));
        return *this;
    }
    BigInt& operator*=(const int rhs){
        value = multiply(value,to_string(rhs));
        return *this;
    }
};

BigInt operator+(const BigInt lhs,
        const int rhs)
{
    BigInt result;
    result += rhs;
    return result;
}

int main() {
    BigInt x;
    x = x+3;
    x *= 4;
    cout<<x.value<<endl;
}