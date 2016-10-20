#include <vector>
#include <map>
#include <stdio.h>
#include <iostream>
#include <stdlib.h>

using namespace std;

class  Token
{
public:
    virtual bool isValue() = 0;
    void setValue(int v)
    {
        value = v;
    }
    int getValue(){
        return value;
    }
    virtual void execute(vector<Token* >& s) = 0;
private:
    int value;
};

class Operand:public Token {
public:
    bool isValue(){
        return true;
    }

    void execute(vector<Token*>& s)
    {
        s.push_back(this);
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

    void execute(vector<Token*>& s)
    {
        Token* num1 = s.back();
        s.pop_back();
        Token* num2 = s.back();
        s.pop_back();
        Operand* num = new Operand;
        num->setValue(num2->getValue() + num1->getValue());
        s.push_back(num);
    }
};

class minusSign: public Token{
public:
    bool isValue()
    {
        return false;
    }

    void execute(vector<Token*>& s)
    {
        Token* num1 = s.back();
        s.pop_back();
        Token* num2 = s.back();
        s.pop_back();
        Operand* num = new Operand;
        num->setValue(num2->getValue() - num1->getValue());
        s.push_back(num);
    }
};

class Creator{
public:
    virtual Token* create(string& value) = 0;
};

class OperandCreator : public Creator{
public:
    Token* create(std::string& value){
        Operand* op = new Operand;
        op->setValue(atoi(value.c_str()));
        return op;
    }
};

class plusCreator : public Creator{
public:
    Token* create(string& value){
        return new plusSign;
    }
};

class minusCreator : public Creator{
public:
    Token* create(string& value){
        return new minusSign;
    }
};

class Factory{
private:
    map<string, Creator*>  table;

public:
    Token* create(string& value)
    {
        map<string, Creator*>::iterator it = table.find(value);
        if (it!= table.end())
        {
            return (Token*)it->second->create(value);
        }
        return NULL;
    }

    void registe(string name, Creator* creator)
    {
        table[name] = creator;
    }
};

int main()
{
    Factory factory;
    Creator* plus_creator = new plusCreator;
    Creator* minus_creator = new minusCreator;
    Creator* operand_creator = new OperandCreator;


    factory.registe(string("+"), plus_creator);
    factory.registe(string("-"), minus_creator);
    factory.registe(string("0"), operand_creator);
    factory.registe(string("1"), operand_creator);
    factory.registe(string("2"), operand_creator);
    factory.registe(string("3"), operand_creator);
    factory.registe(string("4"), operand_creator);
    factory.registe(string("5"), operand_creator);
    factory.registe(string("6"), operand_creator);
    factory.registe(string("7"), operand_creator);
    factory.registe(string("8"), operand_creator);
    factory.registe(string("9"), operand_creator);


    vector<Token*> stk;
    vector<string> input;
    input.push_back(string("1"));
    input.push_back(string("1"));
    input.push_back(string("-"));
    for (int i = 0; i < input.size(); ++i)
    {
        factory.create(input[i])->execute(stk);
    }
    cout << stk.back()->getValue() << endl;
}


