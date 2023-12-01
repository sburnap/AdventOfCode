#include "aoc_utils.h"

#include <cstring>

using namespace std;

class Set
{
private:
    bool m_data[52];

public:
    Set()
    {
        memset(m_data, 0, 52 * sizeof(bool));
    }

    void set(unsigned int i, bool val)
    {
        m_data[i] = val;
    }
    bool get(unsigned int i)
    {
        return m_data[i];
    }
};

class OldenDay3 : public au::OldenDay
{
public:
    OldenDay3() : OldenDay(2022, 3) {}

    unsigned int letter_to_uint(char ch)
    {
        if (ch >= 'a' && ch <= 'z')
            return ch - 'a';
        else
            return 26 + ch - 'A';
    }

    int sum_sides(char **input, unsigned int length)
    {
        unsigned int sm = 0;
        for (auto i = 0; i < length; i++)
        {
            Set left;

            for (auto j = 0; j < strlen(input[i]) / 2; j++)
                left.set(letter_to_uint(input[i][j]), true);

            unsigned int both = 0;
            for (auto j = strlen(input[i]) / 2; j < strlen(input[i]) && both == 0; j++)
            {
                auto val = letter_to_uint(input[i][j]);
                if (left.get(val))
                    both = val + 1;
            }
            sm += both;
        }
        return sm;
    }

    int sum_triplets(char **input, unsigned int length)
    {
        unsigned int sm = 0;
        for (auto i = 0; i < length - 2; i += 3)
        {
            Set one, two;
            for (auto j = 0; j < strlen(input[i]); j++)
                one.set(letter_to_uint(input[i][j]), true);

            for (auto j = 0; j < strlen(input[i + 1]); j++)
            {
                auto val = letter_to_uint(input[i + 1][j]);
                two.set(val, one.get(val));
            }

            unsigned int all = 0;
            for (auto j = 0; j < strlen(input[i + 4]); j++)
            {
                auto val = letter_to_uint(input[i + 2][j]);
                if (two.get(val))
                    all = val + 1;
            }
            sm += all;
        }
        return sm;
    }

    au::Answer test_one(void *input, unsigned int length)
    {
        return (au::Answer)sum_sides((char **)input, length);
    }

    au::Answer part_one(void *input, unsigned int length)
    {
        return (au::Answer)sum_sides((char **)input, length);
    }

    au::Answer test_two(void *input, unsigned int length)
    {
        return (au::Answer)sum_triplets((char **)input, length);
    }

    au::Answer part_two(void *input, unsigned int length)
    {
        return (au::Answer)sum_triplets((char **)input, length);
    }
};

int main()
{
    OldenDay3().run_all(true);
}
