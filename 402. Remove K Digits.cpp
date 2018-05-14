class Solution {
public:
    string removeKdigits(string num, int k) {
        cout << num.length() << endl;
        if (num.length() <= k) {
            return "0";
        }
        int n = num.length(); 
        string ret;
    // declaring character array
        for(char& n : num) {
            if (k == 0) {
                ret.push_back(n);
                continue;
            }
            while (ret.size()> 0 && ret.back() > n  && k > 0) {
                    ret.pop_back();
                    k -= 1;
            }
            if ((n == '0' && ret.size() > 0) || n != '0'){
                ret.push_back(n);
            }
        }
        while (k > 0) {
            ret.pop_back();
            k -= 1;
        }
        if (ret.size() == 0) {
            return "0";
        }
        string rs;
        for (auto n: ret) {
            rs += n;
        }
        return rs;
    }
};
