class TimeMap {
public:
    unordered_map<string, vector<pair<int, string>>> hmap;
    TimeMap() {
        // hmap.clear();
    }

    void set(string key, string value, int timestamp) {
        hmap[key].push_back({timestamp, value}); // you can use make_pair as well
    }

    string get(string key, int timestamp) {
        if(!hmap.count(key)){
            return "";
        }

        int left=0, right=hmap[key].size();

        while(left<right){
            int mid = left + (right-left)/2;
            // if(hmap[key][mid].first == timestamp)
            //     return hmap[key][mid].second;

            if(hmap[key][mid].first > timestamp)
                right = mid;
            else
                left = mid +1;
        }

        // cout<< hmap[key][left].second << endl;
        // if(left <= 0 && left >hmap[key].size())
        //     return "";

        // return hmap[key][left-1].second;
        if (left > 0 && left <= hmap[key].size()){
            return hmap[key][left-1].second;
        }
        return "";
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */