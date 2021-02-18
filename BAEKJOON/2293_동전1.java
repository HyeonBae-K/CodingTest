import java.util.Scanner;

public class 동전1 {
	
	/*
	 *      1   2   3   4   5   6   7   8   9   10
	 * 1    1   1   1   1   1   1   1   1   1   1
	 * 2    0   1   1   2   2   3   3   4   4   5
	 * 5    0   0   0   0   1   1   2   2   3   4
	 *      1   2   2   3   4   5   6   7   8   10
	 */

	public static void main(String[] args) {
		int coin[] = new int[101]; //n : 종류의 개수
		int dp[] = new int[10001]; //k : 가치의 합
		
		Scanner scan = new Scanner(System.in);
		int numCoin = scan.nextInt(); //동전의 개수 입력
		int money = scan.nextInt(); //동전으로 만들 금액 입력
		
		for (int i = 1; i<= numCoin ; i++) { //동전의 금액 입력
			coin[i] = scan.nextInt(); 
		}
		dp[0] = 1;
		for (int i = 1 ; i<=numCoin; i++) { //동전의 종류를 돌리는 for (1,2,5)
			for(int j = coin[i];j<=money;j++) { //경우의 수를 돌면서 total을 갱신
				dp[j]+=dp[j-coin[i]];
			}
		}
		System.out.println(dp[money]);
	}

}