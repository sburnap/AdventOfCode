#include "aoc_utils.h"

#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

#include <iostream>

using namespace std;

class Day2 : public au::Day<vector<string>>
{
private:
    int score(const string &game)
    {
        int scoremap[3][3] = {
            {4, 8, 3},
            {1, 5, 9},
            {7, 2, 6}};

        auto them = game.c_str()[0];
        auto me = game.c_str()[2];
        return scoremap[them - 'A'][me - 'X'];
    }

    int score2(const string &game)
    {
        int scoremap[3][3] = {
            {3, 4, 8},
            {1, 5, 9},
            {2, 6, 7}};

        auto them = game.c_str()[0];
        auto me = game.c_str()[2];
        return scoremap[them - 'A'][me - 'X'];
    }

public:
    Day2() : Day(2022, 2) {}

    int test_one(const vector<string> &input)
    {
        auto sm = 0;
        for (auto game : input)
            sm += score(game);
        return sm;
    }

    int part_one(const vector<string> &input)
    {
        int sm = 0;
        for (auto game : input)
            sm += score(game);
        return sm;
    }

    int test_two(const vector<string> &input)
    {
        auto sm = 0;
        for (auto game : input)
            sm += score2(game);
        return sm;
    }

    int part_two(const vector<string> &input)
    {
        auto sm = 0;
        for (auto game : input)
            sm += score2(game);
        return sm;
    }
};

int main()
{
    Day2().run_all(true);
}
