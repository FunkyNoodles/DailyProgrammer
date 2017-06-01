/*From r/DailcolProgrammer
 *Link: https://www.reddit.com/r/dailcolprogrammer/comments/6dgiig/20170526_challenge_316_hard_longest_uncrossed/
 *Name: Longest Uncrossed Knight's Path
 */

package dailyProgrammer;

import java.util.ArrayList;

public class May26_2017 {
	
	public class Point{
		int row, col;
		Point(int row, int col){
			this.row = row;
			this.col = col;
		}
	}
	
	public class KnightPosition{
		boolean present;
		Point from;
		Point to;
		public void setFrom(int row, int col){
			from.row = row;
			from.col = col;
		}
		public void setTo(int row, int col){
			to.row = row;
			to.col = col;
		}
		public void setPresent(boolean present){
			this.present = present;
		}
	}
	
	public static int findLongestPath(int n){
		KnightPosition[][] board = new KnightPosition[n][n];
		for(int i = 0; i < n; ++i){
			for(int j = 0; j < n; ++j){
				board[i][j].setPresent(false);
			}
		}
		int maxPath = -1;
		for(int i = 0; i < Math.ceil(n / 2.0); ++i){
			for(int j = 0; j < Math.ceil((n / 2.0)); ++j){
				board[i][j].setPresent(true);
				int tmp = longestPath(n, board);
				board[i][j].setPresent(false);
				if(tmp > maxPath){
					maxPath = tmp;
				}
			}
		}
		return maxPath;
	}
	
	private static int longestPath(int n, KnightPosition[][] board){
		return 0;
	}
	
	private static ArrayList<Point> buildSuccessors(KnightPosition[][] board, int row, int col){
		ArrayList<Point> successors = new ArrayList<Point>();
		return successors; 
	}
	public static void main(String[] args){
		findLongestPath(4);
	}
}
