class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        boolean flag;	// 스킬 순서 만족 여부
        
        for(int i = 0; i < skill_trees.length; i++) {
        	flag = true;
        	for(int j = 1; j < skill.length(); j++) {
        		int first_level = skill_trees[i].indexOf(skill.charAt(j-1));	// 선행 스킬
        		int now_level = skill_trees[i].indexOf(skill.charAt(j));	// 후행 스킬
        		
        		if(first_level == -1 && now_level != -1)	// 선행 스킬이 나오지 않았는데, 후행 스킬이 나온 경우 
        			flag = false;
        		if(now_level != -1 && first_level > now_level)	// 후행 스킬이 스킬 트리에 포함되어있는데, 선행 스킬보다 후행 스킬을 더 먼저 배운 경우.
        			flag = false;
        		
        		if(flag == false) break;
        	}
        	if(flag) answer++;	// 순서를 만족했다면 answer++
        }
        return answer;
    }
}
