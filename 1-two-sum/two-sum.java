import java.util.*;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int i = 0 ; i<nums.length;i++)
        {
            for(int j =i+1;j<nums.length;j++)
            {
                if(nums[i]+nums[j]==target)
                {
                    return new int[] {i,j};
                }
            }
        }
          return new int[] {};
    }

public static void main(String[] args)
{
    Scanner s = new Scanner(System.in);
    int n = s.nextInt();
    int target = s.nextInt();
    int[] nums = new int[n];
    for(int i = 0;i<n;i++)
    {
        nums[i] = s.nextInt();
    }
    Solution sol = new Solution();
    int[] ans = sol.twoSum(nums, target);
    System.out.println(Arrays.toString(ans));
}
}