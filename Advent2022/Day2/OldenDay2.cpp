#include "aoc_utils.h"

using namespace std;

class OldenDay2 : public au::OldenDay
{
private:
public:
    OldenDay2() : OldenDay(2022, 2) {}

    int score(const char *game)
    {
        int scoremap[3][3] = {
            {4, 8, 3},
            {1, 5, 9},
            {7, 2, 6}};

        auto them = game[0];
        auto me = game[2];
        return scoremap[them - 'A'][me - 'X'];
    }

    int score2(const char *game)
    {
        int scoremap[3][3] = {
            {3, 4, 8},
            {1, 5, 9},
            {2, 6, 7}};

        auto them = game[0];
        auto me = game[2];
        return scoremap[them - 'A'][me - 'X'];
    }

    int test_one(char **input, unsigned int length)
    {
        auto sm = 0;

        for (unsigned int i = 0; i < length; i++)
            sm += score(input[i]);
        return sm;
    }

    int part_one(char **input, unsigned int length)
    {
        auto sm = 0;

        for (unsigned int i = 0; i < length; i++)
            sm += score(input[i]);
        return sm;
    }

    int test_two(char **input, unsigned int length)
    {
        auto sm = 0;

        for (unsigned int i = 0; i < length; i++)
            sm += score2(input[i]);
        return sm;
    }

    int part_two(char **input, unsigned int length)
    {
        auto sm = 0;

        for (unsigned int i = 0; i < length; i++)
            sm += score2(input[i]);
        return sm;
    }
};

int main()
{
    OldenDay2().run_all(true);

    return 0;
}
