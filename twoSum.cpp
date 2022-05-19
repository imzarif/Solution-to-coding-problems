#include<iostream>
#include<vector>
#include<unordered_map>

using namespace std;

int main(){
     vector <int> nums{2,7,11,15};
     int target = 9;

     vector <int> ret;
     int val;
     unordered_map<int,int> hm;
     for (int i=0; i<nums.size(); i++)
     {
         val = target-nums[i];
         if(hm.find(val) != hm.end())
         {
             ret.push_back(hm[val]);
             ret.push_back(i);
         }
         else
         {
             hm[nums[i]] = i;
         }
     }

   cout<<ret[1];
}
