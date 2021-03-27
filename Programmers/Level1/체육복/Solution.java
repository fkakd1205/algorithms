class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        int[] arr = new int[n];
        
        //여분의 체육복이 있는 학생은 1로 지정, 체육복을 도난당한 학생은 1을 빼준다.
        //(여분의 체육복이 있는 학생이 도난당했다면 -1이 아니고 0이 된다.)
        for(int i : reserve){
            arr[i-1]++;
        }
        for(int i : lost){
            arr[i-1]--;
        }
        
        for(int i = 0; i < arr.length; i++){
            if(arr[i] < 0){ //여분의 체육복이 없는 학생이 체육복을 도난당했을 때
                if(i != arr.length-1 && arr[i+1] > 0){  //마지막 학생이 아니면서, 뒷번호 학생에게 빌릴 수 있는 경우
                    arr[i]++;
                    arr[i+1]--;
                }
                else if(i != 0 && arr[i-1] > 0){    //첫번째 학생이 아니면서, 앞번호 학생에게 빌릴 수 있는 경우
                    arr[i]++;
                    arr[i-1]--;
                }
            }
        }
        
        for(int i = 0; i < arr.length; i++){
            if(arr[i] >= 0)
                answer++;
        }
        return answer;
    }
}
