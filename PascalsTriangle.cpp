#include<bits/stdc++.h>

using namespace std;

int main()
{
    int numRows = 5;
    vector < vector <int> > output;
    vector <int> temp;




    for(int i=0;i<numRows;i++)
    {
        for(int j=0;j<=i;j++)
        {
            if(j==0 || j==i)
            {
                temp.push_back(1);
            }
            else
            {
                temp.push_back(output[i-1][j-1]+output[i-1][j]);
            }
        }
        output.push_back(temp);
        temp = {};
    }

    for(int x=0; x<output.size(); x++)
    {
        cout<<"{";
       for(int y=0; y<output[x].size();y++)
       {
           cout<<output[x][y]<<",";
       }
       cout<<"}"<<" ";
    }
}


