class Solution {
    public boolean hasDuplicate(int[] nums) {
        Arrays.sort(nums);
        for(int i = 1;i<nums.length;i++){
            if(nums[i]==nums[i-1])
            return true;
        }
        
       /* Set<Integer> unique = new HashSet<>();

        for(int i = 0; i<nums.length;i++){
            if(unique.contains(nums[i])){
                return true;
            }
            unique.add(nums[i]); */

        
        return false;
 
    }
}
