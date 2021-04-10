#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string solution2(vector<string> participant, vector<string> completion) {
    sort(participant.begin(), participant.end());  // 참가자 이름을 오름차순 정렬
    sort(completion.begin(), completion.end());  // 완주자 이름을 오름차순 정렬
    
    // 완주자 명단에 없는 참가자를 확인
    for(int i = 0; i < participant.size(); i++){
        if(participant[i] != completion[i])
            return participant[i];
    }
    
    //완주자 명단에 없으며, 참가자 이름을 오름차순했을 때의 마지막 참가자
    return participant[participant.size()];
}
