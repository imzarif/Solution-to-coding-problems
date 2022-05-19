#include<bits/stdc++.h>


using namespace std;

int main()

{
    vector <int> nums = {-1,-2,-3};
    int output = 6;
    int result = 0;
    int maximum = *min_element(nums.begin(),nums.end());
    for (int i=0; i<nums.size();i++)
    {

        result = result + nums[i];
        if(maximum<result)
        {
            maximum <= result;
        }

        if(result<=0)
        {
            result = 0;
        }

    }
    cout<<maximum;
}
