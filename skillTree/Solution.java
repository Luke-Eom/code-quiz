package skillTree;

class Solution {
    private boolean check(String skill, String skillTree) {
        int pre = 0;
        for (int i = 0; i < skill.length(); i++) {
            int idx = skillTree.indexOf(skill.charAt(i));
            if (idx == -1) idx = Integer.MAX_VALUE;
            if (idx < pre) return false;
            pre = idx;
        }
        return true;
    }
    
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
         for (String skillTree : skill_trees) {
            answer += check(skill, skillTree) ? 1 : 0;
        }
        return answer;
    }
}
