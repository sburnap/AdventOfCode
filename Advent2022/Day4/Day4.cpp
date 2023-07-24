#include "aoc_utils.h"

#include <string>
#include <regex>
#include <iostream>
#include <ostream>

using namespace std;

class AreaTuple
{

private:
    int first_start;
    int first_end;
    int second_start;
    int second_end;

public:
    AreaTuple(const string &s)
    {
        static const regex area_regex("(\\d*)-(\\d*),(\\d*)-(\\d*)");

        smatch base_match;

        if (std::regex_match(s, base_match, area_regex))
        {
            first_start = stoi(base_match[1].str());
            first_end = stoi(base_match[2].str());
            second_start = stoi(base_match[3].str());
            second_end = stoi(base_match[4].str());
        }
        else
            first_start = first_end = second_start = second_end = -1;
    }

    bool contains()
    {
        return (first_start <= second_start && first_end >= second_end) ||
               (second_start <= first_start && second_end >= first_end);
    }

    bool overlap()
    {
        return (second_start <= first_start && first_start <= second_end) ||
               (first_start <= second_start && second_start <= first_end);
    }
};

class Day4 : public au::Day<AreaTuple>
{
public:
    Day4() : Day(2022, 4) {}

    int test_one(const vector<AreaTuple> &input)
    {
        unsigned int cnt = 0;
        for (AreaTuple at : input)
            if (at.contains())
                cnt++;

        return cnt;
    }

    int part_one(const vector<AreaTuple> &input)
    {
        unsigned int cnt = 0;
        for (AreaTuple at : input)
            if (at.contains())
                cnt++;

        return cnt;
    }

    int test_two(const vector<AreaTuple> &input)
    {
        unsigned int cnt = 0;
        for (AreaTuple at : input)
            if (at.overlap())
                cnt++;

        return cnt;
    }

    int part_two(const vector<AreaTuple> &input)
    {
        unsigned int cnt = 0;
        for (AreaTuple at : input)
            if (at.overlap())
                cnt++;

        return cnt;
    }
};

int main()
{
    Day4().run_all(true);

    return 0;
}
