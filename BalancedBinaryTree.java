import java.lang.Math.*;
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isBalanced(TreeNode node) {
        return (Boolean) branchMaxLen(node)[0];
    }

    public Object[] branchMaxLen(TreeNode node) {
        if (node == null) {
            return new Object[] {true, 0};
        }
        
        Object[] ret = new Object[2];
        Object[] lb = branchMaxLen(node.left);
        Object[] rb = branchMaxLen(node.right);

        ret[0] = (Boolean) lb[0] && (Boolean) rb[0] && Math.abs((Integer) lb[1] - (Integer) rb[1]) <= 1;
        ret[1] = 1 + Math.max((Integer) lb[1], (Integer) rb[1]);

        return ret;
    }
}