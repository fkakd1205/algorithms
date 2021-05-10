class Solution {
    public String solution(String new_id) {
		String answer = "";
		StringBuffer id_buf = new StringBuffer();	// 유저가 입력한 아이디를 가공하기 위한 공간
		char id_char;
		
		if(new_id.length() == 0) new_id = "a";	// 빈 문자열이 들어오면 먼저 a를 채운다.
		
		// [1단계] 대문자를 소문자로 변경
		new_id = new_id.toLowerCase();
		
		// [2단계] 입력된 아이디 문자 중 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)만 id_buf에 추가
		for(int i = 0; i< new_id.length(); i++) {
			id_char = new_id.charAt(i);
			
			if((id_char >= '0' && id_char <= '9') || (id_char >= 'a' && id_char <= 'z') || id_char == '-' || id_char == '_' || id_char == '.'){
				id_buf.append(id_char);
			}
		}
		
		// [3단계] 마침표가 연속된 부분을 마침표 하나로 치환
		for(int i = 0; i< id_buf.length();) {
			id_char = id_buf.charAt(i);
			
			if((i != id_buf.length()-1) && id_char == '.' && id_buf.charAt(i+1) == '.') {
				id_buf.deleteCharAt(i+1);
				continue;
			}
			i++;
		}
		
		// [4단계] 마침표가 처음이나 끝에 위치한다면 제거
		if(id_buf.charAt(0) == '.') {
			id_buf.deleteCharAt(0);
		}
		if(id_buf.length() != 0 && id_buf.charAt(id_buf.length()-1) == '.') {
			id_buf.deleteCharAt(id_buf.length()-1);
		}
		
		// [5단계] 빈 문자열이라연, a를 대입
		if(id_buf.length() == 0) id_buf.append("a");
		
		// [6단계] 길이가 16자 이상이면, 15개의 문자를 제외한 나머지 제거
		if(id_buf.length() > 15) {
			id_buf.delete(15, id_buf.length());
			
			while(id_buf.charAt(id_buf.length()-1) == '.') {
				id_buf.deleteCharAt(id_buf.length()-1);
			}
		}
		
		// [7단계] 길이가 2자 이하라면, 마지막 문자를 길이가 3이상이 되도록 끝에 추가
		while(id_buf.length() <= 2) id_buf.append(id_buf.charAt(id_buf.length()-1));
		
		// 최종 변경된 아이디 반환
		answer = id_buf.toString();
	    return answer;
	}
}
