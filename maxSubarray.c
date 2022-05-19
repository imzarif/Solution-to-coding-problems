#include<iostream>
#include<vector>

using namespace std;

int main()

{
    vector <int> nums = {-2,1,-3,4,-1,2,1,-5,4};
    int output = 6;
    int result = 0;
    int max = 0;
    for (int i=0; i<nums.size();i++)
    {
        if(max<result)
        {
            max = result;
        }
        result = result + nums[i];
        if(result<=0)
        {
            result = 0;
        }

    }
    cout<<max;
}
