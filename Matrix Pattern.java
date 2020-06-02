/* 
	Input: N = 3
	Matrix: 1	3	10
		6	15	28
		21	36	45
	
	Input: N = 4
	Matrix:	1	3	10	28
		6	15	36	66
		21	45	78	105
		55	91	120	136
*/
import java.util.*;
import java.io.*;

public class Main {
  
  static final int MAX = 100;
  
  static int[][] a = new int[MAX][MAX];
  
  
  public static void PrintPattern(int n){
    
    int c = 1;
    
    for(int k=0;k<n;k++){
      int i=0; 
      int j=k;
      while(j >= 0){
        a[i][j] = (c * (c+1))/2;
        i++;
        j--;
        c++;
      }
    }
    
    for(int k=1;k<n;k++){
      int i=k;
      int j=n-1;
      
      while(i<n){
        a[i][j] = (c * (c+1))/2;
        i++;
        j--;
        c++;
      }
    }
    
    for(int i=0;i<n;i++){
      for(int j=0;j<n;j++){
        System.out.print(a[i][j] + " ");
      }
      System.out.println(); 
    }
  }
  
  public static void main(String args[]) throws IOException {
    
    //write your code here
    Scanner s = new Scanner(System.in);
    int t = s.nextInt();
    
    while(t>0){
      
      int n = s.nextInt();
      PrintPattern(n);
      --t;
      
    }
    
  }
}