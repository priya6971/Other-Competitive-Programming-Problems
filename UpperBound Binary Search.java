/*
It returns index of first element which is grater than searched value.

In a binary search for 3, we will have
   v-- lower bound
1 2 3 4 5 5 5 6 7 9
     ^-- upper bound


And in a binary search for 5:

       v-- lower bound
1 2 3 4 5 5 5 6 7 9
             ^-- upper bound


The lower and upper bound are the same if the element does not exist in the range. In a binary search for 8:

                 v-- lower bound
1 2 3 4 5 5 5 6 7 9
                 ^-- upper bound

*/

public class UpperBound {

    private UpperBound() { }

    public static int upperBound(int[] array, int length, int value) {
        int low = 0;
        int high = length;
        while (low < high) {
            final int mid = (low + high) / 2;
            if (value >= array[mid]) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }
}
