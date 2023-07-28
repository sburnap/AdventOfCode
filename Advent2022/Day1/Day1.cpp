#include "aoc_utils.h"

#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

class Day1 : public au::Day<vector<string>>
{
private:
    vector<int> collapse(const vector<string> &input)
    {
        vector<int> rc;

        int calories = 0;
        for (auto line : input)
        {
            if (line.empty())
            {
                rc.push_back(calories);
                calories = 0;
            }
            else
                calories += stoi(line);
        }

        rc.push_back(calories);
        return rc;
    }

public:
    Day1() : Day(2022, 1) {}

    int test_one(const vector<string> &foods)
    {
        const vector<int> elves = collapse(foods);
        return *max_element(elves.begin(), elves.end());
    }

    int part_one(const vector<string> &foods)
    {
        const vector<int> elves = collapse(foods);
        return *max_element(elves.begin(), elves.end());
    }

    int test_two(const vector<string> &foods)
    {
        vector<int> elves = collapse(foods);
        sort(elves.begin(), elves.end());
        return accumulate(elves.end() - 3, elves.end(), 0);
    }

    int part_two(const vector<string> &foods)
    {
        vector<int> elves = collapse(foods);
        sort(elves.begin(), elves.end());
        return accumulate(elves.end() - 3, elves.end(), 0);
    }
};

int main()
{
    Day1().run_all(true);

    return 0;
}