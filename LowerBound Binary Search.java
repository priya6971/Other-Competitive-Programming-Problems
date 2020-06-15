/* 
If searched element doesn't exist function returns index of first element which is bigger than searched value.
  
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

public class LowerBound {

    private LowerBound() { }

    public static int lowerBound(int[] array, int length, int value) {
        int low = 0;
        int high = length;
        while (low < high) {
            final int mid = (low + high) / 2;
            //checks if the value is less than middle element of the array
            if (value <= array[mid]) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
}