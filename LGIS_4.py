import java.util.ArrayList;
import java.util.List;


class LongestIncreasingSubsequence {
    public static void main(String[] args) {
        int[] arr = { 0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15 };
        increasingSubsequenceValues(arr);
    }

    public static void increasingSubsequenceValues(int[] seq) {
        List<Integer> list = new ArrayList<Integer>();
        for (int i = 0; i < seq.length; i++) {
            int j = 0;
            boolean elementUpdate = false;
            for (; j < list.size(); j++) {
                if (list.get(j) > seq[i]) {
                    list.add(j, seq[i]);
                    list.remove(j + 1);
                    elementUpdate = true;
                    break;
                }
            }
            if (!elementUpdate) {
                list.add(j, seq[i]);
            }
        }
        System.out.println("Longest Increasing Subsequence" + list);
    }


}
