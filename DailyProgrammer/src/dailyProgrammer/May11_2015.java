/*From r/DailyProgrammer
 *Link: http://www.reddit.com/r/dailyprogrammer/comments/36cyxf/20150518_challenge_215_easy_sad_cycles/
 *Written in Java, compiler:1.8u45
 *Name: Calculating Standard Deviation
 */
package dailyProgrammer;

import java.util.ArrayList;
import java.util.Scanner;

public class May11_2015 {
	static ArrayList<Integer> arr = new ArrayList<Integer>();
	
	static Scanner a = new Scanner(System.in);
	public static void main(String[] args){
		
		int totalSum = 0;
		double mean = 0;
		double dSum= 0;
		//double variance = 0;
		boolean first = true;
		
		while(first){// a.hasNext(" ")==false){
			//input = a.nextInt();
			arr.add(a.nextInt());
			first = false;
			first = a.hasNextInt();
			//arr.add(input);
			System.out.println(arr);
			//System.out.println(arr.get(1));
			//System.out.println(a.hasNextInt());
			//System.out.println(a.hasNext(" "));
		}
		
		for(int i=0; i<arr.size();i++){
			totalSum += arr.get(i);
		}
		mean = totalSum/arr.size();
		
		
		for(int j=0;j<arr.size();j++){
			dSum += Math.pow(arr.get(j)-mean,2);
		}
		
		System.out.println(Math.sqrt(dSum/arr.size()));
	}
}
