class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];

        // brown = 2*(width-1) + 2*(height-1)
        int size = (brown + 4) / 2;

        for(int i = 3; i * 3 <= (brown + yellow); i++){
            int width = i;
            int height = size - width;

            if(height >= 3 && (width - 2) * (height - 2) == yellow){
                answer[0] = width;
                answer[1] = height;
            }
        }
        return answer;
    }
}