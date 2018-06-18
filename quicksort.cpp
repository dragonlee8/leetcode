void quicksort(vector<int>& v, int begin, int end){
    if(end - begin<=1) return;
    int pivot = v[end-1], less_end = begin;

    for(int i=begin; i<end-1; i++)
        if(v[i]<pivot) swap(v[i], v[less_end++]);

    swap(v[end-1], v[less_end]);
    quicksort(v, begin, less_end);
    quicksort(v, less_end + 1, end);
}
