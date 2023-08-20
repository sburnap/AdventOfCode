#include "aoc_utils.h"

#include <cstring>

using namespace std;

class Set
{
private:
    bool m_data[26];

public:
    Set(char *s = nullptr, unsigned int len = 0)
    {
        memset(m_data, 0, 26 * sizeof(bool));
        if (s != nullptr)
            set(s, len);
    }

    void set(char *s, unsigned int len)
    {
        for (auto i = 0; i < len; i++)
            m_data[s[i] - 'a'] = true;
    }

    unsigned int count()
    {
        unsigned int rc = 0;
        for (auto i = 0; i < 26; i++)
            if (m_data[i])
                rc++;
        return rc;
    }
};

class OldenDay6 : public au::OldenDay
{
public:
    OldenDay6() : OldenDay(2022, 6) {}

    int distinct_start(char *input, unsigned int number)
    {
        for (auto i = number; i < strlen(input); i++)
            if (Set(input + (i - number), number).count() == number)
                return i;

        return -1;
    }

    au::Answer test_one(void *inp, unsigned int length)
    {
        char **input = (char **)inp;

        for (auto i = 0; i < length; i++)
            printf("Test: %d     <- [ %s ]\n", distinct_start(input[i], 4), input[i]);
        return (au::Answer)0;
    }

    au::Answer part_one(void *inp, unsigned int length)
    {
        char **input = (char **)inp;

        return (au::Answer)distinct_start(input[0], 4);
    }

    au::Answer test_two(void *inp, unsigned int length)
    {
        char **input = (char **)inp;

        for (auto i = 0; i < length; i++)
            printf("Test: %d     <- [ %s ]\n", distinct_start(input[i], 14), input[i]);
        return (au::Answer)0;
    }

    au::Answer part_two(void *inp, unsigned int length)
    {
        char **input = (char **)inp;

        return (au::Answer)distinct_start(input[0], 14);
    }
};

int main()
{
    OldenDay6().run_all(true);
}
