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
	
	// Given three colinear points p, q, r, the function checks if
	// point q lies on line segment 'pr'
	boolean onSegment(Point p, Point q, Point r)
	{
	    if (q.row <= Math.max(p.row, r.row) && q.row >= Math.min(p.row, r.row) &&
	        q.col <= Math.max(p.col, r.col) && q.col >= Math.min(p.col, r.col))
	       return true;
	 
	    return false;
	}
	
	// To find orientation of ordered triplet (p, q, r).
	// The function returns following values
	// 0 --> p, q and r are colinear
	// 1 --> Clockwise
	// 2 --> Counterclockwise
	int orientation(Point p, Point q, Point r)
	{
	    // See http://www.geeksforgeeks.org/orientation-3-ordered-points/
	    // for details of below formula.
	    int val = (q.col - p.col) * (r.col - q.col) -
	              (q.row - p.row) * (r.row - q.row);
	 
	    if (val == 0) return 0;  // colinear
	 
	    return (val > 0)? 1: 2; // clock or counterclock wise
	}
	
	// The main function that returns true if line segment 'p1q1'
	// and 'p2q2' intersect.
	boolean doIntersect(Point p1, Point q1, Point p2, Point q2)
	{
	    // Find the four orientations needed for general and
	    // special cases
	    int o1 = orientation(p1, q1, p2);
	    int o2 = orientation(p1, q1, q2);
	    int o3 = orientation(p2, q2, p1);
	    int o4 = orientation(p2, q2, q1);
	 
	    // General case
	    if (o1 != o2 && o3 != o4)
	        return true;
	 
	    // Special Cases
	    // p1, q1 and p2 are colinear and p2 lies on segment p1q1
	    if (o1 == 0 && onSegment(p1, p2, q1)) return true;
	 
	    // p1, q1 and p2 are colinear and q2 lies on segment p1q1
	    if (o2 == 0 && onSegment(p1, q2, q1)) return true;
	 
	    // p2, q2 and p1 are colinear and p1 lies on segment p2q2
	    if (o3 == 0 && onSegment(p2, p1, q2)) return true;
	 
	     // p2, q2 and q1 are colinear and q1 lies on segment p2q2
	    if (o4 == 0 && onSegment(p2, q1, q2)) return true;
	 
	    return false; // Doesn't fall in any of the above cases
	}
	
	private static ArrayList<Point> buildSuccessors(KnightPosition[][] board, int row, int col){
		ArrayList<Point> successors = new ArrayList<Point>();
		return successors; 
	}
	public static void main(String[] args){
		findLongestPath(4);
	}
}
