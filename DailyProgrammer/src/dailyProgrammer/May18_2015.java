/*From r/DailyProgrammer
 *Link: http://www.reddit.com/r/dailyprogrammer/comments/36cyxf/20150518_challenge_215_easy_sad_cycles/
 *Written in Java, compiler:1.8u45
 *Name: Sad Cycles
 */

package dailyProgrammer;

import java.util.ArrayList;
import java.util.Scanner;

public class May18_2015 {
	
	static ArrayList<Long> arr = new ArrayList<Long>();
	
	public static void main(String[] args){
		
		@SuppressWarnings("resource")
		Scanner a = new Scanner(System.in);
		
		boolean first = true;
		int exponent = 0;
		int number = 0;
		exponent = a.nextInt();
		number = a.nextInt();
		long numP=number;
		long tempSum = 0;
		int beginPrint=-1;
		
		
		while(beginPrint==-1){
			if(first){
				numP = number;
			}else{
				numP = tempSum;
			}
			//System.out.println(numP);
			tempSum = 0;
			for(int i=(int) (Math.log10(numP)+1);i>0;i--){
				tempSum = (long) Math.pow(numP/(long)(Math.pow(10,i-1)), exponent)+tempSum;
				//System.out.println(tempSum);
				numP = (long)(numP-((long)(numP/(Math.pow(10, i-1))))*Math.pow(10, i-1));
				//System.out.println(numP);
			}
			//System.out.println(tempSum + ", ");
			arr.add(tempSum);
			if(!first){
				beginPrint = check(tempSum);
			}
			first = false;
		}
		
		for(int k=beginPrint; k<arr.size()-1;k++){
			System.out.print(arr.get(k));
			if(k!=arr.size()-2){
				System.out.print(", ");
			}
		}
	}
	public static int check(long temp){
		for(int j=0; j<arr.size()-1; j++){
			if(temp==arr.get(j)){
				//System.out.println(j);
				return j;
			}
		}
		return -1;
	}
}
