// input : [1,2,3,-1,0,1,2,3,0,1,2,3]
// output : -1,0,1,2,3



import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    int a[]= {1,2,3,-1,0,1,2,3,0,1,2,3};
	    int n = a.length;
	   
	    ArrayList l= new ArrayList();
	    HashMap<Integer,Integer> hmp = new HashMap<>();
	    int d[]= new int [n];
	    int max = Integer.MIN_VALUE;
	   // System.out.println("hey Max:" + max);
	    int x=-1;
	    for(int i=0; i<a.length ; i++)
	    {
	      if(hmp.get(a[i] - 1) != null)
	      {
	          int last = hmp.get(a[i] - 1) - 1;
	          d[i]= 1 + d[last];
	      }
	      else
	      {
	          d[i] = 1;
	      }
	      hmp.put(a[i] , i + 1);
	      if(max <d[i])
	      {
	          max = d[i];
	          x=i;
	      }
	    }
	    for (int curr = a[x] -max + 1 ; curr <= a[x]; curr ++)
	    {
	        System.out.print(curr +" ");
	    }
		System.out.println("Hello World");
	}
}