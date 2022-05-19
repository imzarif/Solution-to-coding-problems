#include<iostream>
#include<map>

using namespace std;

int main()
{
    string s = "MCMXCIV";
    int total = 0;
    map< char, int> rtoI = { {'I',1}, {'V',5}, {'X',10}, {'L',50}, {'C',100}, {'D',500}, {'M',1000} };

    int i=0;

    while(i<s.length())
    {
        auto key_val = rtoI.find(s[i]);
        auto next_key_val = rtoI.find(s[i+1]);

       if( key_val->second<next_key_val->second)
       {
           total = total+next_key_val->second-key_val->second;
           i = i+2;
           continue;
       }


        total = total + key_val->second;
        i++;



    }
cout<<total;
}


