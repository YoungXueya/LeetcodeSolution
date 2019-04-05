import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class FourSum {
//    Test Case[1,0,-1,0,-2,2]
//            0
//    Call ThreeSum in this problem

    public static List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> res=new ArrayList();
        int len=nums.length;
        Arrays.sort(nums);
        if(len<4) return res;
        int max=nums[len-1];
        for(int i=0;i<len-3;i++){
            if(i>0&&nums[i]==nums[i-1]) continue;
            else if(nums[i]+3*max<target) continue;
            else if(nums[i]*4>target) break;

            threeSum(nums,target-nums[i],i+1,len-1,res);
        }
        return res;
    }
    public static void threeSum(int[] nums,int target,int lo,int hi, List<List<Integer>> res){
        for(int i=lo;i<hi-1;i++){
            if(i>lo&&nums[i]==nums[i-1]) continue;

            int l=i+1,r=hi,t=target-nums[i];
            while(l<r){
                if(nums[l]+nums[r]==t){
                    res.add(Arrays.asList(nums[lo-1],nums[i],nums[l],nums[r]));
                    l++;r--;
                    while(l<r&&nums[l]==nums[l-1]) l++;
                    while(l<r&&nums[r]==nums[r+1]) r--;
                }
                else if(nums[l]+nums[r]<t) l++;
                else r--;
            }
        }
    }
    public static int[] stringToIntegerArray(String input) {
        input = input.trim();
        input = input.substring(1, input.length() - 1);
        if (input.length() == 0) {
            return new int[0];
        }

        String[] parts = input.split(",");
        int[] output = new int[parts.length];
        for(int index = 0; index < parts.length; index++) {
            String part = parts[index].trim();
            output[index] = Integer.parseInt(part);
        }
        return output;
    }

    public static String integerArrayListToString(List<Integer> nums, int length) {
        if (length == 0) {
            return "[]";
        }

        String result = "";
        for(int index = 0; index < length; index++) {
            Integer number = nums.get(index);
            result += Integer.toString(number) + ", ";
        }
        return "[" + result.substring(0, result.length() - 2) + "]";
    }

    public static String integerArrayListToString(List<Integer> nums) {
        return integerArrayListToString(nums, nums.size());
    }

    public static String int2dListToString(List<List<Integer>> nums) {
        StringBuilder sb = new StringBuilder("[");
        for (List<Integer> list: nums) {
            sb.append(integerArrayListToString(list));
            sb.append(",");
        }

        sb.setCharAt(sb.length() - 1, ']');
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int[] nums = stringToIntegerArray(line);
            line = in.readLine();
            int target = Integer.parseInt(line);

            List<List<Integer>> ret = fourSum(nums, target);

            String out = int2dListToString(ret);

            System.out.print(out);
        }
    }
}
