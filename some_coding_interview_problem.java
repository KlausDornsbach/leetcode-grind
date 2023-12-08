
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Stream;

public class some_coding_interview_problem {

    public static void main(String[] args) {
        //Não alterar a main
        int[] nums = {2, 5, 8, 10, 16, 40};
        System.out.println(Arrays.toString(resolver(nums, 80)));
    }

    public static int[] resolver(int[] nums, int x) {

        int[] solucao = new int[] { Integer.MAX_VALUE, 0 };
        System.out.println("here");
        int l = 0;
        int r = nums.length - 1;
        while (l < r) {
            int mul = nums[l] * nums[r];
            if (mul == x) {
                if (nums[l] + nums[r] < solucao[0] + solucao[1]) {
                    solucao[0] = nums[l];
                    solucao[1] = nums[r];
                }
                System.out.println(solucao);
                r -= 1;
            } else if (mul < x) {
                l += 1;
            } else {
                r -= 1;
            }
        }

        if (solucao[0] == Integer.MAX_VALUE) {
            solucao[0] = 0;
            solucao[1] = 1;
            return solucao;
        }
        return solucao;
    }
}
