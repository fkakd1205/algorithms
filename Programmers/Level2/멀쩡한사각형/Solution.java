class Solution {
    public long solution(int w, int h) {
        long answer = 1;
        long min = (long)w;
        long max = (long)h;
        
        // 크기 비교
        if(min > max){
            min = (long)h;
            max = (long)w;
        }
        
        // 최종 max값이 최대공약수가 되도록.('유클리드 호제법' 활용)
        long num = 1;
        while(num > 0){
            num = max % min;
            max = min;
            min = num;
        }
        
        // 겹치는 종이 개수는 (w/max + h/max - 1) * max -> w + h - max (여기서 max는 최대공약수)
        answer = ((long)w * (long)h) - ((long)w + (long)h - max);
        return answer;
    }
}
