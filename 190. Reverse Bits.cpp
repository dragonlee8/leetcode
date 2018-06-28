class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        int ret = 0;
        for (int i = 0; i < 32; ++i, n>>=1)
        {
            ret = ret << 1 | (n & 1);
        }
        return ret;
    }
};
