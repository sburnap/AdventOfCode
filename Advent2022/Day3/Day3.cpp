#include "aoc_utils.h"

#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <numeric>
#include <iterator>

#include <iostream>

using namespace std;

class Day3 : public au::Day<vector<string>>
{
private:
    string letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

    vector<int> inboth(const vector<string> &input)
    {
        vector<int> priorities;

        for (string line : input)
        {
            set<wchar_t> left(line.begin(), line.begin() + line.size() / 2);
            set<wchar_t> right(line.begin() + line.size() / 2, line.end());

            set<wchar_t> both;
            set_intersection(left.begin(), left.end(), right.begin(), right.end(),
                             std::inserter(both, both.begin()));

            priorities.push_back(1 + letters.find(*both.begin()));
        }
        return priorities;
    }

    vector<int> in_three(const vector<string> &input)
    {
        vector<int> priorities;

        for (auto it = input.begin(); it != input.end(); advance(it, 3))
        {
            set<wchar_t> first(it->begin(), it->end());
            set<wchar_t> second((it + 1)->begin(), (it + 1)->end());
            set<wchar_t> third((it + 2)->begin(), (it + 2)->end());

            set<wchar_t> two;
            set_intersection(first.begin(), first.end(), second.begin(), second.end(),
                             inserter(two, two.begin()));
            set<wchar_t> three;
            set_intersection(two.begin(), two.end(), third.begin(), third.end(),
                             inserter(three, three.begin()));

            priorities.push_back(1 + letters.find(*three.begin()));
        }
        return priorities;
    }

public:
    Day3() : Day(2022, 3) {}

    int test_one(const vector<string> &input)
    {
        vector<int> priorities = inboth(input);

        return accumulate(priorities.begin(), priorities.end(), 0);
    }

    int part_one(const vector<string> &input)
    {
        vector<int> priorities = inboth(input);

        return accumulate(priorities.begin(), priorities.end(), 0);
    }

    int test_two(const vector<string> &input)
    {
        vector<int> priorities = in_three(input);

        return accumulate(priorities.begin(), priorities.end(), 0);
    }

    int part_two(const vector<string> &input)
    {
        vector<int> priorities = in_three(input);

        return accumulate(priorities.begin(), priorities.end(), 0);
    }
};

int main()
{
    Day3().run_all(true);
}
