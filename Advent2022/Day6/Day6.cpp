#include "aoc_utils.h"

#include <iostream>
#include <string>
#include <set>

using namespace std;

class Day6 : public au::Day<vector<string>>
{
private:
public:
    Day6() : Day(2022, 6) {}

    int distinct_start(string input, unsigned int number)
    {
        for (unsigned int i = number; i < input.length(); i++)
            if (set<char>(input.begin() + (i - number), input.begin() + i).size() == number)
                return i;

        return -1;
    }

    int test_one(const vector<string> &input)
    {
        for (string s : input)
            cout << "Test: " << distinct_start(s, 4) << "   <- [ " << s << " ]" << endl;
        return 0;
    }

    int part_one(const vector<string> &input)
    {
        return distinct_start(input[0], 4);
    }

    int test_two(const vector<string> &input)
    {
        for (string s : input)
            cout << "Test: " << distinct_start(s, 14) << "   <- [ " << s << " ]" << endl;
        return 0;
    }

    int part_two(const vector<string> &input)
    {
        return distinct_start(input[0], 14);
    }
};

int main()
{
    Day6().run_all(true);

    return 0;
}
