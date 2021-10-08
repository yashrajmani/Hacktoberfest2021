#include<bits/stdc++.h>
using namespace std;

vector<int> subarray(vector<int> &nums){

    vector<int> ans;
    int left = 0;
    int right = 0;
    int l1 = 0;
    int r1 = 0;
    int meh = 0;
    int msf = INT_MIN;

    for(int i=0; i<nums.size(); i++){
        if(nums[i] >= meh + nums[i]){
            meh = nums[i];
            l1 = i;
            r1 = i;
        }
        else{
            meh = meh + nums[i];
            r1 = i;
        }

        if(meh >= msf){
            msf = meh;
            left = l1;
            right = r1;
        }
    }

    cout<<"The starting index is : "<<left<<endl;
    cout<<"The ending index is : "<<right<<endl;

    for(int i=left; i<=right; i++)
        ans.push_back(nums[i]);

    return ans;

}

int main(){

    vector<int> nums {5,4,-1,7,8};
    cout<<endl<<endl;
    vector<int> max_sum = subarray(nums);
    cout<<"The subarray is : ";
    for(int i=0; i<max_sum.size(); i++)
        cout<<max_sum[i]<<" ";
    cout<<endl;

    int count = 0;
    for(int i=0; i<max_sum.size(); i++)
        count += max_sum[i];
    cout<<"The maximum sum subarray is : "<<count<<endl;
    cout<<endl<<endl;
    
    return 0;
}