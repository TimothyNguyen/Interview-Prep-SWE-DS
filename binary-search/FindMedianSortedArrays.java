public class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // if nums1 length is greater than input2, switch
        if(nums1.length > nums2.length) return findMedianSortedArrays(nums2, nums1);
        // Get the size
        int x = nums1.length, y = nums2.length;
        int l = 0, r = x;
        while(l <= r) {
            int partitionX = (l + r) / 2;
            int partitionY = (x + y + 1) / 2 - partitionX;
            
            // Binary search
            int maxLeftX = (partitionX == 0) ? Integer.MIN_VALUE : nums1[partitionX - 1];
            int minRightX = (partitionX == x) ? Integer.MAX_VALUE : nums1[partitionX];
            int maxLeftY = (partitionY == 0) ? Integer.MIN_VALUE : nums2[partitionY - 1];
            int minRightY = (partitionY == y) ? Integer.MAX_VALUE : nums2[partitionY];

            if(maxLeftX <= minRightY && maxLeftY <= minRightX) {
                if((x + y) % 2 == 0) {
                    return ((double) Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY)) / 2;
                } else {
                    return ((double) Math.max(maxLeftX, maxLeftY);
                }
            } else if(maxLeftX > minRightY) r = partitionX - 1;
            else l = partitionX + 1;
        }
        return 0.0;
    }
}