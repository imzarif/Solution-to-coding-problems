#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector <int> twoSum(vector <int> nums, int length, int target);
    vector <int>nums;
    nums.push_back(2);
    nums.push_back(7);
    nums.push_back(11);
    nums.push_back(15);
    int nums_length = nums.size();
    int target = 9;

    vector <int> result = twoSum(nums, nums_length, target);

  
    /*for (int i=0; i<result.size();i++)
    {
        cout <<result[i];
    }
    cout<<endl;*/
   
}

vector <int> twoSum(vector <int> nums, int length, int target) 
    { 
        int a = 0;
        int b = length-1;
        vector <int> result;

        while (a<b)
        {
            if(nums[a]+nums[b]==target)
            {
                result.push_back(a);
                result.push_back(b);
                break;
            }
            if (nums[a]+nums[b]<target)
            {
                a = a+1;
            }
            
            if (nums[a]+nums[b]>target)
            {
                b=b-1;
            }
            
        }

  cout << result[0];

    }