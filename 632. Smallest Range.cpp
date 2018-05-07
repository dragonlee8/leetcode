typedef vector<int>::iterator IT;
class Compare
{
public:
    bool operator() (pair<IT, IT> a, pair<IT, IT> b) {
        return *(b.first) < *(a.first);
    }
};

void add(deque<int>& maxNums, int num) {
    for (int i = maxNums.size()-1; i >=0; --i) {
        if (maxNums[i] < num) {
            maxNums.pop_back();
        }
    }
    maxNums.push_back(num);
}
class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        vector<int> ret = {0, 0};
        if (nums.size()  == 0) {
            return ret;
        }
        int n = nums.size();
        priority_queue<pair<IT, IT>, vector<pair<IT, IT> >, Compare > pq;
        deque<int> maxNums;
        for (int i = 0; i < nums.size(); ++i) {
            pq.push(pair<IT, IT>(nums[i].begin(), nums[i].end()));
            add(maxNums, nums[i][0]);
        }
        
        int minDiff = maxNums.front() - *(pq.top().first);
        ret[0] = *(pq.top().first);
        ret[1] = maxNums.front();

        while (1) {
            auto elm = pq.top();
            
            int popVal = *(elm.first);
            pq.pop();
            if (popVal == maxNums[0]) {
                maxNums.pop_front();
            }
            
            if (++elm.first == elm.second) {
                break;
            }            
            
            add(maxNums, *(elm.first));
            pq.push(pair<IT, IT>(elm.first, elm.second));

            if (maxNums.front()- *(pq.top().first) < minDiff) {
                ret[0] = *(pq.top().first);
                ret[1] = maxNums.front();
                minDiff =  ret[1] - ret[0];
            }
            

        }
        return ret;
    }
};
