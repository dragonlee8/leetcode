#include <vector>
#include <map>
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string>     // std::string, std::stod

using namespace std;

class  Token
{
public:
	Token() {};
    virtual bool isValue() = 0;
    virtual void execute(vector<double>& s) = 0;
};

class Operand:public Token {
public:
	Operand(const string& num) {
        value = atoi(num.c_str());
    }
    bool isValue(){
        return true;
    }

    void execute(vector<double>& s)
    {
        s.push_back(value);
    }

private:
    int value;
};

class plusSign: public Token{
public:
    bool isValue()
    {
        return false;
    }

    void execute(vector<double>& s)
    {
        double num1 = s.back();
        s.pop_back();
        double num2 = s.back();
        s.pop_back();
        double num = (num1 + num2);
        s.push_back(num);
    }
};

class minusSign: public Token{
public:
    bool isValue()
    {
        return false;
    }

    void execute(vector<double>& s)
    {
        double num1 = s.back();
        s.pop_back();
        double num2 = s.back();
        s.pop_back();
        double num = num2 - num1;
        s.push_back(num);
    }
};

class Creator{
public:
    virtual Token* create(string& value) = 0;
};

class Factory{
private:
    map<string, Token*>  table;

public:
    Token* create(string& value)
    {
        map<string, Token*>::iterator it = table.find(value);
        if (it!= table.end())
        {
            return (Token*)it->second;;
        }
        else
        {
        	return new Operand(value);
        }

    }

    void registe(string name, Token* operators)
    {
        table[name] = operators;
    }
};

int main()
{
    Factory factory;
    Token* plus_creator = new plusSign;
    Token* minus_creator = new minusSign;


    factory.registe(string("+"), plus_creator);
    factory.registe(string("-"), minus_creator);


    vector<double> stk;
    vector<string> input;
    input.push_back(string("1"));
    input.push_back(string("1"));
    input.push_back(string("+"));
    for (int i = 0; i < input.size(); ++i)
    {
        factory.create(input[i])->execute(stk);
    }
    cout << stk.back() << endl;
}
