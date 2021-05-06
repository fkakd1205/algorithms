class Solution {
    public int solution(String dartResult) {
        int answer = 0;
        int gameChance[] = new int[3];   // 게임 기회 세번
        int scoreIdx = 0, scoreCnt = 0;    // 스타상 계산 횟수
        
        for(int i = 0; i < dartResult.length(); i++){
            char dartChar = dartResult.charAt(i);   // *, #을 알아내기 위해
            int dartScore = Character.getNumericValue(dartChar);   // 다트 점수
            
            // 해당 인덱스의 값이 문자가 아닌 숫자인 경우
            if(dartScore >= 0 && dartScore <= 10){
                if(dartScore == 1){    // 점수가 10점인 경우
                    if(dartResult.charAt(i+1) == '0'){
                        dartScore = 10;
                        i++;
                    }
                }
                
                gameChance[scoreIdx] = dartScore;    // 점수 저장
            }
            else{
                switch(dartChar){
                    case 'S' :
                        // 점수 1제곱은 점수 그대로
                        scoreIdx++;
                        break;
                    case 'D' :
                        gameChance[scoreIdx] = (int)(Math.pow(gameChance[scoreIdx], 2));    // 점수 제곱
                        scoreIdx++;
                        break;
                    case 'T' :
                        gameChance[scoreIdx] = (int)(Math.pow(gameChance[scoreIdx], 3));    // 점수 세제곱
                        scoreIdx++;
                        break;
                    case '*' :  // 스타상
                        scoreCnt = 0;   // 점수를 2배 한 횟수
                        while((scoreIdx-scoreCnt) > 0 && scoreCnt < 2){
                            scoreCnt++;
                            gameChance[scoreIdx-scoreCnt] *= 2;
                        }
                        break;
                    case '#' :  // 아차상
                        gameChance[scoreIdx-1] *= -1;
                        break;
                }
            }
        }
        answer = gameChance[0] + gameChance[1] + gameChance[2];
        return answer;
    }
}
