/*From r/DailyProgrammer
 *Link: https://www.reddit.com/r/dailyprogrammer/comments/3i99w8/20150824_challenge_229_easy_the_dottie_number/
 *Written in Java, compiler:1.8
 *Name: The Dottie Number
 */
package dailyProgrammer;

public class Aug24_2015 {
	public static void main(String[] args){
		dottie(4);
	}

	public static void dottie(double n){
		double x = Math.cos(n);
		double y = Math.cos(x);
		while(x != y){
			x =y;
			y=Math.cos(y);
		}
		System.out.println(y);
	}
}
