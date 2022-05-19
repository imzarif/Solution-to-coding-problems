#include<iostream>
#include<vector>

using namespace std;

int main()
{
    vector <int> nums = {1,3,5,6};
    int length = nums.size();

    int target = 7;
    int result;

    for(int i=0; i<length;i++)
    {
        if(nums[i]==target)
        {
            result = i;
            break;
        }
        else if(nums[i]>target)
        {
            result = i;
            break;
        }
        else if(i==length-1)
        {
            result = i+1;

        }
    }
    cout<<result;

}
