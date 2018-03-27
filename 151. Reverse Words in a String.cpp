class Solution {
public:
    std::string reverseS(string s) {
        int start = 0, end = s.length()-1;
        while (s[start] == ' ') {
            start ++;
        }
        while (s[end] == ' ') {
            end--;
        }        
        s = s.substr(start, end+1-start);
        start = 0, end = s.length()-1;

        while (start < end) {
            swap(s[start], s[end]);
            start++;
            end--;
        }
        return s;
    }
    void reverseWords(string &s) {
        s = reverseS(s);
        string ret;
        int start = 0;
        int end = s.find(' ');
        while (end != string::npos) {
            string word = reverseS(s.substr(start, end-start));
            if (word.length()) {
                if (start != 0) {
                    ret += ' ';
                }
                ret += word;
            }
            start = end+1;
            end = s.find(' ', start);
        }
        if (start != 0)
            ret += ' ';
        ret += reverseS(s.substr(start, end-start));

        s = ret;
    }
};
