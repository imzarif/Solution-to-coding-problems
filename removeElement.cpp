#include<bits/stdc++.h>

using namespace std;

int main()
{
    vector <int> nums = {2,2,2,2};
    int val = 3;

    int f = 0;
    int s = 0;
    int result = 0;
    int temp;

    while (s<nums.size() )
    {
while(nums[f]!=val && f<nums.size())
        {
            f+=1;

        }

        s = f;


        while(nums[s]==val )
        {
            s+=1;
            if(s>nums.size()-1)
        {
            break;
        }
        }


        if(s>nums.size()-1)
        {
            break;
        }



        cout<<"value of f: "<<f<<endl;
        cout<<"value of s: "<<s<<endl;


        temp = nums[s];
        nums[s] = nums[f];
        nums[f] = temp;
        f+=1;




    }


    for(int i=0;i<nums.size();i++)
    {
        cout<<nums[i]<<',';
    }
    cout<<f;

}


























































































